from .models import Cart


def cart_processor(request):
    return {"cart": Cart.objects.first()}
