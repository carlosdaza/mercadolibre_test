from django.shortcuts import render

# Create your views here.
from rest_framework import status, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from dna_manager.models import DNASample, Stats
from dna_manager.validator import dna_validator


class ValidateDNASample(APIView):
    queryset = DNASample.objects.all()

    # authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        data = request.data
        try:
            is_mutant = dna_validator(data['dna'])
            DNASample.objects.create(sample=str(data['dna']), is_mutant=is_mutant)
            if is_mutant:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_400_BAD_REQUEST)


class StatsSerializer(serializers.ModelSerializer):
    ratio_description = serializers.SerializerMethodField()

    class Meta:
        model = Stats
        fields = ['mutant_samples', 'human_samples', 'ratio', 'ratio_description']

    def get_ratio_description(self, stats):
        return 'h/m' if stats.mutant_samples > stats.human_samples else 'm/h'


class GetStatsView(ListAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)