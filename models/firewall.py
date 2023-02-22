from dataclasses import dataclass, field
from typing import List, Optional

from models.rule import Rule

@dataclass
class Firewall:
    name: str
    rules: Optional[List[Rule]] = field(default_factory=list)