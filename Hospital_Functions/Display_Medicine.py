def Display_Med():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        q="select * from Medicine"
        cur.execute(q)
        All=cur.fetchall()
        print('**************************************************************')
        print('M_code   ','  M_Name        ','      Price','   Symptom')
        for x in All:
            n=0
            j=list(x)
            for i in j:
                print(i,end='    ')
                n=n+1
                if n==4:
                    print(' ')
        print('**************************************************************')
    except Exception as Error:
        print(Error)
