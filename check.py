import pymysql
def mysqlconnect():
    # To connect MySQL database
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
    print(output)
    user=[]
    passwd=[]
    for i in output:
        user.append(i[0])
        passwd.append(i[1])
    print(user,passwd)
      
    # To close the connection
    conn.close()
if __name__ == "__main__" :
    mysqlconnect()
    