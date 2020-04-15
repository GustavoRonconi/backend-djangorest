from rest_framework.serializers import ModelSerializer

from .models import Viagem


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Viagem
        fields = ("data_inicio", "data_fim", "classificacao", "nota")