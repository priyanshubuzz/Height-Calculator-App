from flask import Flask, render_template, request
from database import Database
from send_email import send_email
import traceback

app = Flask(__name__)
db = Database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/success", methods=["GET", "POST"])
def success():
    try:
        if request.method == "POST":
            email = request.form["email"]
            height = request.form["height"]
            existing_emails = db.extract_emails()
            if email not in existing_emails:
                db.insert(email, height)
                #this is for sending height and email to sendmail after insertion
                total_heightsum, total_heightlength = sum(db.extract_heights()), len(db.extract_heights())
                send_email(email, height, total_heightsum//total_heightlength, total_heightlength)
                return render_template("success.html")
            else:                                                                                                                             
                return render_template("index.html",
                text = "Email already exists, try again!")
        elif request.method == "GET":
            return render_template("success.html")
    except: 
        return traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=False)