import aiohttp
from aiohttp.web_exceptions import HTTPUnauthorized, HTTPOk
from furl import furl
from typing import Optional
import logging


logger = logging.getLogger(__name__)


class DeliveryClubClient:
    def __init__(self, refresh_token: str, token: str, secret: str, url: str):
        self._refresh_token = refresh_token
        self._token = token
        self._secret = secret
        self.base_url = url

    async def refresh_token(self):
        url = furl(self.base_url) / 'user/login'
        json = {
            'refresh_token': self._refresh_token,
        }
        response = await self._query('POST', url, json=json)
        data = await response.json()

        self._token = data['token']
        self._secret = data['secret']
        self._refresh_token = data['refresh_token']

        logger.info('Successfully refreshed token')

    @staticmethod
    async def _query(
        method: str,
        url: furl,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.request(
                method, url.tostr(), params=params, json=json, headers=headers
            )

    async def _api_query(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        recall: Optional[bool] = False,
    ) -> dict:
        url = furl(self.base_url) / endpoint
        headers = {
            'x-user-authorization': f'{self._token}.{self._secret}',
        }

        response = await self._query(method, url, params, json, headers=headers)
        if response.status == HTTPUnauthorized.status_code and recall is False:
            logger.info('Refreshing token')
            await self.refresh_token()
            return await self._api_query(method, endpoint, params, json, recall=True)
        if response.status != HTTPOk.status_code:
            raise Exception(response.status)
        return await response.json()

    async def get_user(self) -> dict:
        return await self._api_query('GET', 'user', {})

    async def get_orders(
        self, offset: Optional[int] = 0, limit: Optional[int] = 5
    ) -> list:
        orders = await self._api_query(
            method='GET', endpoint='orders', params={'offset': offset, 'limit': limit}
        )
        return orders.get('items', [])

    async def get_last_order(self, active: bool = False) -> dict:
        orders = await self.get_orders(offset=0, limit=1)
        if len(orders):
            order = orders[0]
            order_status = order['status']['name']['short']
            if order_status != 'Доставлен' or not active:
                return order
