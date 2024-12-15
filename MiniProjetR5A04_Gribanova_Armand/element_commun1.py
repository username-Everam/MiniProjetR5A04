import time

# Fonction pour trouver le premier élément commun entre deux listes en utilisant un tri manuel.
def element_commun1(L1, L2):
    """
    Renvoie le premier élément commun des deux listes triées en les parcourant.
    Les listes ne sont pas modifiées mais leur structure initiale est utilisée.
    """
    while L1 and L2:
        min_L1 = min(L1)  # Trouve le plus petit élément de L1
        min_L2 = min(L2)  # Trouve le plus petit élément de L2
        if min_L1 == min_L2:
            return min_L1  # Renvoie le premier élément commun
        elif min_L1 < min_L2:
            L1.remove(min_L1)  # Supprime le plus petit élément de L1
        else:
            L2.remove(min_L2)  # Supprime le plus petit élément de L2
    return float('nan')  # Renvoie NaN si aucune correspondance n'est trouvée

# Mesure du temps pour `element_commun1`
def chronometre_element_commun1(L1, L2):
    """
    Chronomètre la durée d'exécution de la fonction `element_commun1`.
    """
    start_time = time.time()
    element_commun1(L1, L2)
    end_time = time.time()
    return end_time - start_time