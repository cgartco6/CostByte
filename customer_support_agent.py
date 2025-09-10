import nltk
from nltk.chat.util import Chat, reflections
import random
import sqlite3
from datetime import datetime

class CustomerSupportAgent:
    def __init__(self, db_path):
        self.db_path = db_path
        self.pairs = [
            [
                r"my name is (.*)",
                ["Hello %1! How can I help you today?",]
            ],
            [
                r"what is your name?",
                ["I'm Penny, your customer support assistant. How can I help you?",]
            ],
            [
                r"how are you?",
                ["I'm doing well, thank you! How can I assist you today?",]
            ],
            [
                r"(.*) (price|cost|how much)",
                ["HeadsUp AI is priced at R799 per month. Would you like to know more about our features?",]
            ],
            [
                r"(.*) (feature|what can|do)",
                ["HeadsUp AI offers real-time food cost tracking, price change alerts, waste monitoring, inventory automation, and more!",]
            ],
            [
                r"(.*) (demo|trial)",
                ["We'd be happy to schedule a demo for you! Please provide your email and we'll reach out to arrange a convenient time.",]
            ],
            [
                r"(.*) (contact|email|phone)",
                ["You can reach us at info@costbyte.co.za or call Nicholas at 0691081301. We're here to help!",]
            ],
            [
                r"(.*) (refund|guarantee)",
                ["We offer a full refund after 3 months of use if you're not satisfied with the results. We're confident you'll see savings!",]
            ],
            [
                r"(.*)",
                ["I'm not sure I understand. Could you please rephrase your question? Or you can contact us directly at info@costbyte.co.za for more specific inquiries.",]
            ]
        ]
        
        self.chatbot = Chat(self.pairs, reflections)
        self.setup_database()
    
    def setup_database(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS conversations
                     (id INTEGER PRIMARY KEY, timestamp TEXT, user_input TEXT, bot_response TEXT)''')
        conn.commit()
        conn.close()
    
    def respond(self, user_input):
        response = self.chatbot.respond(user_input)
        if not response:
            response = "I'm not sure I understand. Could you please rephrase your question?"
        
        # Log conversation to database
        self.log_conversation(user_input, response)
        
        return response
    
    def log_conversation(self, user_input, response):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        timestamp = datetime.now().isoformat()
        c.execute("INSERT INTO conversations (timestamp, user_input, bot_response) VALUES (?, ?, ?)",
                  (timestamp, user_input, response))
        conn.commit()
        conn.close()
    
    def get_conversation_history(self, limit=10):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT timestamp, user_input, bot_response FROM conversations ORDER BY timestamp DESC LIMIT ?", (limit,))
        results = c.fetchall()
        conn.close()
        return results
