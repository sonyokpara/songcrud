from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name+" "+self.last_name


class Song(models.Model):
    title = models.CharField(max_length=150)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

