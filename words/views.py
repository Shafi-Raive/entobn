from django.views.generic import ListView

from . models import EnglishWords
from . models import Level

class HomeView(ListView):
    template_name = "home.html"
    model = EnglishWords

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('Level')
