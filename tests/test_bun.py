import pytest
from praktikum.bun import Bun

class TestBun:
    
    @pytest.mark.parametrize('name, price', [
        ('Бриошь', 100),
        ('Краторная булка', 125), 
        ('Грибная булка', 88)
    ])
    def test_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize('name, price', [
        ('Бриошь', 100),
        ('Краторная булка', 125),
        ('Грибная булка', 88)
    ])
    def test_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
    
    def test_bun_creation_with_minimal_data(self):
        bun = Bun('Minimal', 1)
        assert bun.get_name() == 'Minimal'
        assert bun.get_price() == 1
    
    def test_bun_attributes_consistency(self):
        bun_name = 'Test Bun'
        bun_price = 150
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name
        assert bun.get_name() == bun_name
        assert bun.get_price() == bun_price
        assert bun.get_price() == bun_price
