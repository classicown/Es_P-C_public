# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    # Configure Flask pour le mode test
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_main_page(client):
    """Teste si la page d'accueil se charge correctement"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Formulaire" in response.data  # Remplacez "Formulaire" par du texte présent dans votre template

def test_resultat_correct(client):
    """Teste le cas où les réponses 1 et 2 sont cochées"""
    response = client.post('/resultat', data={'reponse1': 'Oui', 'reponse2': 'Oui'})
    assert response.status_code == 200
    assert b"resultat.html" in response.data  # Vérifiez la réponse de succès

def test_resultat_incorrect(client):
    """Teste le cas où les réponses 3 ou 4 sont cochées, donc résultat incorrect"""
    response = client.post('/resultat', data={'reponse3': 'Oui'})
    assert response.status_code == 200
    assert b"Vous avez faux" in response.data

def test_missing_answers(client):
    """Teste le cas où toutes les réponses ne sont pas cochées"""
    response = client.post('/resultat', data={})
    assert response.status_code == 400
    assert b"Veuillez répondre à toutes les questions." in response.data
