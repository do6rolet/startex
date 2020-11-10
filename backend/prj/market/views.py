import csv, io
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.contrib import messages
from .models import Product
from rest_framework import viewsets


from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


@permission_required('admin.can_add_log_entry')
def product_upload(request):
    template = "product_upload.html"

    prompt = {
        'order': 'Order of the CSV is articule, name, price_in'
    }

    if request.method == "GET":
        return render(request, template, prompt)
    if request.method == 'POST':
        try:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a csv file')
                return render(request, template, {})

            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            Product.objects.all().delete()
            for column in csv.reader(io_string, delimiter=';'):
                if float(column[2]) < 1000:
                    Product.objects.update_or_create(
                        articule=column[0],
                        name=column[1],
                        price_in=float(column[2])*0.9,
                        price_out=float(column[2])*1.2
                    )
                else:
                    Product.objects.update_or_create(
                        articule=column[0],
                        name=column[1],
                        price_in=float(column[2]) * 0.9,
                        price_out=float(column[2]) * 1.1
                    )


            context = {}
            return render(request, template, context)
        except:
            messages.error(request, 'Something wrong with your csv file')
            return render(request, template, {})



