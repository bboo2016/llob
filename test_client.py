
import random
import lob
from lob import Side,Cancel
import logging

def on_fill_print(fill):
  logging.info(fill)

def place_ten():
  """ place test orders """
  for i in range(1000):
    q = random.randint(10,20)
    p = round(random.random()*100,2)
    o = lob.Order(None,"ES",Side.Buy,20,10.10,on_fill_print)
    lob.submit(o)

def place_and_cancel():
  """ place one, then cancel it """
  q = random.randint(10,20)
  p = round(random.random()*100,2)
  o = lob.Order(None,"ES",Side.Buy,20,10.10,on_fill_print)
  o = lob.submit(o)
  lob.getbook("ES")
  logging.info("remove %s" % str(o))
  # TODO: just pass the order without this object wrapper?
  lob.cancel(Cancel(o.orderid))
  lob.getbook("ES")
  
  
if __name__=="__main__":
  #place_ten()
  place_and_cancel()
