from flask import Flask
app = Flask(__name__)

@app.route('/')
def page1():
   return 'welcome to the world of programming'

#@app.route('/page2/')
def page2():
	return 'welcome '
app.add_url_rule('/','page2',page2)



if __name__ == '__main__':
   app.run(port=5009,debug=True)