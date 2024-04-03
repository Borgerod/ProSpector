import CompanyProfile from '@/components/Profile/CompanyProfile'
import { fetchDiscoveryData } from '@/data/profile/discovery'
import { fetchReviewsData } from '@/data/profile/reviews'
import { env } from '@/env/client.mjs'
import LayoutLanding from '@/layouts/Content/LayoutLanding'
import LayoutPrimary from '@/layouts/LayoutPrimary'
import { omniApi } from '@/server/omniApi'

const Company = ({ id, company, reviews, discovery }) => {
	return <CompanyProfile id={id} company={company} reviews={reviews} discovery={discovery} />
}

export async function getServerSideProps(context) {
	const id = context?.params?.id

	const company = await omniApi.fetchCompany({
		brand: env.NEXT_PUBLIC_BRAND,
		id
	})

	if (!company) {
		return { notFound: true }
	}

	const [reviews, discovery] = await Promise.all([fetchReviewsData(company), fetchDiscoveryData(company)])

	return {
		props: {
			company,
			reviews,
			discovery,
			id
		}
	}
}

export default Company

Company.getLayout = function getLayout(page) {
	return (
		<LayoutPrimary withFooter>
			<LayoutLanding bgColor='#E5E5E5'>{page}</LayoutLanding>
		</LayoutPrimary>
	)
}
