from flask import Flask, render_template, flash, jsonify, make_response
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
import tweepy
from Twitter_Authentication import ACCESS_KEY,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiop987654321'

#Defining the Form Fields
class getTweets(FlaskForm):
    query = StringField('Enter Search Query',validators=[InputRequired()])


#First visit to app renders this Form
@app.route("/")
def form():
    form = getTweets()
    return render_template('index.html', form=form) #Call to render our HTML webpage


#Render results Post Submission
@app.route("/", methods = ['POST'])
def form_post():
    form = getTweets()
    if form.validate_on_submit():
        auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) #Authorization for accessing
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)               #Twitter API 
        api = tweepy.API(auth)
        query = form.query.data     #Stores the query entered by user in the query variable
        form.query.data = ""        #Clears the query field post submission
        max_tweets = 30             #Defining number of tweets to be retrieved
        tweet_results = {}          #Empty dictionary to store the tweets
        i=1                         #A simple counter for tweet_count
        
        #result_type: options are popular,recent,mix. Since we want latest we select recent.
        #lang: en is english
        #tweet_mode: by default twitter only returns 140chars for retweets, in order to access full tweet we use extended mode.
        for tweet in tweepy.Cursor(api.search, q=query, result_type="recent", lang = "en", tweet_mode="extended").items(max_tweets):
            if "retweeted_status" in dir(tweet):
                tweet_results[i] = (tweet.retweeted_status.full_text)
            else:
                tweet_results[i] = (tweet.full_text)
            i=i+1

        return render_template('index.html',tweet_results=tweet_results,form=form)  #call to HTML page for displaying results     

if __name__ == '__main__':
    app.run(debug=True)
