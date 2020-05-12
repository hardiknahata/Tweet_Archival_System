# Tweet_Archival_System

LINK: https://twitter-archival-system.el.r.appspot.com/

This is a Flask Application which is served on the Google App Engine. The best part about App Engine is that it takes care of the server envoronment and lets us concentrate on just code.

So the main.py file instantiates the Flask object which renders the Form (powered by Flask_WTF) to the webpage. The HTML file is placed in the templates folder, and the optional CSS,JS files are placed in the Static folder.

The template folder further has 2 files called base and index. The base file has the basic structure which is extended by child templates. This is powered by Jinja templates, which is really powerful for developing bigger projects with multiple webpages. Jinja also provides ways to access variables from Flask for ease between both Python and Web Tech.

For accessing the tweets, I have used the tweepy library. Authentication keys which are given by Twitter to a developer are accessed from the file called Twitter_Authentication.py . I haven't shared the file on the repo for obvious reasons. But this problem can be overcomed by saving the API keys in .env so that the server holds the keys safely.

The requirements.txt file holds all the necessary libraries required to run our application. The Google AppEngine automatically provides an environment satisfied with the requirements mentioned in this file.

The App.yaml file is a configuration file which tells the App Engine which version of Python do we require in the runtime environment.

The code has necessary comments which will further explain the approach.

Thanks for reading!

