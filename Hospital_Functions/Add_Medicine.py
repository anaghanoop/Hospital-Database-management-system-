def Add_Med():
    import mysql.connector as myc
    import random
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        def Med_Name(Me):
            c=0   
            for i in range(0,len(Me)):
                if(Me[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                Me=Me+' '
            return Me
        def Symptom_(D):
            c=0   
            for i in range(0,len(D)):
                if(D[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                D=D+' '
            return D
        def Price_(P):
            c=0   
            for i in range(0,len(P)):
                if(P[i]!=''):
                    c=c+1
            e=5-c
            for i in range(0,e):
                P=P+' '
            return P
        M_Name=input('Enter the Medicine Name :')
        Price=input('Enter the Price of the Medicine:')
        Symptom=input('Enter the Symptom:')
        Me=Med_Name(M_Name)
        S=Symptom_(Symptom)
        P=Price_(Price)
        a=random.choice('ABCDEFCGHIJKLMNOPQRSTUVWXYZ')
        b=random.choice('1234567890')
        c=random.choice('1234567890')
        d=random.choice('1234567890')
        e=random.choice('1234567890')
        M_code=str(a)+str(b)+str(c)+str(d)+str(e)
        q="insert into medicine values('{}','{}','{}','{}')".format(M_code,Me,P,S)
        cur.execute(q)
        print(cur.rowcount,'Record(s) Added')
        print('**********************')
        print('Your M_code is',M_code)
        print('**********************')
        db.commit()
        cur.close()
        db.close()
    except Exception as Error:
        print(Error)





























