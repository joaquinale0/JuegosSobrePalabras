import sqlite3
class SqliteMy:
    def __init__(self):
        self.conn = sqlite3.connect("palabrasLocas.db")
        self.conn.close()

    @classmethod
    def id_tabla(self, columna, tabla):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select count(" + columna + ") from " + tabla + ";"
        cursor.execute(query)
        cantidad = cursor.fetchone()
        query = "select max(" + columna + ") from " + tabla + ";"
        if(cantidad[0] == 0):
            return 1
        else:
            cursor.execute(query)
            id_tab = cursor.fetchone()
            return id_tab[0] + 1

    @classmethod
    def tablaVacia (self, columna, tabla):
        if(self.id_tabla( columna , tabla) == 1):
            return True
        else:
            return False