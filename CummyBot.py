import dataset
import praw
import sqlalchemy




def main():
    true = True

    reddit = praw.Reddit(client_id='u_g1d7tgpI-wcQ',
                         client_secret='bVpo6TYomjKvR_MUjYhnqsNDb0s',
                         username='CummyLover2000',
                         password='Emilia11',
                         user_agent='CummyLover2000 by u/Dplepler')



    subreddit = reddit.subreddit("copypasta")

    

    db = dataset.connect('sqlite:///CommentIDs.db')

    db.create_table('replied_to')
   
    db['replied_to'].create_column('comment_id', sqlalchemy.String)

  
    for comment in subreddit.stream.comments():
        if comment.author == "CummyBot2000":
           
            if db['replied_to'].find_one(comment_id=comment.id) == None:
                    random_Submission = reddit.subreddit('copypasta').random()
                    try:
                        comment.reply(random_Submission.selftext)
                        db['replied_to'].insert(dict(comment_id=comment.id))
                        print("posted")
                    except:
                        print("Cooldown")
            
   

if __name__ == "__main__":
    main()