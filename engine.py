
# a matching engine

import random
import lob 
import logging

from collections import defaultdict

# engine has a few functions
# submit
# cancel
# getbook

logging.getLogger().setLevel(logging.DEBUG)

# two major data structures
# <SYM><PRC> --> List of Orders
# <ID> --> Order 

idmap = {}
symprc = defaultdict(lambda:defaultdict(list))

# implementations
def mkid():
  """ generates a unique order id for each order """
  return random.randint(10,1000000000)

def do_fills(o):
  """ walk the price level of this order, crossing this order against any opposite side orders"""
  # here we are...  XXXX
  # return o, True if the order survives and posts into the order book

def true_submit(order):
  """ submit the order """
  o = lob.Order(mkid(),order.sym,order.side,order.qty,order.prc,order.cb)
  if o.orderid in idmap:
    raise RuntimeError("dup order? %s" % o.orderid)
  # add to the order map
  o,posts = do_fills(o)
  if posts:
    idmap[o.orderid] = o  
    symprc[o.sym][o.prc].append(o)
  return o
  
def true_cancel(cancel):
  if not cancel.orderid in idmap:
    raise RuntimeError("unknown id! %s" % o.orderid)
  o = idmap[cancel.orderid]
  symprc[o.sym][o.prc] = [x for x in symprc[o.sym][o.prc] if not x.orderid == cancel.orderid]
  del idmap[o.orderid]
  assert(not o.orderid in idmap)

def submit_with_random_fill(order):
  """ test method, accept order, return with id, randomly filling some of them """
  o = lob.Order(mkid(),order.sym,order.side,order.qty,order.prc,order.cb)
  if random.randint(0,10)>3:
    f = lob.Fill(o.orderid,o.qty,o.prc)
    order.cb(f)
  logging.info(order)
  return o

def log_cancel(cancel):
  """ log only cancel """
  logging.info("[CX] %s" % cancel)

# ========== official defs ===========
# redirects to the implementations above
def submit(order):
  #submit_with_random_fill(order)
  return true_submit(order)

def cancel(cancel):
  return true_cancel(cancel)

def getbook(sym):
  """ for the sym, loop over the prices and the orders at the prices """
  for p in symprc[sym]:
    logging.info("@ %s" % p)
    qty = 0 
    for o in symprc[sym][p]:
      qty += o.qty 
      logging.info("\t %s" % str(o))
    logging.info("T. Qty %s" % qty)
   
