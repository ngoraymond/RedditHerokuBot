import os
import praw

def login():
    print ("Logging in..")
    try:
        r = praw.Reddit(username = os.environ["reddit_username"],
                password = os.environ["reddit_password"],
                client_id = os.environ["client_id"],
                client_secret = os.environ["client_secret"],
                user_agent = "Reddit C_Prest Bot 0.17")
        print ("Logged in!")
    except:
        print ("Failed to log in!")
    return r

def commentBotLogin():
    print ("Logging in..")
    try:
        r = praw.Reddit(username = os.environ["reddit_username_2"],
                password = os.environ["reddit_password"],
                client_id = os.environ["client_id_2"],
                client_secret = os.environ["client_secret_2"],
                user_agent = "Reddit TopCom Bot 0.17")
        print ("Logged in!")
    except:
        print ("Failed to log in!")
    return r