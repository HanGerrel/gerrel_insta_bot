import telebot
import os
from datetime import datetime, time
from download_stories import InstaStories

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

viewed_stories = list()
insta_stories = InstaStories()


vs = open('./viewed_stories', 'a+')
for line in vs:
    viewed_stories.append(line[:len(line)-1])
vs.close()


@bot.message_handler(content_types=['text'])
def get_instagram_stories(message):
    if(message.chat.id == int(os.getenv('CHAT_ID'))):
        insta_stories.update()
        file_names = os.listdir('stories/')

        for name in file_names:
            if name not in viewed_stories:
                vs = open('./viewed_stories', 'a')
                viewed_stories.append(name)
                if(name[-3:] == 'jpg'):
                    photo = open('stories/' + name, 'rb')
                    bot.send_photo(message.chat.id, photo)
                    photo.close()

                if(name[-3:] == 'mp4'):
                    video = open('stories/' + name, 'rb')
                    bot.send_video(message.chat.id, video)
                    video.close()
                vs.write(viewed_stories[len(viewed_stories)-1] + '\n')
                vs.close()

bot.polling(none_stop=False, interval=0, timeout=60)