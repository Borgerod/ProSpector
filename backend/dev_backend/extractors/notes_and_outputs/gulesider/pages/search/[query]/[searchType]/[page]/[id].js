import { NextSeo } from 'next-seo'
import useTranslation from 'next-translate/useTranslation'
import dynamic from 'next/dynamic'
import { useRouter } from 'next/router'
import { QueryClient } from 'react-query'
import { dehydrate } from 'react-query/hydration'

import {
	buildCompanyGroupCanonicalLink,
	buildCompanyGroupMetaDescription,
	buildCompanyResultCanonicalLink,
	buildCompanyResultPageMetaDescription,
	buildPersonResultCanonicalLink,
	buildPersonResultPageMetaDescription,
	buildResultPageMetaTitle
} from '@/components/Common/SEO'
import ResultsActions from '@/components/Search/results/ResultsActions'
import ResultsHeader from '@/components/Search/results/ResultsHeader'
import ResultsTabs from '@/components/Search/results/ResultsTabs'
import { getPageTypeSuffixByProfile } from '@/configs/next.config/urls/index.mjs'
import { extractCompanyGroupData, extractSearchData, fetchSearch, useSearch } from '@/data/search'
import { env } from '@/env/client.mjs'
import LayoutResults from '@/layouts/Content/LayoutResults'
import LayoutPrimary from '@/layouts/LayoutPrimary'
import { useStore } from '@/store'
import {
	companyPagesSelector,
	geoPositionSelector,
	personPagesSelector,
	searchTypeSelector,
	wordcloudSelector
} from '@/store/selectors'
import { useSettings } from '@/store/settings'
import { isPhoneNumber } from '@/utils/common'
import { isInternalRequest } from '@/utils/isInternalRequest'
import { decodeQuery } from '@/utils/urls/decodeQuery'

const ResultsCompanies = dynamic(() => import('@/components/Search/results/ResultsCompanies'))
const ResultsPersons = dynamic(() => import('@/components/Search/results/ResultsPersons'))
const ResultsWordcloud = dynamic(() => import('@/components/Search/results/ResultsWordcloud'))
const ResultsPagination = dynamic(() => import('@/components/Search/results/ResultsPagination'))

const SearchResults = ({ showAxInfo }) => {
	useSearch()
	const searchType = useStore(searchTypeSelector)
	const wordcloud = useStore(wordcloudSelector)
	const companyPages = useStore(companyPagesSelector)
	const personPages = useStore(personPagesSelector)

	// We only run the search filters after hydration i.e. client side
	const { query } = useRouter()
	const { brand } = useSettings()
	const { t } = useTranslation()

	const nearby = query?.nearby
	const review = query?.review

	const setSearchFilters = useStore((store) => store.setSearchFilters)
	const setMapFitResults = useStore((store) => store.setMapFitResults)

	const geoPosition = useStore(geoPositionSelector)

	let nearbyCoords, rating
	if (nearby === 'true' && geoPosition) {
		nearbyCoords = `${geoPosition.latitude},${geoPosition.longitude}`
	}

	if (review) {
		rating = parseInt(review, 10)
	}

	if (nearbyCoords || rating) {
		setMapFitResults(true)
		setSearchFilters(nearbyCoords, rating)
	}

	let canonical
	let description

	if (searchType === 'companies') {
		canonical = buildCompanyResultCanonicalLink({
			query: decodeQuery(query.query),
			brand,
			page: query.page
		})
		description = buildCompanyResultPageMetaDescription(decodeQuery(query.query), wordcloud, t)
	} else if (searchType === 'companyGroup') {
		canonical = buildCompanyGroupCanonicalLink({
			groupId: query.id,
			query: decodeQuery(query.query),
			brand,
			page: query.page
		})
		description = buildCompanyGroupMetaDescription(decodeQuery(query.query), t)
	} else {
		canonical = buildPersonResultCanonicalLink({
			query: decodeQuery(query.query),
			brand,
			page: query.page
		})
		description = buildPersonResultPageMetaDescription(decodeQuery(query.query), t)
	}

	return (
		<>
			<NextSeo
				title={buildResultPageMetaTitle(searchType, decodeQuery(query.query), query.page, t, brand)}
				description={description}
				canonical={canonical}
			/>
			<ResultsTabs />
			{searchType !== 'companyGroup' && <ResultsActions />}
			<ResultsHeader />
			{searchType === 'companies' || searchType === 'companyGroup' ? (
				<ResultsCompanies showAxInfo={showAxInfo} />
			) : (
				<ResultsPersons />
			)}
			<ResultsPagination
				pages={
					searchType === 'companies' || searchType === 'companyGroup' ? companyPages : personPages
				}
			/>
			{wordcloud && wordcloud.length > 0 && <ResultsWordcloud wordcloud={wordcloud} />}
		</>
	)
}

SearchResults.getLayout = function getLayout(page) {
	return (
		<LayoutPrimary>
			<LayoutResults>{page}</LayoutResults>
		</LayoutPrimary>
	)
}

SearchResults.getInitialState = async function getInitialState(
	searchType,
	searchQuery,
	page,
	companies,
	persons,
	companyHits,
	personHits,
	totalHits,
	companyPages,
	personPages,
	wordcloud,
	queryParts,
	companyGroup
) {
	const initialState = {
		searchType,
		searchQuery,
		searchPage: page,
		companies,
		persons,
		companyHits,
		personHits,
		totalHits,
		companyPages,
		personPages,
		wordcloud,
		queryParts,
		companyGroup
	}

	return initialState
}

export async function getServerSideProps({ params, query, req }) {
	const showAxInfo = isInternalRequest(req) && query?.ax === 'info'

	const searchQuery = params?.query

	const page = parseInt(params?.page, 10)

	const searchType = params?.searchType
	let searchData, searchResult
	// company groups are a special (annoying) case
	let companyGroup = params?.id
	if (companyGroup === 0) {
		companyGroup = null
	}
	if (searchType === 'companyGroup') {
		searchData = await fetchSearch(searchQuery, page, searchType, companyGroup)
		searchResult = extractCompanyGroupData(searchData)
	} else {
		searchData = await fetchSearch(searchQuery, page, page > 1 ? searchType : null)
		searchResult = extractSearchData(searchData)
	}

	const {
		companies,
		persons,
		companyHits,
		personHits,
		totalHits,
		companyPages,
		personPages,
		wordcloud,
		queryParts
	} = searchResult

	const initialState = await SearchResults.getInitialState(
		searchType,
		searchQuery,
		page,
		companies,
		persons,
		companyHits,
		personHits,
		totalHits,
		companyPages,
		personPages,
		wordcloud,
		queryParts,
		companyGroup
	)

	if (totalHits === 0 && isPhoneNumber(searchQuery)) {
		const suffix = getPageTypeSuffixByProfile('phoneListing', true, env.NEXT_PUBLIC_BRAND, false)
		const phoneNumber = searchQuery.replace(/[\s+-]+/g, '')
		return {
			redirect: {
				destination: `/${phoneNumber}${suffix.replace(/\\/g, '')}`,
				permanent: true
			}
		}
	}

	const queryKey = [
		'search',
		searchQuery,
		page,
		page > 1 || searchType === 'companyGroup' ? searchType : null,
		searchType === 'companyGroup' ? companyGroup : null,
		null,
		null,
		0
	]

	const ssrQueryClient = new QueryClient({
		defaultOptions: {
			queries: {
				staleTime: Infinity,
				cacheTime: Infinity
			}
		}
	})

	ssrQueryClient.setQueryData(queryKey, searchData)

	const dehydratedState = dehydrate(ssrQueryClient)

	ssrQueryClient.clear()

	return {
		props: {
			showAxInfo,
			initialState,
			dehydratedState
		}
	}
}

export default SearchResults
