import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredientTypes:
    
    def test_sauce_type_exists(self):
        assert INGREDIENT_TYPE_SAUCE is not None
        assert isinstance(INGREDIENT_TYPE_SAUCE, str)
    
    def test_filling_type_exists(self):
        assert INGREDIENT_TYPE_FILLING is not None
        assert isinstance(INGREDIENT_TYPE_FILLING, str)
    
    def test_types_are_different(self):
        assert INGREDIENT_TYPE_SAUCE != INGREDIENT_TYPE_FILLING
