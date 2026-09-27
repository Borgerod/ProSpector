from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from core.config import settings

conf = ConnectionConfig(
		MAIL_USERNAME = settings.MAIL_USERNAME,
		MAIL_PASSWORD = settings.MAIL_PASSWORD,
		MAIL_FROM = settings.MAIL_FROM,
		MAIL_PORT = settings.MAIL_PORT,
		MAIL_SERVER = settings.MAIL_SERVER,
		MAIL_FROM_NAME = settings.MAIL_FROM_NAME,
		MAIL_STARTTLS = settings.MAIL_STARTTLS,
		MAIL_SSL_TLS = settings.MAIL_SSL_TLS,
		USE_CREDENTIALS = settings.USE_CREDENTIALS,
		VALIDATE_CERTS = True
)

async def send_email_async(email_to: str, verify_num):

		message = MessageSchema(
				subject = 'Email Verification',
				recipients = [email_to],
				subtype = 'javascript',
				html = build_auth_email(verify_num),)
		fm = FastMail(conf)

		await fm.send_message(message)

def build_auth_email(verify_num):
		return f'''
<html>
<body style="margin: 0; padding: 0; box-sizing: border-box; font-family: Poppins;">
<div style="width: 100%; background: #efefef; border-radius: 10px; padding: 10px;">
	<div style="margin: 0 auto; width: 90%; text-align: center;">
		<h1 style="background-color: rgba( 34, 40, 47, 255); padding: 5px 10px; border-radius: 5px; color: white;"> ProSpector </h1>
		<div style="margin: 30px auto; background: white; width: 40%; border-radius: 10px; padding: 20px; text-align: center;">
			<h3 style="margin-bottom: 20px; font-size: 20px;">Email Authentication</h3>
			<p style="margin-bottom: 30px;">Please copy & paste this code in the app to verify your email.</p>      
			<a style="display: block; margin: 0 auto; border: none; background-color: #5d8387; color: #ffffff; width: 200px; line-height: 24px; padding: 10px; font-size: 16px; border-radius: 0px; cursor: pointer; text-decoration: none;"
			onClick="showMessage()">
				{verify_num}</a>
<p style="margin-bottom: 0px;"></p> 
		</div>
	</div>
</div>
</body>
</html>
'''

