from loguru import logger
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from category.converters import convert_category_query_params_to_vo
from category.serializers import CategorySerializer
from category.service import CategoryService
from category.value_objects import CategoryQueryParamsVo


class CategoryView(APIView):
    @staticmethod
    def get(request: Request, id_: int | None = None):
        logger.debug(f"{id_=}")
        logger.debug(f"{request.query_params=}")

        query_params_vo: CategoryQueryParamsVo = convert_category_query_params_to_vo(id_=id_)
        logger.debug(f"{query_params_vo=}")
        categories = CategoryService.get(query_params_vo)
        if isinstance(categories, list):
            logger.info(f"found {len(categories)} items")
            serializer = CategorySerializer(categories, many=True)
        else:
            logger.info("found 1 item")
            serializer = CategorySerializer(categories)
        return Response(serializer.data, status=200)
