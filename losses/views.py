from django.shortcuts import render
from .models import Header
from .xls_data import Losses

losses = Losses()
# headers = losses.headers

# Create your views here.
def index(request):
    """Домашняя страница приложения losses"""
    current_data = losses.get_current_data
    headers_and_losses = losses.read_headers_and_total_losses()
    context = {'current_dates': current_data, 'headers_and_losses': headers_and_losses}
    return render(request, 'losses/index.html', context)


def diagrams(request):
    """Cтраница diagrams"""
    headers = Header.objects.order_by('id')
    context = {'headers': headers}
    return render(request, 'losses/diagrams.html', context)

def header(request, header_id):
    """Monthly chart for some header."""
    header = Header.objects.get(id=header_id)
    headers_and_losses = losses.read_headers_and_total_losses()
    num_header = losses.headers[header_id - 1]
    total = headers_and_losses[num_header]
    months = losses.months
    datas = losses.read_month_data(header_id + 1)
    context = {'header': header, 'total': total, 'months': months, 'datas': datas}
    return render(request, 'losses/header.html', context)