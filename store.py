import pymysql
import re
from flask import Flask,render_template,request,session
from flask_session import Session
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly
import pandas as pd
import json
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

app=Flask(__name__,template_folder="sign_up")
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
reg=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

@app.route("/",methods=["POST","GET"])
def display():
    session["values"][0]=False
    session["values"][1]=False
    return render_template("validate.html",message="")
@app.route("/",methods=["POST","GET"])
def logout():
    session["values"][0]=False
    session["values"][1]=False
    return render_template("validate.html")
@app.route("/signup",methods=["POST","GET"])
def signup():
    
    if request.method=="POST":
        message=""
        username=request.form.get("username")
        password=request.form.get("password")
        rpassword=request.form.get("rpassword")
        conn = pymysql.connect(
            host='localhost',
            user='root', 
            password = "rahul9115",
            db='assignment2',
            )
        cur = conn.cursor()
        cur.execute("select username from administrator")
        output = cur.fetchall()
        user=False
        message5=""
        message6=""
        for i in output:
            if(i[0]==username):
                user=True
        if user==True:
            return render_template("validate.html",message5="Username already exists")

        print("This",password)
        if(password!=rpassword and len(password)>0):
            print("wohooo")
            message="Passwords dont match"
            return render_template("validate.html",message6=message)
        else:
            
            
            conn = pymysql.connect(
            host='localhost',
            user='root', 
            password = "rahul9115",
            db='assignment2',
            )
            cur = conn.cursor()
            cur.execute("select * from administrator")
            output = cur.fetchall()
            if(len(output)==0):
                cur = conn.cursor()
                cur.execute(f"insert into administrator values(1,{username},AES_ENCRYPT('{password}','password'))")
                print(f"insert into administrator values(1,{username},AES_ENCRYPT('{password}','password')")
            else:
                cur = conn.cursor()
                print(f"insert into administrator values(1,{username},AES_ENCRYPT('{password}','password')")
                cur.execute(f'insert into administrator(username,password) values("{username}",AES_ENCRYPT("{password}","password"))')
                
                conn.commit()
    
        return render_template("validate.html",message="")
            

@app.route("/validate",methods=["POST","GET"])
def validate():
    print("in")
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        print(username,password)
        conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "rahul9115",
        db='assignment2',
        )
      
        cur = conn.cursor()
        #print(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
        cur.execute("select username,cast(AES_decrypt(password,'password') as char) from administrator")
        #cur.execute(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
        output = cur.fetchall()
        print("validation output",output)
        user=[]
        passwd=[]
        
        for i in output:
            user.append(i[0])
            
            passwd.append(i[1])
        u=False
        p=False
        print(user,passwd)
        for i,j in zip(user,passwd):
            if(i==username):
                u=True
            if(j==password):
                p=True
        print(u,p)
        session["values"][0]=u
        session["values"][1]=p
        cur = conn.cursor()
        cur.execute("select stream_name from stream")
        output=cur.fetchall()
        streams=[]
        message=""
        message1=""
        message2=""

        for i in output:
            streams.append(i[0])
        print(streams)    
        if(u==True and p==True):
            return render_template("info.html",list=streams)
        elif(u==False and p==True):
            return render_template("validate.html",message="Invalid username")
        elif(u==True and p==False):
            return render_template("validate.html",message1="Invalid password")
        else:
            return render_template("validate.html",message2="Invalid username and password")


@app.route("/regex",methods=["POST","GET"])
def regex():
    print(session["values"][0],session["values"][1])
    if(session["values"][0]==True and session["values"][1]==True):
        if request.method=="POST":
            fname=request.form.get("first_name")
            lname=request.form.get("last_name")
            age=request.form.get("age")
            email=request.form.get("email")
            ac=request.form.get("area_code")
            phone=request.form.get("phone")
            subject=request.form.get("subject")
            gender=request.form.get("gender")
            marks=request.form.get("marks")
            print(fname,lname,age,email,marks,subject) 
            b_fname=False
            b_lname=False
            b_age=False
            b_email=False
            b_phone=False
            b_marks=False
            message=""
            message1=""
            message2=""
            message3=""
            message4=""
            message5=""
            if(b_fname==False):
                if(any(map(str.isdigit,fname))):
                    message4="Please enter valid firstname"
                    
                else:
                    b_fname=True
            if(b_lname==False):
                if(any(map(str.isdigit,lname))):
                    message5="Please enter valid lastname"
                    
                else:
                    b_lname=True
            if(b_age==False):
                if int(age)<0 or int(age)>150:
                    message="Please enter valid age"
                    
                else:
                    b_age=True
            
            if(b_email==False):
                if(re.fullmatch(reg,email)):
                    b_email=True
                else:
                    message1="The email is not valid please enter again"
                    
            if(b_phone==False):
                if len(phone)!=10:
                    message2="Please enter 10 digit phone number"
                    
                else:
                    b_phone=True
            if(b_marks==False):
                if(int(marks)<0 or int(marks)>100):
                    message3="Please enter marks between 0 to 100"
                    
                else:
                    b_marks=True    
            print("here")
            print(b_fname,b_fname,b_age,b_email,b_marks,b_marks)        
            if(b_fname==True and b_lname==True and b_phone==True and b_email==True and b_age==True and b_marks==True):
            
                
                conn = pymysql.connect(
                host='localhost',
                user='root', 
                password = "rahul9115",
                db='assignment2',
                )
                cur=conn.cursor()
                cur.execute(f"select streamid from stream where stream_name='{subject}'")
                output = cur.fetchall()
                streamid=output[0][0]
                
                cur = conn.cursor()
                #print(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
                cur.execute("select * from person")
                output = cur.fetchall()
                if(len(output)==0):
                    print("in")
                    conn = pymysql.connect(
                    host='localhost',
                    user='root', 
                    password = "rahul9115",
                    db='assignment2',
                    )
                    cur = conn.cursor()
                    cur.execute(f"insert into person(personid,adminid,fname,lname,age,gender,email,streamid,phn_no,marks) values(1,1,'{fname}','{lname}',{int(age)},'{gender}','{email}',{streamid},{phone},{marks})")
                    conn.commit()
                    cur = conn.cursor()
                    cur.execute("select stream_name from stream")
                    output=cur.fetchall()
                    streams=[]
                    for i in output:
                        streams.append(i[0])
                    print(streams)    
                    return render_template("final.html",list1=streams)
                else:
                    print("out")
                    conn = pymysql.connect(
                    host='localhost',
                    user='root', 
                    password = "rahul9115",
                    db='assignment2',
                    )
                    cur = conn.cursor()
                    cur.execute(f"insert into person(adminid,fname,lname,age,gender,email,streamid,phn_no,marks) values(1,'{fname}','{lname}',{int(age)},'{gender}','{email}',{streamid},{phone},{marks})")
                    conn.commit()
                    cur = conn.cursor()
                    cur.execute("select stream_name from stream")
                    output=cur.fetchall()
                    streams=[]
                    for i in output:
                        streams.append(i[0])
                    print(streams)    
                    return render_template("final.html",list1=streams)
            else:
                return render_template("info.html",message1=message1,message2=message2,message=message,message3=message3,message4=message4,message5=message5)
    
        
                



@app.route("/display1")
def display1():
    if(session["values"][0]==True and session["values"][1]==True):
        conn=pymysql.connect(
                host='localhost',
                user='root', 
                password = "rahul9115",
                db='assignment2',

            )
        
        cur=conn.cursor()
        cur.execute("select stream_name from stream")
        output=cur.fetchall()
        streams=[]
        for i in output:
            streams.append(i[0])
        print(streams)   
        return render_template("final.html",list1=streams)
    else:
        return render_template("validate.html")      
@app.route("/finish",methods=["POST","GET"])
def finish():
    if(session["values"][0]==True and session["values"][1]==True):
        if request.method=="POST":
            subject=request.form.get("subject")
            conn=pymysql.connect(
                host='localhost',
                user='root', 
                password = "rahul9115",
                db='assignment2',

            )
            message=0
            cur=conn.cursor()
            cur.execute(f"select streamid from stream where stream_name='{subject}'")
            output = cur.fetchall()
            streamid=output[0][0]
            cur=conn.cursor()
            cur.execute(f"select personid,fname,lname,marks from person where streamid={streamid}")
            output = cur.fetchall()
            cur=conn.cursor()
            cur.execute(f"select personid,lname,fname,marks from person where streamid={streamid}")
            output = cur.fetchall()
            personid=[]
            name=[]
            marks=[]
            for i in output:
                personid.append(i[0])
                name.append(i[1]+i[2])
                marks.append(i[3])
            if not marks:
                message=1
            data={"name":name,"marks":marks}
            df=pd.DataFrame(data=data)
            fig=px.bar(df,x="name",y="marks",title="Performance in science")
            fig1=px.pie(df,values="marks",names="name",title="Performance in science")
            fig2=px.line(df,x="name",y="marks",title="performance in science")
            plt.show()
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
            cur.execute("select stream_name from stream")
            output1=cur.fetchall()
            streams=[]
            for i in output1:
                streams.append(i[0])
            print(streams)   
            return render_template("final.html",list=output,graphJSON=graphJSON,graphJSON1=graphJSON1,graphJSON2=graphJSON2,message=message,list1=streams)
    else:
        return render_template("validate.html")










    # To connect MySQL database
 
    
  
# Driver Code
if __name__ == "__main__" :
    
    app.debug=True
    app.run(host="127.0.0.1",port=5000)