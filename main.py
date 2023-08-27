# 6417872030:AAG352xW0_9oyEngmdvV8pZ3GDo92kA319w

import requests
import json

# Replace with your actual bot token
BOT_TOKEN = '6417872030:AAG352xW0_9oyEngmdvV8pZ3GDo92kA319w'

# Function to send a message
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    return response.json()

# Main function
def main():
    print("Bot is running...")
    offset = None

    while True:
        # Get updates from Telegram
        response = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}')
        updates = response.json().get('result', [])

        # Process each update
        for update in updates:
            offset = update['update_id'] + 1
            chat_id = update['message']['chat']['id']
            text = update['message']['text']

            if text == '/start':
                send_message(chat_id, "Hello! I'm your bot.")
            elif text == '/help':
                send_message(chat_id, "I'm here to help!")
            

if __name__ == '__main__':
    main()
