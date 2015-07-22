from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def test():
    
    return render_template("student-search.html") 

@app.route("/student")
def get_student():
    """Show information about a student."""


    github = request.args.get('github')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)

    return html    

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""


    return render_template("student-search.html")


@app.route("/add_student")
def add_student_form():

    return render_template("new-student.html")

@app.route("/new-student")
def add_student():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    github = request.args.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("added-student.html",
                            first=first_name,
                            last=last_name,
                            github=github)     

if __name__ == "__main__":
    app.run(debug=True)