from django_filters import FilterSet
from .models import Note

class NoteFilter(FilterSet):
    class Meta:
        model=Note
        fields={
            'title': ['icontains']    
        }