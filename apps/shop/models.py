from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    PRODUCT_CATEGORIES = (
        ("1", "Computers"),
        ("2", "Laptops"),
        ("3", "Cameras"),
        ("4", "Hardware"),
        ("5", "Smartphones"),
        ("6", "TV & Audio"),
        ("7", "Gadgets"),
        ("8", "Car Electronics"),
        ("9", "Videogames"),
        ("10", "Accessories"),
    )

    PRODUCT_COLORS = (
        ("#000000", "Black"),
        ("#FFFFFF", "White"),
        ("#808080", "Gray"),
        ("#A52A2A", "Brown"),
        ("#FF0000", "Red"),
        ("#008000", "Green"),
        ("#0000FF", "Blue"),
        ("#FFFF00", "Yellow"),
    )

    category = models.CharField("Category", max_length=2, choices=PRODUCT_CATEGORIES)
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    price = models.PositiveIntegerField("Price")
    slug = models.SlugField(_("Url-label"), max_length=100, unique=True)
    color = models.CharField("Product color", max_length=7, choices=PRODUCT_COLORS)

    def __str__(self):
        return f"{self.name}_{self.get_color_display()}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Product")
    image = models.ImageField("Image", upload_to='product_images/', blank=True)


class Cart(models.Model):

    products = models.ManyToManyField(Product, through='CartLine', verbose_name='Products', blank=True)

    def get_total_cost(self):
        return sum(line.item.price * line.quantity for line in self.cartlines.all())

    def __str__(self):
        return "Cart ID # " + str(self.id)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartLine(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartlines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField("Quantity", default=1)

    def __str__(self):
        return "CartLine ID # " + str(self.id)

    class Meta:
        unique_together = (("cart", "product"),)
