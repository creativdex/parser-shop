from fastapi import APIRouter, HTTPException
from schemas import OutputSchemas, InputSchemas, SpecSchemas
from parser_shop import Parser
from pydantic import parse_obj_as


router = APIRouter()


@router.post("/get_spec_dns", response_model=list[OutputSchemas])
async def get_spec_dns(body: list[InputSchemas]):
    async with Parser() as parser:
        result_list = []
        for item in body:
            guid_url = await parser.guid_url(item)
            try:
                guid_url.url = await parser.check_url_dns(guid_url.url)
            except Exception:
                raise HTTPException(
                    422,
                    detail={
                        "err": "Не верный URL",
                    },
                )
            try:
                page = await parser.get_page(guid_url.url)
            except Exception:
                raise HTTPException(
                    400,
                    detail={
                        "err": "Не удалось получить страницу",
                    },
                )
            spec = await parser.get_spec_dns(page)
            conv = parse_obj_as(list[SpecSchemas], spec)
            result = {guid_url.guid: conv}
            result_list.append(result)
        return result_list
