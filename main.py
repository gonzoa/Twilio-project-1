import schedule
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)



message = client.messages \
                .create(
                     body="I will always love you. No matter what.",
                     from_='+19292961163',
                     to='+13464008794'
                 )

print(message.sid)

schedule.every().day.at("23:40").do(send_sms)