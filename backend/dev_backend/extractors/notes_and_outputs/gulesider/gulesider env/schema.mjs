// @ts-check
import { z } from 'zod'

/**
 * Specify your server-side environment variables schema here.
 * This way you can ensure the app isn't built with invalid env vars.
 */
export const serverSchema = z.object({
	ANALYZE: z.string().optional(),
	NODE_ENV: z.enum(['development', 'test', 'production']),
	SENTRY_RELEASE: z.string().optional(),
	MINIO_ENDPOINT: z.string(),
	MINIO_SECRET_KEY: z.string(),
	MINIO_ACCESS_KEY: z.string(),
	OMNI_API_USERNAME: z.string(),
	OMNI_API_PASSWORD: z.string()
})

/**
 * Specify your client-side environment variables schema here.
 * This way you can ensure the app isn't built with invalid env vars.
 * To expose them to the client, prefix them with `NEXT_PUBLIC_`.
 */
export const clientSchema = z.object({
	NEXT_PUBLIC_BRAND: z.enum(['eniro', 'krak', 'degulesider', 'gulesider']),
	NEXT_PUBLIC_ENV: z.enum(['test', 'development', 'production']),
	NEXT_PUBLIC_ONE_BACK: z.string().url(),
	NEXT_PUBLIC_OMNI_API_URL: z.string().url(),
	NEXT_PUBLIC_CDN_URL: z.string().min(1),
	NEXT_PUBLIC_SENTRY_DSN: z.string().optional(),
	NEXT_PUBLIC_SENTRY_ENVIRONMENT: z.string().optional(),
	NEXT_PUBLIC_SENTRY_TRACES_SAMPLE_RATE: z.number().optional(),
	NEXT_PUBLIC_SITE_VERSION: z.string().optional()
})

export const formatErrors = (
	/** @type {import('zod').ZodFormattedError<Map<string,string>,string>} */
	errors
) =>
	Object.entries(errors)
		.map(([name, value]) => {
			if (value && '_errors' in value) return `${name}: ${value._errors.join(', ')}\n`
		})
		.filter(Boolean)
