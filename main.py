class Personne:
    def __init__(self, nom, age: int):
        self.nom = nom
        self.age = age
        print("Constructeur personne " + nom)

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18


personne1 = Personne("Jean", 30)
personne2 = Personne("Paul", 15)

personne1.SePresenter()
personne2.SePresenter()
