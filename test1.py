from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/')
def sample1():
    return render_template('sample1.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form.get('nm')
      return redirect(url_for('success',name = user))
   else:
       print("get = ",request.args)
       user = request.args['nm']
       return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
