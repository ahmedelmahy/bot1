

  
#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
from solutions import  txtArray


app = Flask(__name__)
ACCESS_TOKEN = 'EAAFLBvAmOd0BAKVKAF3df5Sghin1OmB73pAMiQz0Hb8731vsFEg2Xz1xCIa7QECQ9r49gzAVTUXVjTXSNb11Sqft5X2TNf4VSvL60MTLD337ZBZBR95kxtZCzQcZA3kSL6W3lTB31g3mNrZAq8vej7YaeUNFGPOKIORcYo478A94XyxMLnMT2'
VERIFY_TOKEN = 'TESTINGTOKEN'
bot = Bot(ACCESS_TOKEN)











#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text') == '9':
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text[0])
                    send_message(recipient_id, response_sent_text[1])
                #if user sends us a GIF, photo,video, or any other non-text item
                #if message['message'].get('attachments'):
                #    response_sent_nontext = get_message()
                #    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    
    sample_responses = ['https://druggo-app.github.io/rosheta/imgs/{}.jpg'.format(i) for i in range(1,251)]
    # return selected item to the user
    i = random.choice(range(1,255))
    img = sample_responses[i]
    txt = txtArray[i]
    return (img, txt)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()


