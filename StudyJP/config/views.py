from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return super().get(request, *args, **kwargs)


class IndexPage(TemplateView):
    template_name = "index.html"


class ThanksPage(TemplateView):
    template_name = "thanks.html"
