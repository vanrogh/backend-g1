from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def blogs_handler(request):
    if request.method == 'GET':
        categories = Blog.objects.all()
        serializer = BlogSerializer(categories, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)


def get_blogs(pk):
    try:
        blogs = Blog.objects.get(id=pk)
        return {
            'blogs': blogs,
            'status': 200
        }
    except Blog.DoesNotExist as e:
        return {
            'blogs': None,
            'status': 404
        }


@csrf_exempt
def blog_handler(request, pk):
    result = get_blogs(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Blog not found'}, status=404)

    blogs = result['blogs']

    if request.method == 'GET':
        serializer = BlogSerializer(blogs)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data, instance=blogs)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        category = Blog.objects.get(id=pk)
        category.delete()
        return JsonResponse({'message': 'Blog successfully deleted'}, status=200)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)