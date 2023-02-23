from models.factory import host

import shared.hosts

host1 = host("10.0.1.10", shared.hosts.special)
host2 = host("10.0.1.11")
