from django.db import models
from django.utils import timezone

#Post è il nome del nostro modello. Possiamo dargli un nome diverso (ma dobbiamo evitare caratteri speciali e spazi). Inizia sempre il nome di una classe con un lettera maiuscola.
#models.Model significa che il Post è un modello Django, quindi Django sa che dovrebbe essere salvato nel database.
class Post(models.Model):
    #models.ForeignKey - questo è un link a un altro modello.
    author = models.ForeignKey('auth.User')
    #models.CharField - così si definisce un testo con un numero limitato di lettere
    title = models.CharField(max_length=200)
    #models.TextField - questo è il codice per definire un testo senza un limite.
    #Sembra l'ideale per i contenuti di un post, vero?
    text = models.TextField()
    #models.DateTimeField - questo per la data ed l'ora.
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
