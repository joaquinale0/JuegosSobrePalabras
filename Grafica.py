import tkinter as tk
from tkinter import ttk, messagebox
# from tkinter import *
from Usuario import Usuario
from Palabra import Palabra
# import threading
from PalabrasLocasClass import PalabrasLocasClass


class App(ttk.Frame): 
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent    # guardamos una referencia de la ventana ppal
        parent.title("Juegos de Palabras")
        parent.geometry("410x250+800+200")
        self.parent.iconbitmap("img/logo.ico")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(True, True)

        # VARIBLES
        self.usuario = tk.StringVar()
        self.contrasena = tk.StringVar()
        self.id_user = 0

        #-------------- BOTONES -------------#
        ttk.Label(self, text = "Usuario", padding = 3, font="Arial 8 bold").grid(row=1, column=1)
        ttk.Entry(self, textvariable = self.usuario , width = 35).grid(row=1, column=2) #
        ttk.Label(self, text = "Contraseña", padding = 3, font="Arial 8 bold").grid(row=2, column=1)
        ttk.Entry(self, textvariable = self.contrasena , width = 35, show="*").grid(row=2, column=2) 

        ttk.Button(self, text="Registrarse" , padding = 3, command = self.registrar).grid(row=4, column=2, pady=40)
        ttk.Button(self, text="Iniciar Sesion", padding = 3,  command = self.IniciarSesion).grid(row=4, column=1, pady=40)
        ttk.Button(self, text="Salir", padding = 3 ,  command = self.boton_volver).grid(row=4, column=3, pady=40)

    def IniciarSesion(self):
        self.id_user = Usuario.iniciarSesion(self.usuario.get(),self.contrasena.get())
        if(self.id_user == -1):
            messagebox.showinfo("Inicio Sesion", "No hay usuario en tabla")
        elif(self.id_user == -2):
            messagebox.showinfo("Inicio Sesion", "No existe el usuario")
        elif(self.id_user == -3):
            messagebox.showinfo("Inicio Sesion", "Contraseña erronea")
        else:
            if(Usuario.get_administracion(self.id_user) == 1):
                self.menu_admin()
            else:
                self.id_user = Usuario.get_id_usuario(self.usuario.get())
                self.menu_juegos()
    
    def menu_juegos(self):
        self.parent.destroy()
        semilla = tk.Tk()
        MenuJuegos(semilla, self.id_user).grid()
        root.mainloop()
    
    def menu_admin(self):
        self.parent.destroy()
        semilla = tk.Tk()
        MenuAdmin(semilla, self.id_user).grid() 
        root.mainloop()
    
    def boton_volver(self):
        self.parent.destroy() 

    def registrar(self):
        if(Usuario.existe_usuario(self.usuario.get()) == False):
            Usuario.cargar_usuario(self.usuario.get(),self.contrasena.get())
            PalabrasLocasClass.cargar_cuenta_palabraLocas(Usuario.get_id_usuario(self.usuario.get()),0)
            messagebox.showinfo("Registrarse","Se registro correctamente")
        else:
            messagebox.showinfo("Registrarse","No se pudó registrar el usuario ya existe")

#################### MENU DE JUEGOS #######################

class MenuJuegos(ttk.Frame):
    def __init__(self, parent, id_user):
        super().__init__(parent, padding=(20))
        self.id_user = id_user
        self.parent = parent
        parent.title("Juegos de Palabras")
        parent.geometry("410x250+800+200")
        self.parent.iconbitmap("img/logo.ico")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        # VARIBLES
        self.usuarioIn = tk.StringVar
        self.contrasenaIn = tk.StringVar

        ttk.Button(self, text="Palabras Locas", command=self.ingresar_palabras_locas, padding=10, width=20).grid(row=1, column=1 , columnspan=2)
        

        ttk.Button(self, text="Cerrar Sesion", padding=10, command=self.cerrar_sesion).grid(row=10, column=1 , padx=40 , pady=120)
        ttk.Button(self, text="Salir", padding=10, command=self.salir).grid(row=10, column=2 , padx=40 , pady=120)

    def cerrar_sesion(self):
        self.parent.destroy()
        semilla = tk.Tk()
        App(semilla).grid() 
        root.mainloop()

    def salir(self):
        self.parent.destroy()

    def ingresar_palabras_locas(self):
        semilla = tk.Tk()
        PalabrasLocas(semilla, self.id_user).grid() 
        root.mainloop()

################### PALABRAS LOCAS ###################

class PalabrasLocas(ttk.Frame):
    def __init__(self, parent, id_user):
        super().__init__(parent, padding=(20))
        # VARIBLES
        self.id_user = id_user
        self.parent = parent
        parent.title("Palabras Locas")
        parent.geometry("410x250+800+200")
        self.parent.iconbitmap("img/logo.ico")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        
        # VARIBLES TABLERO
        self.vida = tk.IntVar(self, value=0)
        self.puntaje_maximo = tk.IntVar(self)
        self.puntaje_actual = tk.IntVar(self, value=0)
        
        # VARIBLES JUEGO  
        self.nom_boton = tk.StringVar(self)
        self.palabra_random = tk.StringVar(self)
        self.palabra_usuario = tk.StringVar(self)
        self.palabra = ""
        
        self.puntaje_maximo.set(PalabrasLocasClass.get_puntajeMax(self.id_user))
        self.palabra_random.set("Presione en comenzar")
        self.nom_boton.set("Comenzar")

        # TABLERO
        ttk.Label(self, text="VIDA", font="Arial 8 bold" ).grid(row=1, column=1) 
        ttk.Label(self, text="PUNTAJE MAXIMO", font="Arial 8 bold" ).grid(row=1, column=2) 
        ttk.Label(self, text="PUNTAJE ACTUAL", font="Arial 8 bold" ).grid(row=1, column=3) 


        ttk.Label(self, textvariable=self.vida , font="Arial 8 bold" ).grid(row=2, column=1) 
        ttk.Label(self, textvariable=self.puntaje_maximo , font="Arial 8 bold" ).grid(row=2, column=2) 
        ttk.Label(self, textvariable = self.puntaje_actual , font="Arial 8 bold").grid(row=2, column=3) 

        ttk.Label(self, textvariable=self.palabra_random , font="Arial 12 bold" ).grid(row=3, column=2, pady=5) 
        ttk.Entry(self, textvariable=self.palabra_usuario ).grid(row=4, column=2, pady=5)
        ttk.Button(self, text="Enviar", padding=10 , command = self.enviar ).grid(row=5, column=2, pady=5 )

        ttk.Button(self, text="Menu Juegos", padding=10, command = self.menu_juegos_PalabrasLocas).grid(row=6, column=1 , pady=13 )
        ttk.Button(self, text="Ranking", padding=10, command = self.ranking).grid(row=6, column=2 , pady=13 )
        ttk.Button(self, textvariable=self.nom_boton , padding=10, command=self.comenzar).grid(row=6, column=3 , pady=13 )

    def ranking(self):
        listaPuntaje = PalabrasLocasClass.ranking_puntaje()
        semilla = tk.Tk()
        semilla.grid() 
        # semilla.geometry("250x250+800+200")
        semilla.title("Palabras Locas")
        semilla.iconbitmap("img/logo.ico")

        ttk.Label(semilla, text="Nombre", font="arial 14 bold").grid(row=1,column=1, padx=20, pady=10)
        ttk.Label(semilla, text="Puntaje", font="arial 14 bold").grid(row=1,column=2, padx=20, pady=10)

        ttk.Label(semilla, text=Usuario.get_usuario_id(listaPuntaje[0][1]) , font="arial 10 bold").grid(row=2,column=1, padx=20)
        ttk.Label(semilla, text=str(listaPuntaje[0][0]), font="arial 12 bold").grid(row=2,column=2, padx=20)

        ttk.Label(semilla, text=Usuario.get_usuario_id(listaPuntaje[1][1]), font="arial 10 bold").grid(row=3,column=1, padx=20)
        ttk.Label(semilla, text=str(listaPuntaje[1][0]), font="arial 12 bold").grid(row=3,column=2, padx=20)

        ttk.Label(semilla, text=Usuario.get_usuario_id(listaPuntaje[2][1]), font="arial 10 bold").grid(row=4,column=1, padx=20)
        ttk.Label(semilla, text=str(listaPuntaje[2][0]), font="arial 12 bold").grid(row=4,column=2, padx=20)

        ttk.Label(semilla, text=Usuario.get_usuario_id(listaPuntaje[3][1]), font="arial 10 bold").grid(row=5,column=1, padx=20)
        ttk.Label(semilla, text=str(listaPuntaje[3][0]), font="arial 12 bold").grid(row=5,column=2, padx=20)

        ttk.Label(semilla, text=Usuario.get_usuario_id(listaPuntaje[4][1]), font="arial 10 bold").grid(row=6,column=1, padx=20)
        ttk.Label(semilla, text=str(listaPuntaje[4][0]), font="arial 12 bold").grid(row=6,column=2, padx=20)

        root.mainloop()

    def menu_juegos_PalabrasLocas(self):
        self.parent.destroy() 

    def titulo(self):
        self.palabra_random.set(self.palabra_usuario.get()) 

    def comenzar(self):
        if(self.vida.get() == 0):
            self.cambiar_palabra()
            self.vida.set(3)
            self.puntaje_actual.set(0)
            self.nom_boton.set("Saltear")
        else:
            if(self.vida.get() > 1):
                self.cambiar_palabra()
                self.vida.set(self.vida.get() - 1)

    def enviar(self):
        self.palabra_usuario.set(self.palabra_usuario.get().upper())
        if(self.palabra != ""):
            if(self.palabra == self.palabra_usuario.get()):
                self.puntaje_actual.set(self.puntaje_actual.get()+1)
                self.cambiar_palabra()
            else:
                self.vida.set(self.vida.get()-1)
                if(self.vida.get() == 0 ):
                    self.guardar_datos()
                    self.parent.destroy()
                    messagebox.showinfo("Palabras Locas", "Fin del juego")
        else:
            messagebox.showinfo("Palabras Locas", "Presione el botón comenzar")

    def guardar_datos(self):
        if(self.puntaje_actual.get() > self.puntaje_maximo.get() ):
            PalabrasLocasClass.modif_puntajeMax(self.puntaje_actual.get(), self.id_user)

    def cambiar_palabra(self):
        self.palabra = Palabra.obtener_palabra()
        palabras = Palabra(self.palabra)
        if(self.palabra == False):
            messagebox.showinfo("Palabras Locas","No hay elementos de Palabra")
        else:
            self.palabra_random.set(palabras.palabra_mezclada())

################ ADMINISTRADOR ###################

class MenuAdmin(ttk.Frame):
    def __init__(self, parent, id_user):
        super().__init__(parent, padding=(20))
        self.id_user = id_user
        self.parent = parent
        parent.title("Juegos de Palabras Admin")
        parent.geometry("410x250+800+200")
        self.parent.iconbitmap("img/logo.ico")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        # VARIBLES
        self.palabra = tk.StringVar()

        ttk.Label(self, text="Agregar una palabra", padding=10, font="Arial 8 bold").grid(row=1 , column=1)
        ttk.Entry(self, textvariable = self.palabra , width = 30).grid(row=1, column=2)

        ttk.Button(self, text="Guardar", padding=5, command=self.agregar_palabra , width=25).grid(row=2 , column=1,columnspan=2)
        ttk.Button(self, text="Cerrar Sesion", padding=10, command=self.cerrar_sesion).grid(row=10, column=1 , padx=40 , pady=60)
        ttk.Button(self, text="Salir", padding=10, command=self.salir).grid(row=10, column=2, padx=40 , pady=60)

    def cerrar_sesion(self):
        self.parent.destroy()
        semilla = tk.Tk()
        App(semilla).grid() 
        root.mainloop()

    def salir(self):
        self.parent.destroy()

    def agregar_palabra(self):
        palabra = self.palabra.get()
        palabra = palabra.upper()
        if(Palabra.existe_palabra(palabra) == False):
            Palabra.cargar_palabra(palabra)
            messagebox.showinfo("Agregar Palabra","Se agrego correctamente")
        else:
            messagebox.showinfo("Agregar Palabra","No se agrego palabra ya existe")


################### MAIN ##################

Usuario.crear_tabla_usuario() 
Palabra.crear_tabla_palabra()
PalabrasLocasClass.crear_tabla_palabraLocas()
root = tk.Tk()
App(root).grid() 
root.mainloop()