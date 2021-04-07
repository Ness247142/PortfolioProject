from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(
        max_length=200, default="")
    technology = models.CharField(
        max_length=200, default="")
    image = models.ImageField(
        null=True, blank=True, default='default.jpeg', upload_to="images/")
    category = models.CharField(max_length=200)

    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"
