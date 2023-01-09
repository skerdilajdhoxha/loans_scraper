from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Loan
from .serializers import LoanSerializer


@api_view(["GET"])
def loans_list(request):
    loans = Loan.objects.all()
    serializer = LoanSerializer(loans, many=True)
    from pathlib import Path
    print(str(
            Path(__file__).resolve().parent.parent.parent / "requirements/chromedriver"
        ))
    return Response(serializer.data)


@api_view(["GET"])
def country_list(request):
    loans = Loan.objects.all()
    serializer = LoanSerializer(loans, many=True, context={"fields": ["country"]})
    return Response(serializer.data)


class SectorList(APIView):

    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True, context={"fields": ["sector"]})
        return Response(serializer.data)
