
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.api.serializers import FachSerializer, AntwortSerializer
from main.models import Fach, Antwort
from main.views import results


# Create your views here.
@api_view(['GET','POST'])
def mainfach(request):
    if request.method == 'GET':
        latest_fach_list = Fach.objects.all()
        fach_data = FachSerializer(latest_fach_list, many=True).data
        return Response({"data": fach_data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        fach_serializer = FachSerializer(data=request.data)
        if fach_serializer.is_valid():
            fach_serializer.save()
            data = {
                "status": 1,
                "message": "Fach added successfully",
                "data": fach_serializer.data
                }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            error_details = []
            for key in fach_serializer.errors.keys():
                error_details.append({"field": key, "message": fach_serializer.errors[key][0]})
            data = {
                "error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - pease correct the below errors",
                    "error_details": error_details
                }
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            "error": {
                "status": 400,
                "message": "Your submitted data was not valid - please correct the below errors",
            }
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def specfach(request, fachid):
    try:
        fach = Fach.objects.get(pk=fachid)  # Hole das Fach-Objekt basierend auf der ID
    except Fach.DoesNotExist:
        return Response({
            "status": 404,
            "message": "Fach not Found"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        fach = Fach.objects.get(pk=fachid)
        fach_data = FachSerializer(fach).data
        return Response(fach_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        fach = Fach.objects.get(pk=fachid)
        fach.delete()
        data = {
            "status": 1,
            "message": "Fach deleted successfully",
        }
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        fach_serializer = FachSerializer(fach, data=request.data, partial=True)
        if fach_serializer.is_valid():
            fach_serializer.save()
            return Response({
                "status": 1,
                "message": "Fach updated successfully",
                "data": fach_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key, value in fach_serializer.errors.items():
                error_details.append({"field": key, "message": value[0]})
            return Response({
                "error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Fach not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def choicemain(request):
    if request.method == 'GET':
        antworten = Antwort.objects.all()
        antworten_data = AntwortSerializer(antworten, many=True).data
        return Response({"data": antworten_data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        antworten_serializer = AntwortSerializer(data=request.data)
        if antworten_serializer.is_valid():
            antworten_serializer.save()
            data = {
                "status": 1,
                "message": "Antwort added successfully",
                "data": antworten_serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return
    else:
        data = {
            "error": {
                "status": 400,
                "message": "Your submitted data was not valid - please correct the below errors",
            }
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def specchoice(request, antwortid):
    try:
        antwort = Antwort.objects.get(pk=antwortid)
    except Antwort.DoesNotExist:
        return Response({
            "status": 404,
            "message": "Antwort not Found"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        antwort = Antwort.objects.get(pk=antwortid)
        antwort_data = AntwortSerializer(antwort).data
        return Response(antwort_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        antwort = Antwort.objects.get(pk=antwortid)
        antwort.delete()
        data = {
            "status": 1,
            "message": "Antwort deleted successfully",
        }
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        antwort_serializer = AntwortSerializer(antwort, data=request.data, partial=True)
        if antwort_serializer.is_valid():
            antwort_serializer.save()
            return Response({
                "status": 1,
                "message": "Antwort updated successfully",
                "data": antwort_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key, value in antwort_serializer.errors.items():
                error_details.append({"field": key, "message": value[0]})
            return Response({
                "error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Antwort not found", status=status.HTTP_404_NOT_FOUND)
