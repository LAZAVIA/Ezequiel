class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            #VER SI ESTO SE QUEDA
            sql = """CREATE TABLE IF NOT EXISTS producto
                        (COD VARCHAR(15) NOT NULL,
                        LOTE VARCHAR(20) NOT NULL, 
                        NOMBRE VARCHAR(50) NOT NULL,
                        DETALLE TEXT(500),
                        CANTIDAD INT(10) NOT NULL,
                        FECHA_ING DATE NOT NULL,
                        FECHA_VENC DATE NOT NULL)
                        PRECIO (30) NOT NULL"""
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
    
    def updateProduct(self,cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio):
        with self.conn.cursor() as cursor:
            sql = """UPDATE producto SET
            COD = %s, 
            LOTE = %s, 
            NOMBRE = %s, 
            DETALLE = %s, 
            CANTIDAD = %s, 
            FECHA_ING = %s, 
            FECHA_VENC = %s, 
            PRECIO = %s 
            WHERE cod = %s """
            cursor.execute(sql,(cod, lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio))
            self.conn.commit()

    def deleteProduct(self,cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM producto WHERE cod = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
    
    def insertProduct(self,cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO producto (cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio))
            self.conn.commit()