from flask import Flask, render_template, redirect, url_for, request, abort

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('test4.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' :
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else :
            abort(401)

@app.route('/success')
def success():
    return 'logged in successfully as admin'

if __name__ == '__main__' :
    app.run(port = 5014, debug = True)
