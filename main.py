import pandas as pd
from telethon.sync import TelegramClient

from data import config

messages_matrix = []
with TelegramClient('edulix_full_dump', config.API_ID, config.API_HASH) as client:
    for message in client.iter_messages('edulix'):
        messages_matrix.append([message.raw_text, message.file.id if message.file else None, str(message.audio.id) if message.audio else None, str(message.video.id) if message.video else None])

df = pd.DataFrame(messages_matrix, columns=['raw_text','file_id', 'audio_id', 'video_id'])
df.to_csv('dump/full_messages_dump.csv', index=False)
