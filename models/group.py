from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class FrozenGroup:
    name: str
    members: tuple

    def __str__(self) -> str:
        return self.name

@dataclass
class Group:
    name: str
    members: set

    def __str__(self) -> str:
        return self.name
    
    def dependencies(self):
        dependencies = set()
        for m in self.members:
            dependencies.add(m)
        return dependencies

    def freeze(self):
        return FrozenGroup(self.name, tuple(self.members))