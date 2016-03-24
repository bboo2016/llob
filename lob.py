
# defines the lob interface
# data objects 
#   and 
# calls submit / cancel which are implemented in engine.py

from collections import namedtuple 
import random
import sys
import engine as e

from enum import Enum
class Side(Enum):
  Buy = 1
  Sell = 2

# data objects
# give an order with None id, get a copy back with an id
Order = namedtuple('Order', ['orderid','sym','side','qty','prc','cb'])
def print_order(self):
  return "O[%s] %s: %s %s@%s" % (self.orderid,self.sym,self.side,self.qty,self.prc)
Order.__str__ = print_order

Cancel = namedtuple('Cancel', ['orderid'])
def print_cancel(self):
  return "X[%s] " % (self.orderid)
Cancel.__str__ = print_cancel

Reject = namedtuple('Reject', ['orderid','msg'])
def print_reject(self):
  return "?![%s] %s " % (self.orderid,self.msg)
Reject.__str__ = print_reject

Fill = namedtuple('Fill', ['orderid','qty','prc'])
def print_fill(self):
  return "F[%s] %s@%s " % (self.orderid,self.qty,self.prc)
Fill.__str__ = print_fill

# the api
def submit(order):
   return e.submit(order)

def cancel(cancel):
  return e.cancel(cancel)

def getbook(sym):
  e.getbook(sym)

 
