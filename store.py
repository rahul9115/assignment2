import pymysql
import re
from flask import Flask,render_template,request
app=Flask(__name__,template_folder="sign_up")
reg=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
@app.route("/",methods=["POST","GET"])
def display():
    return render_template("validate.html")
@app.route("/",methods=["POST","GET"])
def logout():
    return render_template("validate.html")
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
        cur.execute("select username,password from administrator")
        #cur.execute(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
        output = cur.fetchall()
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
        if(u==True and p==True):
            return render_template("info.html")
        else:
            return render_template("validate.html")

@app.route("/regex",methods=["POST","GET"])
def regex():
    if request.method=="POST":
        fname=request.form.get("first_name")
        lname=request.form.get("last_name")
        age=request.form.get("age")
        email=request.form.get("email")
        ac=request.form.get("area_code")
        phone=request.form.get("phone")
        subject=request.form.get("subject")
        gender=request.form.get("gender")
        
        b_age=False
        b_email=False
        b_phone=False
        message=""
        if(b_age==False):
            if int(age)<0:
                message="Please enter valid age"
                return render_template("info.html",message=message)
            else:
                b_age=True
        
        if(b_email==False):
            if(re.fullmatch(reg,email)):
                b_email=True
            else:
                message1="The email is not valid please enter again"
                return render_template("info.html",message1=message1)
        if(b_phone==False):
            if len(phone)!=10:
                message2="Please enter 10 digit phone number"
                return render_template("info.html",message2=message2)
            else:
                b_phone=True
        if(b_phone==True and b_email==True and b_age==True):
          
            
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
                cur.execute(f"insert into person(personid,adminid,fname,lname,age,gender,email,streamid,phn_no) values(1,1,'{fname}','{lname}',{int(age)},'{gender}','{email}',{streamid},{phone})")
                conn.commit()
                return render_template("final.html")
            else:
                print("out")
                conn = pymysql.connect(
                host='localhost',
                user='root', 
                password = "rahul9115",
                db='assignment2',
                )
                cur = conn.cursor()
                cur.execute(f"insert into person(adminid,fname,lname,age,gender,email,streamid,phn_no) values(1,'{fname}','{lname}',{int(age)},'{gender}','{email}',{streamid},{phone})")
                conn.commit()
                return render_template("final.html")
    return render_template("info.html")
                
           
            
           







@app.route("/info.html",methods=["POST","GET"])

def insert():
    name=""
    age=0
    stream=""
    gender=""
    print("in")
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        stream=request.form.get("stream")
        gender=request.form.get("gender")
        print(name,age,stream,gender)
        conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "rahul9115",
        db='assignment',
        )
        cur = conn.cursor()
        print(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
        str=f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');"
        cur.execute(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
        #cur.execute("insert into user_information(name,age,stream,gender) values("+"'"+name+"',"+"'"+age+"',"+"'"+stream+"',"+"'"+gender+"');")
        conn.commit()
        output = cur.fetchall()
        print(output)
      
    # To close the connection
    conn.close()
    return render_template("final.html")


    # To connect MySQL database
 
    
  
# Driver Code
if __name__ == "__main__" :
    
    app.debug=True
    app.run(host="127.0.0.1",port=5000)