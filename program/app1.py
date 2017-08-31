from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql=MySQL()

app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='admin'
app.config['MYSQL_DATABASE_DB']='test'
app.config['MYSQL_DATABASE_host']='localhost'
mysql.init_app(app)

@app.route('/test')
def hello():
	return "Hello World"

@app.route('/login',methods=['GET','POST'])
def login():
    username = request.form['uname']
    password = request.form['pass']
    connection = mysql.get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * from Emp1 where Uname='" + username + "' and Upassword='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

@app.route('/',methods=['GET','POST'])
def get_data():
  if request.method=='POST':
    user_name=request.form['uname']
    user_password=request.form['pass']
    user_emailid=request.form['email']
    connection = mysql.get_db()
    cursor = connection.cursor()
    query="INSERT INTO Emp1(Uname,Upassword,Uemail) VALUES(%s,%s,%s)"

    a=cursor.execute(query,(user_name,user_password,user_emailid))
    connection.commit()
  return render_template("index1.html")

if __name__=='__main__':
	app.run(debug=True)
