from dataclasses import asdict, dataclass, field
from typing import List, Optional

from models.group import Group
from models.rule import Rule

@dataclass
class Firewall:
    name: str
    rules: Optional[List[Rule]] = field(default_factory=list)

    def dependencies(self):
        dependencies = set()
        for rule in self.rules:
            for targets in [rule.sources, rule.destinations, rule.services]:
                for target in targets:
                    if isinstance(target, Group):
                        dependencies.add(target.freeze())
                        dependencies = dependencies.union(target.dependencies())
                    else:
                        dependencies.add(target)
        return dependencies