
from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *
from support import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#This route will get the data for the charts
@app.route('/routeOne', methods=['GET', 'POST'])
def routeOne():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        category = post_data['category']
        state = post_data['state']
        currency = post_data['currency']
        country = post_data['country']
        start_date = post_data['startDate']
        end_date = post_data['endDate']
        money_goal = float(post_data['moneyGoal'])
        backers = float(post_data['backers'])
        first_chart_data = data.first_chart(category, state, currency, country, start_date, end_date, money_goal, backers)
        return jsonify(first_chart_data)

@app.route('/fetchDrillDownData', methods=['GET', 'POST'])
def routeTwo():
    if request.method == 'POST':
        data = Data()
        support = Support()
        post_data = request.get_json()
        date = post_data['date']
        month_as_digit = support.convert_stringDate_to_numberDate(date)
        year = support.get_year(date)
        data.get_data_for_drilldown(month_as_digit, year)
        return jsonify('HI')

if __name__ == '__main__':
    app.run()
