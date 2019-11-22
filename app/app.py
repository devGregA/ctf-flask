from flask import Flask, Response, redirect, url_for, request, session, abort
app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="ctf"
)

mycursor = mydb.cursor()



@app.route('/')
def hello():
    return "Mr. Robots: HELLO FRIEND, that flag has to be here somewhere, but I can't find it."


@app.route('/robots.txt')
def robots():
    return "User-agent: * <br/> Disallow: /143ce.html"

@app.route('/143ce.html')
def secret():
    return "the flag is: notsecret"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        print (username)
        print (password)
        if password == username + "_secret":
            #id = username.split('user')[1]
            #user = User(id)
            #login_user(user)
            return ('''
		<h2> Congrats! The flag is: hiddenelement</h2>''')
        else:
            return abort(401)
    else:
        return Response('''
	<h2> VERY Secure Login </h2>
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>

<div type=form_action hidden </div>
<input type="hidden" id="form_id" name="login">
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print (username)
        print (password)
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
</div>
        ''')
"""
@app.route("/query_db", methods=["GET", "POST"])
def query():
    if request.method == 'POST':
        answer = request.form['answer']        
        mycursor.execute(("SELECT * FROM answers where the_flag_is  = " + answer + ';'))
        myresult = mycursor.fetchall()
	query = 
        return Response('''
	<h2> VERY Sensitive Database </h2>
        <form action="" method="post">
            <p><input type=text name=answer>
            <p><input type=submit>
        </form>
        ''')
    else:
        return Response('''
	<h2> VERY Sensitive Database </h2>
        <form action="" method="post">
            <p><input type=text name=answer>
            <p><input type=submit>
        </form>
        ''')
"""
if __name__ == '__main__':
    app.run()
