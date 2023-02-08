from flask import Flask,render_template,make_response,request,session,redirect,url_for

from flask_mail import Mail,Message
from flaskext.mysql import MySQL
from random import *


app = Flask(__name__,template_folder="templates")

# EMAIL SENDER CONFIGURATION
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'hezronmmisagal@gmail.com'
app.config['MAIL_PASSWORD'] = 'urghnriklqurbihg'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(00000,99999)

# DATABASE CONNECTION
mysql = MySQL()

app.config['SECRET_KEY'] = 'JFAKJFHLKA.JFLAJW'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_final'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql.init_app(app)

# API ROUTES

#def server():
#    return "hello API Server"

 # HOME LANDING PAGE
 
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

# CONTENT LANDING PAGE
@app.route('/content')
def content():
    return render_template('content.html')


# AGENCY LANDING PAGE
@app.route('/agency')
def agency():
    return render_template('agency.html')


# PRIVILEGES LANDING PAGE
@app.route('/privileges')
def priv():
    return render_template('privileges.html')
    

# PORTAL AFTER LOGIN
@app.route('/portal')
def portal():
    return render_template('portal.html')


@app.route('/loan')
def loan():
    return render_template('loans.html')


@app.route('/requirements')
def req():
    return render_template('requirements.html')



@app.route('/sssportal',methods=['GET', 'POST'])
def sssportal():
    msg = ''
    if request.method == 'POST':
        
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        id_pwd = request.form['pwd']	
        id_sss	= request.form['sss']
        f_address = request.form['f_address']	
        tol	= request.form['tol']
        gender= request.form['gender']
        zip_f = request.form['zip_f']

        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "INSERT INTO sss_table( fname, lname, user_email, id_pwd, id_sss, f_address,tol, gender, zip_f) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
        val = (fname,lname,email,id_pwd,id_sss,f_address,tol,gender,zip_f)
        result = cursor.execute(sql,val)
        connection.commit()
        cursor.close()
        connection.close()
        if result:
            msg ="YOU ARE SUCCESSFULLY PASSED THE APPLICATION OF SSS DISABILTY CLAIM.!! NOTE:  We will sent you an email confirmation for approval just wait 24 hours for proccessing your application thank you!"
        
               
    return render_template('sss-membership.html',msg=msg)

#ADMIN  SSS APPLICATION INFO
@app.route('/get_sss_info', methods=['GET'])
def get_sss_info():
        connection = mysql.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM sss_table")
        result = cursor.fetchall()
        json_res = {}
        for res in result:
            sss_id,fname,lname,user_email,id_pwd,id_sss,f_address,tol,gender,zip_f = res
            json_res[sss_id] = {"sss_id":sss_id,"fname":fname,"lname":lname,"user_email":user_email,"id_pwd":id_pwd,"id_sss":id_sss,"f_address":f_address,"tol":tol,"gender":gender,"zip_f":zip_f}

        return json_res
    



@app.route('/dswd',methods=['GET', 'POST'])
def dswd():
    msg = ''
    if request.method == 'POST':
        dswd_fname = request.form['dswd_fname']
        dswd_lname = request.form['dswd_lname']
        dswd_email = request.form['dswd_email']
        pwd_id = request.form['pwd_id']
        City = request.form['City']
        barangay = request.form['barangay']
        region_a = request.form['region_a']	
        zip_d = request.form['zip_d']

        connection = mysql.connect()	
        cursor = connection.cursor()

        sql = "INSERT INTO dswd_table (dswd_fname, dswd_lname, dswd_email, pwd_id, City, barangay, region_a, zip_d) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (dswd_fname, dswd_lname, dswd_email, pwd_id,City, barangay, region_a,zip_d)
        result = cursor.execute(sql,value)
        connection.commit()
        cursor.close()
        connection.close()
        if result:
            msg ="YOU ARE SUCCESSFULLY SUBMIT THE APPLICATION OF Cash Assistance from DSWD PROGRAM.!! NOTE:  We will sent you an email confirmation for approval just wait 24 hours for proccessing your application thank you!"
        
    
    return render_template('dswd.html',msg=msg)
#admin dswd application info 
 
@app.route('/get_dswd_info',methods=['GET'])
def get_dswd_info():
    connection = mysql.connect()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM dswd_table")
    result = cursor.fetchall()
    json_res = {}
    for res in result:
        dswd_id,dswd_fname, dswd_lname, dswd_email, pwd_id,City, barangay, region_a,zip_d = res
        json_res[dswd_id] = {"dswd_id":dswd_id,"dswd_fname":dswd_fname,"dswd_lname":dswd_lname,"dswd_email":dswd_email,"pwd_id":pwd_id,"City":City,"barangay":barangay,"region_a":region_a,"zip_d":zip_d}

    return json_res
    


@app.route('/ched')
def ched():
    return render_template('ched.html')


@app.route('/philhealth')
def philhealth():
    return render_template('philhealth.html')



@app.route('/cswd')
def cswd():
    return render_template('cswd.html')

@app.route('/pagibig')
def pagibig():
    return render_template('pag-ibig.html')


# REGISTRATION PAGE
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/faq')
def faq():
    return render_template('FAQ.html')

#admin login 
@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    msg = '' 
   
    try:
        
        if request.method == 'POST' and 'email_ad' in request.form and 'user_pass' in request.form:
            
            log_email = request.form['email_ad']
            log_userpass = request.form['user_pass']

            connection = mysql.connect()
            cursor = connection.cursor()

            
            cursor.execute("SELECT * FROM user_login WHERE login_email = %s AND user_pass = %s",(log_email,log_userpass))
            result = cursor.fetchone()
            if result:
                
                session['id_login'] = result['id_login']
                session['email_id'] = result['login_email']
            
                session['user_pass'] = result['user_pass']
                msg = 'the user has been successfully login'
            else:
                msg = 'User not found. Invalid password and Email!'
        return render_template('admin_login.html',msg=msg)
    except Exception as error:
        print(error)
            
    return render_template('admin.html',msg=msg)

@app.route('/logout')
def logout():
    session.pop('submit', None)
    session.pop('id_login', None)
    session.pop('email_id', None)
    return redirect(url_for('admin_login'))

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')
 
# ADMIN HOME PAGE
@app.route('/admin')
def admin():
    return render_template('admin.html')
 

@app.route('/application_info')
def application_info():
    return render_template('application.html')

@app.route('/sss_application')
def sss_application():
    return render_template('sss_application.html')
    
@app.route('/dswd_app')
def dswd_app():
    return render_template('dswd_app.html')
    

# REGISTRATION BACK END PROCCESSING REQUEST FROM USER
@app.route('/registration',methods=['GET','POST'])
def registration():
    try:
        if request.method == 'POST':

            fullname = request.form['fullname']
            email = request.form['email']
            pwd_id = request.form['pwd_id']
            address = request.form['address']
            age = request.form['age']
            status = request.form['status']

            connection = mysql.connect()
            cursor = connection.cursor()

            sql = "INSERT INTO user (p_fullname,p_email, pwd_id, p_adress, p_age, p_status) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (fullname,email,pwd_id,address,age,status)
            cursor.execute(sql,val)
            connection.commit()
            cursor.close()
            connection.close()

            return make_response({ "fullname":fullname }, 200)
        else:
            return render_template("register.html")
    except Exception as error:
        print(error)

    return ""

# get all the data from user

@app.route('/getdata',methods=['GET'])
def getdatainfo():
    connection = mysql.connect()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    json_res = {}
    for res in result:
        id,p_fullname,p_email,pwd_id,p_adress,p_age,p_status = res
        json_res[id] = {"id":id,"p_fullname":p_fullname,"p_email":p_email,"pwd_id":pwd_id,"p_adress":p_adress,"p_age":p_age,"p_status":p_status}

    return json_res

# delete data users
@app.route("/getdelete",methods=["POST"])
def delete():
    connection = mysql.connect()
    cursor = connection.cursor()

    userid= request.form['userid']
    cursor.execute("DELETE FROM user WHERE id = %s",(userid))

    connection.commit()
    cursor.close()
    connection.close()
    
    return make_response({ "userid":userid }, 200)

# LOGIN USER BACK END VALIDATION 
@app.route('/login',methods=['GET','POST'])
def login():
    msg = '' 
   
    try:
        
        if request.method == 'POST' and 'email' in request.form and 'fullname' in request.form:
            
            log_email = request.form['email']
            log_fullname = request.form['fullname']

            connection = mysql.connect()
            cursor = connection.cursor()

            
            cursor.execute("SELECT * FROM user WHERE p_email = %s AND p_fullname = %s",(log_email,log_fullname))
            result = cursor.fetchone()
            if result:
                session['login'] = True
                session['email'] = result['p_email']
                session['fullname'] = result['p_fullname']
                msg = 'the user has been successfully login'
            elif result != result['p_email']:
                msg = 'Please check your email'
            elif result != result['p_fullname']:
                msg = 'Please check your full name'
            else:
                msg = 'User not found. Create an account first and try again!'
        

        return render_template('register.html',msg=msg)

            
    except Exception as error:
        print(error)
    return render_template('verification.html',msg=msg)
# user logout
@app.route('/user_logout')
def user_logout():
    session.pop('login', None)
    session.pop('email', None)
    session.pop('fullname', None)
    return redirect(url_for('login'))

# LOGIN USER BACK END user verification
@app.route('/verification',methods=['POST'])
def verification():
 
        email = request.form['email-verify']
        msg = Message(subject='OTP Verification',sender='hezronmmisagal@gmail.com',recipients=[email])
        msg.body=str(otp)
        mail.send(msg)
        return render_template('otp-login.html')
  

@app.route('/OTP',methods=['GET','POST'])
def user_verify():
    msg = ''
    if request.method == 'POST':
        otp_user = request.form['otp']
       
        if otp == int(otp_user):
            return render_template('portal.html')
        else:
            msg = 'Invalid Please try again later'
         
       
    return render_template('otp-login.html',msg=msg)
   


if __name__=="__main__":
    app.run(debug=True)

    
    
