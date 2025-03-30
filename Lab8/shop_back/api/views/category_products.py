from loguru import logger
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from product.converters import convert_product_query_params_to_vo
from product.serializers import ProductSerializer
from product.service import ProductService


class CategoryProductView(APIView):
    @staticmethod
    def get(request: Request, id_: int | None = None):
        logger.debug(f"{id_=}")
        logger.debug(f"{request.query_params=}")

        query_params_vo = convert_product_query_params_to_vo(category_id=id_)
        logger.debug(f"{query_params_vo=}")

        products = ProductService.get(query_params_vo)
        if isinstance(products, list):
            logger.debug(f"found {len(products)} items")
            serializer = ProductSerializer(products, many=True)
        else:
            logger.info("found 1 item")
            serializer = ProductSerializer(products)
        return Response(serializer.data, 200)
