from pydantic import BaseModel


class InputSchemas(BaseModel):
    __root__: dict[str, str]


class GuidIrl(BaseModel):
    guid: str
    url: str


class SpecSchemas(BaseModel):
    key: str
    value: str


class OutputSchemas(BaseModel):
    __root__: dict[str, list[SpecSchemas]]


class Splash(BaseModel):
    url: str
    html: str = "1"
    http2: str = "1"
    wait: str = "0.5"
    headers: dict | None
