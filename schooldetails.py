from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

postgres_url = "localhost"
postgres_user = "postgres"
postgres_pw = "postgres"
postgres_db = "test"

db_url = 'postgres://{user}:{pw}@{url}/{db}'.format(user = postgres_user, pw = postgres_pw, url = postgres_url, db = postgres_db)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

@app.route('/')
def login():
    return render_template('school.html')

@app.route('/home' , methods = ['POST', 'GET'])
def home():
    n = request.args.get('n')
    c = request.args.get('c')
    d = request.args.get('d')
    u = request.args.get('u')
    if u == 'student':
        return 'Hello %s , you are a %s  %s student' % (n, c, d)
    else:
        return 'Hello %s , you are a %s  %s teacher' % (n, c, d)
#@app.route('/student', methods = ['GET'])
#def student():
#    return render_template('student.html')

#@app.route('/teacher')
#def teacher():
#    return render_template('teacher.html')

@app.route('/finduser', methods = ['POST','GET'])
def finduser():
    user = request.form['category']
    if user == 'student':
        nam = request.form['name']
        clas = request.form['cls']
        divis = request.form['div']
        sql = "insert into studenttab values ('{0}','{1}','{2}')" .format(nam,clas,divis)
        db.session.execute(sql)
        db.session.commit()
        return redirect(url_for('home',n=nam,c=clas,d=divis,u=user))
    else:
        user = 'teacher'
        nam = request.form['name']
        clas = request.form['cls']
        divis = request.form['div']
        sql = "insert into teacher values ('{0}','{1}','{2}')" .format(nam,clas,divis)
        db.session.execute(sql)
        db.session.commit()
        return redirect(url_for('home',n=nam,c=clas,d=divis,u=user))

#@app.route('/addvalues', methods = ['POST'])
#def addvalues():
#    if methods == 'POST':

#        nam = request.form['name']
#        cls = request.form['class']
#        divis = request.form['div']
#        sql =

#@app.route('/hometeachers', methods = ['POST', 'GET'])
#def hometeachers():
#    if methods == 'POST':
#        nam = request.form['name']
#        cls = request.form['class']
#        div = request.form['div']
#        sql = "insert into teachers values()"



if __name__ == '__main__' :
    app.run(port = 5012, debug = True)
