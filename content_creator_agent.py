import openai
import requests
import json
from datetime import datetime

class ContentCreatorAgent:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.platforms = ["facebook", "instagram", "twitter", "linkedin", "tiktok"]
        
    def generate_content(self, topic, platform):
        prompt = f"Create engaging marketing content about {topic} for {platform} platform. Make it professional and appealing to restaurant and hotel owners."
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        
        return response.choices[0].text.strip()
    
    def create_multiple_posts(self, topic, num_posts=5):
        posts = {}
        for platform in self.platforms:
            posts[platform] = []
            for i in range(num_posts):
                content = self.generate_content(topic, platform)
                posts[platform].append({
                    "content": content,
                    "scheduled_time": None,
                    "posted": False
                })
        return posts
    
    def schedule_posts(self, posts, schedule_times):
        # Schedule posts for specific times
        for platform in posts:
            for i, post in enumerate(posts[platform]):
                if i < len(schedule_times):
                    post["scheduled_time"] = schedule_times[i]
        return posts
