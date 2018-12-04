fichier = open("part-r-00000",'r')
lines = fichier.readlines()[1:]

mx = 0
emax = ''

# Parcours ligne par ligne
for line in lines:
    ln = line.split('\t')
    # Repère du max sur le deuxieme élément "casté" en entier
    if (mx < int(ln[1])):
        mx = int(ln[1])
        # Récuperation du mot assigné au Max à chaque mise à jour de max
        emax = ln[0]

# Affichage du mot avec le plus d'occurence
print(emax+": "+str(mx))