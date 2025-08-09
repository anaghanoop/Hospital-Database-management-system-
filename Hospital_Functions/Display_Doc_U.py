def Display_U():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        q="select dr_id,Dr_Name,Gender,Specialisation,Age,Salary,Fees from Doctor"
        cur.execute(q)
        All=cur.fetchall()
        print('*******************************************************************************')
        print('Dr_id   ','  Dr_Name     ','      Gender ',' Specialisaton     ','    Age',' Salary','  Fee')
        for x in All:
            n=0
            j=list(x)
            for i in j:
                print(i,end='   ')
                n=n+1
                if n==7:
                   print(' ')
        print('*******************************************************************************')
    except Exception as Error:
        print(Error)

