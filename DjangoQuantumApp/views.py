from rest_framework.response import Response
from rest_framework.views import APIView

from DjangoQuantumApp.models import UserDB
from DjangoQuantumApp.serializers import LoginSerializer, UserSerializer

__author__ = 'bairagi'



class LoginView(APIView):

    def post(self,request):
        status=200
        detail="Login Success"
        loginSer=LoginSerializer(data=request.DATA)
        if loginSer.is_valid():
            loginDict=loginSer.data
            userList=UserDB.objects.filter(email=loginDict.get('email'),password=loginDict.get('password'))
            if userList.count()>0:
               userOb=userList[0]
            else:
               detail='login failure'
               status=400
            return Response(data=detail,status=status,content_type='application/json')
        else:
            detail='bad input'
            return Response(data=detail,status=400,content_type='application/json')


class GetAllUser(APIView):

     def get(self,request):
         status=200
         try:
            userList=UserDB.objects.all()
            return Response(data=UserSerializer(userList,many=True).data,status=status,content_type='application/json')
         except Exception,err:
            status=500
            detail='Internal Error'
            return Response(data=detail,status=status,content_type='application/json')



class UserRegister(APIView):

    def post(self,request):
        status=200
        detail='Registration failure'
        userSer=UserSerializer(data=request.DATA)
        try:
            if userSer.is_valid():
                userDict=userSer.data
                user=UserDB(email=userDict.get('email'),password=userDict.get('password'),firstName=userDict.get('firstName'),lastName=userDict.get('lastName'))
                user.save()
                return Response(data=UserSerializer(user).data,status=status,content_type='application/json')
            else:
                return Response(data=detail,status=400,content_type='application/json')
        except Exception,err:
            status=500
            detail='Internal Error'
            return Response(data=detail,status=status,content_type='application/json')


    def get(self,request,user_id):
        status=200
        try:
            userOb=UserDB.objects.get(id=user_id)
        except UserDB.DoesNotExist,err:
            detail=str(err)
            status=400
            return Response(data=detail,status=status,content_type='application/json')
        except Exception,err:
            detail=str(err)
            status=500
            return Response(data=detail,status=status,content_type='application/json')
        return Response(data=UserSerializer(userOb).data,status=status,content_type='application/json')


    def put(self,request,user_id):
        status=200
        userSer=UserSerializer(data=request.DATA)
        try:
            userOb=UserDB.objects.get(id=user_id)
            if userSer.is_valid():
               userDict=userSer.data
               userOb.email=userDict.get('email')
               userOb.password=userDict.get('password')
               userOb.firstName=userDict.get('firstName')
               userOb.lastName=userDict.get('lastName')
               userOb.save()
        except Exception,err:
            detail=str(err)
            status=500
            return Response(data=detail,status=status,content_type='application/json')
        return Response(data=UserSerializer(userOb).data,status=status,content_type='application/json')




    def delete(self,request,user_id):
        status=200
        detail="Successfully delete user"
        try:
            userList=UserDB.objects.filter(id=user_id)
            if userList.count()>0:
               userOb=userList[0]
               userOb.delete()
            else:
               detail='user does not exist'
               status=400
            return Response(data=detail,status=status,content_type='application/json')
        except Exception,err:
            detail=str(err)
            status=500
            return Response(data=detail,status=status,content_type='application/json')













