from utils.gestioTasques import *

"""
El fet de importar el fitxer "utils.gestioTasques.py"
com que en el fitxer apareix
# Llista per emmagatzemar les tasques
llistaDeTasques = list()

# Inicialització de variables
llistaDeTasques = []  
És com si en aquest programa es definís la variable
llistaDeTasques, per això la podem fer servir.

D'igual manrea, podem fer servir tote les funcions
que estàn definides al fitxer "utils.gestioTasques.py"
"""

# Programa principal
if __name__ == '__main__':
    # Declaració de variables
    titolNovaTasca = str()
    descripcioNovaTasca = str()
    quantitatDeNovesTasques = int()
    marcarComCompletada = str()
    pos = int()

    # Inicialització de variables
    marcarComCompletada = False

    # Demanem la quantitat de tasques que vol entrar
    print(f"Entra la quantitat de tasques que vols entrar per començar: ", end="")
    quantitatDeNovesTasques = int(input())

    # Demanem les dades de dues tasques
    pos = 0
    while (pos < quantitatDeNovesTasques):
        print(f"Entra el títol de la tasca {pos + 1} de {quantitatDeNovesTasques}: ", end="")
        titolNovaTasca = input()
        print(f"Entra la descripció de la tasca {titolNovaTasca}: ", end="")
        descripcioNovaTasca = input()

        # Afegim la nova tasca a la llista de tasques "llistaDeTasques"
        afegirTasca(titolNovaTasca, descripcioNovaTasca)

        pos += 1

    # Mostrem la llista de tasques
    print("\nLlista de tasques")
    mostrarTasques()

    # Marquem la primera tasca com a completada
    print(f"Vols marcar la tasca {titolNovaTasca} com a completada (s/n): ", end="")
    marcarComCompletada = input().lower()[0]
    if (marcarComCompletada == "s"):
        marcarComACompletada(0)
        print(f"S'ha marcat la tasca {titolNovaTasca} com a completada!")
    else:
        print(f"No s'ha marcat la tasca {titolNovaTasca} com a completada!")

    print("\nDesprés de marcar, o no, la primera tasca com a completada")
    mostrarTasques()
