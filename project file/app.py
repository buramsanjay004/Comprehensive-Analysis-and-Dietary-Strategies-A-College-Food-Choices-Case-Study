from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("boot.html")

@app.route("/dashboard")
def dashboard():
    return render_template("boot.html")

@app.route("/story")
def story():
    return render_template("boot.html")

if __name__ == "__main__":
    app.run(debug=True)