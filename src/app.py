from flask import Flask, request, jsonify
from flask_cors import CORS
from src.Wastewater import createWastewaterCounties as cwc
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
    
    # Use the argument in the home function
    message = f"Hello from Python! You passed in the argument: {arg}"
    print(request.args.get("email"))
    return message



if __name__ == '__main__':
    app.run(debug=True)