class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            
            sql = """CREATE TABLE IF NOT EXISTS producto
                        (Nombre varchar,
                        Cantidad int,
                        StockMax int,
                        StockMin int,
                        Precio float)"""
            cursor.execute(sql)
            self.conn.commit()
    
    def getProducts(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM producto"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getProduct(self, nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM producto WHERE Nombre = %s"""
            cursor.execute(sql, nombre)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateProduct(self,nombre,cantidad,stockmax,stockmin,precio):
        with self.conn.cursor() as cursor:
            sql = """UPDATE producto SET
              
            NOMBRE = %s, 
            CANTIDAD = %s, 
            STOCKMAX = %s,
            STOCKMIN = %s,
            PRECIO = %s 
            WHERE nombre = %s """
            cursor.execute(sql,(nombre,cantidad,stockmax,stockmin,precio))
            self.conn.commit()

    def deleteProduct(self,nombre):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM producto WHERE nombre = %s"""
            cursor.execute(sql, nombre)
            self.conn.commit()
    
    def insertProduct(self, nombre, cantidad, stockmax, stockmin, precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO producto (nombre, cantidad, stockmax, stockmin, precio) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nombre, cantidad, stockmax, stockmin, precio))
            self.conn.commit()