from django.conf.urls.defaults import *
from custard import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^test/', views.test, {}, 'custard-test'),
)
