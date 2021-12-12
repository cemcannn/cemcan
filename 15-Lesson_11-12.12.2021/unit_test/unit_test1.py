## installation
## linux - mac : pip3 install pytest
## windows:  pip install pytest

##################################3 basit ornek

import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def test_square():
   num = 7
   assert 7*7 == 40

def test_equality():
   assert 10 == 11




