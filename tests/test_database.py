import pytest
from praktikum.database import Database

class TestDatabase:
    
    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        # Если метод возвращает непустой список
        if len(buns) > 0:
            assert hasattr(buns[0], 'get_name')
            assert hasattr(buns[0], 'get_price')
    
    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        # Если метод возвращает непустой список
        if len(ingredients) > 0:
            assert hasattr(ingredients[0], 'get_type')
            assert hasattr(ingredients[0], 'get_name')
            assert hasattr(ingredients[0], 'get_price')
