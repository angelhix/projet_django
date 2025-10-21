from django.db import models

class Candidat(models.Model):
    NOM_CONCOURS_CHOIX = [
        ('TWIN', 'Technologie du Web et Image Numerique'),
        ('Srit', 'Sytemes et Reseaux Informatiques et Telecom'),
        ('Mp2i', 'Classe préparatoire: Mathématiques Physique et Informatique'),
        ('Entd', 'Economie Numérique et Transformation Digitale'),
        ('Dasi', 'Data Science et Intelligence Artificielle'),
    ]

    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    niveau_etude = models.CharField(max_length=100)
    etablissement_origine = models.CharField(max_length=255)
    concours_souhaite = models.CharField(max_length=4, choices=NOM_CONCOURS_CHOIX)

    extrait_naissance = models.FileField(upload_to='documents/')
    certificat_nationalite = models.FileField(upload_to='documents/')
    lettre_motivation = models.FileField(upload_to='documents/')
    diplome = models.FileField(upload_to='documents/')
    photo = models.ImageField(upload_to='photos/')

    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenoms}"
