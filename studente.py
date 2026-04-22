# ============================================================
#  Esercitazione Finale – Classe Studente
# ============================================================

class Studente:
    """Rappresenta uno studente con informazioni personali e metodi di azione."""

    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []          # lista vuota: ogni istanza ha i propri voti

    # ----------------------------------------------------------
    def presentati(self):
        """Restituisce una breve presentazione dello studente."""
        return (
            f"Ciao! Sono {self.nome} {self.cognome}, "
            f"ho {self.eta} anni e la mia matricola è {self.matricola}."
        )

    # ----------------------------------------------------------
    def aggiungi_voto(self, voto):
        """Aggiunge un voto (intero o float) alla lista dei voti."""
        if 0 <= voto <= 30:
            self.voti.append(voto)
            print(f"  [+] Voto {voto} aggiunto per {self.nome} {self.cognome}.")
        else:
            print(f"  [!] Voto non valido ({voto}): deve essere compreso tra 0 e 30.")

    # ----------------------------------------------------------
    def calcola_media(self):
        """Restituisce la media dei voti oppure None se non ci sono voti."""
        if not self.voti:
            return None
        return sum(self.voti) / len(self.voti)

    # ----------------------------------------------------------
    def studia(self, ore):
        """Stampa un messaggio sull'attività di studio dello studente."""
        if ore <= 0:
            print(f"  {self.nome} non ha studiato oggi.")
        elif ore == 1:
            print(f"  {self.nome} ha studiato 1 ora. Bravo, è un inizio!")
        elif ore <= 4:
            print(f"  {self.nome} ha studiato {ore} ore. Buon lavoro!")
        else:
            print(f"  {self.nome} ha studiato ben {ore} ore. Impegno straordinario!")

    # ----------------------------------------------------------
    def __str__(self):
        """Rappresentazione leggibile dell'oggetto (usata da print)."""
        media = self.calcola_media()
        media_str = f"{media:.2f}" if media is not None else "nessun voto"
        return (
            f"Studente({self.nome} {self.cognome} | "
            f"età: {self.eta} | matricola: {self.matricola} | "
            f"voti: {self.voti} | media: {media_str})"
        )


# ============================================================
#  Creazione degli oggetti e dimostrazione dei metodi
# ============================================================

separatore = "=" * 55

# --- Studente 1 ---
print(separatore)
print("STUDENTE 1")
print(separatore)

s1 = Studente(nome="Marco", cognome="Rossi", eta=20, matricola="MAT001")
print(s1.presentati())

s1.aggiungi_voto(28)
s1.aggiungi_voto(30)
s1.aggiungi_voto(25)
s1.aggiungi_voto(31)          # voto non valido → messaggio di errore

s1.studia(6)

media1 = s1.calcola_media()
print(f"  Media dei voti di {s1.nome}: {media1:.2f}")
print(f"  {s1}")

# --- Studente 2 ---
print()
print(separatore)
print("STUDENTE 2")
print(separatore)

s2 = Studente(nome="Giulia", cognome="Bianchi", eta=22, matricola="MAT002")
print(s2.presentati())

s2.aggiungi_voto(30)
s2.aggiungi_voto(29)
s2.aggiungi_voto(30)

s2.studia(3)

media2 = s2.calcola_media()
print(f"  Media dei voti di {s2.nome}: {media2:.2f}")
print(f"  {s2}")

# --- Confronto finale ---
print()
print(separatore)
print("CONFRONTO FINALE")
print(separatore)

studenti = [s1, s2]
migliore = max(studenti, key=lambda s: s.calcola_media() or 0)

for s in studenti:
    m = s.calcola_media()
    print(f"  {s.nome} {s.cognome}: media = {m:.2f}")

print(f"\n  🏆 Lo studente con la media più alta è: {migliore.nome} {migliore.cognome}")
print(separatore)
