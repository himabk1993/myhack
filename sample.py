import psycopg2
import sys

try:
    conn = psycopg2.connect("dbname='test' user= 'postgres' password='postgres' ")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()

class common:
	def userdet(self):
		self.name = input("Enter your name : ")
		self.age = int(input("Enter your age : "))
		self.loc = input("Enter your loc : ")
		return(self.name,self.age,self.loc)
i = 1
while(int(i) == 1):
	num = input(" click 1 for student or 2 for employee : ")
	c = common()
	a = c.userdet()


#conn = psycopg2.connect("dbname=test user=postgres password=postgres")
	if (int(num) == 1):
		sql = "insert into student values('%s',%d,'%s')" %a
		print(sql)
		cur.execute(sql)
		conn.commit()
	#rows = cur.fetchall()
	elif(int(num) == 2):
		sql = "insert into emp values('%s',%d,'%s')" %a
		print(sql)
		cur.execute(sql)
		conn.commit()
	else:
		print("neither student nor employee")
	print("### STUDENT TABLE ###")
	sql1 = "select * from student"
	#print(sql1)
	cur.execute(sql1)
	rows1 = cur.fetchall()
	print(rows1)
	k = 1
	for y in rows1:
		print("*** STUDENT No : ", k)
		print("name : ",y[0])
		print("age : ",y[1])
		print("loc : ",y[2])
		k += 1
	print("### EMPLOYEE TABLE ###")
	sql2 = "select * from emp"
	#print(sql1)
	cur.execute(sql2)
	rows2 = cur.fetchall()
	print(rows2)
	k = 1
	for z in rows2:
		print("*** EMPLOYEE No : ", k)
		print("name : ",z[0])
		print("age : ",z[1])
		print("loc : ",z[2])
		k += 1
	i = input("enter 1 for adding another employee/student details else click 0 : ")

