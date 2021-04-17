from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 7500


@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():


    
    year_list = [1990,1995,2000,2005,2010]

    sea_level = [0.5,16,24.4, 30, 38]

                

    result_dict = {
        'year': year_list,
        'title': 'Mean Sea level ',
        'subtitle': 'Source: ourworldindata.org',
        's_level': sea_level
        
    }

    return jsonify(result_dict)

    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
