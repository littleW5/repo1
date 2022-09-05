from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

# Create your views here.
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField()
#
#     def create(self, validated_data):
#         new_book = Book.objects.create(**self.validated_data)
#         return new_book
#
#     def update(self, instance, validated_data):
#         Book.objects.filter(pk=instance.pk).update(**validated_data)
#         updata_book = Book.objects.get(pk=instance.pk)
#         return updata_book


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import BasePermission

# class MyAuthentication(object):
#     def authenticate(self, request):
#         return ("lee", None)

# class Mypermission(BasePermission):
#     def has_permission(self, request, view):
#         return False
#
#
# class BookSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"
#
#
# class BookView(APIView):
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [Mypermission]
#
#     def delete(self, request):
#         Book.objects.all().delete()
#         return Response()
#
#     def get(self, request):
#         print("ds::", request.user)
#         book_list = Book.objects.all()
#
#         serializer = BookSerializers(instance=book_list, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializers(data=request.data)
#         if serializer.is_valid():
#             # new_book = Book.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class BookDetailView(APIView):
#     def get(self, request, id):
#         book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=book, many=False)
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         Book.objects.get(pk=id).delete()
#         return Response()
#
#     def put(self, request, id):
#         updata_book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=updata_book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication


# class MyAuthentication(object):
#     def authentication(self,request):
#         return ("lee",None)


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers



# def get(self, request):
#     return self.list(request)

# serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#
# return Response(serializer.data)


# def post(self, request):
#     return self.create(request)
# serializer = self.get_serializer(data=request.data)
# if serializer.is_valid():
#     # new_book = Book.objects.create(**serializer.validated_data)
#     serializer.save()
#     return Response(serializer.data)
# else:
#     return Response(serializer.errors)


#     def delete(self, request):
#         #return self.delete(request)
#         self.get_queryset().delete()
#         return Response()
#
#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

# def get(self, request, pk):
#     return self.retrieve(request, pk)
# serializer = self.get_serializer(instance=self.get_object(), many=False)
# return Response(serializer.data)

# def delete(self, request, pk):
#     return self.destroy(request, pk)
# self.get_object().delete()
# return Response()
#
# def put(self, request, pk):
#     return self.update(request, pk)

# serializer = self.get_serializer(instance=self.get_object(), data=request.data)
# if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data)
# else:
#     return Response(serializer.errors)
