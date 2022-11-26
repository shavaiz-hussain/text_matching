from django.db import models


class Key(models.Model):
    name = models.CharField(max_length=1024, unique=True, db_index=True)


class Value(models.Model):
    name = models.CharField(max_length=1024, unique=True, db_index=True)
