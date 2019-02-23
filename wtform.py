from flask_wtf import Form
from wtforms import TextField

class ContactForm(Form):
   name = TextField("Name Of Student")
