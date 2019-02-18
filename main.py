from flask import Flask, render_template, request
from map import *
from api import *
import sys

app = Flask(__name__)

@app.route("/",methods = ['GET'])
def home():

    return render_template("home.html")


@app.route("/map/",methods = ['POST'])
def create_map():

    location_map = create_location_map()

    nickname = request.form['nickname']
    number = request.form['number_of_friends']

    api = get_api()

    try:
        number = int(number)
        user = get_the_user(api, nickname)

    except:
        sys.exit()

    for friend in user.friends(count=number):
        if not friend.location:
            continue

        location = get_location(friend.location)
        add_map_child(location_map, location, friend.name + '\n' + friend.location)


    return location_map._repr_html_()



if __name__ == "__main__":
    app.run()