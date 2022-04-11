from flask import Flask,render_template,request

from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Aryams#11"
app.config['MYSQL_DB'] = "project"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)



@app.route('/')
def home():
 
 return render_template("home.html")
@app.route('/enter', methods=['GET','POST'])
def enter():
  if request.method == 'POST':
        username = request.form['name']
        gender =request.form['gender']
        bp =request.form['bp']
        diabetics =request.form['diabetic']
        smoking =request.form['radio']
        address =request.form['address']
        cur = mysql.connection.cursor()
        
        
        cur.execute("INSERT into worker (name,gender,bp,diabetic,smoking,address) values (%s,%s,%s,%s,%s,%s)",(username,gender,bp,diabetics,smoking,address))
        mysql.connection.commit()
        cur.close()
        return render_template("home.html")

  return render_template("enter.html")
@app.route('/view')
def view(): 
    mycursor=mysql.connection.cursor()
    mycursor.execute("SELECT workerid,name,gender,address FROM worker")
    
    workers = mycursor.fetchall()
  
    print(workers)
    mycursor.close()
    return render_template('view.html', workers= workers)
@app.route('/predict', methods=['GET','POST'])
def predict(): 
    if request.method == 'POST':
        userid = request.form['id']
        pulse = request.form['pulse']
        oxygencon=request.form['oxygen']
        cur = mysql.connection.cursor()
        
        
        cur.execute("select gender,bp,diabetic,smoking from worker where workerid=%s",userid)
        details = cur.fetchall()
        if details[0]['gender'] == 'female':
          gen=1
        else :
          gen=0
        if details[0]['bp'] == 'normal':
          bprate=1
        else :
          bprate=0
        if details[0]['diabetic'] == 'yes':
           sugarlevel=1
        else :
          sugarlevel=0
        if details[0]['smoking'] == 'no':
          smoke=0
        else :
          smoke = 1
           
        print(details)
        print(smoke)
        cur.close()
    return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)