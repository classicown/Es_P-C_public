from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')  # Affichage de la page d'accueil
def main():
    return render_template("question_1.html", style="questiontheme1.css")

@app.route('/resultat', methods=['POST'])  # Affichage des résultats en utilisant la méthode POST
def resultat():
    # Récupération des réponses envoyées par le formulaire
    reponse1 = request.form.get('reponse1')  # Utilisation de .get() pour éviter les erreurs si la clé n'existe pas
    reponse2 = request.form.get('reponse2')
    reponse3 = request.form.get('reponse3')
    reponse4 = request.form.get('reponse4')

    # Affichage des valeurs dans la console pour déboguer
    print(f"Réponse 1: {reponse1}")
    print(f"Réponse 2: {reponse2}")

    # Vérification si certaines réponses ont été cochées
    if reponse3 or reponse4:
        return"Vous avez faux"
    elif reponse1 and reponse2:  # Si les deux réponses sont présentes
        return render_template('resultat.html',style="questiontheme1.css", reponse1=reponse1,reponse2=reponse2)
    else:
        return "Veuillez répondre à toutes les questions.", 400  # Retourne une erreur si une des réponses est manquante

if __name__ == '__main__':
    app.run(debug=True)
