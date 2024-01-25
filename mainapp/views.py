import decimal
import json
import requests
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Rate
from .serializers import RateModelSerializer


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
}

API_URL = f'http://apilayer.net/api/live?access_key=5ac1b45ecdd081436271a245070b73f7&currencies=RUB&source=USD&format=1'


def rates1():
    response = requests.get(API_URL, headers=HEADERS)
    if response.status_code == requests.codes.ok:
        response_dict = json.loads(response.text)
        return response_dict
    else:
        print("Error:", response.status_code, response.text)


class RateViewSet(ViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateModelSerializer

    # @action(detail=True, methods=['GET'])
    def list(self, request):
        queryset = Rate.objects.all().order_by('-id')
        last_record = Rate.objects.all().last()
        time_difference = datetime.now(timezone.utc) - last_record.datetime
        time_difference_in_seconds = time_difference.total_seconds()
        if time_difference_in_seconds > 60:
            print('request for new rate')
            rate_value = rates1()
            new_rate = Rate()
            new_rate.currency='USD'
            new_rate.rate = decimal.Decimal(str(rate_value['quotes']['USDRUB']))
            new_rate.save()
        else:
            print('Use recorded data')
        if len(queryset) > 15:
            oldest_rate = queryset.reverse()[0]
            Rate.objects.filter(id=oldest_rate.id).delete()
            print(f'Item with {oldest_rate.id=}  deleted')
        result_queryset = queryset[:10]
        serializer = RateModelSerializer(result_queryset, many=True)
        return Response(serializer.data)
