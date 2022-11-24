from twilio.rest import Client
import phonenumbers

# Nessasary for importing config 
import sys; sys.path.insert(0, '.')
from virtual_env.config import Config


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
		config = Config.getPhoneConfig # Get Appropriate config variables 
		self.account_sid: str = config["TWILIO_ACCOUNT_SID"]
		self.auth_token: str = config['TWILIO_AUTH_TOKEN']
		self.client = None
		self.verify_sid = None
		self.phone_number = None
		self.otp_code = None
		self.is_valid = False

	def gen_service(self):
		self.service = self.client.verify.v2.services.create(friendly_name='ProSpector Verification')
		self.verify_sid = self.service.sid

	def getClient(self):
		self.client = Client(self.account_sid, self.auth_token)


	def sendVerificationSMS(self):
		verification = self.client.verify.services(
			self.verify_sid
		).verifications.create(to=self.phone_number, channel='sms')
		print(verification.status)
		return self.verify_sid
	
	async def checkVerificationCode(self, verify_sid:str, otp_code:str, phone_number:str):
		self.getClient()
		verification_check = self.client.verify.services(
			verify_sid
			).verification_checks.create(to=phone_number, code=otp_code)
		print(verification_check.status)
		if verification_check.status == 'approved':
			return True

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
		self.gen_service()
		self.sendVerificationSMS() 
		return self.verify_sid

async def send_sms_async(sms_to:str):
	await Verification().requestVerification(phone_number = sms_to)
	 
'''
for sms:
http://127.0.0.1:8000//verification/phone/send_verification?sms_to=$phone_number

eksempel:
'http://127.0.0.1:8000/ResetPassword/Authentication?email_to=$email&verify_num=$verifyNum');

'''