from django.http import HttpResponse, Http404
from django.shortcuts import render , get_object_or_404
from django.template import loader

from .models import Order

def index(request):
    latest_order_list = Order.objects.order_by("date")[:5]
    context = {"latest_order_list": latest_order_list}
    return render(request, "stockIorders/index.html", context)

def detail(request, order_id):
    order = get_object_or_404(Order, pk = order_id)
    return render(request, "stockIorders/detail.html", {"order": order})

def results(request, order_id):
    response = "You're looking at the final basket for order %s."
    return HttpResponse(response % order_id)


def vote(request, order_id):
    return HttpResponse("You're shopping on order %s." % order_id)