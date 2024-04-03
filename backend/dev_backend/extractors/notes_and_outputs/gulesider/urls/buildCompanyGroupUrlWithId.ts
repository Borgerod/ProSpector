import { buildFilters } from './buildFilters'
import { encodeQuery } from './encodeQuery'

import { getPageTypeSuffixByProfile } from '@/configs/next.config/urls/index.mjs'

export const buildCompanyGroupUrlWithId = ({ groupId, query, filter, brand }) => {
	const pageTypeSuffix = getPageTypeSuffixByProfile('companyGroup', true, brand)
	const escapedQuery = encodeQuery(query)
	return `/${escapedQuery}/${groupId}${pageTypeSuffix}${buildFilters(filter)}`.toLowerCase()
}

// buildCompaniesUrl.ts
import { buildResultUrl } from './buildResultUrl'

import { getPageTypeSuffixByProfile } from '@/configs/next.config/urls/index.mjs'

export const buildCompaniesUrl = ({ query, page, filter, brand }) => {
	const pageTypeSuffix = getPageTypeSuffixByProfile('companies', true, brand)
	return buildResultUrl(pageTypeSuffix, query, page, filter)
}


// buildCompanyUrl.ts
import { buildIdUrl } from './buildIdUrl'

import { getPageTypeSuffixByProfile } from '@/configs/next.config/urls/index.mjs'

export const buildCompanyUrl = ({ item, filter, suggest, brand }) => {
	const pageTypeSuffix = getPageTypeSuffixByProfile('company', true, brand)
	return buildIdUrl(pageTypeSuffix, item, filter, suggest)
}
