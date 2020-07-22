import praw
import time
import os
import pdb
import re
import random
import login


def main():
    poster = login.login()
    commentBot = login.commentBotLogin()
    subred = poster.subreddit('College_Prestige')
    risingSubs = ['all','funny','memes','dankmemes','wallstreetbets','stocks']
    index = 0
    while True:
        print("--------------------------------------")
        # Get top 5 rising posts in the risingSubs list
        currentSub = poster.subreddit(risingSubs[index])
        print('r/'+risingSubs[index])
        for submission in currentSub.rising(limit=5):
            print(submission.title)
            #print(submission.permalink)
            #print(submission.url)
            urlLink = None
            selfText = None
            #Determines if it is a selftext or a url post
            if len(submission.selftext) != 0:
                selfText = submission.selftext
            else:
                urlLink = submission.url
            #Posts it with title, time of post, subreddit it was from
            Title = submission.title+' from r/'+risingSubs[index]+' at '+time.ctime(time.time())
            subred.submit(Title, selftext=selfText, url=urlLink , spoiler=submission.spoiler,
            nsfw=submission.over_18)
            #Mark down the post was made
            with open('posts_made.txt','a') as f:
                try:
                    f.write(submission.permalink+'\n')
                except:
                    f.write('\n')
            time.sleep(random.randint(5,30))
            #Create permalink of original post as a comment
            for subReply in poster.redditor(os.environ['reddit_username']).submissions.new(limit=1):
                poster.submission(id=subReply.id).reply('From: https://www.reddit.com'+submission.permalink)
                time.sleep(random.randint(3,10))
                #Upvote the repost from my other bot
                #commentBot.submission(id=subReply.id).upvote()
                time.sleep(random.randint(3,10))
                if submission.permalink[3:7] != 'rpan':
                    for comment in submission.comments:
                        commentBot.submission(id=subReply.id).reply(comment.body)
                        time.sleep(random.randint(3,10))
        #move on to the next subreddit
        index = (index+1)%(len(risingSubs))
        #wait up to 10 minutes
        sleeptime = random.randint(60,600)
        print('Sleeping for '+str(sleeptime)+' seconds')
        time.sleep(sleeptime)

if __name__ == "__main__":
    main()