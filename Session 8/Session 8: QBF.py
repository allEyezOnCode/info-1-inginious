class Employe:
    def __init__(self, name, salaire):
        self.nom = name
        self.salaire = salaire
    def __str__(self):
        return f"{self.nom} : {self.salaire}"
    def augmente(self, add):
        self.salaire += add
