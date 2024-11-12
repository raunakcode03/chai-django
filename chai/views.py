from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, "chai/all_chai.html", {"chais": chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "chai/chai_detail.html", {"chai": chai})

def order_summary(request):
    orders = request.session.get('orders', [])
    total_price = sum(float(item['price']) * int(item['quantity']) for item in orders) if orders else 0
    context = {
        "orders": orders,
        "total_price": total_price
    }
    return render(request, "chai/order_summary.html", context)

def order_chai(request):
    if request.method == 'POST':
        # Handle order processing here
        return HttpResponse("Order placed successfully! Thank you for ordering.")

    chais = ChaiVariety.objects.all()
    return render(request, "chai/all_order.html", {"chais": chais})

@csrf_exempt
def sync_orders(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        orders = data.get('orders', [])
        request.session['orders'] = orders
        request.session.modified = True
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
