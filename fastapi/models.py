import orjson as orjson
from pydantic import BaseModel


def orjson_dumps(data, *, default):
    # orjson.dumps возвращает bytes, а pydantic требует unicode,
    # поэтому декодируем
    return orjson.dumps(data, default=default).decode()


class Data(BaseModel):
    phone: str
    address: str

    class Config:
        # Заменяем стандартную работу с json на более быструю
        json_loads = orjson.loads
        json_dumps = orjson_dumps
