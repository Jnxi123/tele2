import openai
import telebot

YOUR_OAPI_KEY = "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"
YOUR_TBOT_TOKEN = "6159128326:AAFXf62Awz4-EDkFZ0TPqtAlrSoyOtR1bBY"

# Initialize the ChatGPT and DALL-E models
openai.api_key = YOUR_OAPI_KEY
model_engine = "text-davinci-003"

# Create a TeleBot instance
bot = telebot.TeleBot(YOUR_TBOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """<b>Hi! I am Neo AI</b> <i>(NEW AI)</i> an assistant bot made to be the NEW 
    AI, I'll generate responses to your messages with my own intellect. To get started, just send me a /help to get 
    the list of all the commands""")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, """
Here are the Available command(s)
<b>1: /Start to start the bot</b>
<b>2: /help to get this help text again</b>
<b>3: /nai if you have anything you want to ask or tell</b>\n                        
<i>Note: This bot is still in development.</i>\n
<pre>This bot is created by</pre>\n<b>Neo AI</b>
<b>Join NEO AI</b>\n<a href='https://t.me/NeoAiPortal'>Neo AI</a>""")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Hi there! I'm Nai, your funny and sarcastic AI friend. How can I help you today?")


# noinspection PyArgumentList
@bot.message_handler()
def respond_to_message(message):
    if "nai" in message.text.lower():
        # Use the GPT-3 model to generate a response
        response = openai.Completion.create(
            engine=model_engine,
            prompt="Nai, respond to the user in a funny and sarcastic way: " + message.text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

        # Send the response to the user
        bot.send_message(message.chat.id, response)


def run_bot():
    try:
        # Start the bot
        bot.polling(none_stop=True, timeout=123)
    except Exception as e:
        # If the bot crashes, print the error message and start the bot again
        print(e)
        run_bot()


# Run the bot indefinitely
while True:
    run_bot()
