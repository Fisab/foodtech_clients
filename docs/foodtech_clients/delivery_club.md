# Delivery Club

> Auto-generated documentation for [foodtech_clients.delivery_club](../../foodtech_clients/delivery_club.py) module.

- [Foodtech_clients](../README.md#foodtech) / [Modules](../MODULES.md#foodtech_clients-modules) / [Foodtech Clients](index.md#foodtech-clients) / Delivery Club
    - [DeliveryClubClient](#deliveryclubclient)
        - [DeliveryClubClient().get_last_order](#deliveryclubclientget_last_order)
        - [DeliveryClubClient().get_orders](#deliveryclubclientget_orders)
        - [DeliveryClubClient().get_user](#deliveryclubclientget_user)
        - [DeliveryClubClient().refresh_token](#deliveryclubclientrefresh_token)

## DeliveryClubClient

[[find in source code]](../../foodtech_clients/delivery_club.py#L11)

```python
class DeliveryClubClient():
    def __init__(refresh_token: str, token: str, secret: str, url: str):
```

### DeliveryClubClient().get_last_order

[[find in source code]](../../foodtech_clients/delivery_club.py#L78)

```python
async def get_last_order(active: bool = False) -> dict:
```

### DeliveryClubClient().get_orders

[[find in source code]](../../foodtech_clients/delivery_club.py#L70)

```python
async def get_orders(
    offset: Optional[int] = 0,
    limit: Optional[int] = 5,
) -> list:
```

### DeliveryClubClient().get_user

[[find in source code]](../../foodtech_clients/delivery_club.py#L67)

```python
async def get_user() -> dict:
```

### DeliveryClubClient().refresh_token

[[find in source code]](../../foodtech_clients/delivery_club.py#L18)

```python
async def refresh_token():
```
