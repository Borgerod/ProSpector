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
    MAIL_USERNAME = Envs.MAIL_USERNAME,
    MAIL_PASSWORD = Envs.MAIL_PASSWORD,
    MAIL_FROM = Envs.MAIL_FROM,
    MAIL_PORT = Envs.MAIL_PORT,
    MAIL_SERVER = Envs.MAIL_SERVER,
    MAIL_FROM_NAME = Envs.MAIL_FROM_NAME,
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    TEMPLATE_FOLDER = './templates/emails'
)

# def get_user_email(email: str, db: Session):
#     # NB: username is email in this case
#     try:
#         user = get_user_by_email(email, db)
#         return user.email
#     except:
#         pass
#         # return "Did not find email in database"

# def authenticateUserEmail(email: str, db: Session):
#     user_emial = get_user_email(email, db)
#     if user_emial:
#         subject, body = get_authentication_email()
#         send_email_async(subject = subject: str, email_to = user_emial: str, body = body: dict)


# async def send_email_async(subject: str, email_to: str):
#     message = MessageSchema(
#         subject = subject,
#         recipients = [email_to],
#         subtype = 'html',
#     )
#     print(conf)
#     fm = FastMail(conf)
#     print(fm)
    # await fm.send_message(message, template_name = 'email_reset_password.html')

html = """
<p>Thanks for using Fastapi-mail</p> 
"""
# gslysnqzqoihayin

async def send_email_async():
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=["borgerod@hotmail.com"],
        body=html,
        subtype="html"
        )
    print(conf)
    fm = FastMail(conf)
    await fm.send_message(message)
    # return JSONResponse(status_code=200, content={"message": "email has been sent"})   



'''
How to use it
    Open the “Mail” app.
    Open the “Settings” menu.
    Select “Accounts” and then select your Google Account.
    Replace your password with the 16-character password shown above.
'''