import random
import json
import os
#Ci-dessus on importe les différents modules qui nous seront utiles

def main(): #La fonction principale qui s'occupera de tout le jeu
    MIN_RAND = 0
    MAX_RAND = 100
    score = {}
    userGuess = None
    nb = 0
    tries = 0
    finalScore = {}
    randomNb = random.randrange(MIN_RAND,MAX_RAND) #L'ordinateur choisit un chiffre au hasard entre 0 et 100
    print("Higher and Lower game, try to guess the number")
    name = input("Enter your name please : ") #On demande le nom du joueur
    #Ci-dessus on initialise nos variables

    while userGuess != randomNb: #Lorsque le chiffre donné par le joueur est faux alors on rajoute + 1 au nombre total de coups joués
        tries = tries + 1
        userGuess = int(input("Your guess : "))
        if userGuess > MAX_RAND: #Si le joueur écrit un chiffre au-dessus de 100 l'ordinateur lui demande d'écrire entre 0 et 100
                print("Try between " + str(MIN_RAND) + " and " + str(MAX_RAND) + ", it will work better")
        elif userGuess < MIN_RAND: #Si le joueur écrit un chiffre en-dessous de 0 l'ordinateur lui demande d'écrire entre 0 et 100
                print("Try between " + str(MIN_RAND) + " and " + str(MAX_RAND) + ", it will work better")
        elif userGuess < randomNb: #Si le joueur donne un chiffre inférieur au chiffre de l'ordinateur ce dernier lui répond que le chiffre à trouver est plus grand
                print("It's higher")
        elif userGuess > randomNb: #Si le joueur donne un chiffre supérieur au chiffre de l'ordinateur ce dernier lui répond que le chiffre à trouver est plus petit
                print("It's lower")

    finalScore = {str(name): int(tries)} #Le score final avec le nom et le total de coups joués pour deviner le chiffre de l'ordinateur

    if not os.path.isfile("highscores.json"): #Si il n'y a pas de fichier JSON sur l'ordinateur avec le nom "highscores" alors on en crée un
            with open("highscores.json", 'w') as f_write: #On ouvre le fichier en mode écriture et on lui écrit le nom du joueur et son score
                    f_write.write(json.dumps(finalScore, indent=4, separators=(',', ': ')))
    else: #Sinon, si le fichier est déjà existant
            with open("highscores.json") as f: #On l'ouvre
                    score = json.load(f)
            
            score[str(name)] = int(tries)
            with open("highscores.json", "w") as f_write: #On l'ouvre en mode écriture et on lui écrit le nom du joueur et son score
                    f_write.write(json.dumps(score, indent=4, separators=(',', ': ')))
                    f_write.close() #On arrête d'écrire
                    print(finalScore) #On écrit le score final
                    print(score) #On écrit les scores de tous les joueurs
                    again() #On lance notre fonction qui va demander si l'on veut rejouer ou non
        
# Todo: trier le tableau en fonction des scores



def again(): #La fonction qui va nous permettre de relancer la partie si on le souhaite
    again=str(input("Do you want to play again ? (yes/no) :"))         
    if again == "yes": #Si la réponse est "yes" on relance la fonction principale
        print("Let's go again !")
        main() 
    elif again == "no": #Si la réponse est "no" on arrête le programme
        print("Thanks for playing.")          
    else: #Si on ne marque pas "yes" ou "no" ça ne fonctionne pas, donc on redemande d'écrire "yes" ou "no"
        again=str(input("Answer with yes or no :"))

   
main() #On lance notre fonction principale
