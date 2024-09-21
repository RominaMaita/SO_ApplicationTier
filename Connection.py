import mysql.connector

class CConection:
    def ConectionDataBase():
        try:
            conection = mysql.connector.connect(user='root',
                                                password='Admin123admin', 
                                                host = '127.0.0.1',
                                                database='greenbiteproject', 
                                                port='3306')
            print("Conexion exitosa")
            
            return conection
        except mysql.connector.Error as error:
            print("No funciona mi chamo".format(error))        