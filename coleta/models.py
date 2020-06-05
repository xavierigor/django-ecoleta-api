from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item')

    def __str__(self):
        return self.title


class Point(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='point')
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    items = models.ManyToManyField(Item, related_name='points')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
