import aiohttp
from furl import furl
from typing import Optional


class PapaJohns:
    def __init__(self, url: str, city_id: int, restaurant_id: int):
        self.base_url = url
        self.city_id = city_id
        self.restaurant_id = restaurant_id

    @staticmethod
    async def _query(
        url: furl, method: Optional[str] = 'GET', json: Optional[dict] = None
    ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url.tostr(), json=json) as response:
                return await response.json()

    async def init_cart(self, goods_to_check: list) -> str:
        url = furl(self.base_url) / '/cart/add'
        json = {
            'city_id': self.city_id,
            'composition': [
                {'good_id': good_id, 'ingredients': [], 'type': 'good'}
                for good_id in goods_to_check
            ],
        }
        response = await self._query(url, method='POST', json=json)
        return response.get('unauthorized_token')

    async def get_goods_out_of_stock(self, goods_to_check: list) -> list[int]:
        """
        :return: массив из id отсутствующих товаров в корзине
        """
        unauthorized_token = await self.init_cart(goods_to_check)
        url = furl(self.base_url) / '/cart/stop-list'
        url.add(
            {
                'city_id': self.city_id,
                'restaurant_id': self.restaurant_id,
                'unauthorized_token': unauthorized_token,
            }
        )
        response = await self._query(url)
        return [row.get('good') for row in response]

    async def check_goods_in_stock(self, good_id: int) -> bool:
        goods_out_of_stock = await self.get_goods_out_of_stock([good_id])
        return good_id not in goods_out_of_stock

    async def get_delivery_time(self, location: tuple) -> str:
        """
        :return: примерное время доставки
        """
        url = furl(self.base_url) / '/restaurant/delivery-time'
        url.add(
            {
                'city_id': self.city_id,
                'restaurant_id': self.restaurant_id,
                'address_coordinates': f'[{",".join(location)}]',
            }
        )
        response = await self._query(url)
        return response.get('delivery_time')
