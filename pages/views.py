from django.shortcuts import render

def index_page(request):
    return render(request, 'index_page.html')

def math_operations(request):
    return render(request, 'math_operations.html')