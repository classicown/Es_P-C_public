# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_main_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Formulaire" in response.data.decode('utf-8')  # Décodage en UTF-8

def test_resultat_correct(client):
    response = client.post('/resultat', data={'reponse1': 'Oui', 'reponse2': 'Oui'})
    assert response.status_code == 200
    assert "resultat.html" in response.data.decode('utf-8')  # Décodage en UTF-8

def test_resultat_incorrect(client):
    response = client.post('/resultat', data={'reponse3': 'Oui'})
    assert response.status_code == 200
    assert "Vous avez faux" in response.data.decode('utf-8')  # Décodage en UTF-8

def test_missing_answers(client):
    response = client.post('/resultat', data={})
    assert response.status_code == 400
    assert "Veuillez répondre à toutes les questions." in response.data.decode('utf-8')  # Décodage en UTF-8
