from django.shortcuts import render
from app.models import Product, Customer, Order

from django.shortcuts import render
from django.db.models import Count, Sum, F
from django.db.models.functions import TruncDate
from .models import Product, Order, Customer


def stats_view(request):
    top_customers = Customer.objects.values('name').annotate(total_products=Count('order__products')).order_by(
        '-total_products')[:1]
    top_products = Product.objects.annotate(order_count=Count('order')).order_by('-order_count')
    product_quantities = Product.objects.annotate(total_quantity=Sum('order__quantity')).order_by('-total_quantity')
    customer_orders_count = Customer.objects.values('name').annotate(total_orders=Count('order')).order_by(
        '-total_orders')
    most_ordered_products = Product.objects.annotate(total_quantity=Sum('order__quantity')).order_by('-total_quantity')
    orders_per_day = Order.objects.annotate(order_date=TruncDate('on_date')).values('order_date').annotate(
        daily_orders=Count('id')).order_by('-order_date')

    context = {
        'top_customers': top_customers,
        'top_products': top_products,
        'product_quantities': product_quantities,
        'customer_orders_count': customer_orders_count,
        'most_ordered_products': most_ordered_products,
        'orders_per_day': orders_per_day
    }
    return render(request, 'app/index.html', context)
