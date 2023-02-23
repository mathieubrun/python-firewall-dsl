from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Host:
    ip: str

    def __str__(self) -> str:
        return self.ip