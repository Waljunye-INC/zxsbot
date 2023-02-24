from telethon import TelegramClient, events, sync
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

client = TelegramClient('base_session', api_id, api_hash)
client.start()

array_of_redirects = [os.environ.get('REDIRECT_FROM_' + str(i)) for i in range(1, int(os.environ.get('NUMBER_OF_CHANELS')) + 1) ]

print(array_of_redirects)


@client.on(events.NewMessage(array_of_redirects))
async def reply(event):
    message = event.message
    print("[", end='')
    print(message.date, end='')
    print(']', end='user_id=')
    print(message.from_id.user_id, end=': ')
    print(message.text)

    await client.forward_messages(os.environ.get('REDIRECT_TO'), [message])


with client:
    client.loop.run_forever()
