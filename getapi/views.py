from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
import requests, json
from django.http import JsonResponse
from .serializers import TaskSerializer
from user.models import Task
from rest_framework import generics
from rest_framework import generics, permissions  # New


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_api(request):
    # theme = request.COOKIES.get("theme")

    url = f'https://randomuser.me/api/'

    try:
        response = requests.get(url, stream=True, verify=False, timeout=1)
        response.raise_for_status()

        if len(response.text) > 200:
            obj = json.loads(response.text)
        else:
            obj = {}
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException) as e:
        print(f"Error: {type(e).__name__}: {e}")
        obj = {}

    if obj:
        print(obj)
    else:
        print('obj not found')

    


    return JsonResponse(obj)





class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Only an authenticated user can access this API endpoint
    # permission_classes = [permissions.IsAuthenticated]


    # return Response(queryset.data)