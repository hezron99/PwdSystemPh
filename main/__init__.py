
from flask import Flask

from flask_mail import Mail
from flaskext.mysql import MySQL
from random import *

app = Flask(__name__,template_folder="templates")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'hezronmmisagal@gmail.com'
app.config['MAIL_PASSWORD'] = 'urghnriklqurbihg'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(00000,99999)

mysql = MySQL()

app.config['SECRET_KEY'] = 'JFAKJFHLKA.JFLAJW'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_final'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql.init_app(app)

from main import route