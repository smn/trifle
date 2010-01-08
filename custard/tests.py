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