from httpx import AsyncClient
from app.config import settings
from app.schemas.appeal import Appeal
from datetime import date


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

    @staticmethod
    async def send_appeal_to_bx(appeal: Appeal):
        url = settings.BITRIX_WEBHOOK
        query = "crm.item.add"
        text = (
            f"{appeal.division.name}\n\
            {appeal.user.name}\n\
            {appeal.user.phone}\n\
            {appeal.type_of_problem.name}\n\
            {appeal.description}",
        )
        data = {
            "entityTypeId": "184",
            "fields": {
                "title": appeal.division.name,
                "createdBy": "466",  # Пользователь автор в BX
                "ufCrm10_1644911192216": appeal.type_of_problem.id,
                "ufCrm10_1644926802": f"{date.today()}",  # noqa TODO устанавливать в базе и забирать от туда 
                "ufCrm10_1644927739266": "162",  # Кого касается инцедент
                "ufCrm10_1644926433": text,
                "ufCrm10_1651723524": appeal.user.name,
                "ufCrm10_1644926079790": appeal.files,
            },
        }
        async with AsyncClient() as client:
            response = await client.post(url=url + query, data=data)
        return response.json()
