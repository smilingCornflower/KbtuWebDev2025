from dataclasses import dataclass
from typing import Self
from uuid import UUID


@dataclass(frozen=True)
class Id:
    value: UUID

    @classmethod
    def from_string(cls, id_str: str) -> Self:
        try:
            return cls(UUID(id_str))
        except ValueError as e:
            raise ValueError(f"Invalid ID: {id_str}") from e

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class CompanyId(Id):
    pass


@dataclass(frozen=True)
class VacancyId(Id):
    pass
