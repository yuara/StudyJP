from django.db import models

# Create your models here.
class Voca(models.Model):
    kanji = models.CharField(max_length=256)
    kana = models.CharField(max_length=256)
    pos = models.CharField(max_length=256)  # Parts of speech
    meaning = models.CharField(max_length=256)
    en_example = models.CharField(max_length=256)
    ja_example = models.CharField(max_length=256)
    example_kana = models.CharField(max_length=256)
    level = models.CharField(max_length=32)
