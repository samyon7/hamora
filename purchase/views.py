import os

from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Chart


# Create your views here.
def index(request):
    list_products = Product.objects.all().values()
    page = request.GET.get('page', 1)
    paginator = Paginator(list_products, 10)

    if len(list_products) == 0:
        last_count = 1
    else:
        last_count = int(list_products[len(list_products) - 1]["code"][2:]) + 1
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'products': products, "last_count": last_count, "page": page})


def save(request):
    if request.method == "POST":
        myfile = request.FILES['product_image']
        fs = FileSystemStorage()
        _, extension = os.path.splitext(myfile.name)
        fs.save("media/" + request.POST.get("code") + extension, myfile)
        product = Product.create(
            request.POST.get("code"),
            request.POST['product_name'],
            request.POST['real_price'],
            request.POST['stock'],
            request.POST.get("code") + extension
        )
        product.save()
        return redirect("/")


def buy(request):
    if request.method == "POST":
        product = Product.objects.get(pk=request.POST.get('code'))
        try:
            found_chart = Chart.objects.filter(product_id=product.code).get()
            found_chart.quantity += 1
            found_chart.total_price = found_chart.quantity * product.price
            found_chart.save()
        except:
            chart = Chart.create(product, 1, 1 * product.price)
            chart.save()
        return redirect("/")

def chart(request):
    list_chart = Chart.objects.all()
    total = 19000
    for chart in list_chart:
        total += chart.total_price
    return render(request, 'chart.html', {'charts': list_chart, 'total': total})

def decrement(request):
    if request.method == "POST":
        chartId = request.POST.get('chart_id')
        chart = Chart.objects.get(chart_id=chartId)
        if chart.quantity == 1:
            chart.delete()
        else:
            chart.quantity -= 1
            chart.total_price = chart.quantity * chart.product.price
            chart.save()
    return redirect("/chart")
def incerment(request):
    if request.method == "POST":
        chartId = request.POST.get('chart_id')
        print(chartId)
        chart = Chart.objects.get(chart_id=chartId)
        chart.quantity += 1
        chart.total_price = chart.quantity * chart.product.price
        chart.save()

    return redirect("/chart")

def checkout(request):
    if request.method == "POST":
        Chart.objects.all().delete()
    return redirect("/chart")