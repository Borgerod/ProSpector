import os
from fastapi import BackgroundTasks
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os
from twilio.rest import Client
import phonenumbers

load_dotenv('.env')

class Input:
	def __init__(self):
		self.otp_code = None
		self.phone_number = ""

	@property	
	def request_otp_code(self):
		return input("Please enter your verification code:")

	@property	
	def request_phone_number(self):
		self.phone_number = input("Please enter your phone number (with country code):")
		self.checkForCountryCode()
		return self.phone_number

	def checkForCountryCode(self):
		'''
		checks if phonenumber contains countrycode, 
		if not it will add default calue "+47"
		'''
		try:
			phonenumbers.parse(self.phone_number)
		except phonenumbers.NumberParseException:
			self.phone_number = '+47'+self.phone_number
	
class Verification:
	def __init__(self) -> None:
		self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
		self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.verify_sid = 'VA0af259d1f90eef02d4cfe86f45e64b8f'
		self.client = None
		self.phone_number = None
		self.otp_code = None
		self.is_valid = False
		
	def getClient(self):
		self.client = Client(self.account_sid, self.auth_token)

	def sendVerificationSMS(self):
		verification = self.client.verify.services(
			self.verify_sid
		).verifications.create(to=self.phone_number, channel='sms')
		print(verification.status)
	
	async def checkVerificationCode(self, otp_code:str, phone_number:str):
		self.getClient()
		verification_check = self.client.verify.services(
			self.verify_sid
			).verification_checks.create(to=phone_number, code=otp_code)
		print(verification_check.status)
		if verification_check.status == 'approved':
			return True
			# self.is_valid = True
		

	# @property
	# def getValidation(self):
	# 	return self.is_valid

	def checkForCountryCode(self):
		'''
		checks if phonenumber contains countrycode, 
		if not it will add default calue "+47"
		'''
		try:
			phonenumbers.parse(self.phone_number)
		except phonenumbers.NumberParseException:
			self.phone_number = '+47'+self.phone_number

	def requestVerification(self, phone_number:str):
		'''
		the class manager, class this to run verification process
		'''
		self.phone_number = phone_number
		self.checkForCountryCode()
		self.getClient()
		self.sendVerificationSMS() 
		
		
		#! OLD: check verification call 
		# self.otp_code = user_input.request_otp_code
		# self.checkVerificationCode()
		# if self.getValidation:
		# 	allowingAcsess()



def allowingAcsess():
	'''
			placeholder
	'''
	print("Accsess allowed --> creating account")

# otp_code:str

# async def send_sms_async(sms_to:str):
# 	await Verification().requestVerification(phone_number = sms_to)
	 
# async def recieve_otp_code_async(sms_to:str, otp_code:str):
# 	return await Verification().checkVerificationCode(otp_code)


'''
for sms:
http://127.0.0.1:8000//verification/phone/send_verification?sms_to=$phone_number

eksempel:
'http://127.0.0.1:8000/ResetPassword/Authentication?email_to=$email&verify_num=$verifyNum');

'''