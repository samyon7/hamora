from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    product_name = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_image = models.TextField()

    @classmethod
    def create(cls, code, product_name, price, stock, product_image):
        product = cls(code=code, product_name=product_name, price=price, stock=stock, product_image=product_image)
        return product

class Chart(models.Model):
    chart_id = models.AutoField(primary_key=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, to_field="code")
    quantity = models.IntegerField()
    total_price = models.IntegerField()

    @classmethod
    def create(cls, product, quantity, total_price):
        chart = cls(product=product, quantity=quantity, total_price=total_price)
        return chart

