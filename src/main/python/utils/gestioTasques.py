"""
La idea és crear una llista de tasques "llistaDeTasques",
    on cada tasca que guardarem tindrà tres camps,
    "titol", "descripcio" i "completada"
* el camp "titol" de tipus cadena,
        a on guardarem el títol de la tasca.
* el camp "descripcio" de tipus cadena,
        a on guardarem la descripció de la tasca.
* el camp "completada" de tipus booleà,
        a on guardarem l'estat de la tasca
    si la tasca està completada
        tindrà un valor de "True", i
    si la tasca NO està completada
        tindrà un valor de "False".
Per defecte, qualsevol que afegim a la llistaDeTasques
    NO estarà completada, per tant, per defecte
    el camp "completada" tindrà un valor de "False"
"""

# Declaració de variables
# Llista per emmagatzemar les tasques
llistaDeTasques = list()

# Inicialització de variables
llistaDeTasques = []

"""
    Funció que afegirà una tasca a la llista,
    de la tasca, només ens cal, el títol (titolRebut),
    de tipus cadena, i la descripció (descripcioRebuda)
    de tipus cadena, ja que sempre que afegim una tasca,
    aquesta estarà sense completar, és a dir, completada a False
    Dades d'entrada
        el títol (titolRebut), i
        la descripció (descripcioRebuda)
    Dades de sortida
        No retorna res
"""
def afegirTasca(titolRebut, descripcioRebuda):
    tasca = {"titol": titolRebut,
             "descripcio": descripcioRebuda,
             "completada": False}
    llistaDeTasques.append(tasca)

"""
    Funció per mostrar les tasques que
    es troben guardades a la
    llista de tasques (llistaDeTasques)
    Dades d'entrada
        No rep res
    Dades de sortida
        No retorna res, mostra per consola
        la informació de totes les tasques
        que es troben guardades a la
        llista de tasques (llistaDeTasques)
"""
def mostrarTasques():
    pos = 0
    while(pos < len(llistaDeTasques)):
        tascaActual = llistaDeTasques[pos]
        if tascaActual["completada"]:
            estatDeLaTascaAvtual = "Completada"
        else:
            estatDeLaTascaAvtual = "Pendent"
        print(f"{pos + 1}."
              f"{tascaActual['titol']}"
              f" - "
              f"{estatDeLaTascaAvtual}")
        pos += 1

"""
    Funció per marcar una tasca com a completada
    Dades d'entrada
        posTascaAMarcar de tipus enter
        Indica la posició de la tasca
        a marcar com a completada.
    Dades de sortida
        No retorna res
"""
def marcarComACompletada(posTascaAMarcar):
    if (0 <= posTascaAMarcar and posTascaAMarcar < len(llistaDeTasques)):
        llistaDeTasques[posTascaAMarcar]["completada"] = True