from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'scuffle/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hi, welcome to Scuffle module!'
        return context