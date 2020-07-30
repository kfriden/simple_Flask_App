#Kaitlyn Friden 2/25/2020 Python Web App
#Install Flask on your command line by typing in PIP install Flask if you don't already have Flask
#Run the program as any other Python program by typing python and then the name of the program
#Copy and paste the link provided into your browser after everything loads in the command line
#Click on the Login page when the website loads, fill out the form, when everything submits, a happy Pikachu will appear
#Your email, username and password that you supplied are then stored in the command line


from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        print(user, email, password)
        return render_template("details.html", content=user)
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return render_template("details.html")
    

if __name__ == "__main__":
    app.run(debug=True)