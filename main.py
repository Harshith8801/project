from flask import Flask,render_template,request,redirect
import sqlite3

app  = Flask(__name__)

def create_connection():
    conn= sqlite3.connect("contact.db")
    return conn

def create_table():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,number TEXT)')
    conn.commit()
    conn.close()

def create_con():
    log= sqlite3.connect("login.db")
    return log


def create_tables():
    log=create_con()
    cure = log.cursor()
    cure.execute('CREATE TABLE IF NOT EXISTS login(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,number TEXT)')
    log.commit()
    log.close()
    




@app.route('/admin')
def admin():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contact')
    data=cur.fetchall()
    print(data)
    return render_template('admin.html',users=data)




    

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")
@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        name=request.form['inp1']
        num=request.form['inp2'] 
        conn= create_connection()
        cur=conn.cursor()
        cur.execute('''INSERT INTO contact(name , number)VALUES(?,?)''',(name,num)) 
        conn.commit()
        conn.close()
        print(name,num)
        redirect('/admin')
    return render_template("contact.html")
@app.route("/registation", methods=['GET','POST'])
def registation():
    if request.method == 'POST':
        name1=request.form['int1']
        num2=request.form['int2'] 
        log= create_con()
        cure=log.cursor()
        cure.execute('''INSERT INTO login(name , number)VALUES(?,?)''',(name1,num2)) 
        log.commit()
        log.close()
        print(name1,num2)
    return render_template("/registation.html")

@app.route("/home", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input from the login form
        name_input = request.form['out1']
        number_input = request.form['out2']

        # Connect to the database
        log = create_con()
        cure = log.cursor()

        # Query the database to find a matching record
        cure.execute("SELECT * FROM login WHERE name = ? AND number = ?", (name_input, number_input))
        result = cure.fetchone()  # Fetch a single matching record

        log.close()
        print(name_input, number_input)

        # If a match is found, render the home page
        if result:
            return render_template("home.html")
        else:
            print("fuck off")
            return "Invalid credentials. Please try again."

    # Render the login page if the request method is GET
    return render_template("home.html")

        


if __name__=="__main__":
    create_connection()
    create_table()
    create_con()
    create_tables()
    app.run(debug=True)
    
