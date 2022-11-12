export const buildMapQueryUrl = (mapUrl, index, query) => {
	return `${mapUrl}/?index=${index}&q=${query}`
}
