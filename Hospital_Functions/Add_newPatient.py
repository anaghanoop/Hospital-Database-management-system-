def Add_New_Pa():
    import mysql.connector as myc
    import random
    db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
    cur=db.cursor()
    try:
        def Gender_(G):
            c=0   
            for i in range(0, len(G)):
                if(G[i]!=''):
                    c=c+1
            if c==4:
                G=G+"  "
            return G
        def P_Name(P):
            c=0   
            for i in range(0,len(P)):
                if(P[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                P=P+' '
            return P
        def Symptom_(D):
            c=0   
            for i in range(0,len(D)):
                if(D[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                D=D+' '
            return D
        Patient_Name=input('Enter the name of Patient:')
        Mobile_No=int(input('Enter Mobile Number:'))
        Gender=input('Enter Gender of the Patient:')
        Age=int(input('Enter the Age of Patient:'))
        Height_cm_=int(input('Enter the Height of Patient:'))
        Weight_kg_=int(input('Enter the Weight of Patient:'))
        Dt_admit=input('Enter the Date:')
        Symptom=input('Enter the Symptom of Patient:')
        dr_id=input("Enter Doctor's Id:")
        Null=' '
        P=P_Name(Patient_Name)
        G=Gender_(Gender)
        S=Symptom_(Symptom)
        a=random.choice('ABCDEFCGHIJKLMNOPQRSTUVWXYZ')
        b=random.choice('1234567890')
        c=random.choice('1234567890')
        d=random.choice('1234567890')
        e=random.choice('1234567890')
        f=random.choice('1234567890')
        P_Code=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
        q="insert into Patient values('{}','{}',{},'{}',{},{},{},'{}','{}','{}','{}')".format(P_Code,P,Mobile_No,G,Age,Height_cm_,Weight_kg_,Dt_admit,S,Null,dr_id)
        cur.execute(q)
        db.commit()
        print(cur.rowcount,'Record(s) inserted')
        print('**********************')
        print('Your P_code is',P_Code)
        print('**********************')
        cur.close()
        db.close()
    except Exception as Error:
        print(Error)




























