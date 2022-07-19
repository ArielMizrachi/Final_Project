from urllib import request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from base.models import Airline_Companies, Countries
from base.api.Airline_Companies.airline_companies_serializer import AirlineCompaniesSerializer


@api_view(['GET'])
def GetRoutes(request):
    routes = [
        'GetAirlines/',
        'AddAirline/',
        'DelCountries/',
        'PutCountries/',
    ]
 
    return Response(routes)
 

# getting all of the countries 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetAirlines(request,id=-1):
    if int(id) > -1:
        return Response(AirlineCompaniesSerializer().GetAirlineById(id))
    else:
        return Response(AirlineCompaniesSerializer().GetAllAirlines())
  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddAirline(request):
    country= Countries.objects.get(name = request.data['country'])
    user= request.user

    Airline_Companies.objects.create(name=request.data['name'] ,country=country,user=user)
    return Response({"add": request.data['name']})


# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def DelCountries(request,id): 
#     temp= Countries.objects.get(id = id)
#     temp.delete()
#     return Response({'DELETE': id})


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def PutCountries(request,id): 
#     temp=Countries.objects.get(id = id)
#     temp.name =request.data['name']
#     temp.flag =request.data['flag']
#     temp.save()
#     return Response({'PUT': id})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getCars(request):
#     print("innnn")
#     user = request.user
#     print(user)
#     cars = user.car_set.all()
#     print(cars)
#     serializer = CarSerializer(cars, many=True)
#     return Response(serializer.data)
 
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def addNote(request):
#     user = request.user
#     Note.objects.create(body=request.data['newnote'],user=user)
#     print(user)
#     notes = user.note_set.all()
#     print(notes)
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)




# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def addCar(request):
#     print(request.data)
#     user = request.user
#     Car.objects.create(color=request.data["color"],model=request.data["model"],user=user)
#     print(user)
#     return Response({'car':'added'})