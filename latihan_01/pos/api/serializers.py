from rest_framework import serializers
from pos_app.models import (
  TableResto
)

class TableRestoSerializer(serializers.ModelSerializer):
  class Meta:
    model = TableResto
    # fields = '__all__'
    fields = ('id', 'code', 'name', 'capacity', 'table_status', 'status')