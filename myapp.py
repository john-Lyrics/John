from flask import Flask
from flask import render_template
 
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
 
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/whereami')
def whereami():
    return 'Ghana!'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')