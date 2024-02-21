from flask import Flask 
app = Flask(__name__)

@app.route('/profile/<user>')
def index(user):
	return "<h1>This profile is for %s</h1>" % user

@app.route('/id/<int:user_id>')
def user(user_id):
	return "<h1>This profile is for %d</h1>" % user_id

app.run()