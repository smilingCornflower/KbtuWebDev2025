from domain.models.enums import SortDirection


class DjangoSortAdapter:
    @staticmethod
    def to_django(direction: SortDirection) -> str:
        return '-' if direction.DESCENDING else ''
