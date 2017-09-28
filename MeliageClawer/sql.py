import pymysql

ip = 'localhost'
username = 'root'
userpassword = 'root'
dbname = 'airline'
conn = pymysql.connect(ip, username, userpassword, dbname)
cursor = conn.cursor()

class MileageDBManager:

    def __init__(self):
        #self.conn = sqlite3.connect('text.db')
        #print("database initiated")
        pass
    def isInCityList(self,cityName):
        sql=('SELECT CITYNAME FROM CITY')
        cursor.execute(sql)
        lst = cursor.fetchall()
        for a in lst:
            if cityName in a:
                return True
        return False

    def insertNewCity(self,cityName):
        if self.isInCityList(cityName):
            print("False")
            return

        
        cursor.execute("INSERT INTO CITY(CITYNAME) VALUES (\'%s\')"%cityName)
        conn.commit()

    def insertNewConnectData(self,cityName1,cityName2,FullMileage,ThreeQuaterMileage,HalfMileage):
        if self.isInConnectList(cityName1,cityName2,FullMileage):
            return

        cursor.execute("""
            INSERT INTO CONNECT(CITY1,CITY2,MILEAGEFULL,MILEAGE3QUARTER,MILEAGEHALF)
            VALUES ("%s","%s",'%s','%s','%s')
        """,(cityName1,cityName2,int(FullMileage),int(ThreeQuaterMileage),int(HalfMileage)))
        conn.commit()

    def isInConnectList(self,cityName1,cityName2,FullMileage):
        cursor.execute("""
            SELECT CITY1,CITY2,MILEAGEFULL FROM CONNECT
        """)

        lst = cursor.fetchall()
        for a in lst:
            if (FullMileage == a[2]) and ((cityName1 in a[0] and cityName2 in a[1]) or (cityName1 in a[1] and cityName2 in a[0])):
                return True
        return False