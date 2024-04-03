from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# Nessasary for importing config 
import sys; sys.path.insert(0, '..')
from virtual_env.config import Config

class Envs:
		config = Config.getEmailConfig # Get Appropriate config variables 
		MAIL_USERNAME: str = config["MAIL_USERNAME"]
		MAIL_PASSWORD = config['MAIL_PASSWORD']
		MAIL_FROM = config['MAIL_FROM']
		MAIL_PORT = int(config['MAIL_PORT'])
		MAIL_SERVER = config['MAIL_SERVER']
		MAIL_FROM_NAME = config['MAIL_FROM_NAME']
try:
	conf = ConnectionConfig(
			MAIL_USERNAME=Envs.MAIL_USERNAME,
			MAIL_PASSWORD=Envs.MAIL_PASSWORD,
			MAIL_FROM=Envs.MAIL_FROM,
			MAIL_PORT=Envs.MAIL_PORT,
			MAIL_SERVER=Envs.MAIL_SERVER,
			MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
			MAIL_STARTTLS = True, #! sometimes fastapi_mail requires this, sometimes the other 
			MAIL_SSL_TLS = False, #! sometimes fastapi_mail requires this, sometimes the other 
			USE_CREDENTIALS = True,
			VALIDATE_CERTS = True
	)
except:
	ConnectionConfig(
		MAIL_USERNAME=Envs.MAIL_USERNAME,
		MAIL_PASSWORD=Envs.MAIL_PASSWORD,
		MAIL_FROM=Envs.MAIL_FROM,
		MAIL_PORT=Envs.MAIL_PORT,
		MAIL_SERVER=Envs.MAIL_SERVER,
		MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
		MAIL_TLS=True,          #* sometimes fastapi_mail requires this, sometimes the other 
		MAIL_SSL=False,         #* sometimes fastapi_mail requires this, sometimes the other 
		USE_CREDENTIALS = True,
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

