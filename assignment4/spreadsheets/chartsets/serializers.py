from chartsets.models import Chartset
from rest_framework import serializers

class ChartsetSerializer(serializers.ModelSerializer):
    #задать вопрос про отображение поля ManyToMany
    userschartsets = serializers.CharField(read_only=True)
    class Meta:
        model = Chartset
        fields = ['id', 'name', 'userschartsets', 'date_modified']