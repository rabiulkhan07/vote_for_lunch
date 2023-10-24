from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed,APIException
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import EmployeeSerializer
from .models import Employee
import jwt,datetime


class RegisterView(APIView) :
    def post(self,request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except APIException as error:
            return Response({'detail': str(error)}, status=error.status_code)
class GetAllUserView(APIView):
    def get(self,request):
        query_results = Employee.objects.all()
        serializer = EmployeeSerializer(query_results,many=True)
        return Response(serializer.data) 
    
class GetSingleData(APIView):    
    def get(self,request,user_id):
        query_results = Employee.objects.filter(id=user_id)
        serializer = EmployeeSerializer(query_results,many=True)
        return Response(serializer.data) 
    
    def put(self, request, user_id):
        try:
            employee = Employee.objects.get(id=user_id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'})
    
    def delete(self, request,user_id):
        try:
            
            employee = Employee.objects.get(id=user_id)
            employee.delete()
            return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoginView(APIView):
    def post(self, request):
        employeeId = request.data['employeeId']
        password = request.data['password']

        user = Employee.objects.filter(employeeId=employeeId).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        algorithm = 'HS256'

        # Generate the token
        token = jwt.encode(payload, 'secret', algorithm=algorithm)

        # Save the token to the user's model
        user.jwt_token = token
        user.save()

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response
    
class EmployeeView(APIView):
    def get(self,request):
         token = request.COOKIES.get('jwt')

         if not token:
             raise AuthenticationFailed('Unauthenticated')
         
         try:
             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
         except jwt.ExpiredSignatureError :
             raise AuthenticationFailed('Unauthenticated')
         
         user = Employee.objects.filter(id=payload['id']).first()
         serializer = EmployeeSerializer(user)
             
         return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }

        return response
    



    
         