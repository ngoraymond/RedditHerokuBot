import os

def login():
    print ("Logging in..")
    try:
        r = praw.Reddit(username = os.environ["reddit_username"],
                password = os.environ["reddit_password"],
                client_id = os.environ["client_id"],
                client_secret = os.environ["client_secret"],
                user_agent = "Reddit C_Prest Bot 0.1")
        print ("Logged in!")
    except:
        print ("Failed to log in!")
    return r