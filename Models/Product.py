class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            #VER SI ESTO SE QUEDA
            sql = """CREATE TABLE IF NOT EXISTS producto
                        (Cod int,
                        Nombre varchar,
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
    
    def getProduct(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM producto WHERE cod = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateProduct(self,cod,nombre,cantidad,stockmax,stockmin,precio):
        with self.conn.cursor() as cursor:
            sql = """UPDATE producto SET
            COD = %s,  
            NOMBRE = %s, 
            CANTIDAD = %s, 
            STOCKMAX = %s,
            STOCKMIN = %s,
            PRECIO = %s 
            WHERE cod = %s """
            cursor.execute(sql,(cod,nombre,cantidad,stockmax,stockmin,precio))
            self.conn.commit()

    def deleteProduct(self,cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM producto WHERE cod = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
    
    def insertProduct(self,cod, nombre, cantidad, stockmax, stockmin, precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO producto (cod, nombre, cantidad, stockmax, stockmin, precio) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (cod, nombre, cantidad, stockmax, stockmin, precio))
            self.conn.commit()