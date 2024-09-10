import tkinter as tk
from random import randint

# Función para generar el número secreto
def generar_numero_secreto():
    numero_secreto = []
    while len(numero_secreto) < 4:
        digito = str(randint(0, 9))
        if digito not in numero_secreto:
            numero_secreto.append(digito)
    return ''.join(numero_secreto)

# Función para calcular los toques y famas
def calcular_toques_y_famas(intento, secreto):
    toques = 0
    famas = 0
    for i in range(4):
        if intento[i] == secreto[i]:
            famas += 1
        elif intento[i] in secreto:
            toques += 1
    return toques, famas

# Función que maneja la verificación del número ingresado por el jugador
def comprobar_numero():
    intento = entrada.get()

    # Validar que el jugador ingrese un número válido de 4 dígitos y sin repetir
    if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
        resultado.set("Por favor, ingresa un número válido de 4 dígitos no repetidos.")
        return

    # Comparar intento con el número secreto
    toques, famas = calcular_toques_y_famas(intento, numero_secreto)
    intentos.append(1)  # Incrementar el número de intentos

    # Mostrar el resultado del intento
    if famas == 4:
        resultado.set(f"¡Ganaste en {len(intentos)} intentos! El número secreto era {numero_secreto}.")
    elif len(intentos) == max_intentos:
        resultado.set(f"¡Perdiste! El número secreto era {numero_secreto}.")
    else:
        resultado.set(f"{toques} Toques – {famas} Famas. Intentos restantes: {max_intentos - len(intentos)}")

# Función para reiniciar el juego
def reiniciar_juego():
    global numero_secreto, intentos
    numero_secreto = generar_numero_secreto()
    intentos = []
    print(f"El número secreto es: {numero_secreto}")  # Mostrar el número en la consola para pruebas
    resultado.set("Nuevo juego, intenta adivinar el número secreto.")

# Configuración de la ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Juego de Toques y Famas")
ventana.geometry("500x350")
ventana.configure(bg="#FADADD")

# Variables globales
numero_secreto = generar_numero_secreto()
print(f"El número secreto es: {numero_secreto}")  # Mostrar el número en la consola al iniciar el juego
intentos = []
max_intentos = 6  # Límite de intentos
resultado = tk.StringVar()

# Elementos de la interfaz gráfica
etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenido al juego de Toques y Famas!", font=("Helvetica", 18, "bold"), fg="#FF1493", bg="#FADADD")
etiqueta_bienvenida.pack(pady=15)

etiqueta_instrucciones = tk.Label(ventana, text="Intenta adivinar el número secreto", font=("Helvetica", 12), fg="#333333", bg="#FADADD")
etiqueta_instrucciones.pack()

etiqueta_ingresa = tk.Label(ventana, text="Ingresa un número de cuatro dígitos:", font=("Helvetica", 12), fg="#333333", bg="#FADADD")
etiqueta_ingresa.pack(pady=5)

entrada = tk.Entry(ventana, font=("Helvetica", 14), width=10)
entrada.pack(pady=5)

boton_comprobar = tk.Button(ventana, text="Comprobar", command=comprobar_numero, font=("Helvetica", 12), bg="#FF69B4", fg="white", relief="flat", padx=5, pady=5, activebackground="#FF1493", activeforeground="white")
boton_comprobar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="#333333", bg="#FADADD")
etiqueta_resultado.pack(pady=15)

boton_reiniciar = tk.Button(ventana, text="Reiniciar juego", command=reiniciar_juego, font=("Helvetica", 12), bg="#FF69B4", fg="white", relief="flat", padx=5, pady=5, activebackground="#FF1493", activeforeground="white")
boton_reiniciar.pack(pady=5)

# Ejecutar la ventana principal
ventana.mainloop()
