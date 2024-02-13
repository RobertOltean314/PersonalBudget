"""
A view is a 'type' of web page in your Django application that
generally serves a specific function and has
a specific template.
"""
from django.views.generic import TemplateView


# Folosim clasa Home Page ca sa dam display la home_page.html, dupa care in home_page html vom avea o referinta care face
# link cu navbar-ul, care se va afla in toate fisierele

class HomePage(TemplateView):
    template_name = 'home_page/home_page.html'
