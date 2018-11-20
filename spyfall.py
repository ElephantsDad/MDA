#C:\Users\Asus\Projects\Environments\spyfall\Scripts\activate.bat
#cd C:\Users\Asus\Desktop\spyfall
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/rules")
def rules():
    return render_template('rules.html')

@app.route("/locations")
def locations():
    return render_template('locations.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
