class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        print("Constructeur personne " + nom)

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom + " et j'ai " + str(self.age) + " ans")


personne1 = Personne("Jean", 25)
personne2 = Personne("Paul", 40)

personne1.SePresenter()
personne2.SePresenter()
