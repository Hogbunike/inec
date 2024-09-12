from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import PollingUnit, AnnouncedPUResult, LGA
from .serializers import PollingUnitSerializer, AnnouncedPUResultSerializer, LGASerializer

# Create your views here.


# View to display results for a single polling unit
class PollingUnitResultsView(APIView):
    def get(self, request, uniqueid):
        try:
            results = AnnouncedPUResult.objects.filter(polling_unit__uniqueid=uniqueid)
            serializer = AnnouncedPUResultSerializer(results, many=True)
            return Response(serializer.data)
        except PollingUnit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# View to display summed results for an LGA
class SummedLGAResultsView(APIView):
    def get(self, request, lga_id):
        results = AnnouncedPUResult.objects.filter(polling_unit_wardlga_id=lga_id)
        total_results = {}
        for result in results:
            if result.party_abbreviation in total_results:
                total_results[result.party_abbreviation] += result.party_score
            else:
                total_results[result.party_abbreviation] = result.party_score
        return Response(total_results)

# View to store results for a new polling unit
class AddPollingUnitResultsView(APIView):
    def post(self, request):
        serializer = AnnouncedPUResultSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)