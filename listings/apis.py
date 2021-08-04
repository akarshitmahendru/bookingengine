from rest_framework import views, response, status
from .serializers import AvailableRoomsSerializer
from . import models as model


class AvailableRoomsAPI(views.APIView):
    model = model.ReservationModel
    serializer_class = AvailableRoomsSerializer

    def get_serializer_class(self):
        return AvailableRoomsSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        check_in = self.request.query_params.get("check_in", None)
        check_out = self.request.query_params.get("check_in", None)
        max_price = self.request.query_params.get("max_price", None)
        if check_in and check_out and max_price:
            excluded_ids = self.model.objects.exclude(check_in_date__gte=check_in,
                                                      check_out_date__lte=check_out).values_list('hotel_id',
                                                                                                 flat=True)
            queryset = model.Listing.objects.filter(booking_info__price__lte=max_price).exclude(id__in=
                                                                                                excluded_ids).\
                order_by('booking_info__price')
            if queryset:
                serializer = serializer(queryset, many=True).data
                return response.Response(
                    {"items": serializer},
                    status=status.HTTP_200_OK
                )
            else:
                return response.Response(
                    {"items": {}},
                    status=status.HTTP_200_OK
                )

        else:
            return response.Response(
                {"error": "check_in, check_out and max_price is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
