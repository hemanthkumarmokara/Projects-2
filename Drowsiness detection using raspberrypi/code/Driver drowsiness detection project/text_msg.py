from twilio.rest import Client

account_sid ="AC9ecfeef37fc35c0e91eaed2b72b2117c" # Put your Twilio account SID here
auth_token ="117e11f4731a63fae4796fa753a417d7" # Put your auth token here

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
		to="+919676097157", # Put your cellphone number here
		from_="+15169284482", # Put your Twilio number here
		body="This is my message that I am sending to my phone!")
