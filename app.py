from flask import Flask

# 2. Create an app
app = Flask(__name__)

# 3. Define static routes
@app.route("/")
def hello_world():
    return "Hello, world!"


    