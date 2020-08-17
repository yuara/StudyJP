from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Voca

# Create your views here.


class IndexVoca(generic.TemplateView):
    template_name = "quiz/voca_index.html"


class ListVoca(generic.ListView):
    model = Voca
    template_name = "quiz/voca_list.html"


class QuizVoca(generic.ListView):
    template_name = "quiz/voca_quiz.html"

    paginate_by = 1

    def get_queryset(self):
        return Voca.objects.filter(level=self.kwargs["level"]).order_by("?")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the level
        context["level"] = self.kwargs["level"]
        return context
