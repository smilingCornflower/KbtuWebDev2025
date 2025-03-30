from dataclasses import dataclass

from common.value_objects import QueryParamsVo


@dataclass
class ProductQueryParamsVo(QueryParamsVo):
    category_id: int | None = None

