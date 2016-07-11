from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from snippets.models import Snippet 
from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippetList(requeset, format = None):
	"""
    List all snippets, or create a new snippet.
    """
    if requeset.method == 'GET':
    	snippets = Snippet.objects.all()
    	serializer = SnippetSerializer(snippets, many = True)
    	return Response(serializer.data)
    elif requeset.method == 'POST':
    	serializer = SnippetSerializer(requeset.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status = status.HTTP_201_CREATED)
    	return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

	pass
@api_view(['GET', 'PUT', 'DELETE'])
def snippetDetail(requeset, pk, format = None):
	"""
    Retrieve, update or delete a snippet instance.
    """
    try:
    	snippet = Snippet.objects.get(pk = pk)
    	pass
    except Snippet.DoesNotExist:
    	return Response(status = status.HTTP_404_NOT_FOUND)
    if requeset.method == 'GET':
    	serializer = SnippetSerializer(snippet)
    	return Response(serializer.data)
    elif requeset.method == 'PUT':
    	serializer = SnippetSerializer(snippet,data = requeset.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data)
    	return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    elif requeset.method == 'DELETE':
    	snippet.delete()
    	return Response(status =status.HTTP_204_NO_CONTENT)
	pass