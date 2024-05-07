class EtreVivant:
    ESPECE_ETRE_VIVANT = ""

    def afficher_infos_etre_vivant(self):
        print("Infos être vivant :" + self.ESPECE_ETRE_VIVANT)


class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain"

    def __init__(self, nom: str = "", age: int = 0):
        if nom == "":
            self.nom = self.demanderNom()
        else:
            self.nom = nom
        self.age = age

        print("Constructeur personne " + self.nom)

    def sePresenter(self):
        infos_personne = "Bonjour, je m'appelle " + self.nom
        if self.age > 0:
            infos_personne += ", j'ai " + str(self.age) + " ans"
        print(infos_personne)
        if self.age > 0:
            if self.estMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def estMajeur(self):
        return self.age >= 18

    def demanderNom(self):
        nom = input("Quel est votre nom ? ")
        return nom


liste_personnes = [
                 Personne("Jean", 30),
                 Personne("Paul", 15),
                 Personne("Zoe",45)]

for personne in liste_personnes:
    personne.sePresenter()
    personne.afficher_infos_etre_vivant()
    print()
