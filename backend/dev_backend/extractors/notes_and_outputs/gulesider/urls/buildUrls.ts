import { buildFilters } from './buildFilters'
import { encodeQuery } from './encodeQuery'

const getFullName = (name) => [name.firstName, name.middleName, name.lastName].filter(Boolean).join(' ')

const getItemName = (item) => {
	const name = typeof item?.name === 'object' ? getFullName(item?.name) : item?.name
	return name || item?.phones?.[0]?.companyOwner || ' '
}

export const buildIdUrl = (pageTypeSuffix, item, filter, suggest) => {
	const itemName = getItemName(item)
	const escapedQuery = encodeQuery(itemName)
	let address =
		item.addresses && item.addresses[0] && item.addresses[0].postalArea
			? `+${encodeQuery(item.addresses[0].postalArea)}`
			: ''

	if (suggest && item.postalArea) {
		address = `+${encodeQuery(item.postalArea)}`
	}

	const itemId = item?.eniroId || item?.id

	return `/${escapedQuery}${address}/${itemId}${pageTypeSuffix}${buildFilters(filter)}`.toLowerCase()
}
