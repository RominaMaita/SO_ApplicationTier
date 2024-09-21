from Connection import *

class Products:
    def addProducts(name, price, date, stock):
        try:
            conect = CConection.ConectionDataBase()
            cursor = conect.cursor()
            
            sql = "insert into products values(null, %s, %s, %s, %s);"
            
            values = (name, price, date, stock)
            cursor.execute(sql, values)
            conect.commit()
            print(cursor.rowcount, "Registro ingresado")
            conect.close()
            
        except mysql.connector.Error as error:
            print("Error".format(error))
        
        