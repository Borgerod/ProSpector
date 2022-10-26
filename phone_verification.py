import os
from twilio.rest import Client
import phonenumbers

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
	
	def checkVerificationCode(self):
		verification_check = self.client.verify.services(
			self.verify_sid
			).verification_checks.create(to=self.phone_number, code=self.otp_code)
		print(verification_check.status)
		if verification_check.status == 'approved':
			self.is_valid = True

	@property
	def getValidation(self):
		return self.is_valid

	def requestVerification(self):
		'''
		the class manager, class this to run verification process
		'''
		user_input = Input()
		self.phone_number = user_input.request_phone_number
		self.getClient()
		self.sendVerificationSMS() 
		self.otp_code = user_input.request_otp_code
		self.checkVerificationCode()
		if self.getValidation:
			allowingAcsess()

def allowingAcsess():
	'''
			placeholder
	'''
	print("Accsess allowed --> creating account")


if __name__ == "__main__":	
	Verification().requestVerification()
