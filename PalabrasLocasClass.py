import time
import sqlite3
from SqliteMy import SqliteMy

class PalabrasLocasClass:
    def __init__(self, id_juego, id_usuario, puntaje_max):
        self.id_juego = id_juego
        self.id_usuario = id_usuario
        self.puntaje_max = puntaje_max

    @classmethod
    def tiempo(self, numero):
        # for i in range(numero):
        time.sleep(1)
        numero -= 1
        return numero



    @classmethod
    def ranking_puntaje(self):
        lista_puntaje = []
        lista_completa = self.lista_puntajeMax()
        lista_completa.sort()
        for i in range(5):
            lista_puntaje.insert(i,lista_completa.pop())
        return lista_puntaje



    @classmethod
    def cargar_cuenta_palabraLocas(self, id_jugador, puntajemax):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        bd = SqliteMy()
        id_palabraLoca = bd.id_tabla("id_juego", "palabraLocas")
        cursor.execute("insert into palabraLocas values(?,?,?)", (id_palabraLoca, id_jugador, puntajemax))
        conn.commit()
        conn.close()

    @classmethod
    def crear_tabla_palabraLocas(self):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        cursor.execute("""
            create table if not exists palabraLocas(
            id_juego integer primary key,
            id_jugador integer,
            puntajeMax integer,
            foreign key (id_jugador) references usuario(id_usuario)
        );""")
        conn.commit()
        conn.close()

    @classmethod
    def get_puntajeMax(self, id_jugador):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select puntajeMax from palabraLocas where id_jugador = " + str(id_jugador) + ";"
        cursor.execute(query)
        puntMax = cursor.fetchone()
        conn.commit()
        conn.close()
        return puntMax[0]

    @classmethod
    def modif_puntajeMax(self, puntMax, id_jugador):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "update palabraLocas set puntajeMax = " + str(puntMax) + " where id_jugador = " + str(id_jugador) + ";"
        cursor.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def lista_puntajeMax(self):
        conn = sqlite3.connect("palabrasLocas.db")
        cursor = conn.cursor()
        query = "select puntajeMax, id_jugador from palabraLocas ;"
        cursor.execute(query)
        puntMax = cursor.fetchall()
        conn.commit()
        conn.close()
        return puntMax