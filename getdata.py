import praw
#set up pretty printer
from pprint import pprint
import pandas as pd
#connect to reddit
r = praw.Reddit('TotallyNotMarkov')
# connect to r/totallynotrobots
subreddit = r.get_subreddit('totallynotrobots')


# retrieve top 1000 posts from this year
GetPosts = [x for x in subreddit.get_top_from_year(limit = 1000)]
#make dict out of posts
AllPosts =[{'Title': x.title, 'Post':''.join(x.selftext), 'Upvotes': x.ups} for x in GetPosts]

#port into pandas dataframe
df = pd.DataFrame(AllPosts)
#df.head()
#len(df.index) == 999

#save to csv
df.to_csv('postcontent.csv')