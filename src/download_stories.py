import instaloader
import os


class InstaStories():
    def __init__(self):        
        self.obj = instaloader.Instaloader(save_metadata=False, 
            filename_pattern="{owner_username}_{date_utc}", download_video_thumbnails='')
        self.obj.load_session_from_file(os.getenv('SESSION_NAME'))

    def update(self):
        self.obj.download_stories(None, True, 'stories')