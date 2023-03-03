from django.http import HttpResponse
from django.views.generic import TemplateView
from mainapp import models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["objects"] = models.DataBase.objects.all()
        return context

# get data from address panel
def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")