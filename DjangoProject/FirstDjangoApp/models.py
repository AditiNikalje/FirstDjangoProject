from django.db import models

# Create your models here.

# ========================================================
# Project model
# ========================================================
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)

    class Meta:
        db_table = 'Project'   
 
    def __str__(self):
        return f'{self.title}'
