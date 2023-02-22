from dataclasses import dataclass
from typing import List

from models.host import Host
from models.service import Service

@dataclass
class Rule:
    name: str
    sources: List[Host]
    destinations: List[Host]
    services: List[Service]
