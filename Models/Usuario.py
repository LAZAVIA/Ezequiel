class Usuario():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            
            sql = """CREATE TABLE IF NOT EXISTS usuario
                        (Nombre varchar(50) NOT NULL,
                        contrasena varchar(50) NOT NULL)"""
            cursor.execute(sql)
            self.conn.commit()
            
    def getUsuario(self, usuario, contrasena):
        with self.conn.cursor() as cursor:
            sql = """SELECT usuario_nombre FROM usuario WHERE usuario_nombre = %s AND contrasena = %s"""
            cursor.execute(sql, (usuario, contrasena))
            result = cursor.fetchone()
            return result