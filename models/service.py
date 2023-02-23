from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Service:
    port: int
    name: str

    def __str__(self) -> str:
        return self.name