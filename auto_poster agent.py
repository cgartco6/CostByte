import schedule
import time
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.page import Page
from instabot import Bot
import tweepy

class AutoPosterAgent:
    def __init__(self, facebook_config, instagram_config, twitter_config):
        self.facebook_config = facebook_config
        self.instagram_config = instagram_config
        self.twitter_config = twitter_config
        
        # Initialize Facebook API
        FacebookAdsApi.init(
            facebook_config['app_id'],
            facebook_config['app_secret'],
            facebook_config['access_token']
        )
        
        # Initialize Instagram Bot
        self.instagram_bot = Bot()
        self.instagram_bot.login(
            username=instagram_config['username'],
            password=instagram_config['password']
        )
        
        # Initialize Twitter API
        auth = tweepy.OAuthHandler(
            twitter_config['consumer_key'],
            twitter_config['consumer_secret']
        )
        auth.set_access_token(
            twitter_config['access_token'],
            twitter_config['access_token_secret']
        )
        self.twitter_api = tweepy.API(auth)
    
    def post_to_facebook(self, content):
        page = Page(self.facebook_config['page_id'])
        page.api(
            'post',
            fields='',
            params={'message': content}
        )
        print(f"Posted to Facebook: {content}")
    
    def post_to_instagram(self, content, image_path=None):
        if image_path:
            self.instagram_bot.upload_photo(image_path, caption=content)
        else:
            # Instagram requires an image, so we'll create a text-based image
            self._create_text_image(content)
            self.instagram_bot.upload_photo("text_image.jpg", caption=content)
        print(f"Posted to Instagram: {content}")
    
    def post_to_twitter(self, content):
        self.twitter_api.update_status(content)
        print(f"Posted to Twitter: {content}")
    
    def schedule_post(self, platform, content, post_time, image_path=None):
        schedule.every().day.at(post_time).do(
            lambda: self._post_to_platform(platform, content, image_path)
        )
    
    def _post_to_platform(self, platform, content, image_path=None):
        if platform == "facebook":
            self.post_to_facebook(content)
        elif platform == "instagram":
            self.post_to_instagram(content, image_path)
        elif platform == "twitter":
            self.post_to_twitter(content)
    
    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
