from django.views.generic import TemplateView


class PageAccueil(TemplateView):
    template_name = 'home.html'


class Apropos(TemplateView):
    template_name = 'apropos.html'
