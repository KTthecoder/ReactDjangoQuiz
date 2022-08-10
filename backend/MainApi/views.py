from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def AllQuizes(request):
    if request.method == 'GET':
        quizes = QuizModel.objects.all()[:8]
        data = {}
        if quizes.exists():
            serializer = QuizSerializerMaxEight(quizes, many = True)
            return Response(serializer.data)
        else:
            data['response'] = 'There is not any quizes in database'
            return Response(data)
    else:
        data = {}
        data['response'] = 'Invalid method (Try GET)'
        return Response(data)

@api_view(['GET'])
def QuizesByCategory(request, categorySlug):
    if request.method == 'GET':
        data = {}
        try:
            categoryId = QuizCategoryModel.objects.get(slug = categorySlug)
            quizes = QuizModel.objects.filter(cateogry = categoryId.id)[:8]
            if quizes.exists():
                serializer = QuizSerializerMaxEight(quizes, many = True)
                return Response(serializer.data)
            else:
                data['response'] = 'There is not any quizes in database'
                return Response(data)
        except:
            data['response'] = 'This slug is invalid'
            return Response(data)
    else:
        data['response'] = 'Invalid method (Try GET)'
        return Response(data)

@api_view(['GET'])
def AllCategories(request):
    if request.method == 'GET':
        data = {}
        try:
            categories = QuizCategoryModel.objects.all()
            if categories.exists():
                serializer = CategorySerializer(categories, many = True)
                return Response(serializer.data)
            else:
                data['response'] = 'There is not any categories in database'
                return Response(data)
        except:
            data['response'] = 'This slug is invalid'
            return Response(data)
    else:
        data['response'] = 'Invalid method (Try GET)'
        return Response(data)
