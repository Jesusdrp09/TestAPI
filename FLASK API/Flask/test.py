from flask import Flask, request, render_template
import os 

app = Flask(__name__)

@app.route("/get")
def get():
    return f"{request.args["username"]}"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        return f"Tu nombre es {request.form["name"]}"
    
@app.route("/login", methods=["GET", "POST"])
def register(): 
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        return f"{request.form["username"]}, {request.form["password"]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=True)