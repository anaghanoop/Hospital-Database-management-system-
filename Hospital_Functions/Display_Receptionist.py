def Display_Recept():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        q="select * from Receptionist"
        cur.execute(q)
        All=cur.fetchall()
        print('****************************************************************************')
        print('R_id   ','  R_Name        ','      Age ',' Salary','  Work_Hours','   Password',' Gender')
        for x in All:
            n=0
            j=list(x)
            for i in j:
                print(i,end='    ')
                n=n+1
                if n==7:
                    print(' ')
        print('****************************************************************************')
    except Exception as Error:
        print(Error)
