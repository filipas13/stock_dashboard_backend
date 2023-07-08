from rest_framework import serializers
from .models import Stock, StockProfile, StockQuote

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class StockProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProfile
        fields = '__all__'

class StockQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockQuote
        fields = '__all__'
