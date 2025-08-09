def Display_Pa():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        while True:
            print("Enter 1 :- If you want to check the Patient details with 'P_code'")
            print("Enter 2 :- If You want to check the Patient details with 'Mobile_No'")
            ch=int(input('Enter Your Choice:'))
            if ch==1:
                P_Code=input('Enter the P_Code:')
                q="select P_Code,Patient_name,Mobile_No,Gender,Age,Height_cm_,Weight_Kg_,Dt_admit,Disease,Med_Prescribed,dr_id from Patient where P_Code='{}'".format(P_Code)
                cur.execute(q)
                All=cur.fetchall()
                print('******************************************************************************************************************************************************************************')
                print('P_Code   ','   Patient_Name       ','        Mobile_No   ','   Gender  ','    Age','     Height','   Weight','    Date    ','      Symptom       ','           Med_Prescribed     ','       dr_id')
                for x in All:
                    n=0
                    j=list(x)
                    for i in j:
                        print(i,end='       ')
                        n=n+1
                        if n==11:
                            print(' ')
                print('*******************************************************************************************************************************************************************************')
                break
            elif ch==2:
                M=input('Enter the Mobile_No:')
                q="select P_code,Patient_name,Mobile_No,Gender,Age,Height_cm_,Weight_Kg_,Dt_admit,Disease,Med_Prescribed,dr_id from Patient where Mobile_No='{}'".format(M)
                cur.execute(q)
                All=cur.fetchall()
                print('******************************************************************************************************************************************************************************')
                print('P_Code   ','   Patient_Name       ','        Mobile_No   ','   Gender  ','    Age','     Height','   Weight','    Date    ','      Symptom       ','           Med_Prescribed     ','       dr_id')
                for x in All:
                    n=0
                    j=list(x)
                    for i in j:
                        print(i,end='       ')
                        n=n+1
                        if n==11:
                            print(' ')
                print('******************************************************************************************************************************************************************************')
                break
            else:
                print('Please Enter Valid Option')
    except Exception as Error:
        print(Error)


