import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from dotenv import load_dotenv
load_dotenv('.env')


class Envs:
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_FROM = os.getenv('MAIL_FROM')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)


'''
<!DOCTYPE html>
<html>
<head>
<title>Word page</title>
</head>
<body>
<form action="/submit" method="post" target="frame>
  <label for="word">Word:</label><br>
  <input type="text" id="word" name="word" value={{ word }}><br><br>
  <input type="submit" value="Submit">
</form>
<iframe name="frame" style="display:none;"></iframe>
</body>
</html>
'''


# async def send_email_async():
async def send_email_async(email_to: str, verify_num):

    message = MessageSchema(
        subject = 'Email Verification',
        recipients = [email_to],
        subtype = 'javascript',
        html = build_auth_email(verify_num),)
    fm = FastMail(conf)

    await fm.send_message(message)
    # await fm.send_message(message, template_name='email_authentication.html')



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
#     MAIL_USERNAME = Envs.MAIL_USERNAME,
#     MAIL_PASSWORD = Envs.MAIL_PASSWORD,
#     MAIL_FROM = Envs.MAIL_FROM,
#     MAIL_PORT = Envs.MAIL_PORT,
#     MAIL_SERVER = Envs.MAIL_SERVER,
#     MAIL_FROM_NAME = Envs.MAIL_FROM_NAME,
#     MAIL_TLS = True,
#     MAIL_SSL = False,
#     USE_CREDENTIALS = True,
#     TEMPLATE_FOLDER = './templates/emails'
# )

# # def get_user_email(email: str, db: Session):
# #     # NB: username is email in this case
# #     try:
# #         user = get_user_by_email(email, db)
# #         return user.email
# #     except:
# #         pass
# #         # return "Did not find email in database"

# # def authenticateUserEmail(email: str, db: Session):
# #     user_emial = get_user_email(email, db)
# #     if user_emial:
# #         subject, body = get_authentication_email()
# #         send_email_async(subject = subject: str, email_to = user_emial: str, body = body: dict)


# # async def send_email_async(subject: str, email_to: str):
# #     message = MessageSchema(
# #         subject = subject,
# #         recipients = [email_to],
# #         subtype = 'html',
# #     )
# #     print(conf)
# #     fm = FastMail(conf)
# #     print(fm)
#     # await fm.send_message(message, template_name = 'email_reset_password.html')

# html = """
# <html>
# <body style="margin: 0; padding: 0; box-sizing: border-box; font-family: Poppins;">
# <div style="width: 100%; background: #efefef; border-radius: 10px; padding: 10px;">
#   <div style="margin: 0 auto; width: 90%; text-align: center;">
#     <h1 style="background-color: rgba( 34, 40, 47, 255); padding: 5px 10px; border-radius: 5px; color: white;"> ProSpector </h1>
#     <div style="margin: 30px auto; background: white; width: 40%; border-radius: 10px; padding: 20px; text-align: center;">
#       <h3 style="margin-bottom: 20px; font-size: 20px;">Email Authentication</h3>
#       <p style="margin-bottom: 30px;">Please authenticate your email, in order to complete your account creation.</p>      
#       <a style="display: block; margin: 0 auto; border: none; background-color: rgba(93, 131, 135, 255); color: white; width: 200px; line-height: 24px; padding: 10px; font-size: 16px; border-radius: 0px; cursor: pointer; text-decoration: none;"
#       onClick="showMessage()">
#         Authenticate</a>
# <p style="margin-bottom: 0px;"></p> 
#     </div>
#   </div>
# </div>
# </body>
# <script type="text/javascript">
#   function showMessage() {
#       alert("Your Email has been Authenticated");
#   }
# </script>
# </html>
# """
# # gslysnqzqoihayin

# async def send_email_async():
#     message = MessageSchema(
#         subject="Email Authentication",
#         recipients=["borgerod@hotmail.com"],
#         body=html,
#         subtype="html"
#         )
#     print(conf)
#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code = 200, content = {"message": "email has been sent"})   



# '''
# How to use it
#     Open the “Mail” app.
#     Open the “Settings” menu.
#     Select “Accounts” and then select your Google Account.
#     Replace your password with the 16-character password shown above.
# '''

# '''
# gslysnqzqoihayin
# '''


# '''
# udrpwxglgjbspweo
# '''

# '''
# Your app password for Windows Computer
# udrpwxglgjbspweo
# How to use it
# Open the “Mail” app.
# Open the “Settings” menu.
# Select “Accounts” and then select your Google Account.
# Replace your password with the 16-character password shown above.
# Just like your normal password, this app password grants 
# complete access to your Google Account. You won't need to remember it, 
# so don't write it down or share it with anyone.

# Learn more


# '''