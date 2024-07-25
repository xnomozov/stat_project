from django.shortcuts import render
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate
from .models import Product, Order, Customer

def stats_view(request):
    # Product Aggregates
    product_quantities = Product.objects.annotate(total_quantity_ordered=Sum('order__quantity')).order_by('-total_quantity_ordered')
    average_price = Product.objects.aggregate(avg_price=Sum('price')/Count('id'))  # Example for average price
    total_stock = Product.objects.aggregate(total_stock=Sum('stock'))

    # Order Aggregates
    orders_per_day = Order.objects.annotate(order_date=TruncDate('on_date')).values('order_date').annotate(daily_orders=Count('id')).order_by('-order_date')
    order_quantities = Order.objects.annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')

    # Customer Aggregates
    customer_orders_count = Customer.objects.values('name').annotate(total_orders=Count('order')).order_by('-total_orders')
    customer_products_count = Customer.objects.values('name').annotate(total_products=Sum('order__quantity')).order_by('-total_products')
    top_customers_by_value = Customer.objects.annotate(total_value=Sum('order__products__price')).order_by('-total_value')

    context = {
        'product_quantities': product_quantities,
        'average_price': average_price,
        'total_stock': total_stock,
        'orders_per_day': orders_per_day,
        'order_quantities': order_quantities,
        'customer_orders_count': customer_orders_count,
        'customer_products_count': customer_products_count,
        'top_customers_by_value': top_customers_by_value,
    }
    return render(request, 'app/index.html', context)
