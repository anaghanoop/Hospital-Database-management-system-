def Display_Pa_Doc():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        while True:
            print("Enter 1 :- To Display The List of Patients under a Dr_id'")
            print("Enter 2 :- To Display a Particular Patient under a Dr_id'")
            ch=int(input('Enter Your Choice:'))
            if ch==1:
                dr_id=input('Enter the dr_id:')
                q="select * from Patient where dr_id='{}'".format(dr_id)
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
                P_Code=input('Enter the P_Code:')
                dr_id=input('Enter the dr_id:')
                q="select * from Patient where dr_id='{}' and P_code='{}'".format(dr_id,P_Code)
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



