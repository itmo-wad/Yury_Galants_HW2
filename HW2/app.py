from flask import Flask, render_template, request, redirect, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient(‘localhost’,27017)
db = mongo.pratice

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form.get('username', 0)
        password = request.form.get('password', 0)
        if not (username and password):
            return 'Error'

        data = list(db.users.find({'username' : username}, {'password' : password}))
        if len(data):
            data = data[0]['password']
            print(data)
            if password == data:
                return redirect('/profile')

    return render_template('auth.html')


@app.route(‘/profile’)
def index():
    return render_template('profile.html')

if __name__ == ‘__main__’:
    app.run(host=‘localhost’, port=5000, debug=True)