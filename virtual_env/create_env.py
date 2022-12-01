import os
from numpy import var
from dotenv import load_dotenv, find_dotenv
from os.path import join, dirname

'''
soruce, tutorial:
    https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn
'''

''' #* STEP 1
    Create a .env file
    First, you need to create a new .env file, and then load the name and value of the variables as a key-value pairs:
'''


''' #* STEP 2
    Create app.py (NOTE will call it "create_env.py") ;Import and Call python-dotenv
'''

from dotenv import load_dotenv # importing the load_dotenv from the python-dotenv module
import os #provides ways to access the Operating System and allows us to read the environment variables

# load_dotenv(find_dotenv())
load_dotenv()

''' #* STEP 3
   Access the Environment Variables
'''
my_id = os.getenv("my_id")
my_secret_key = os.getenv("my_secret_key")

def myEnvironment():
    print(f'My id is: {my_id}.')
    print(f'My secret key is: {my_secret_key}.')

if __name__ == "__main__":
    myEnvironment()



















# '''
# #! OLD ENV HANDLER
# '''


# def setEnv(name:str, value:str):
#     '''creates new enviourment variables by name, then sets value
#     '''
#     os.environ[name] = value

# def getEnv(name: str) -> str:
#     ''' gets value by name from enviourment variables
#     '''
#     env = os.getenv(name)         # alt 1
#     print("\n", env, type(env), "\n")
#     return env

# def buildDotEnv():
#     ''' 
#     creates the env file/folder from admins enviourment, 
#     which will be exported to the clients computer
#     '''




# @property
# def getVarNames() -> dict:
#     var_dict = {
#         "POSTGRES_USER",
#         "POSTGRES_PASSWORD",
#         "POSTGRES_SERVER",
#         "POSTGRES_PORT",
#         "POSTGRES_DB",
#         "SECRET_KEY",
#         "USE_SQLITE_DB",
#         "MAIL_FROM",
#         "MAIL_PORT",
#         "MAIL_SERVER",
#         "MAIL_FROM_NAME",
#         "MAIL_USERNAME",
#         "MAIL_PASSWORD",
#         "MAIL_TSL",
#         "MAIL_SSL",
#         "USE_CREDENTIALS",
#         "TWILIO_ACCOUNT_SID",
#         "TWILIO_AUTH_TOKEN",
#         }
#     return var_dict





# if __name__ == '__main__':
#     # get from dict
#     for name in getVarNames:
#         getEnv(name)














# # var_dict = {"varHello":"1234"}

# # set from dict
# # for name, value in var_dict.items():
# #     setEnv(name, value)

# # # env1 = os.environ.get("VarHello")   # alt 2
# # # print("\n", env1, type(env1), "\n")

# # var_dict = {
# # "POSTGRES_USER":"mediavest",
# # "POSTGRES_PASSWORD":"F%K6L51KXGXs",
# # "POSTGRES_SERVER":"prospector-user-api.cpjevlwuwfix.eu-west-2.rds.amazonaws.com",
# # "POSTGRES_PORT":"5432",
# # "POSTGRES_DB":"ProSpector_User_API",
# # "SECRET_KEY":"NO_SECRET_KEY",
# # "USE_SQLITE_DB":"False",
# # "MAIL_FROM":"prospector.feedback@gmail.com",
# # "MAIL_PORT":"587",
# # "MAIL_SERVER":"smtp.gmail.com",
# # "MAIL_FROM_NAME":"ProSpector",
# # "MAIL_USERNAME":"prospector.feedback@gmail.com",
# # "MAIL_PASSWORD":"udrpwxglgjbspweo",
# # "MAIL_TSL":"True",
# # "MAIL_SSL":"False",
# # "USE_CREDENTIALS":"True",
# # "TWILIO_ACCOUNT_SID":"AC2c22cfe2b414f1941eefb50c5a1649e5",
# # "TWILIO_AUTH_TOKEN":"4b0e4a07643383388f2b031f91366ef2",
# # }

