import inspect

from typing import List
from models.firewall import Firewall
from models.group import Group
from models.host import Host
from models.rule import Rule

rules =  []

def group(name: str, members: set = set()):
    return Group(name, members)

def host(ip: str, group: Group = None):
    h = Host(ip)
    if group:
        group.members.add(h)
    return h
    
def rule(**args):
    stk = inspect.stack()[1]
    mod = inspect.getmodule(stk[0])
    print(f"creating rule for {mod.__name__}")
    r = Rule(**args)
    return r
    
def rules(rs: List[Rule], firewall: Firewall):
    firewall.rules = rs