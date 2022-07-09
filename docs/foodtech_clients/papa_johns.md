# Papa Johns

> Auto-generated documentation for [foodtech_clients.papa_johns](../../foodtech_clients/papa_johns.py) module.

- [Foodtech_clients](../README.md#foodtech) / [Modules](../MODULES.md#foodtech_clients-modules) / [Foodtech Clients](index.md#foodtech-clients) / Papa Johns
    - [PapaJohnsClient](#papajohnsclient)
        - [PapaJohnsClient().check_goods_in_stock](#papajohnsclientcheck_goods_in_stock)
        - [PapaJohnsClient().get_delivery_time](#papajohnsclientget_delivery_time)
        - [PapaJohnsClient().get_goods_out_of_stock](#papajohnsclientget_goods_out_of_stock)
        - [PapaJohnsClient().init_cart](#papajohnsclientinit_cart)

## PapaJohnsClient

[[find in source code]](../../foodtech_clients/papa_johns.py#L6)

```python
class PapaJohnsClient():
    def __init__(url: str, city_id: int, restaurant_id: int):
```

### PapaJohnsClient().check_goods_in_stock

[[find in source code]](../../foodtech_clients/papa_johns.py#L48)

```python
async def check_goods_in_stock(good_id: int) -> bool:
```

### PapaJohnsClient().get_delivery_time

[[find in source code]](../../foodtech_clients/papa_johns.py#L52)

```python
async def get_delivery_time(location: tuple) -> str:
```

#### Returns

примерное время доставки

### PapaJohnsClient().get_goods_out_of_stock

[[find in source code]](../../foodtech_clients/papa_johns.py#L32)

```python
async def get_goods_out_of_stock(goods_to_check: list) -> list[int]:
```

#### Returns

массив из id отсутствующих товаров в корзине

### PapaJohnsClient().init_cart

[[find in source code]](../../foodtech_clients/papa_johns.py#L20)

```python
async def init_cart(goods_to_check: list) -> str:
```
