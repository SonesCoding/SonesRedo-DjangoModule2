from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Star(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=300)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Quote(models.Model):
    name = models.CharField(max_length=50)
    Qtext = models.TextField()
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    

"""
        Sirius, 50.00, Blue
        Regulus, 50.00, Orange
        Aldebaram, 65.00, Gold
        Maia, 100.00, Purple
        Electra, 150.00, ???
        Alcyone, 100.00, Red
        Celaeno, 75.00, Pink
        
        Beyonce,
        Emma Xu,
        Vincent Van Gogh
        Maya Angelou
        Socrates
        Oscar Wilde
        
        A, "Shine Bright Like a diamond.", Beyonce
        B, "You can be the brightest star in someones darkest nights.", Emma Xu
        C, "For my part I know nothing with any certainty, but the sight of the stars makes me dream." , Vincent Van Gogh
        D, "Nohting can dim the light which shines from within.", Maya Angelou
        E, "Be as you wish to seem.", Socrates
        F, "Wisdom begins in wonder.", Socrates
        G, "You can never be overdressed or overeducated.", Oscar Wilde
        
        """