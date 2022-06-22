from .helpers import Cart


def cart(request):
    return {'cart': Cart(request)}
