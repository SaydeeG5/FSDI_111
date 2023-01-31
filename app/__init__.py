from flask import Flask # From the flask module import the Flask class


app= Flask(__name__)    # Create an instance of the Flask class 
                        # into the app variable (now an object).


@app.route("/")           # Flask decorator that creates routes. 
def index():            # Flask calls these "view functions".
    me = {              # Python dictionary with key/value pairs. 
        "first_name": "Saydee",
        "last_name": "Guevarra",
        "hobbies": "cricut",
        "is_active": True
    }

    return me           # When a view function returns a dictionary
                        # Flask automatically converts it to JSON. 