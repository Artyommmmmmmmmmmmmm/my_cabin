from django.views.generic import ListView, DetailView
from .filters import NoteFilter
from .models import Note

class MainPage(ListView):

    model = Note

    template_name='main.html'

    context_object_name='main_page'

    def get_queryset(self):

        queryset = super().get_queryset()

        self.filterset = NoteFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        
        return context
    
class DetailPage(DetailView):

    model = Note

    template_name = 'note.html'

    context_object_name = 'note'