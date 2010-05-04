"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import client
from django.core.urlresolvers import reverse
from custard.models import Ingredient

class CustardTest(TestCase):
    
    fixtures = ['custard']
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_output(self):
        c = client.Client()
        response = c.get(reverse('custard-test'), {
            'name': 'Simon'
        })
        self.assertContains(response, 'Hello Simon', count=1)
    
    def test_pretty_string(self):
        i = Ingredient(name='Vanilla', amount=3)
        self.assertEquals(i.pretty_string(), '3 amounts of Vanilla')
    
    def test_monkey_patched_name_field(self):
        i = Ingredient(name="a" * 40, amount=3)
        i.save()
        name_field = i._meta.get_field_by_name('name')[0]
        self.assertEquals(name_field.max_length, 50)
        self.assertEquals(i.name,"a" * 40)