from django.views.generic import ListView
from . models import Word_Mng

# Class indexView
class indexView(ListView):
    template_name = "index.html"
    model = Word_Mng
