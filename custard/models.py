from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """Ingredient for custard"""
    name = models.TextField(blank=True)
    amount = models.IntegerField(blank=True, null=True)
    
    def pretty_string(self):
        """
        >>> i = Ingredient(name='Vanilla', amount=3)
        >>> i.pretty_string()
        '3 amounts of Vanilla'
        
        """
        return "%s amounts of %s" % (self.amount, self.name)
    
    class Meta:
        verbose_name, verbose_name_plural = "custard", "custards"
    
    def __unicode__(self):
        return u"Ingredient"
    
    @models.permalink
    def get_absolute_url(self):
        return ('Ingredient', [self.id])