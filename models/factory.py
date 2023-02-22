import inspect

from typing import List
from models.firewall import Firewall
from models.rule import Rule

rules =  []

def rule(**args):
    stk = inspect.stack()[1]
    mod = inspect.getmodule(stk[0])
    print(f"creating rule for {mod.__name__}")
    r = Rule(**args)
    return r
    
def rules(rs: List[Rule], firewall: Firewall):
    firewall.rules = rs