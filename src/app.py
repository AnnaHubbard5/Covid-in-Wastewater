from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # Get the argument from the request
    arg = request.args.get("arg", default="")
    
    # Use the argument in the home function
    message = f"Hello from Python! You passed in the argument: {arg}"
    print(arg)
    return message



if __name__ == '__main__':
    app.run(debug=True)