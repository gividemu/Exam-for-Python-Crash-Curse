class Studente:

    def __init__(self, nome, cognome, eta, matricola, voti=None):
        self.nome = nome.title()
        self.cognome = cognome.title()
        self.eta = eta
        self.matricola = matricola
        self.voti = voti if voti is not None else []

    def __str__(self):
        media = self.calcola_media()
        media_str = str(round(media, 2)) if media else "nessun voto"
        return ("Studente: " + self.nome + " " + self.cognome +
                " | Eta': " + str(self.eta) +
                " | Matricola: " + str(self.matricola) +
                " | Voti: " + str(self.voti) +
                " | Media: " + media_str)

    def presentati(self):
        sep = "=" * 55
        print(sep)
        print("PROFILO STUDENTE: " + self.nome.upper() + " " + self.cognome.upper())
        print("Eta': " + str(self.eta) + " | Matricola: " + str(self.matricola))
        print("Voti: " + (str(self.voti) if self.voti else "Libretto vuoto"))
        print(sep)

    def aggiungi_voto(self, voto):
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print("Voto " + str(voto) + " registrato per " + self.nome + " " + self.cognome + ".")
        else:
            print("Errore: " + str(voto) + " non e' un voto valido (deve essere tra 18 e 30).")

    def calcola_media(self):
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        print("Ore di studio di " + self.nome + ": " + str(ore))
        if ore > 10:
            print("Eccellente! Sei prontissimo.")
        elif ore > 5:
            print("Buono, ma continua cosi'.")
        elif ore > 0:
            print("Attenzione: studio insufficiente.")
        else:
            print(self.nome + " non ha studiato oggi.")
        print("")


# ============================================================
# Programma principale
# ============================================================

if __name__ == "__main__":

    s1 = Studente("marco", "rossi", 20, "MAT001")
    s2 = Studente("giulia", "bianchi", 22, "MAT002")

    s1.aggiungi_voto(28)
    s1.aggiungi_voto(30)
    s1.aggiungi_voto(25)

    s2.aggiungi_voto(30)
    s2.aggiungi_voto(29)
    s2.aggiungi_voto(30)

    for s in [s1, s2]:
        s.presentati()
        print("Media: " + str(round(s.calcola_media(), 2)))
        s.studia(6)
        print(s)
        print("")

    sep = "=" * 55
    print(sep)
    print("CONFRONTO FINALE")
    print(sep)

    studenti = [s1, s2]
    migliore = max(studenti, key=lambda s: s.calcola_media())
    print("Studente con la media piu' alta: " + migliore.nome + " " + migliore.cognome)
    print(sep)
