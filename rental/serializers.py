from rest_framework import serializers
from rental.models import Offer
from django.contrib.auth.models import User


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'address', 'size', 'type', 'price', 'sharing', 'text']


class UserSerializer(serializers.ModelSerializer):
    offers = serializers.PrimaryKeyRelatedField(many=True, queryset=Offer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'offers']
