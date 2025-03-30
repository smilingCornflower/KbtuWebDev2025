from django.http import QueryDict

from category.value_objects import CategoryQueryParamsVo


def convert_category_query_params_to_vo(
        query_params: QueryDict | None = None,
        id_: int | None = None
) -> CategoryQueryParamsVo:
    return CategoryQueryParamsVo(id=id_)

