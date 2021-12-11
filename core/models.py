from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

label_choices = (
    ('N', 'New'),
    ("Bs", "BestSeller")
)


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ("s")

    def __str__(self):
        return self.category_name


class Item(models.Model):
    flower_name = models.CharField(max_length=100, default="")
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.CharField(choices=label_choices, default="", max_length=2)
    item_image = models.ImageField(
        upload_to="uploads/", default='/images/Default_Flower.jpg')
    is_auctioned = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.flower_name

    def get_absolute_url(self):
        return reverse("core:products", kwargs={"pk": self.pk})

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={'pk': self.pk})

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={'pk': self.pk})


class CartItem(models.Model):
    """Model definition for CartItem."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        """Meta definition for CartItem."""
        verbose_name_plural = 'CartItems'

    def __str__(self):
        """Unicode representation of CartItem."""
        return f"{self.quantity} of {self.item.flower_name}"


class Order(models.Model):
    """Model definition for Order."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(CartItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return self.user.username
