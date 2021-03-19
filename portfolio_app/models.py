from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=200)

    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"
