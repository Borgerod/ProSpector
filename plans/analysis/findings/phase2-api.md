## Routes

| Method | Path | Handler (file:line) |
|--------|------|-------------------|
| POST | /login/token | route_login.py:26-45 |
| POST | /users/ | route_users.py:15-25 |
| GET | /users/verification/phone/send_code | route_users.py:28-31 |
| GET | /users/verification/phone/recieve_code | route_users.py:34-41 |
| GET | /users/verification/search_for_user_in_db | route_users.py:46-51 |
| GET | /callList | main.py:41-43 |
| GET | /currentcallList | main.py:45-48 |
| PUT | /callList/ringe_status | main.py:50-52 |
| GET | /RenewList | main.py:54-57 |
| GET | /overView | main.py:59-63 |
| GET | /ShowUser | main.py:65-68 |
| GET | /ResetPassword/Authentication | main.py:70-73 |
| PUT | /ResetPassword | main.py:75-78 |
| GET | /ResetPassword | main.py:80-88 |

## Auth Flow

1. **Token Creation**: User POSTs username/password to `/login/token` (route_login.py:26-45)
2. **User Validation**: `authenticate_user()` queries DB and verifies password hash (route_login.py:18-24)
3. **JWT Generation**: `create_access_token()` encodes JWT with `settings.SECRET_KEY` using HS256 (security.py:6-18)
4. **Cookie Storage**: Token set in httpOnly cookie named `access_token` (route_login.py:42-44)
5. **Protected Access**: Endpoints extract token from cookies via `OAuth2PasswordBearerWithCookie` (utils.py:21-36)
6. **Token Validation**: `get_current_user_from_token()` decodes JWT and retrieves user from DB (route_login.py:49-66)

## Config & Secrets

| File:Line | Config Key / Access |
|-----------|-------------------|
| config.py:3 | Import: `virtual_env.config.Config` |
| config.py:9 | `Config.getPostgresConfig` |
| config.py:11 | `config["USE_SQLITE_DB"]` |
| config.py:13 | `config["POSTGRES_PASSWORD"]` |
| config.py:14 | `config["POSTGRES_SERVER"]` |
| config.py:15 | `config["POSTGRES_PORT"]` |
| config.py:16 | `config["POSTGRES_DB"]` |
| security.py:16 | `settings.SECRET_KEY` (undefined in config.py) |
| send_email.py:4 | Import: `virtual_env.config.Config` |
| send_email.py:7 | `Config.getEmailConfig` |
| send_email.py:8 | `config["MAIL_USERNAME"]` |
| send_email.py:9 | `config["MAIL_PASSWORD"]` |
| send_email.py:10 | `config["MAIL_FROM"]` |
| send_email.py:11 | `config["MAIL_PORT"]` |
| send_email.py:12 | `config["MAIL_SERVER"]` |
| send_email.py:13 | `config["MAIL_FROM_NAME"]` |
| send_sms.py:6 | Import: `virtual_env.config.Config` |
| send_sms.py:36 | `Config.getPhoneConfig` |
| send_sms.py:37 | `config["TWILIO_ACCOUNT_SID"]` |
| send_sms.py:38 | `config["TWILIO_AUTH_TOKEN"]` |
