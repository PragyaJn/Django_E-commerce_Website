# import datetime
#
# from django.db import models
# from .product import Product
# from .customer import Customer
#
# class Order(models.Model):
#      product = models.ForeignKey(Product ,on_delete=models.CASCADE)
#      customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#      quantity=models.IntegerField(default=1)
#      price=models.IntegerField()
#      address =models.CharField(max_length=50 , default='',blank=True)
#      phone = models.CharField(max_length=50 , default='' , blank=True)
#      date=models.DateField(default=datetime.datetime.today)
#
#      def placeOrder(self):
#           self.save()
#
# again
#
# from django.shortcuts import render, redirect
#
# from django.contrib.auth.hashers import check_password
# from store.models.customer import Customer
# from django.views import View
#
# from store.models.product import Product
# from store.models.orders import Order
# from store.middlewares.auth import auth_middleware
#
# class OrderView(View):
#
#
#     def get(self , request ):
#         customer = request.session.get('customer')
#         orders = Order.get_orders_by_customer(customer)
#         print(orders)
#         return render(request , 'orders.html'  , {'orders' : orders})

from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')