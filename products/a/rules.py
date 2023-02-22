from models.rule import rule, rules

import products.a.hosts
import products.b.hosts
import products.b.rules
import shared.services
import shared.firewalls

rules([
    rule(
        name="first rule",
        sources=[
            products.a.hosts.host1
        ],
        destinations=[
            products.b.hosts.host2
        ],
        services=[
            shared.services.ssh
        ]
    )],
    firewall = shared.firewalls.fw1
)
