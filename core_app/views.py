from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'core_app/index.html'
