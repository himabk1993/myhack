from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/hi/<name>')
def add_name(name):
    return 'welcome %s' % name

@app.route('/admin/<a>')
def hello_admin(a):
    return 'hello admin %s' % a

@app.route('/guest/<b>')
def hello_guest(b):
    return 'hello guest %s' % b

@app.route('/user/<name>', methods = ['GET','POST'])
def user(name):
    if method == 'POST':
        user = reqest.form('nm')
        if user == 'admin':
            return redirect(url_for(hello_admin, name = user))
        else :
            return redirect(url_for(hello_guest,))

def hi_world():
  return 'hi world'
app.add_url_rule('/','hi',hi_world)

if __name__ == '__main__' :
  app.run(port = 5010, debug = True )
