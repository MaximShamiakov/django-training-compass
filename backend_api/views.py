from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Material, Сategories, ProjectInformation
from django.http import HttpResponse
import bcrypt
import json
from uuid import uuid4
import uuid
import random
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@csrf_exempt
def register_user_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            return JsonResponse({'message': 'Passwords do not match'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=400)

        user = User.objects.create_user(
            username=username, email=email, password=password)
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('name')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'message': 'Success'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)


class Categories(APIView):
    def post(self, request):
        indexTask = request.data.get("indexTask")
        category = request.data.get("category")
        materials = Material.objects.filter(
            title=category).exclude(id__in=indexTask)
        output = []
        unique_indexes = random.sample(
            range(len(materials)), min(5, len(materials)))
        if materials:
            for index in unique_indexes:
                material = materials[index]
                output.append({
                    'id': material.id,
                    "title": material.title,
                    "question": material.question,
                    "answer": material.answer,
                })
            return Response(output)

        return Response(output)


def get_categories(request):
    categories_list = []
    for categories in Сategories.objects.all():
        categories_list.append({
            'title': categories.title,
            'category': categories.category
        })
    return HttpResponse(json.dumps(categories_list, ensure_ascii=False))


def projectInformations(request):
    informations = ProjectInformation.objects.all()
    data = []
    for info in informations:
        data.append({'title': info.title, 'body': info.body})

    return HttpResponse(json.dumps(data, ensure_ascii=False))
