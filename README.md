# foodtech

На данный момент есть работа со следующими API:

### Delivery club
  - Получить историю заказов
  - Получить активный заказ (примерное время доставки, из какого ресторана был сделан заказ)

### Papa Johns
    - Примерное время доставки до точки
    - Определить наличие в определенном ресторане блюд


## Примеры работы:

### Delivery club

Информацию о `refresh_token`, `token`, `secret` можно вытащить при авторизации в веб-версии приложения

```python
from foodtech_clients import DeliveryClubClient
import asyncio

base_url = 'https://api.delivery-club.ru/api1.2'

client = DeliveryClubClient(
    refresh_token='',
    token='',
    secret='',
    url=base_url
)

last_active_order = asyncio.run(client.get_last_order(active=True))
```

### Papa Johns

```python
from foodtech_clients import PapaJohnsClient
import asyncio

base_url = 'https://api.papajohns.ru'
city_id = 10  # Москва
restaurant_id = 10
location = (  # куда доставлять заказ?
    '{широта}',
    '{долгота}'
)


client = PapaJohnsClient(
    url=base_url,
    city_id=city_id,
    restaurant_id=restaurant_id
)

delivery_time = asyncio.run(client.get_delivery_time(location))

```