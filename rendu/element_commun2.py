import time
import heapq

# Fonction pour trouver le premier élément commun entre deux listes en utilisant un tas.
def element_commun2(L1, L2):
    """
    Renvoie le premier élément commun des deux listes en utilisant une structure de tas.
    Les listes doivent être transformées en tas avant l'appel.
    """
    while L1 and L2:
        min_L1 = L1[0]  # Le plus petit élément de L1 (tas)
        min_L2 = L2[0]  # Le plus petit élément de L2 (tas)
        if min_L1 == min_L2:
            return min_L1  # Renvoie le premier élément commun
        elif min_L1 < min_L2:
            heapq.heappop(L1)  # Supprime le plus petit élément de L1
        else:
            heapq.heappop(L2)  # Supprime le plus petit élément de L2
    return float('nan')  # Renvoie NaN si aucune correspondance n'est trouvée

# Mesure du temps pour `element_commun2`
def chronometre_element_commun2(L1, L2):
    """
    Chronomètre la durée d'exécution de la fonction `element_commun2` en utilisant des tas.
    """
    heapq.heapify(L1)  # Transforme L1 en tas
    heapq.heapify(L2)  # Transforme L2 en tas
    start_time = time.time()
    element_commun2(L1, L2)
    end_time = time.time()
    return end_time - start_time