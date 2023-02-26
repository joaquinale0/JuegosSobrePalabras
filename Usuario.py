import sqlite3
from SqliteMy import SqliteMy

class Usuario:
    def __init__(self, usuario, contrasena, administracion, idUsuario): 
        self.__idUsuario = idUsuario 
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__administracion = administracion
  
    def __str__(self):
        cadena= "\nIdUsuario: " + str(self.__idUsuario)
        cadena+= "\nUsuario: " + self.__usuario
        cadena+= "\nContrasena: " + self.__contrasena
        cadena+= "\nAdministracion: " + str(self.__administracion)
        return cadena

    @classmethod
    def get_administracion(self, id_user):
        conexion = sqlite3.connect("palabrasLocas.db")
        cursor = conexion.cursor()
        cursor.execute("select administracion from usuario where id_usuario = ?",(id_user,))
        id_user = cursor.fetchone()
        conexion.commit()
        conexion.close()         
        return id_user[0]
        
    @classmethod
    def iniciarSesion (self, user, contra):
        if(SqliteMy.tablaVacia("id_usuario","usuario")):
            return -1
        else:
            if(self.existe_usuario(user) == False):
                return -2
            else:
                
                if(self.existe_usuario_contrasena(user, contra)[0] == False):
                    return -3
                else:
                    return self.existe_usuario_contrasena(user, contra)[1]

    @classmethod
    def existe_usuario(self, usuario):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select count(usuario) from usuario where usuario = '" + usuario + "';"
        cursor.execute(query)
        cant = cursor.fetchone()
        conn.commit()
        conn.close()
        if (cant[0] == 0):
            return False
        else:
            return True 

    @classmethod
    def existe_usuario_contrasena(self, usuario, contrasena):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select count(usuario), id_usuario from usuario where usuario = '" + usuario + "' and contrasena = '" + contrasena + "';"
        cursor.execute(query)
        cant = cursor.fetchone()
        conn.commit()
        conn.close()
        if (cant[0] == 0):
            return (False, -1)
        else:
            return (True, cant[1])

    @classmethod
    def cargar_usuario(self, username, password):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        bd = SqliteMy()
        id_user = bd.id_tabla("id_usuario", "usuario")
        cursor.execute("insert into usuario values(?,?,?,?)", (id_user, username, password,0))
        conn.commit()
        conn.close()

    @classmethod
    def crear_tabla_usuario(self):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        
        cursor.execute("""create table if not exists usuario(
            id_usuario integer primary key,
            usuario text,
            contrasena text,
            administracion integer
        );""")
        conn.commit()
        conn.close()

    @classmethod
    def get_id_usuario(self, usuario):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select id_usuario from usuario where usuario = '" + usuario  + "';"
        cursor.execute(query)
        id_user = cursor.fetchone()
        conn.commit()
        conn.close()
        return id_user[0]

    @classmethod
    def get_usuario_id(self, id_user):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select usuario from usuario where id_usuario = " + str(id_user)  + ";"
        cursor.execute(query)
        id_user = cursor.fetchone()
        conn.commit()
        conn.close()
        return id_user[0]