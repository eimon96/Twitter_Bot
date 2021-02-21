import tweepy
import datetime
#import json
import time

# Authenticate to Twitter


CONSUMER_KEY = ""	#add
CONSUMER_SECRET = ""	#add
ACCESS_TOKEN = ""	#add
ACCESS_TOKEN_SECRET = ""#add

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK!")
except Exception as e:
    print("Error during authentication..")
    raise e



# --------------------------------------- #

#dt =  datetime.datetime.now()

#api.update_status(f"Whatever, {dt}")

#api.update_status("Hello, World!")

# -------------------------------------- #

#timeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{tweet.user.name} said {tweet.text}")

# --------------------------------------- #

#A_USERNAME =

#user = api.get_user(A_USERNAME)

#print("User details:")
#print(user.name)
#print(user.description)
#print(user.location)

#print("Last 20 Followers:")
#for follower in user.followers():
#    print(follower.name)

# ------------------------------------- #

#A_USERNAME =

#api.create_friendship("A_USERNAME")

# ------------------------------------- #

#api.update_profile(description = "I'm a bot dabadee daba da")

# -------------------------------------- #
'''

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected..")

    def on_connect(self):
        print("Connection established!")

    def on_disconnect(self):
        print("Connection lost..")


api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Cyberpunk", "2077"], languages=["en"])

'''
# ------------------------------------------------------------- #

user = api.get_user("A_USERNAME")
rec = user.id_str

sText = ["gamw th mana sou", "ante gamhsou", "na fas skata",
         "malaka", "gamw to spiti sou", "mpetovlaka", "papara",
         "hlithie", "gamietai h mana sou me ta kourtinoksula", "psofa"]

while True:
    r = random.randint(1, len(sText))
    dm = api.send_direct_message(rec, sText[r - 1])
    time.sleep(96)

# ------------------------------------------------------------- #

