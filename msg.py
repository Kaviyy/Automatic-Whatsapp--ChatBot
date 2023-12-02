from twilio.rest import Client

account_sid = 'ACeb91dad56dfa800c061d7f2e1193ae7d'
auth_token = '5d6de521fd32f43c34ebbc68d2b1baad'
client = Client(account_sid, auth_token)

def send_msg():
      message = client.messages.create(
      from_='whatsapp:+14155238886',
      body='my tom',
      to='whatsapp:+917293138223'  
)

      print(message.sid)
send_msg()