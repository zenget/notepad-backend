from rest_framework import viewsets
from notes.api.serializers import (NoteSerializer)
from notes.models import (Note)


class NoteSerializerViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Note."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        owner = self.request.query_params.get('owner')
        if owner is not None:
            return Note.objects.filter(owner=owner)

        return Note.objects.all()
