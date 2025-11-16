import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    
    @pytest.fixture
    def mock_bun(self):
        mock = Mock()
        mock.get_name.return_value = 'Бриошь'
        mock.get_price.return_value = 100  # Возвращает число, а не Mock
        return mock
    
    @pytest.fixture
    def mock_ingredient(self):
        mock = Mock()
        mock.get_type.return_value = 'SAUCE'
        mock.get_name.return_value = 'Соус'
        mock.get_price.return_value = 50  # Возвращает число, а не Mock
        return mock
    
    def test_set_buns_sets_bun_correctly(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient_adds_ingredient_to_list(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient_removes_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    
    def test_move_ingredient_changes_position(self, mock_ingredient):
        burger = Burger()
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 75
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient
    
    def test_get_price_calculates_correct_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        # Цена: булки (100 * 2) + ингредиент (50) = 250
        assert burger.get_price() == 250
    
    def test_get_receipt_returns_correct_format(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        assert isinstance(receipt, str)
        assert 'Бриошь' in receipt
        assert 'Соус' in receipt
        assert 'Price: 250' in receipt
