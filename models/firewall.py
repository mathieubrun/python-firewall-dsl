from dataclasses import dataclass, field
from typing import List

@dataclass
class Firewall:
    name: str
    rules: List = field(default=None)