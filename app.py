from flask import Flask

#create a simple flask application
app=Flask(__name__)

#Flask app routing
@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to world"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to index page"

#variable rule
@app.route("/sucess/<score>")
def sucess(score):
    return "The person has passed and the score is : " + score


if __name__=="__main__":
    app.run(debug=True)
