from django.db import models
from django.urls import reverse

# Create your models here.

class Regal(models.Model):
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    
    class Meta:
        verbose_name = ("Regal")
        verbose_name_plural = ("Regale")

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse("Regal_detail", kwargs={"pk": self.pk})


class Stellplatz(models.Model):
    nummer = models.IntegerField(("Nummer"))
    regal = models.ForeignKey(Regal, verbose_name=("Regal"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Stellplatz")
        verbose_name_plural = ("Stellplätze")

    def __str__(self):
        return f"{self.regal} ({self.nummer})"

    def get_absolute_url(self):
        return reverse("Stellplatz_detail", kwargs={"pk": self.pk})

class Kategorie(models.Model):
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    
    class Meta:
        verbose_name = ("Kategorie")
        verbose_name_plural = ("Kategorien")

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse("Kategorie_detail", kwargs={"pk": self.pk})
    

class Autor(models.Model):
    name = models.CharField(("Name"), max_length=50)
    
    class Meta:
        verbose_name = ("Autor")
        verbose_name_plural = ("Autoren")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Autor_detail", kwargs={"pk": self.pk})

class Buch(models.Model):
    autor = models.ForeignKey(Autor, verbose_name=("Autor"), on_delete=models.CASCADE)
    stellplatz = models.ForeignKey(Stellplatz, verbose_name=("Stellplatz"), on_delete=models.RESTRICT)
    kategorie = models.ManyToManyField(Kategorie, verbose_name=("Kategorie"))
    titel = models.TextField(("Titel"))

    class Meta:
        verbose_name = ("Buch")
        verbose_name_plural = ("Bücher")

    def __str__(self):
        return f"{self.titel} ({self.autor})"

    def get_absolute_url(self):
        return reverse("Buch_detail", kwargs={"pk": self.pk})

class Kunde(models.Model):
    name = models.CharField(("Name"), max_length=50)    

    class Meta:
        verbose_name = ("Kunde")
        verbose_name_plural = ("Kunden")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kunde_detail", kwargs={"pk": self.pk})

class Verleihung(models.Model):
    buch = models.ForeignKey(Buch, verbose_name=("Buch"), on_delete=models.CASCADE)
    kunde = models.ForeignKey(Kunde, verbose_name=("Kunde"), on_delete=models.CASCADE)
    von = models.DateTimeField(("von"), auto_now=False, auto_now_add=True)
    bis = models.DateTimeField(("bis"), auto_now=False, auto_now_add=False, null=True, blank=True)
    kommentar = models.TextField(("Kommentar"), null=True, blank=True)

    class Meta:
        verbose_name = ("Verleihung")
        verbose_name_plural = ("Verleihungen")

    def __str__(self):
        return f"{self.buch} - {self.kunde} ({self.bis})"

    def get_absolute_url(self):
        return reverse("Verleihung_detail", kwargs={"pk": self.pk})
