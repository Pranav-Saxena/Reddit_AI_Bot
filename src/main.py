from groq_api import get_post_content
from utils.logger import setup_logger
import praw
import schedule
import time
from datetime import datetime

logger = setup_logger('reddit_bot', 'reddit_bot.log')
sub = "Vit"

def authenticate():
    reddit = praw.Reddit(
        client_id='F_TvpHXBWCBXzn7gZ1rdfA',
        client_secret='wDfNe_5ztRV0PpoAKm4YB6kmwGcn1g',
        username='Potential_Plantain18',
        password='ai_bot123',
        user_agent='script:ai_bot:v1.0 (by /u/Potential_Plantain18)'
    )
    return reddit

def post_content():
    try:
        reddit = authenticate()
        prompt = "Generate engaging content for reddit post"
        title,message = get_post_content(prompt)
        subreddit = reddit.subreddit(sub)
        
        try:
            submission = subreddit.submit(title=title, selftext=message)
        except Exception as e:
            if "SUBMIT_VALIDATION_FLAIR_REQUIRED" in str(e):
                flairs = subreddit.flair.link_templates
                flair_id = None
                for flair in flairs:
                    flair_id =  flair['id']
                    break
                submission = subreddit.submit(title=title, selftext=message, flair_id= flair_id)
            else:
                raise e
        print("Post Submitted")
        logger.info('Post submitted successfully')
    except Exception as e:
        logger.error(f'Error occurred: {e}')

def comment_on_posts():

    try:
        reddit = authenticate()
        subreddit = reddit.subreddit(sub)  
        for submission in subreddit.new(limit=5): 
            try:
                if any(comment.author == reddit.user.me() for comment in submission.comments):
                    continue
                
                prompt = f"Generate a friendly and relevant comment for the post titled: {submission.title}"
                comment_text, _ = get_post_content(prompt) 

                submission.reply(comment_text)
                print(f"Commented on post: {submission.title}")
                logger.info(f"Commented on post: {submission.title}")

            except Exception as e:
                logger.error(f"Error while commenting on post {submission.title}: {e}")
    except Exception as e:
        logger.error(f"Error occurred in comment generation: {e}")

def schedule_posts(posting_times):

    for post_time in posting_times:
        schedule.every().day.at(post_time).do(post_content)
        logger.info(f"Post Scheduled at {post_time}")

def schedule_comments(commenting_times):
    for comment_time in commenting_times:
        schedule.every().day.at(comment_time).do(comment_on_posts)
        logger.info(f"Comment Scheduled at {comment_time}")

if __name__ == '__main__':
    
    posting_times = ["09:00", "14:00", "18:28"]
    commenting_times = ["10:00", "15:00", "18:29"]
    schedule_posts(posting_times)
    schedule_comments(commenting_times)

    while True:
        schedule.run_pending()
        time.sleep(1)
