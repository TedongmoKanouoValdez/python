# les tuples

nbre=(15,"valdez",("jordan","jeannies","patric"))
print(nbre[0])

etudiant=("val", 20,("maths","anglais","physique"))

nom,age,filiere=etudiant

print(nom)

# les dictionnaires

Etudiant={"nom": "alex","age":20, "Modules": {"maths","anglais","physique"}}
Etudiant["age"]=21
Etudiant["email"] ="val@gmail.com"

print(Etudiant["email"])

#supprimer dans un dictionnaire
del Etudiant["Modules"]

print(Etudiant)

# les ensembles evitent les doublons
# set() pour definir les ensembles vides
etude = set()
#etude = {"valdez",20,20}
print(type(etude))