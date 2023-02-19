from flask import Flask, request
from flask_cors import CORS
import sys
sys.path.append('/Users/joshkelleran/Covid-in-Wastewater/')
from src.Wastewater import createWastewaterCounties as cwc

app = Flask(__name__)
CORS(app)

@app.route('/jsonfile')
def getjson():
    #pass in county, plantId, date
    arg = request.args.get("arg", default="")
    return cwc.ret_object_for_Chris(request.args['county'], request.args['plantId'], request.args['date'])


@app.route('/')
def home():
    # Get the argument from the request
    arg = request.args.get("arg", default="")
    
    
    # Use the argument in the home function
    message = f"Hello from Python! You passed in the argument: {arg}"
    #print(arg)
    #print(request.args.get("email"))
    print(request.args['email'])
    return message



if __name__ == '__main__':
    app.run(debug=True)