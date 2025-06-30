from django.contrib.auth.models import AbstractUser
from django.db import models

class Pianta(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField(blank=True)
    data_aggiunta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Utente(models.Model):
    nome = models.CharField(max_length=100)
    email= models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)