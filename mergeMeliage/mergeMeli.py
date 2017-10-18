import pymysql
import sys
username = 'root'
userpassword = 'root'
ip = 'localhost'


def connect_mySQL(ip, username, userpassword, dbname):
        try:
            db = pymysql.connect(ip, username, userpassword, dbname)
            cursor = db.cursor()
            db_list = [db,cursor]
            return db_list
        except pymysql.Error as e:
            print ("Error '%d': '%s'"%(e.args[0], e.args[1]))

class mergeMeliage:
    def change_airport_to_Prefecture(self, airport):
        dbname = 'test'
        db_list = connect_mySQL(ip, username, userpassword, dbname)
        db_list[1].execute("SELECT Prefecture FROM airport WHERE IATA='%s'"%(airport))
        lst = db_list[1].fetchall()
        if(len(lst)>1 or len(lst)<1):
            return "error"

        else:
            return lst[0][0]
    def catch_all_airline_airport(self):
        dbname = 'test'
        db_list = connect_mySQL(ip, username, userpassword, dbname)
        db_list[1].execute("SELECT DepartureAirport,ArriveAirport FROM airline WHERE 1")
        lst = db_list[1].fetchall()
        return lst
    def find_the_Meliage(self,departure,arrive):
        dbname = 'airline'
        db_list = connect_mySQL(ip, username, userpassword, dbname)
        print(departure,arrive)
        db_list[1].execute("SELECT MILEAGEFULL FROM CONNECT WHERE CITY1='%s' AND CITY2='%s'"%(departure,arrive))
        lst = db_list[1].fetchall()
        if(len(lst)<1):
            db_list[1].execute("SELECT MILEAGEFULL FROM CONNECT WHERE CITY1='%s' AND CITY2='%s'"%(arrive,departure))
            lst = db_list[1].fetchall()
        if(len(lst)<1):
            return 0
        
        return lst[0][0]
    def upload_the_Meliage(self,Meli,departure,arrive):
        dbname = 'test'
        db_list = connect_mySQL(ip, username, userpassword, dbname)
        db_list[1].execute("UPDATE airline SET kilos='%s' WHERE DepartureAirport = '%s' AND ArriveAirport = '%s'"%(Meli,departure,arrive))
        db_list[0].commit()
        print("OK")


