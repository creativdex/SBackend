from httpx import AsyncClient
from app.config import settings


class Bitrix:
    @staticmethod
    async def get_type_of_problem():
        url = settings.BITRIX_WEBHOOK
        query = "crm.item.fields"
        data = {"entityTypeId": "184"}
        async with AsyncClient() as client:
            response = await client.post(url=url + query, data=data)
        result = response.json()
        type_of_problem = [
            *result["result"]["fields"]["ufCrm10_1644911192216"]["items"]
        ]
        for item in type_of_problem:
            item["id"] = int(item.pop("ID"))
            item["name"] = item.pop("VALUE")
        return type_of_problem
