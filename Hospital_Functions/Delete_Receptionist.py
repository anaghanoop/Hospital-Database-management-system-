def Delete_Recept():
    import mysql.connector as myc
    try:
        db=myc.connect(host='localhost',user='root',passwd='mysql',database='design_project')
        cur=db.cursor()
        R_id=input('Enter R_code:')
        q="Delete from Receptionist where R_code='{}'".format(R_id)
        cur.execute(q)
        db.commit()
        print(cur.rowcount,'Deleted')
        cur.close()
        db.close()
    except Exception as Error:
        print(Error)
