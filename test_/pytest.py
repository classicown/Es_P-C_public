# tests/test_baseserv.py
import pytest
from baseserv import app  # Assurez-vous que l'application Flask est bien importée depuis baseserv.py
@pytest.fixture
def client():
    """Fixture qui initialise un client de test pour Flask"""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_main_page(client):
    """Teste si la page d'accueil se charge correctement"""
    response = client.get('/')
    assert response.status_code == 200
    assert "Formulaire" in response.data.decode('utf-8')  # .decode('utf-8') pour traiter la réponse en chaîne

def test_resultat_correct(client):
    """Teste le cas où les réponses 1 et 2 sont cochées"""
    response = client.post('/resultat', data={'reponse1': 'Oui', 'reponse2': 'Oui'})
    assert response.status_code == 200
    assert "resultat.html" in response.data.decode('utf-8')

def test_resultat_incorrect(client):
    """Teste le cas où les réponses 3 ou 4 sont cochées, donc résultat incorrect"""
    response = client.post('/resultat', data={'reponse3': 'Oui'})
    assert response.status_code == 200
    assert "Vous avez faux" in response.data.decode('utf-8')

def test_missing_answers(client):
    """Teste le cas où aucune réponse n'est cochée"""
    response = client.post('/resultat', data={})
    assert response.status_code == 400
    assert "Veuillez répondre à toutes les questions." in response.data.decode('utf-8')
