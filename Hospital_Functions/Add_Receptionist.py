def Add_Recepti():
    import mysql.connector as myc
    import random
    db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
    cur=db.cursor()
    try:
        def Gender_(Gender):
            c=0   
            for i in range(0, len(Gender)):
                if(Gender[i]!=''):
                    c=c+1
            if c==4:
                Gender=Gender+"  "
            return Gender
        def R_Name(R):
            c=0   
            for i in range(0,len(R)):
                if(R[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                R=R+' '
            return R
        R_Nam=input('Enter the name of Receptionist:')
        Gender=input('Enter Gender of the Receptionist:')
        Age=int(input('Enter the Age of the Receptionist:'))
        Salary=int(input('Enter the Salary of the Receptionist:'))
        Passwd=input('Enter The Password (5 Characters):')
        Work_Ho=input('Enter the Working Hours(--AM - --PM):')
        R=R_Name(R_Nam)
        G=Gender_(Gender)
        a=random.choice('ABCDEFCGHIJKLMNOPQRSTUVWXYZ')
        b=random.choice('1234567890')
        c=random.choice('1234567890')
        R_id=str(a)+str(b)+str(c)
        q="insert into Receptionist values('{}','{}',{},{},'{}','{}','{}')".format(R_id,R,Age,Salary,Work_Ho,Passwd,G)
        cur.execute(q)
        db.commit()
        print(cur.rowcount,'Record(s) inserted')
        print('**********************')
        print('Your R_id is',R_id)
        print('**********************')
        cur.close()
        db.close()
    except Exception as Error:
        print(Error)




















