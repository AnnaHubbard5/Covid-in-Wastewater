from flask import Flask, request, jsonify
from flask_cors import CORS
from src.Wastewater import createWastewaterCounties as cwc
from src.Email import quickstart as qs
import logging


app = Flask(__name__)
CORS(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

@app.route('/jsonfile')
def getjson():
    # pass in county, plantId, date
    county = request.args.get('county')
    logging.debug(f'Received request for county: {county}')
    if county is None:
        print('County parameter not found')
        return jsonify({})
    
    print(county)
    chris = cwc.ret_object_for_Chris(county)
    print(chris)
    
    response = jsonify(chris)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    return response



@app.route('/')
def home():
    # Get the argument from the request
    arg = request.args.get("arg", default="")

    db = cwc.get_dict_from_json("./src/email_database.json")
    x = False
    if request.args.get("email") not in db or request.args.get("email") == "jkelleran@scu.edu":
        db[request.args.get("email")] = {}
        db[request.args.get("email")]['county'] = request.args.get("county")
        db[request.args.get("email")]['threshold'] = request.args.get("threshold")
        cwc.write_dict_to_json(db, "./src/email_database.json")
        percentile = cwc.getAveragePercentage(request.args.get("county"), None)
        if percentile == -1:
            percentile = "Data not reported. N/A"
        qs.send_email(request.args.get("email"), request.args.get("county"), request.args.get("threshold"), percentile, True)

    else:
        print("Your email is already in use")
        return jsonify({'error': "Your email is already in use"})

    # Use the argument in the home function
    
    print(request.args.get("email"), request.args.get("county"), request.args.get("threshold"))
    return jsonify({})



if __name__ == '__main__':
    app.run(debug=True)