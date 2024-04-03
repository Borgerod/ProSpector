export const decodeQuery = (query: string) => {
	if (!query) {
		return query
	}

	if (query.indexOf('%e2%80%ad') >= 0) {
		query = query.replace('%e2%80%ad', '')
	}

	if (query.indexOf('%e2%80%ac') >= 0) {
		query = query.replace('%e2%80%ac', '')
	}

	return decodeURIComponent(query.replace(/\+/g, ' '))
}

export const encodeQuery = (query: string) => {
	if (!query) {
		return query
	}

	/*
		 JAVA      JAVASCRIPT
		 [ ]     +          %20
		 [!]     %21        !
		 [*]     *          *
		 [']     %27        '
		 [(]     %28        (
		 [)]     %29        )
		  [~]     %7E  		~
	 */
	return query
		.split(' ')
		.map((word) => encodeURIComponent(word.toLowerCase()))
		.filter((word) => word !== '')
		.join('+')
		.replace(/!/g, '%21')
		.replace(/~/g, '%7E')
		.replace(/'/g, '%27')
		.replace(/\(/g, '%28')
		.replace(/\)/g, '%29')
}
