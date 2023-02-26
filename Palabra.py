import random
import sqlite3
from SqliteMy import SqliteMy

class Palabra:
    def __init__(self, palabra):
        self.palabra = palabra
    
    def get_palabra(self):
        return self.palabra
    
    def palabra_mezclada(self):
        palabra = []
        posicion = []
        palabra_retornar = ""
        tam = len(self.palabra)
        for i in range(0, tam):
            posicion.append(i)
        tam -=1
        while(tam > 0):
            i = random.randint(0, tam)
            palabra.append(self.palabra[posicion.pop(i)])
            tam -= 1    
        palabra.append(self.palabra[posicion.pop(0)])
        for i in range(0, len(palabra)):
            palabra_retornar = palabra_retornar + palabra[i]
        return palabra_retornar
    
    @classmethod
    def obtener_palabra(self):
        if(SqliteMy.tablaVacia("id_palabra", "palabra") == False):
            lista = self.lista_palabra()
            pos = random.randint(0,len(lista) - 1)
            return lista[pos][0]
        else:
            return False

    @classmethod
    def lista_palabra(self):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select palabra from palabra;"
        cursor.execute(query)
        lista = cursor.fetchall()
        conn.commit()
        conn.close()
        return lista

    @classmethod
    def cant_lista_palabra(self):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select count(palabra) from palabra;"
        cursor.execute(query)
        cant = cursor.fetchone()
        conn.commit()
        conn.close()
        return cant[0]

    @classmethod
    def existe_palabra(self, palabra):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select count(id_palabra) from palabra where palabra = '" + palabra + "';"
        cursor.execute(query)
        cant = cursor.fetchone()
        conn.commit()
        conn.close()
        if (cant[0] == 0):
            return False
        else:
            return True 

    @classmethod
    def cargar_palabra(self, palabra):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        bd = SqliteMy()
        id_pal = bd.id_tabla("id_palabra", "palabra")
        cursor.execute("insert into palabra values(?,?)", (id_pal, palabra))
        conn.commit()
        conn.close()

    @classmethod
    def crear_tabla_palabra(self):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        cursor.execute("""
            create table if not exists palabra(
            id_palabra integer primary key,
            palabra text
        );""")
        conn.commit()
        conn.close()