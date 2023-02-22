from dataclasses import dataclass


@dataclass
class Service:
    port: int
    name: str