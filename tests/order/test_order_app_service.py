import pytest
from unittest.mock import MagicMock
from app.order.order_app_service import OrderAppService
from app.order.order import OrderItem
from app.product.core.product import Product

def test_create_order_success():
    mock_order_service = MagicMock()
    mock_product_service = MagicMock()

    product = Product(
        id=1,
        name="Test Product"
    )

    mock_product_service.get_by_id.return_value = product

    order_data = {
        "customer": "Jan Kowalski",
        "address": "Testowa 1",
        "phone_number": "123456789",
        "products": [
            {"product_id": 1, "quantity": 2}
        ]
    }

    user = MagicMock()

    service = OrderAppService(
        order_service=mock_order_service,
        product_service=mock_product_service
    )

    order = service.create_order(order_data, user)

    assert order.customer == "Jan Kowalski"
    assert order.address == "Testowa 1"
    assert order.phone_number == "123456789"
    assert order.user == user

    assert len(order.items) == 1

    item = order.items[0]
    assert isinstance(item, OrderItem)
    assert item.product == product
    assert item.quantity == 2

    mock_product_service.get_by_id.assert_called_once_with(1)
    mock_order_service.save.assert_called_once_with(order)

def test_create_order_product_not_found():
    mock_order_service = MagicMock()
    mock_product_service = MagicMock()

    mock_product_service.get_by_id.return_value = None

    service = OrderAppService(
        order_service=mock_order_service,
        product_service=mock_product_service
    )

    order_data = {
        "customer": "Jan Kowalski",
        "address": "Testowa 1",
        "phone_number": "123456789",
        "products": [
            {"product_id": 999, "quantity": 1}
        ]
    }

    user = MagicMock()

    with pytest.raises(ValueError) as exc:
        service.create_order(order_data, user)

    assert "Produkt o id 999 nie istnieje" in str(exc.value)
    mock_order_service.save.assert_not_called()
