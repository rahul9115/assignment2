import pymysql
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "rahul9115",
        db='assignment',
        )
      
    cur = conn.cursor()
    #print(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
    cur.execute("select * from user_information")
    #cur.execute(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
    output = cur.fetchall()
    print(output)
      
    # To close the connection
    conn.close()
if __name__ == "__main__" :
    mysqlconnect()
    