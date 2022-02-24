from rest_framework import viewsets
from notes.api.serializers import (NoteSerializer)
from django.db.models import Q
from notes.models import (Note)


class NoteSerializerViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Note."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        search_key = self.request.query_params.get('searchKey')

        filters = Q()
        if(search_key is not None and search_key != ''):
            filters &= (Q(title__contains=search_key) | Q(
                owner__contains=search_key))

        return Note.objects.filter(filters)
