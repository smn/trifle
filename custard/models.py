from django.db import models
from django.db.models import signals

# Create your models here.
class Ingredient(models.Model):
    """Ingredient for custard"""
    name = models.CharField(blank=True, max_length=30)
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


def monkey_patch_name_field(sender, **kwargs):
    instance = kwargs['instance']
    instance._meta.get_field_by_name('name')[0].max_length = 50
    return instance

signals.post_init.connect(monkey_patch_name_field, sender=Ingredient)