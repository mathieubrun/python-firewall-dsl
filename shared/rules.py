from models.factory import rule, rules

import shared.hosts
import shared.services

rules([
    rule(
        name="special",
        sources=[
            shared.hosts.special
        ],
        destinations=[
            shared.hosts.special
        ],
        services=[
            shared.services.all
        ]
    )],
    firewall = shared.firewalls.fw1
)
