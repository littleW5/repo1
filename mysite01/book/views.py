from django.shortcuts import render, HttpResponse

# Create your views here.
# def book(request):
#     if request.method=="GET":
#         return HttpResponse("GET在请求")
#     else:
#         return HttpResponse("POST在请求")
from django.views import View
from rest_framework.views import APIView


class BookView(APIView):
    def get(self, request):
        return HttpResponse("apiGet在请求")

    def post(self, request):
        return HttpResponse("apiPost在请求")

    def delete(self, request):
        return HttpResponse("apidelete 在请求")