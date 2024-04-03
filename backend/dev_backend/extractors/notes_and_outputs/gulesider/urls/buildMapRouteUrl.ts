import { getPageTypeSuffixByProfile } from '@/configs/next.config/urls/index.mjs'

export const buildFormattedAddress = (address) => {
	if (!address || !address.streetName) {
		return null
	}

	return `${address.streetName}+${address.streetNumber}+${address.postalCode}+${address.postalArea}`.replace(
		/\s/g,
		'+'
	)
}

export const buildMapRouteQueryUrl = ({
	toX,
	toY,
	clientLocation = null,
	toName = '',
	zoom = 10,
	transport = 'car'
}) => {
	// If the user has already accepted location, use it as from point
	let fromX = 0
	let fromY = 0
	let fromName = ''
	if (clientLocation && clientLocation.length === 2) {
		fromX = clientLocation[0]
		fromY = clientLocation[1]
		fromName = 'currentPosition'
	}
	// F00 is for fastest route. S00 would be shortest route
	return `?c=${toY},${toX}&z=${zoom}&mode=route&r=${transport};F00;-1;${fromY};${fromX};${fromName};${toY};${toX};${toName}`
}

export const buildMapRouteUrl = (mapUrl, name, address, clientLocation, brand) => {
	const pageTypeSuffix = getPageTypeSuffixByProfile('route', true, brand)
	const formattedAddress = buildFormattedAddress(address)
	let routeUrl = `${mapUrl}${pageTypeSuffix}/+/${formattedAddress}`

	// If lat/lon available, add query
	if (address.coordinates && address.coordinates.length > 0) {
		let coords = address.coordinates.filter((loc) => loc.type === 'route')
		if (coords.length === 0) {
			coords = address.coordinates.filter((loc) => loc.type === 'map')
		}
		if (coords.length > 0) {
			let friendlyName = name
			if (address.postalArea) {
				friendlyName += `, ${address.postalArea}`
			}
			routeUrl += buildMapRouteQueryUrl({
				toX: coords[0].lon,
				toY: coords[0].lat,
				toName: friendlyName,
				clientLocation
			})
		}
	}

	return routeUrl
}



// buildMapUrlWithId.ts
export const buildMapUrlWithId = (mapUrl, id, index, layer, zoom = 17) => {
	return `${mapUrl}/?id=${id}&index=${index}&l=${layer}&zoom=${zoom}`
}
