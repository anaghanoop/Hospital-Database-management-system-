def Hire():
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
        def Dr_Name(Doctor_Name):
            c=0   
            for i in range(0,len(Doctor_Name)):
                if(Doctor_Name[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                Doctor_Name=Doctor_Name+' '
            return Doctor_Name
        def Specialisation_(S):
            c=0   
            for i in range(0,len(S)):
                if(S[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                S=S+' '
            return S
        Doctor_Name=input('Enter the name of Doctor:')
        Gender=input('Enter Gender of the Doctor:')
        Specialisation=input('Enter the Specialisation of the Doctor')
        Age=int(input('Enter the Age of Doctor:'))
        Salary=int(input('Enter the Salary of the Doctor:'))
        Fees=int(input('Enter the Fees:'))
        Passwd=input('Enter The Password (5 Characters):')
        D=Dr_Name(Doctor_Name)
        G=Gender_(Gender)
        S=Specialisation_(Specialisation)
        a=random.choice('ABCDEFCGHIJKLMNOPQRSTUVWXYZ')
        b=random.choice('1234567890')
        c=random.choice('1234567890')
        d=random.choice('1234567890')
        dr_id=str(a)+str(b)+str(c)+str(d)
        q="insert into Doctor values('{}','{}','{}','{}',{},{},{},'{}')".format(dr_id,D,G,S,Age,Salary,Fees,Passwd)
        cur.execute(q)
        db.commit()
        print(cur.rowcount,'Record(s) inserted')
        print('**********************')
        print('Your dr_id is',dr_id)
        print('**********************')
        cur.close()
        db.close()
    except Exception as Error:
        print(Error)































 
