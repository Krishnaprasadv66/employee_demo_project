from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import Employees
from .serializers import EmployeeSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status



@api_view(['GET'])
def index(request):
    people_details = {
        'name' : 'rahul',
        'place' : 'trivandrum'
    }
    return Response(people_details)







# SIGNUP PAGE

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)




# LOGIN PAGE


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please enter valid username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)






################ crud ####################




@api_view(['GET','POST','PUT','DELETE', 'PATCH'])
def employees(request):
    if request.method == 'GET':
        objEmployee = Employees.objects.all()
        serializer = EmployeeSerializer(objEmployee, many = True)
        return Response (serializer.data)
    




    elif request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)


        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=400 )
    




    elif request.method == 'PUT':
        data = request.data
        try:
            obj = Employees.get(id=data['id'])

        except Employees.DoesNotExist:
            return Response ({"error": "employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj , data=data, partial=False)


        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status=400)
    






    elif request.method == 'DELETE':
        data = request.data
        try:
            obj = Employees.objects.get(id=data['id'])

        except Employees.DoesNotExist:
            return Response ({"error" : "employee not found"}, status=404)


        obj.delete()
        return Response({"message": "employee deleted successfully"}, status=204)








    elif request.method == 'PATCH':
        data = request.data 
        try:
            obj = Employees.objects.get(id=data['id'])

        except Employees.DoesNotExist:
            return Response({"error": "employee not found"}, status=404)

        serializer = EmployeeSerializer(obj, data=data, partial=True)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=400)        




