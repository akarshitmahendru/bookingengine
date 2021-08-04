from rest_framework import serializers
from .models import ReservationModel, BookingInfo, Listing


class AvailableRoomsSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        try:
            if obj.booking_info:
                return obj.booking_info.price
            else:
                return None
        except:
            return None

    class Meta:
        model = Listing
        fields = ('listing_type', 'title', 'country', 'city', 'price')