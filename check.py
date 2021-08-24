import pymysql
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "rahul9115",
        db='assignment2',
        )
    subject="science"
    cur = conn.cursor()
    #print(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
    cur.execute(f"select streamid from stream where stream_name='{subject}'")
    #cur.execute(f"insert into user_information(name,age,stream,gender) values('{name}',{age},'{stream}','{gender}');")
    output = cur.fetchall()
    print(output[0][0])
    if(len(output)>0):
        print("great")
    else:
        print("no")
    # To close the connection
    conn.close()
if __name__ == "__main__" :
    mysqlconnect()
    