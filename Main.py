print('✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨')
print("\t\t\t _____________________________________________________________________________")
print("\t\t\t|                                                                             |")
print("\t\t\t|                                                                             |")
print("\t\t\t|                     Welcome Hospital Management System                      |")
print("\t\t\t|                                                                             |")
print("\t\t\t|_____________________________________________________________________________|")

while True:
    print('\t-------------------------------')
    print('\tEnter 1:- To Enter Admin Mode :')
    print('\tEnter 2:- To Enter User Mode:')
    print('\tEnter 3:- To Exit the Database:')
    print('\t-------------------------------')
    ch=int(input('Enter the Mode:'))
    if ch==1:
        print("\t\t\t\t\t  *****************************************")
        print("\t\t\t\t\t  |         Welcome to admin mode         |")
        print("\t\t\t\t\t  *****************************************")
        while True:
            Passwd=input('Enter the Password')
            if Passwd=='123':
                while True:
                    print('\t----------------------------------------')
                    print('\tEnter (a) to Manage Doctor Details')
                    print('\tEnter (b) to Manage Patient Details')
                    print('\tEnter (c) to Manage Receptionist Details')
                    print('\tEnter (d) to Manage Medicine Details')
                    print('\tEnter (e) to Generate Bill')
                    print('\tEnter (f) to Exit Admin Mode:')
                    print('\t----------------------------------------')
                    c=input('Enter the Option:')
                    if c=='a':
                        while True:
                            print('\t-------------------------------')
                            print('\tEnter 1 to Hire a Doctor:')
                            print('\tEnter 2 to Display All Doctors:')
                            print('\tEnter 3 to Go Back ')
                            print('\t-------------------------------')
                            cho=int(input('Enter the Option:'))
                            if cho==1:
                                from Hospital_Functions import Hire_Doctor
                                Hire_Doctor.Hire()
                            elif cho==2:
                                from Hospital_Functions import Display_Doc_Adm
                                Display_Doc_Adm.Display_Adm()
                            elif cho==3:
                                break
                            else:
                                print('Please Enter the Valid Option')
                    elif c=='b':
                        while True:
                            print('\t-------------------------------------------------')
                            print('\tEnter 1 to Add a Patient:')
                            print('\tEnter 2 to Add Medicine Prescribed by the Doctor:')
                            print("\tEnter 3 to Display All Patient's Detail:")
                            print("\tEnter 4 to Display a Paticular Patient's Detail:")
                            print('\tEnter 5 to Go Back ')
                            print('\t-------------------------------------------------')
                            ch=int(input('Enter the Option:'))
                            if ch==1:
                                from Hospital_Functions import Add_newPatient
                                Add_newPatient.Add_New_Pa()
                            elif ch==2:
                                from Hospital_Functions import Add_Med_Prescribed
                                Add_Med_Prescribed.Add_Med()
                            elif ch==3:
                                from Hospital_Functions import Display_allPatient
                                Display_allPatient.Display_All_Pa()
                            elif ch==4:
                                from Hospital_Functions import Display_Patient
                                Display_Patient.Display_Pa()
                            elif ch==5:
                                break
                            else:
                                print('Please Enter the Valid Option')
                    elif c=='c':
                        while True:
                            print('\t----------------------------------------------')
                            print('\tEnter 1 to Add a Receptionist:')
                            print('\tEnter 2 to Display All Receptionists Detail:')
                            print("\tEnter 3 to Delete the Data of A Receptionist:")
                            print('\tEnter 4 to Go Back ')
                            print('\t----------------------------------------------')
                            c=int(input('Enter the Option:'))
                            if c==1:
                                from Hospital_Functions import Add_Receptionist
                                Add_Receptionist.Add_Recepti()
                            elif c==2:
                                from Hospital_Functions import Display_Receptionist
                                Display_Receptionist.Display_Recept()
                            elif c==3:
                                from Hospital_Functions import Delete_Receptionist
                                Delete_Receptionist.Delete_Recept()
                            elif c==4:
                                break 
                            else:
                                print('Please Enter the Valid Option')
                    elif c=='d':
                        while True:
                            print('\t------------------------------------------------------------')
                            print('\tEnter 1 to Add a Medicine:')
                            print("\tEnter 2 to Display All Medicine Details:")
                            print('\tEnter 3 to Display Medicine Detail for a Paticular Patient:')
                            print('\tEnter 4 to Go Back ')
                            print('\t------------------------------------------------------------')
                            c=int(input('Enter the Option:'))
                            if c==1:
                                from Hospital_Functions import Add_Medicine
                                Add_Medicine.Add_Med()
                            elif c==2:
                                from Hospital_Functions import Display_Medicine
                                Display_Medicine.Display_Med()
                            elif c==3:
                                from Hospital_Functions import Display_Med_Pa_
                                Display_Med_Pa_.Display_Med_Pa_s()
                            elif c==4:
                                break 
                            else:
                                print('Please Enter the Valid Option')
                    elif c=='e':
                        from Hospital_Functions import Bill
                        Bill._Bill_()         
                    elif c=='f':
                        break
                    else:
                        print('Please Enter the Valid Option')
                break
            else:
                print('**********************************')
                print('Please Enter The Correct Password:')
                print('**********************************')
                
    elif ch==2:
        print("\t\t\t\t\t  *****************************************")
        print("\t\t\t\t\t  |          Welcome to User mode         |")
        print("\t\t\t\t\t  *****************************************")
        while True:
            print('\t-----------------------------------')
            print('\tEnter 1 To Enter Receptionist mode:')
            print('\tEnter 2 To Enter Doctor mode:')
            print('\tEnter 3 To Enter Pharmacist mode:')
            print('\tEnter E/e To Exit User Mode:')
            print('\t-----------------------------------')
            o=input('Enter Your Option:')
            if o=='1':
                print("\t\t\t\t\t***********************************************")
                print("\t\t\t\t\t|        Welcome to Receptionist mode         |")
                print("\t\t\t\t\t***********************************************")
                while True:
                    print('\t-------------------------------------------------')
                    print('\tEnter 1 to Display All Doctors :')
                    print("\tEnter 2 to Display a Paticular Patient's Detail:")
                    print("\tEnter 3 to Add a Patient:")
                    print('\tEnter E/e to Exit Receptionist Mode:')
                    print('\t-------------------------------------------------')
                    cho=input('Enter the Option:')
                    if cho=='1':
                        from Hospital_Functions import Display_Doc_U
                        Display_Doc_U.Display_U()
                    elif cho=='2':
                        from Hospital_Functions import Display_Patient
                        Display_Patient.Display_Pa()
                    elif cho=='3':
                        from Hospital_Functions import Add_newPatient
                        Add_newPatient.Add_New_Pa()
                    elif cho=='E' or cho=='e':
                        break
                    else:
                        print('Please Enter the Valid Option')
            elif o=='2':
                print("\t\t\t\t\t*******************************************")
                print("\t\t\t\t\t|          Welcome to Doctor mode         |")
                print("\t\t\t\t\t*******************************************")
                while True:
                    print('\t------------------------------------------------------------')
                    print('\tEnter 1 to Add Medicine Prescribed by the Doctor:')
                    print("\tEnter 2 to Display List of Patients and Particular doctor:")
                    print("\tEnter 3 to Display Medicines:")
                    print('\tEnter E/e to Exit Doctor Mode:')
                    print('\t------------------------------------------------------------')
                    c=input('Enter the Option:')
                    if c=='1':
                        from Hospital_Functions import Add_Med_Prescribed
                        Add_Med_Prescribed.Add_Med()
                    elif c=='2':
                        from Hospital_Functions import Display_Pat_Doctor
                        Display_Pat_Doctor.Display_Pa_Doc()
                    elif c=='3':
                        from Hospital_Functions import Display_Medicine
                        Display_Medicine.Display_Med()
                    elif c=='e' or c=='E':
                        break
                    else:
                        print('Please Enter the Valid Option')
            elif o=='3':
                print("\t\t\t\t\t***********************************************")
                print("\t\t\t\t\t|          Welcome to Pharmacist mode         |")
                print("\t\t\t\t\t***********************************************")
                while True:
                    print('\t---------------------------------')
                    print('\tEnter 1 to Add Medicine:')
                    print('\tEnter 2 to Display Medicine:')
                    print("\tEnter 3 to Generate Bill:")
                    print('\tEnter E/e to Exit Pharmicist Mode:')
                    print('\t---------------------------------')
                    c=input('Enter the Option:')
                    if c=='1':
                        from Hospital_Functions import Add_Medicine
                        Add_Medicine.Add_Med()
                    elif c=='2':
                        from Hospital_Functions import Display_Medicine
                        Display_Medicine.Display_Med()
                    elif c=='3':
                        from Hospital_Functions import Bill
                        Bill._Bill_()
                    elif c=='e' or c=='E':
                        break
                    else:
                        print('Please Enter the Valid Option')
                        
            elif o=='e' or o=='E':
                break
            else:
                print('Please Enter the Valid Option')          
    elif ch==3:
        print('\t\t\t\t\t      ***********************************')
        print('\t\t\t\t\t      * Thank You For Your Pleasure Time*')
        print('\t\t\t\t\t      *  Always Welcome To Our Database *\n')
        print('\t\t\t\t\t      *\t😊 Visit Again  😊        *')
        print('\t\t\t\t\t      ***********************************')
        break
    else:
        print('Please Enter the Valid Option')
                    
print('✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨')









































                    
