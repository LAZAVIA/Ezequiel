class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            #VER SI ESTO SE QUEDA
            sql = """CREATE TABLE IF NOT EXISTS producto
                        (COD INT NOT NULL,
                        NOMBRE VARCHAR NOT NULL,
                        CANTIDAD INT NOT NULL,
                        STOCKMAX INT NOT NULL,
                        STOCKMIN INT NOT NULL,
                        FECHA_ING DATE NOT NULL, 
                        FECHA_EGR DATE NOT NULL,
                        FECHA_VTO DATE NOT NULL,
                        PRECIO FLOAT NOT NULL)"""
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
    
    def updateProduct(self,cod,nombre,cantidad,stockmax,stockmin,fecha_ing,fecha_egr,fecha_vto,precio):
        with self.conn.cursor() as cursor:
            sql = """UPDATE producto SET
            COD = %s,  
            NOMBRE = %s, 
            CANTIDAD = %s, 
            STOCKMAX = %s,
            STOCKMIN = %s,
            FECHA_ING = %s,
            FECHA_EGR = %s, 
            FECHA_VTO = %s, 
            PRECIO = %s 
            WHERE cod = %s """
            cursor.execute(sql,(cod,nombre,cantidad,stockmax,stockmin,fecha_ing,fecha_egr,fecha_vto,precio))
            self.conn.commit()

    def deleteProduct(self,cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM producto WHERE cod = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
    
    def insertProduct(self,cod, nombre, cantidad, stockmax, stockmin, fecha_ing, fecha_egr, fecha_vto, precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO producto (cod, nombre, cantidad, fecha_ing, fecha_egr, fecha_vto, precio) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (cod, nombre, cantidad, stockmax, stockmin, fecha_ing, fecha_egr, fecha_vto, precio))
            self.conn.commit()