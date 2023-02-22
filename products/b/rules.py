from models.rule import rule, rules

import products.a.hosts
import products.a.rules
import products.b.hosts
import shared.services
import shared.firewalls

rules([
    rule(
        name="ssh rule",
        sources=[
            products.a.hosts.host1
        ],
        destinations=[
            products.b.hosts.host2
        ],
        services=[
            shared.services.ssh
        ]
    ),

    rule(
        name="ftp rule",
        sources=[
            products.a.hosts.host2
        ],
        destinations=[
            products.b.hosts.host2
        ],
        services=[
            shared.services.ftp
        ]
    )],
    firewall = shared.firewalls.fw2
)
