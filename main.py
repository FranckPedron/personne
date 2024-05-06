class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        if nom == "":
            self.nom = self.DemanderNom()
        else:
            self.nom = nom
        self.age = age

        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        infos_personne = "Bonjour, je m'appelle " + self.nom
        if self.age > 0:
            infos_personne += ", j'ai " + str(self.age) + " ans"
        print(infos_personne)
        if self.age > 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        nom = input("Quel est votre nom ? ")
        return nom


personne1 = Personne("Jean", 0)
personne2 = Personne("Paul", 15)
personne3 = Personne("", 45)

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
