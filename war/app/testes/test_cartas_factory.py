import pytest
from unittest.mock import patch

from war.app.cartas_factory import CartasFactory
from war.app.cartas_repository import CartasRepository
from war.app.cartas_statagy import InsertStrategy, SelectStrategy
from war.app.cartas_objetivos import Objetivos
from war.app.cartas_territorio import CartasTerritorios


@patch('war.app.cartas_factory.CartasRepository')
@patch('war.app.cartas_factory.InsertStrategy')
@patch('war.app.cartas_factory.SelectStrategy')
def test_create_objetivos(mock_select_strategy, mock_insert_strategy, mock_cartas_repository):
    
    mock_insert = mock_insert_strategy.return_value
    mock_select = mock_select_strategy.return_value
    mock_repository = mock_cartas_repository.return_value

   
    objetivos = CartasFactory.create_objetivos('war/app/rsc/cartas_objetivos.json')

   
    mock_insert_strategy.assert_called_once()
    mock_select_strategy.assert_called_once()
    mock_cartas_repository.assert_called_once_with('objetivos', mock_insert, mock_select)

    
    assert isinstance(objetivos, Objetivos)
    assert mock_repository == mock_cartas_repository.return_value


@patch('war.app.cartas_factory.CartasRepository')
@patch('war.app.cartas_factory.InsertStrategy')
@patch('war.app.cartas_factory.SelectStrategy')
def test_create_cartas_territorios(mock_select_strategy, mock_insert_strategy, mock_cartas_repository):
   
    mock_insert = mock_insert_strategy.return_value
    mock_select = mock_select_strategy.return_value
    mock_repository = mock_cartas_repository.return_value

    
    cartas_territorios = CartasFactory.create_cartas_territorios('war/app/rsc/cartas_territorio.json')

   
    mock_insert_strategy.assert_called_once()
    mock_select_strategy.assert_called_once()
    mock_cartas_repository.assert_called_once_with('cartas_territorio', mock_insert, mock_select)

    assert isinstance(cartas_territorios, CartasTerritorios)
    assert mock_repository == mock_cartas_repository.return_value
