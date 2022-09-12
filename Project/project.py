from os.path import exists
import pickle


class Employee:
    empid=0
    ename=""
    sal=0
    deptno=0 
    def __init__(self, empid, ename, sal, deptno, count):
        self.empid = empid
        self.ename = ename
        self.sal = sal
        self.deptno = deptno


def Add_Emp():
    #Add employee function to add employee details like empid,empname,sal,deptno 
    empid=int(input("Enter the empid: "))#getting employee id
    if (len(str(empid))<3):
        print("empid must be 3 digits or more!!")
        return 0
    try:
        with open("emp.txt", 'r') as myfile:
            l = myfile.readlines()
            l = [x.strip() for x in l]
            for line in l:
                if line.startswith("empid") and line.endswith(str(empid)):  
                    print("Employee id already exists!!")
                    return 0
    except FileNotFoundError:
    	print("File emp.txt does not exist!!")
    	return 0

    ename=input("Enter the name: ")#getting name of employee
    ename=ename.upper()

    sal=int(input("Enter the salary: "))#getting salary of employee
    if sal<3000:
        print("Salary should be more than 3000!!")
        return 0

    dep=int(input("Enter the deptno: "))#getting dept no of employee
    if dep!=10 and dep!=20 and dep!=30:
        print("Deptno should be either 10, 20 or 30!!")
        return 0

    #storing details of employee in a file
    with open("emp.txt", "a") as file:
       s="empid = "+str(empid)+"\nename = "+ename+"\nsal = "+str(sal)+"\ndeptno = "+str(dep)+'\n'
       file.write(s)
    
    #storing details of each employee as a dictionary
    mydict={'empid': empid,'ename':ename,'sal':sal,'deptno':dep}
    with open('emp.pkl','rb') as file:
       mylist=pickle.load(file)
    #print(mylist)

    mylist.append(mydict)
    with open('emp.pkl','ab') as file:
       pickle.dump(mylist,file)
    #print(mylist)
    return mydict


#displaying employee details
def Display_Emp():
    try:
        with open('emp.pkl','rb') as myfile:
           mylist=pickle.load(myfile)
           myfile.close()
        for mydict in mylist:
           s="empid = "+str(mydict['empid'])+"\tename = "+mydict['ename']+"\tsal = "+str(mydict['sal'])+"\tdeptno = "+str(mydict['deptno'])+'\n'
           print(s)
	   
    except:
        print("No Employees")

#sorting all employees according to their deptno
def Separate_Data():
        with open("emp.pkl",'rb') as myfile:
            mylist=pickle.load(myfile)
            myfile.close()
            open('emp_10.txt','w').close()
            open('emp_20.txt','w').close()
            open('emp_30.txt','w').close()
            for mydict in mylist:
            	if mydict['deptno']==10:
            	   with open("emp_10.txt","a") as file1:
            	      s="empid = "+str(mydict['empid'])+"\tename = "+mydict['ename']+"\tsal = "+str(mydict['sal'])+"\tdeptno = "+str(mydict['deptno'])+'\n'
            	      file1.write(s)
            	   
            	if mydict['deptno']==20:
            	   with open("emp_20.txt","a") as file2:
            	      s="empid = "+str(mydict['empid'])+"\tename = "+mydict['ename']+"\tsal = "+str(mydict['sal'])+"\tdeptno = "+str(mydict['deptno'])+'\n'
            	      file2.write(s)
            	   
            	if mydict['deptno']==30:
            	   with open("emp_30.txt","a") as file3:
            	      s="empid = "+str(mydict['empid'])+"\tename = "+mydict['ename']+"\tsal = "+str(mydict['sal'])+"\tdeptno = "+str(mydict['deptno'])+'\n'
            	      file3.write(s)
            	   
        print("View details of :\n1.Dept-10\n2.Dept-20\n3.Dept-30")#menu to print specific deptno file
        ch=int(input("Enter your choice: "))
        if ch==1:
            with open("emp_10.txt",'r') as myfile:
                contents =  myfile.read()
                print (contents)
        elif ch==2:
            with open("emp_20.txt",'r') as myfile:
                contents =  myfile.read()
                print (contents)
        elif ch==3:
            with open("emp_30.txt",'r') as myfile:
                contents =  myfile.read()
                print (contents)
        else:
            print("wrong choice")

  
t = True
file=open('emp.pkl','rb')#file to store the list containing all employee details
mylist=pickle.load(file)
file.close()
#display menu
while t:
    ch = int(input("1. Add_emp \n2. Display_emp \n3. Separate_data \n4. Exit \n"))
    if ch == 1:
        dict=Add_Emp()
        if dict!=0:
           mylist.append(dict)
           file=open('emp.pkl','wb')
           pickle.dump(mylist,file)
           file.close()
        else:
           t = False
    elif ch == 2:
        Display_Emp()
    elif ch == 3:
        Separate_Data()
    else:
        t = False
