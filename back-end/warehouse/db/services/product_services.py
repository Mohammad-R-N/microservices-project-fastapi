from models.products import Product


def product_format(pk: str):
    product = Product.get(pk)
    return {
        "pk": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }
