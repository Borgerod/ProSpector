# import os
# from fastapi import BackgroundTasks
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from dotenv import load_dotenv
# load_dotenv('.env')

# class Envs:
#     MAIL_USERNAME = os.getenv('MAIL_USERNAME')
#     MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
#     MAIL_FROM = os.getenv('MAIL_FROM')
#     MAIL_PORT = int(os.getenv('MAIL_PORT'))
#     MAIL_SERVER = os.getenv('MAIL_SERVER')
#     MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')

# conf = ConnectionConfig(
#     MAIL_USERNAME=Envs.MAIL_USERNAME,
#     MAIL_PASSWORD=Envs.MAIL_PASSWORD,
#     MAIL_FROM=Envs.MAIL_FROM,
#     MAIL_PORT=Envs.MAIL_PORT,
#     MAIL_SERVER=Envs.MAIL_SERVER,
#     MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
#     MAIL_STARTTLS = True,
#     MAIL_SSL_TLS = False,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True
# )

# async def send_email_async(email_to: str, verify_num):

#     message = MessageSchema(
#         subject = 'Email Verification',
#         recipients = [email_to],
#         subtype = 'javascript',
#         html = build_auth_email(verify_num),)
#     fm = FastMail(conf)

#     await fm.send_message(message)

# def build_auth_email(verify_num):
#     return f'''
# <html>
# <body style="margin: 0; padding: 0; box-sizing: border-box; font-family: Poppins;">
# <div style="width: 100%; background: #efefef; border-radius: 10px; padding: 10px;">
#   <div style="margin: 0 auto; width: 90%; text-align: center;">
#     <h1 style="background-color: rgba( 34, 40, 47, 255); padding: 5px 10px; border-radius: 5px; color: white;"> ProSpector </h1>
#     <div style="margin: 30px auto; background: white; width: 40%; border-radius: 10px; padding: 20px; text-align: center;">
#       <h3 style="margin-bottom: 20px; font-size: 20px;">Email Authentication</h3>
#       <p style="margin-bottom: 30px;">Please copy & paste this code in the app to verify your email.</p>      
#       <a style="display: block; margin: 0 auto; border: none; background-color: #5d8387; color: #ffffff; width: 200px; line-height: 24px; padding: 10px; font-size: 16px; border-radius: 0px; cursor: pointer; text-decoration: none;"
#       onClick="showMessage()">
#         {verify_num}</a>
# <p style="margin-bottom: 0px;"></p> 
#     </div>
#   </div>
# </div>
# </body>
# </html>
# '''

