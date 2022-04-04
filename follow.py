from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import os
from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

working_directoy = os.getcwd()
df = pd.read_csv(os.path.join(working_directoy,'top_500_likes.csv'))
for u in list(set(df['username'])):

    users = [u]

    env_path = os.path.join(working_directoy,'scweet.env')
    following = get_users_following(users=users, env=env_path, verbose=0, headless=False, wait=4, limit=50, file_path=None)
    with open("following.txt", "a") as myfile:
        myfile.write(str(following))
    followers = get_users_followers(users=users, env=env_path, verbose=0, headless=False, wait=4, limit=50, file_path=None)
    with open("followers.txt", "a") as myfile:
        myfile.write(str(followers))
