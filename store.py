import pymysql
from flask import Flask,render_template,request
app=Flask(__name__,template_folder="sign_up")

@app.route("/",methods=["POST","GET"])
def display():
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