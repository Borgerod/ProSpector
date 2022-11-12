// @ts-check
/* eslint-disable node/no-process-env */
import { z as _z } from 'zod'

import { clientSchema, formatErrors } from './schema.mjs'

/**
 * You can't destruct `process.env` as a regular object, so you have to do
 * it manually here. This is because Next.js evaluates this at build time,
 * and only used environment variables are included in the build.
 */
const clientEnv = {
	NEXT_PUBLIC_BRAND: process.env.NEXT_PUBLIC_BRAND,
	NEXT_PUBLIC_ENV: process.env.NEXT_PUBLIC_ENV,
	NEXT_PUBLIC_ONE_BACK: process.env.NEXT_PUBLIC_ONE_BACK,
	NEXT_PUBLIC_OMNI_API_URL: process.env.NEXT_PUBLIC_OMNI_API_URL,
	NEXT_PUBLIC_CDN_URL: process.env.NEXT_PUBLIC_CDN_URL,
	NEXT_PUBLIC_SENTRY_DSN: process.env.NEXT_PUBLIC_SENTRY_DSN,
	NEXT_PUBLIC_SENTRY_ENVIRONMENT: process.env.NEXT_PUBLIC_SENTRY_ENVIRONMENT,
	NEXT_PUBLIC_SENTRY_TRACES_SAMPLE_RATE: parseFloat(process.env.NEXT_PUBLIC_SENTRY_TRACES_SAMPLE_RATE) || 0
}

const _clientEnv = clientSchema.safeParse(clientEnv)

if (_clientEnv.success === false) {
	console.error('❌ Invalid environment variables:\n', ...formatErrors(_clientEnv.error.format()))
	throw new Error('Invalid environment variables')
}

/**
 * Validate that client-side environment variables are exposed to the client.
 */
for (const key of Object.keys(_clientEnv.data)) {
	if (!key.startsWith('NEXT_PUBLIC_')) {
		console.warn('❌ Invalid public environment variable name:', key)

		throw new Error('Invalid public environment variable name')
	}
}

/**
 * @type {{ [k in keyof _z.infer<typeof clientSchema>]: _z.infer<typeof clientSchema>[k] | undefined }}
 */
export const env = _clientEnv.data
