def Display_Adm():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        q="select * from Doctor"
        cur.execute(q)
        All=cur.fetchall()
        print('*****************************************************************************************')
        print('Dr_id   ','  Dr_Name     ','      Gender ',' Specialisaton     ','    Age',' Salary','  Fee',' Password')
        for x in All:
            n=0
            j=list(x)
            for i in j:
                print(i,end='   ')
                n=n+1
                if n==8:
                   print(' ')
        print('*****************************************************************************************')
    except Exception as Error:
        print(Error)

