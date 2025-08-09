def _Bill_():
    import mysql.connector as myc
    import datetime
    import random
    import math
    def Tup_str(T):
        st=''
        for i in T:
            st=st+i
        return st
    db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
    cur=db.cursor()
    P=input('Enter P_Code:')
    Q=int(input('Enter The Quantity of Medicine:'))
    q="select Patient_name from Patient where P_code='{}'".format(P)
    cur.execute(q)
    All=cur.fetchall()
    A=All[0]
    Pa=Tup_str(A)
    Ag="select Age from Patient where P_code='{}'".format(P)
    cur.execute(Ag)
    ALl=cur.fetchall()
    A=ALl[0]
    Age=Tup_str(A)
    r="select Dr_Name from Patient,Doctor where Doctor.dr_id=Patient.dr_id and P_code='{}'".format(P)
    cur.execute(r)
    Al=cur.fetchall()
    B=Al[0]
    Dr_=Tup_str(B)
    M="select Med_Prescribed from Patient where P_code='{}'".format(P)
    cur.execute(M)
    Alll=cur.fetchall()
    C=Alll[0]
    Med=Tup_str(C)
    M_C="select M_code from Medicine where Med_Name='{}'".format(Med)
    cur.execute(M_C)
    All=cur.fetchall()
    C=All[0]
    Mc=Tup_str(C)
    Pr="select Price from Medicine where Med_Name='{}'".format(Med)
    cur.execute(Pr)
    AL=cur.fetchall()
    D=AL[0]
    Price=Tup_str(D)
    def T_Sec(s):
        c=0   
        for i in range(0,len(s)):
            if(s[i]!=''):
                c=c+1
        e=2-c
        for i in range(0,e):
            s=s+' '
        return s
    print("\t\t\t\t\t\t\t************************")
    print("\t\t\t\t\t\t\t|         Bill         |")
    print("\t\t\t\t\t\t\t************************")
    print(" \t ___________________________________________________________________________________________________________________")
    print("\t|                                                                                                                   |")
    print("\t|                                              A B C HOSPITAL                                                       |")
    print("\t|                                                 PHARMACY                                                          |")
    print("\t|                                                                                  Address:- Near Malabar House     |")
    print("\t| Contact No: +91 9074938234                                                       Email: Qwertyasdf123@gmail.com   |")
    print("\t|___________________________________________________________________________________________________________________|")
    tdate=datetime.datetime.now()
    se=tdate.second
    s=T_Sec(str(se))
    print('\t|Date:- ',datetime.date.today(),'\t\t\t\t\t\t\t\t\t      ','Time:- ',tdate.hour,':',tdate.minute,':',s,'|')
    a=random.choice('1234567890')
    b=random.choice('1234567890')
    c=random.choice('1234567890')
    d=random.choice('1234567890')
    e=random.choice('1234567890')
    f=random.choice('1234567890')
    g=random.choice('1234567890')
    h=random.choice('1234567890')
    i=random.choice('1234567890')
    j=random.choice('1234567890')
    Bill_No=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)
    print('\t|Bill_Number=',Bill_No,'                                                                                           |')
    print('\t|Gst_In: 323DSHJ3348SLKUU8945                                                                                       |')
    print('\t|Patient Name :',Pa,'\t Age :',Age,'                                                                  |')
    print('\t|Doctor Name :',Dr_,'                                                                                |')
    print('\t|   _____________________________________________________________________________________________________________   |')
    print('\t|  | Medicine \t\tMRP/per1 \t Batch \t    Quantity \t  Discount  \t Tax \t      Total              |  |' )
    Mrp=int(Price)*Q
    Tax=int(Price)*8/100
    dis=int(Price)*3/100
    Tot=Mrp+Tax-dis
    To='%.2f'%Tot
    g=Tot*5/100
    h='%.2f'%g
    print('\t|  |',Med,Price,'\t',Mc,'\t     ',Q,'\t ','-',dis,'\t',Tax,'\t    ',To                ,'            |  |')
    print('\t|  |_____________________________________________________________________________________________________________|  |')
    print('\t|  |  \tSGST :',h,'\t\t CGST:',h,'            ','                  Net Price   :  ',To,'            |  |')
    print('\t|  |_____________________________________________________________________________________________________________|  |')
    print("\t|                                                                                                                   |")
    print("\t|                                                                                                                   |")
    print('\t|\t\t\t\t\t *** WhatsApp No: 9342187343 *** \t\t\t\t\t    |')
    print('\t|___________________________________________________________________________________________________________________|')



































    
    
