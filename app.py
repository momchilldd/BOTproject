from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horoscope', methods=['POST'])
def horoscope():
    date = request.form['date']
    sign = request.form['sign']
    response = requests.get(f'https://horoscopes.azurewebsites.net/horoscope')  # Replace with a real horoscope API
    horoscope_data = response.json()
    return render_template('horoscope.html', horoscope=horoscope_data)

if __name__ == '__main__':
    app.run(debug=True)
