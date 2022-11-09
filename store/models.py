from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# one customer has one user
class Customer(models.Model):
    """Creating a one to one relationship between the User model and the Customer model."""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        """
        The __str__ function is a special function that is called when you print an object
        :return: The name of the object.
        """
        return self.name


class Product(models.Model):
    """Creating a table in the database with the name of the class and the fields that are defined in the class."""
    name = models.CharField(max_length=200)
    price = models.FloatField()
    """to check if this is a physical product or digital product for shipping purposes"""
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        The __str__ function is a special function that is called when you print an object
        :return: The name of the object.
        """
        return self.name

    @property
    def imageURL(self):
        """
        If the image field is empty, return an empty string. Otherwise, return the URL of the image
        :return: The url of the image.
        """
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    """customer can have multiple orders
     This is creating a foreign key relationship between the Order model and the Customer model."""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        """
        The __str__ function is a special function that is called when you call str() on an object
        :return: The id of the object.
        """
        return str(self.id)


    @property
    def get_cart_total(self):
        """
        It gets all the order items associated with the order, and then sums up the total of each item
        :return: The total of the order items.
        """
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        """
        It returns the total number of items in the cart
        :return: The total number of items in the cart.
        """
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def get_order_amounts(self):
        """
        It returns the number of order items associated with a particular order
        :return: The number of items in the order.
        """
        order_items = self.orderitem_set.all()
        return len(order_items)



class OrderItem(models.Model):
    """Creating a foreign key relationship between the OrderItem model and the Product model."""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        """
        It returns the total price of the product by multiplying the price of the product by the quantity of the product
        :return: The total price of the product.
        """
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    """ Creating a foreign key relationship between the ShippingAddress model and the Customer model."""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        The __str__ function is a special function that is called when you print an object
        :return: The address of the location.
        """
        return self.address


