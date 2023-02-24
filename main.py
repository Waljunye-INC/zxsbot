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


@client.on(events.NewMessage(os.environ.get('REDIRECT_FROM')))
async def reply(event):
    message = event.message
    print(message.date)
    await client.forward_messages(os.environ.get('REDIRECT_TO'), [message])


with client:
    client.loop.run_forever()
