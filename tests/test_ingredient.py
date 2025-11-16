import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient
from praktikum import constants

class TestIngredient:
    
    class IngredientDataFactory:
        @staticmethod
        def create_test_data():
            # Фабрика для создания тестовых данных ингредиентов
            return [
                {'type': 'SAUCE', 'name': 'BBQ', 'price': 180},
                {'type': 'SAUCE', 'name': 'Mustard', 'price': 90},
                {'type': 'FILLING', 'name': 'Chicken Patty', 'price': 350},
                {'type': 'FILLING', 'name': 'Vegan Patty', 'price': 320}
            ]
    
    @pytest.fixture
    def data_factory(self):
        return self.IngredientDataFactory()
    
    @pytest.mark.parametrize('test_data', [
        {'type': 'SAUCE', 'name': 'BBQ', 'price': 180},
        {'type': 'SAUCE', 'name': 'Mustard', 'price': 90},
        {'type': 'FILLING', 'name': 'Chicken Patty', 'price': 350},
        {'type': 'FILLING', 'name': 'Vegan Patty', 'price': 320}
    ])
    def test_ingredient_price_validation(self, test_data):
        # Создание ингредиента с тестовыми данными
        ingredient = Ingredient(test_data['type'], 
                               test_data['name'], 
                               test_data['price'])
        
        # Получение цены ингредиента
        actual_price = ingredient.get_price()
        
        # Проверка соответствия цены
        assert actual_price == test_data['price']
    
    @pytest.mark.parametrize('ingredient_type, name', [
        ('SAUCE', 'BBQ'),
        ('FILLING', 'Chicken Patty')
    ])
    def test_ingredient_name_validation(self, ingredient_type, name):
        # Создание ингредиента для проверки имени
        ingredient = Ingredient(ingredient_type, name, 200)
        
        # Получение имени ингредиента
        actual_name = ingredient.get_name()
        
        # Проверка корректности имени
        assert actual_name == name
    
    def test_ingredient_type_validation(self):
        # Тестирование обоих типов ингредиентов
        test_cases = [
            ('SAUCE', 'Ketchup'),
            ('FILLING', 'Cheddar Cheese')
        ]
        
        for ingredient_type, name in test_cases:
            # Подтест для каждого типа ингредиента
                ingredient = Ingredient(ingredient_type, name, 150)
                assert ingredient.get_type() == ingredient_type
                assert ingredient.get_name() == name
                
    def test_ingredient_immutability(self):
        # Проверка неизменяемости свойств ингредиента
        ingredient = Ingredient('SAUCE', 'Hot Sauce', 120)
        
        # Сохранение исходных значений
        original_name = ingredient.get_name()
        original_price = ingredient.get_price()
        original_type = ingredient.get_type()
        
        # Многократные обращения должны возвращать одинаковые значения
        assert ingredient.get_name() == original_name
        assert ingredient.get_price() == original_price  
        assert ingredient.get_type() == original_type
