def Display_Med_Pa_s():
    import mysql.connector as myc
    try:
        def Tup_str(T):
            st=''

            for i in T:
                st=st+i

            return st
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        p=input('Enter the P_code:')
        q="select Med_Prescribed from Patient where P_code='{}'".format(p)
        cur.execute(q)
        All=cur.fetchall()
        A=All[0]
        Med=Tup_str(A)
        c="select * from Medicine where Med_Name='{}'".format(Med)
        cur.execute(c)
        All=cur.fetchall()
        print('***************************************************')
        print('M_code  ','Med_Name     ','         Price','    Symptom        ')
        for x in All:
            n=0
            j=list(x)
            for i in j:
                print(i,end='    ')
                n=n+1
                if n==4:
                    print(' ')
        print('***************************************************')
    except Exception as Error:
        print(Error)
    
