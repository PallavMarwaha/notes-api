from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.contrib.postgres.search import SearchQuery

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def note_view(request, id=None):
    """
    NotesView for different HTTP method
    """

    # GET
    if request.method == "GET":
        # List
        if id is None:
            notes = Note.objects.filter(user=request.user, is_deleted=False)
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)

        # Retrieve
        try:
            note = Note.objects.get(user=request.user, id=id, is_deleted=False)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    # CREATE
    if request.method == "POST":
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            note = Note(user=request.user, text=request.data.get("text"))
            note.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # UPDATE
    if request.method == "PUT":
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            try:
                note = Note.objects.get(user=request.user, id=id, is_deleted=False)
            except Note.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            note.text = serializer.validated_data["text"]
            note.save()
            return Response(status=status.HTTP_201_CREATED)

    # DELETE
    if request.method == "DELETE":
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            note = Note.objects.get(user=request.user, id=id, is_deleted=False)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        note.is_deleted = True
        note.save()
        return Response()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def share(request, id=None):
    """
    Shares a note with other users
    """
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        note = Note.objects.get(user=request.user, id=id, is_deleted=False)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(note)

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def search(request):
    """
    Query notes with query string. Case insensitive.
    """
    query = request.query_params.get("q")

    notes = Note.objects.filter(
        text__icontains=SearchQuery(query), is_deleted=False, user=request.user
    )

    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)
