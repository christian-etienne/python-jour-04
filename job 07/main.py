def multiples_de_trois(L):
    compteur = 0
    for nombre in L:
        if nombre % 3 == 0:
            compteur += 1
    return compteur

L = [8, 24,48,2,16]
resultat = multiples_de_trois (L)

print(f"Le nombre de multiples de 3 dans la liste est : {resultat}")
