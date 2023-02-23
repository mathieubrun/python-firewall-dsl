
from models.factory import group, host
import shared.hosts

host1 = host("10.0.0.10", shared.hosts.special)
host2 = host("10.0.0.11")
host3 = host("10.0.0.12")

group1 = group("group of a", [host1, host2])
