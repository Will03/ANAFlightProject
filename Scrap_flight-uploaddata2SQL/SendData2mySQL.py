import pymysql

def uploadAirline(*args):
    """
    pymysql is required to be imported

    if airlineID is already exist in table,
    data will be updated
    if not,
    add new data into table
    """
    Airline_ID= args[0]
    DepartureAirport = args[1]
    ArriveAirport = args[2]
    DepartureTime = args[3]
    ArriveTime = args[4]
    Kilos= args[5]
    ip = 'localhost'
    username = 'root'
    userpassword = 'root'
    dbname = 'test'
    db = pymysql.connect(ip, username, userpassword, dbname)
    cursor = db.cursor()
    
    sql='SELECT * FROM %s.airline WHERE %s.airline.ID = %s'%(dbname, dbname, args[0])
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close
        if(len(result)==0):#not in table, add new airline
            print('not in table')
            addData(Airline_ID,DepartureAirport,ArriveAirport,DepartureTime,ArriveTime,Kilos)
        else:#in the table, update data
            print('update old file')
            updateData(Airline_ID,DepartureAirport,ArriveAirport,DepartureTime,ArriveTime,Kilos)
            print('update done')
    except:
        print('Error')
    #db.close
def updateData(*args):
    ip = 'localhost'
    username = 'root'
    userpassword = 'root'
    dbname = 'test'
    db = pymysql.connect(ip, username, userpassword, dbname)
    cursor = db.cursor()
    sql = 'UPDATE airline SET DepartureAirport=\'%s\', ArriveAirport=\'%s\', DepartureTime=\'%s\', ArriveTime=\'%s\', kilos=\'%s\' WHERE ID = \'%s\''%(args[1], args[2],args[3],args[4],args[5],args[0])
    cursor.execute(sql)
    db.commit()
    db.close()

def addData(*args):
    ip = 'localhost'
    username = 'root'
    userpassword = 'root'
    dbname = 'test'
    db = pymysql.connect(ip, username, userpassword, dbname)
    cursor = db.cursor()
    sql = 'INSERT INTO airline(ID, DepartureAirport, ArriveAirport, DepartureTime, ArriveTime, kilos) VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'%(args[0],args[1],args[2],args[3],args[4],args[5])
    cursor.execute(sql)
    db.commit()
    db.close()

uploadAirline('05545645646546541312001', 'LOSW', 'TPE', '18:00', '19:00', '30')
