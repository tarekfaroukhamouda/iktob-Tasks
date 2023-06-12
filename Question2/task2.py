from flask import Flask, request

app = Flask(__name__)

app.config['login_details'] = {

}


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username", None)
    password = data.get("password", None)
    if username is None or password is None:
        return 'Invaaild Data please make sure to add username and password'
    if len(username) < 5:
        return "Please make sure username not less than 5 letters"
    if len(password) < 4:
        return 'please make sure password length not less than 4'
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if any(c in special_characters for c in password):
        return 'Not Legal'

    app.config['login_details']['username'] = username
    app.config['login_details']['password'] = password

    return "Success registration"


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username", None)
    password = data.get("password", None)
    if username is not None and password is not None:
        if username==app.config['login_details']['username'] and password==app.config['login_details']['password']:
            return 'Login Successfully '
        return 'Bad Authentication'

    return app.config['login_details']


if __name__ == '__main__':
    app.run(debug=True)
