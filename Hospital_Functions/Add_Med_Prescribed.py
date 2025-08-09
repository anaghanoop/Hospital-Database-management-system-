def Add_Med():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        def Med_P(Me):
            c=0   
            for i in range(0,len(Me)):
                if(Me[i]!=''):
                    c=c+1
            e=20-c
            for i in range(0,e):
                Me=Me+' '
            return Me
        while True:
            print("Enter 1 :- If you want to check the Patient details with 'P_code'")
            print("Enter 2 :- If You want to check the Patient details with 'Mobile_No'")
            ch=int(input('Enter Your Choice:'))
            if ch==1:
                P_Code=input('Enter the P_Code:')
                M=input('Enter the Medicine Prescribed by Doctor:')
                Me=Med_P(M)
                q="update Patient set Med_Prescribed='{}' where P_code='{}'".format(Me,P_Code)
                cur.execute(q)
                print(cur.rowcount,'Record(s) Added')
                db.commit()
                cur.close()
                db.close()
                break
                break
        
            elif ch==2:
                Mo=input('Enter the Mobile_No:')
                M=input('Enter the Medicine Prescribed by Doctor:')
                Me=Med_P(M)
                q="update Patient set Med_Prescribed='{}' where Mobile_No={}".format(Me,Mo)
                cur.execute(q)
                print(cur.rowcount,'Record(s) Added')
                db.commit()
                cur.close()
                db.close()
                break
                break
        
            else:
                print('Please Enter Valid Option')
    except Exception as Error:
        print(Error)
Add_Med()

