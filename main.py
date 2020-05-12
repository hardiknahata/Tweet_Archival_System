from flask import Flask, render_template, flash, jsonify, make_response
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
import tweepy
from Twitter_Authentication import ACCESS_KEY,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiop987654321'

#Defining the Form
class getTweets(FlaskForm):
    query = StringField('Enter Search Query',validators=[InputRequired()])


#First visit to app renders form
@app.route("/")
def form():
    form = getTweets()
    return render_template('index.html', form=form)


#Render results post Submission
@app.route("/", methods = ['POST'])
def form_post():
    form = getTweets()
    if form.validate_on_submit():
        auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        query = form.query.data
        form.query.data = ""
        max_tweets = 30
        tweet_results = {}
        i=1
        for tweet in tweepy.Cursor(api.search, q=query, result_type="recent", lang = "en", tweet_mode="extended").items(max_tweets):
            if "retweeted_status" in dir(tweet):
                tweet_results[i] = (tweet.retweeted_status.full_text)
            else:
                tweet_results[i] = (tweet.full_text)
            i=i+1

        return render_template('index.html',tweet_results=tweet_results,form=form)
        # headers = {"Content-Type": "application/json"}
        # return make_response( tweet_results, 200, headers ) 
        
        
if __name__ == '__main__':
    app.run(debug=True)