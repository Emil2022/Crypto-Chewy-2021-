import json
from flask import Flask, render_template, request 

app = Flask(__name__)
@app.route('/')
def index():
  #be at 0, if someone in start submits a distance they get 5 chewycoins
  # chewycoins = determine_points(default_coins, points_per_record 
  chewycoins = 0
  # print(submitted_distance)
  return render_template('index.html', chewycoins=chewycoins)

@app.route('/inputwalk')
def inputwalk():
  return render_template('inputwalk.html')

@app.route('/start')
def start():
  chewycoins = '12'
  return render_template('start.html', chewycoins=chewycoins)

@app.route('/history')
def history():
  return render_template('history.html')


@app.route('/rewards')
def rewards():
  return render_template('rewards.html')
  
@app.route('/clicked', methods=['POST']) # creates a route with the path "/clicked" with the single method "POST"
def buttonClicked():
	data = request.data.decode() # gets the data from the user and puts it in the data variable
	print(data) # will print the data to the output console.
	return 'done' # this won't actually be displayed to the user

@app.route('/submitted', methods=['POST'])
def distanceSubmitted():
  data = request.data.decode()
  print(data)
  return data

# @app.route('/submitted', methods=['POST

app.run('0.0.0.0',8080)

