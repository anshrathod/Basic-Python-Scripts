# send easy alert messages using:-
# Telegram (API)
# Email (Mailgun)
# SMS (Twilio)

# See the cred.py for credential details


from boltiot import Email, Sms
import requests, json, cred

def send_telegram_msg(message, ifprint = False):
    ''' Sends the message using Telegram API\n
        Return boolean about the success    '''

    url = "https://api.telegram.org/" + cred.telegram_bot_id + "/sendMessage"
    data = {
        'chat_id' : cred.telegram_chat_id,
        'text' : message
    }

    try:
        response = requests.request('POST', url, params = data)
        response_data = json.loads(response.text)

        if(ifprint):
            print('Telegram response is:')
            print(response_data)
        return response_data['ok']

    except Exception as e:
        print('An expection occured while sending an alert using Telegram! Details below:')
        print(e)
        return False

def send_mail(subject, body, ifprint = False):
    mailer = Email(cred.MAILGUN_API_KEY, cred.SANDBOX_URL, cred.SENDER_EMAIL, cred.RECIPIENT_EMAIL)
    response = mailer.send_email(subject, body)
    response_text = json.loads(response.text)

    if(ifprint):
        print(response_text)
    if response_text['message'] == 'Queued. Thank you.':
        return True
    else:
        return False

def send_sms(message, ifprint = False):
    sms = Sms(cred.account_sid, cred.auth_token, cred.to_number, cred.from_number)
    response = sms.send_sms(message)

    if(ifprint):
        print(response)

send_telegram_msg("Hi")
send_mail("Hi", "Hello")
send_sms("Hi")
