      from flask import Flask, redirect, url_for, request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(__name__)
POSTGRES_URL = "localhost"
POSTGRES_USER = "postgres"
POSTGRES_PW = "postgres"
POSTGRES_DB = "test"
DB_URL = 'postgres://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/employee',methods=['POST','GET'])
def employee():
	if request.method == 'POST':
		name=request.form['name']
		des=request.form['designation']
		age=request.form['age']
		loc=request.form['loc']
		sql = "insert into emp values('{0}',{1},'{2}','{3}')".format(name,age,loc,des)
		print(sql)
		db.session.execute(sql)
		db.session.commit()
		return redirect(url_for('registration'))


@app.route('/registration')
def registration():
	return render_template('hello.html')

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

@app.route('/hima/<int:postID>')
def hello_world(postID):
   return 'Blog Number %d' % postID

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(port=5004,debug=True)
