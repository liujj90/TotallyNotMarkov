import praw
import pandas as pd
#connect to reddit
r = praw.Reddit('TotallyNotMarkov')
# connect to r/totallynotrobots
subreddit = r.get_subreddit('totallynotrobots')

class getdata(object):
	def __init__(self, name, subreddit, filename):
		self.name = name
		self.subreddit = subreddit
		self.filename = filename
	def connect_and_get(self):
		r = praw.Redit(self.name)
		subreddit = r.get_subreddit(self.subreddit)
		posts = [post for post in subreddit.get_top_from_year(limit = 10000)]
		self.allposts = [{'Title':x.title, 'Post': ''.join(x.selftext), 'Upvotes':x.ups} for x in posts]
		self.df = pd.DataFrame(self.allPosts)
	def save_to_file(self):
		self.df.to_csv(self.filename)