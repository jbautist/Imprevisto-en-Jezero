import time
import os


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def comprobar_entrada(l1, l2, lu):
    '''Comprobar que las entradas del usuario sean válidas. 
    Parámetros: l1=letra opción 1, l2=letra opción 2 y lu=letra del usuario.
    Retorna: True si la entrada es válida.
    '''
    return True if lu == l1 or lu == l2 else print('\nERROR: ha ingresado un carácter inválido.\n')
    

def comenzar_inicio():
    '''Comenzar historia desde el inicio'''
    while True:
        respuesta = input('¿Quiere comenzar de nuevo? [S/N] ').upper()
        clearConsole()
        if comprobar_entrada('S', 'N', respuesta) == True:
            inicio() if respuesta == 'S' else exit()


# Escenarios
def inicio():
    clearConsole()
    print('Te despiertas con una luz intermitente iluminando tu rostro y sintiendo olor a aceite por todas partes...\n')
    time.sleep(7)
    print('''Automáticamente de das cuenta que perdiste la conciencia luego de que la nave Starship se estrellara llegando a Cráter Jezero en Marte.
Al parecer la primera misión con humanos en Marte no tuvo una buena bienvenida, alguien los estaba esperando...\n''')
    time.sleep(19)
    print('''Te desabrochas el cinturón y te levantas para verificar si queda alguien vivo además de ti, pero desafortunadamente, todos los demás 
en el habitáculo perdieron la vida...\n''')
    time.sleep(13)
    print('''Intentas comunicarte con el equipo en Tierra, pero todos los instrumentos de la cabina de mando se encuentran destruidos. 
Tu última esperanza para poder informar sobre lo sucedido es en la base modular de Elon Musk que se encuentra a 3 kilómetros de tu ubicación.\n''')
    time.sleep(20)
    print('Pero primero deberás salir vivo de la nave...\n')
    time.sleep(4)

    ENTER = input('Presione ENTER para continuar.')
    comienzo_decisiones()


def comienzo_decisiones():
    clearConsole()
    print('Te acercas hacia la compuerta del habitáculo para salir y automáticamente escuchas pasos acercándose hacía ti...\n')
    time.sleep(8)
    print('''[A] Abres la compuerta para ver si es alguien de la tripulación que pudo sobrevivir.
[B] Esperas que pase para ver quién es.\n''')
    while True:
        respuesta = input().upper()
        if comprobar_entrada('A', 'B', respuesta) == True:
            escenario_A() if respuesta == 'A' else escenario_B()


def escenario_A():
    clearConsole()
    print('''Al abrir la compuerta te das cuenta que los pasos eran de un Marciano inteligente de 4 pasas con una gran armadura y una espada 
de gran tamaño.\n''')
    time.sleep(12)
    print('''[A] Peleas contra él.
[B] Intentas hacerle entender de que no quieres hacerle daño.\n''')
    while True:
        respuesta = input().upper()
        if comprobar_entrada('A', 'B', respuesta) == True:
            escenario_C() if respuesta == 'A' else escenario_D()


def escenario_B():
    clearConsole()
    print('''Cuando los ruidos se acercan a la compuerta observas que los pasos son de un Marciano inteligente de 4 pasas 
con una gran armadura y una espada de gran tamaño.\n''')
    time.sleep(13)
    print('''[A] Esperas a que se vaya.
[B] Abres la compuerta e intentas hacerle entender de que no quieres hacerle daño.\n''')
    while True:
        respuesta = input().upper()
        if comprobar_entrada('A', 'B', respuesta) == True:
            escenario_E() if respuesta == 'A' else escenario_D()


def escenario_C():
    clearConsole()
    print('Como no tienes armamento para poder hacerle mucho daño te termina matando y esto se convierte en el FIN.\n')
    time.sleep(8)
    comenzar_inicio()


def escenario_D():
    clearConsole()
    print('''Al Marciano no le interesa lo que le quieres decir. El solo vino a asegurarse de que todos dentro de la nave estén muertos. 
Así que te ataca y mueres en ese mismo instante convirtiéndose en tu FIN.\n''')
    time.sleep(17)
    comenzar_inicio()


def escenario_E():
    clearConsole()
    print('''Cuanto se va el Marciano abres la compuerta y te diriges rápidamente hacia el compartimiento de carga, allí encuentras 
una llave francesa de 30 pulgadas y la tomas como arma.\n''')
    time.sleep(13)
    print('Sales del compartimiento y te encuentras con el marciano de espaldas.\n')
    time.sleep(4)
    print('''[A] Lo golpeas con la llave en la cabeza.
[B] Esperas a que se vaya para no entrar en conflicto.\n''')
    while True:
        respuesta = input().upper()
        if comprobar_entrada('A', 'B', respuesta) == True:
            escenario_G() if respuesta == 'A' else escenario_F()


def escenario_F():
    clearConsole()
    print('Observas que se aleja y entonces aprovechas para dirigirte hacia la compuerta de salida…\n')
    time.sleep(6)
    print('''Pero te tropiezas con un cilindro que estaba en el suelo y el Marciano te ve en ese preciso instante. Entonces se acerca hacia ti 
y comienzan a pelear…\n''')
    time.sleep(12)
    print('''Después de unos segundos combatiendo con el extraterrestre tu cuerpo ya está muy lastimado como para seguir, entonces la llave 
cae de tu mano por ser muy pesada y por tener diversos cortes en el brazo. El Marciano no lo duda ni un segundo y clava su espada tu pecho 
matándote en el instante y convirtiéndose en tu FIN.\n''')
    time.sleep(27)
    comenzar_inicio()


def escenario_G():
    clearConsole()
    print('''El Marciano Muere al instante y te diriges hacia la salida.
Te alejaste de la nave antes de que lleguen más extraterrestres y tomas rumbo hacia la base de Elon Musk para comunicarte con la Tierra 
y contar sobre lo sucedido.
FIN.\n''')
    time.sleep(19)
    comenzar_inicio()
    

print('''
                      +-------------------------------------------------------+
                      |                 IMPREVISTO EN JEZERO                  |
                      +-------------------------------------------------------+

Este es un juego de aventura basado en texto. La historia se irá desarrollando acorde a las decisiones que vaya tomando.
''')
ENTER = input('Presione ENTER para comenzar.')
inicio()