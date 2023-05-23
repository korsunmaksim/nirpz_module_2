import pytest 
from gallery.models import Category,Image


def test_case_1():
    cat1=Category.objects.filter(pk=1).first()
    assert cat1=={"id":1,"name":"Nature"}
    
def test_case_2():
    cat1=Category.objects.filter(pk=2).first()
    assert cat1=={"id":2,"name":"Music"}
