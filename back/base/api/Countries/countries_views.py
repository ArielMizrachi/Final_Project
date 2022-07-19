from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from base.models import Countries
from base.api.Countries.countries_serializer import CountriesSerializer


@api_view(['GET'])
def GetRoutes(request):
    routes = [
        'GetCountries/',
        'AddCountries/',
        'DelCountries/',
        'PutCountries/',
    ]
 
    return Response(routes)
 

# getting all of the countries 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCountries(request,id=-1):
    if int(id) > -1:
        return Response(CountriesSerializer().GetCountryById(id))
    else:
        return Response(CountriesSerializer().GetAllCountries())
  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddCountries(request): 
    Countries.objects.create(name=request.data['name'] ,flag=request.data['flag'])
    return Response({"POST":"add"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DelCountries(request,id): 
    temp= Countries.objects.get(id = id)
    temp.delete()
    return Response({'DELETE': id})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def PutCountries(request,id): 
    temp=Countries.objects.get(id = id)
    temp.name =request.data['name']
    temp.flag =request.data['flag']
    temp.save()
    return Response({'PUT': id})

