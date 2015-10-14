from flask import Flask, render_template, session

@app.route("")
@app.route("/home")
def home():
    return render_template("home.html")
    
@app.route("/login", methods=["GET","POST"])
def login(): #confirm uid and password exists
        if request.method == "GET":
            if 'logged_in' in session and session['logged_in']:
                return redirect(url_for("posts"))
            else:
                return render_template("home.html")
        else:
            assert(request.method == "POST")
            #VERIFY USER, SESSION TRUE
            #otherwise redirect login with error message

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for("login"))

@app.route("/register", methods=["GET","POST"]) #add account to table
def register():
    pass

@app.route("/profile", methods=["GET","POST"]) #list of all user posts + most recent comments
def profile():
    pass

@app.route("/posts") #shows all posts, title + most recent comment
def posts():
    pass

@app.route("/posts/<pid>") #for individual posts
def onepost():
    #create comments
    pass

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)