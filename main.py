# Projet Questionnaire V2
def poser_question(question, choix):

    print("QUESTION: ", question["titre"])

    for i in range(len(choix)):
        print(f" {i+1}-", choix[i])


def demander_reponse(min, max):
    reponse_str = input(f"Entrez votre reponse (entre {min} et {max}) : ")

    try:
        reponse_int = int(reponse_str)
        
        if min<= reponse_int <= max:
          return reponse_int
        
        print(f"ERREUR : Veuillez entrer un chiffre entre {min} et {max}")
    except:
        print("ERREUR : Veuillez entrez un chiffre")


def lancer_questionnaire(questionnaire):

    score = 0

    for i in range(len(questionnaire)):

        question = questionnaire[f"question{i+1}"]
        choix = question["choix"]
        bonne_reponse = question["bonne_reponse"]

        poser_question(question, choix)
        reponse = demander_reponse(1, len(choix))

        if choix[reponse-1] == bonne_reponse:
            score += 1
            print("Bonne reponse")
        else:
            print("Mauvaise reponse")

    print(f"Score finale: {score} / {len(questionnaire)}")

#--------------------QUESTIONNAIRE-----------------------
questionnaire = {
    "question1":{"titre":"Capitale de la France ?", "choix":("Marseille", "Lyon", "Paris", "Nice"), "bonne_reponse":"Paris"},
    "question2":{"titre":"Capitale de l'Italie' ?", "choix":("Rome", "Venise", "Pise", "Florence"), "bonne_reponse":"Rome"},
    "question3":{"titre":"Capitale d'Angleterre'' ?", "choix":("Manchester", "Bistrol", "Birmingham", "Londre"), "bonne_reponse":"Londre"}
}

lancer_questionnaire(questionnaire)
