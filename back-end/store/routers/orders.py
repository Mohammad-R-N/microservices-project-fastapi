from fastapi import APIRouter
import requests
from models.orders import ProductOrder, Order
from db.services import order_services

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("")
def create_order(product_order: ProductOrder):
    request = requests.get(f"http://127.0.0.1:7000/product/{product_order.product_id}")
    product = request.json()
    fee = product["price"] * 0.2
    order = Order(
        product_id=product_order.product_id,
        price=product["price"],
        fee=fee,
        total=product["price"] + fee,
        quantity=product_order.quantity,
        status="pending",
    )
    return order.save()


@router.get("/all")
def get_all_orders():
    return [order_services.order_format(pk) for pk in Order.all_pks()]


@router.get("/{pk}")
def get_order(pk: str):
    return order_services.order_format(pk)
