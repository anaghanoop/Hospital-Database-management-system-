def Display_All_Pa():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        q="select * from Patient"
        cur.execute(q)
        All=cur.fetchall()
        print('***********************************************************************************************************************************************************')
        print('P_code  ','  Patient_Name     ','       Mobile_No  ','   Gender  ','  Age','  Height',' Weight','   Date   ','      Symptom        ','        Med_Prescribed     ','Dr_id')
        for x in All:
            n=0
            j=list(x)
            for i in j:
                print(i,end='     ')
                n=n+1
                if n==11:
                   print(' ')
        print('***********************************************************************************************************************************************************')
    except Exception as Error:
        print(Error)

