# #DEBUT
# # print ("BONJOUR MONDE")

# # def retournerSixPlusTrois():
# #     return 6+3
# # def retournerSixPlusX(x):
# #     return 6 + x

# # print(retournerSixPlusX(444444444444444444444444444444444444444444))
# #--------------------------------------------------------------------------------------------------
# # def add(x,y):
# #     return x+y

# # def sub(x,y):
# #     return x-y

# # def multiply(x,y):
# #     return x*y

# # def divide(x,y):
# #     return 

# # def modulo(x,y):
# #     return x%y

# def CalculsalaireSalaireSeconde(s,day,heur):
#     return (s/(day*max(0,min(heur,24))*3600))*12

# print(CalculsalaireSalaireSeconde(12000,235,8))


# def calculSS(Salaire,Jours,Heurs):
#     # return (Salaire * Jours * Jours)/(3600 * 24 * 365)
#     #Assigner SalaireAn, heur travailler / ans
#     SalaireAn = Salaire*Jours*Heurs
#     #Calculer nombre seconde/ans dans SecondeParAns
#     SecondeParAns = 60*60*24*365
#     #return SalireAn/SecondeParAns
#     return SalaireAn/SecondeParAns   

# # #caculer salaire net
# # def calculSN(SalaireBrut,coeff):
# #     #Assigner SalaireNet, par SalaireBrut*coeff
# #     SalaireNet = SalaireBrut*coeff
# #     #return SalireNet
# #     return SalaireNet
# #FIN
#  def withdrawFees(total,percent):
#      #calcul montant des taxes a retiré
#      fees = total*(percent/100)
#      #retourner la valuer totale moins les taxes
#      return total - fees

# def calculSN(SalaireBrut,public):
#     #calcul du salaire net par le salairebrut
#     # return withdrawFees(SalaireBrut, coeff)
#     if public == True:
#         return withdrawFees(SalaireBrut, 15)
#     else: 
#         return withdrawFees(SalaireBrut, 23)
#     #si j'occupe un poste de la fonction public
#     # alors je retourne le salaire brut - 15% de taxes
#     # sinon ? c'est que je travaille dans la fonction privait ! alors je retourne mon salaire brut - 23% de taxes

# def divide(x,y):
#     if y == 0:
#         print("impossible de divisé par 0")
#         return None
#     else:
#         return x/y


# def imput():
#     #renvoie un carractaire de type string aléatoire


# #création du jeu
# def jeu():
#     #demande joueur la lettre demandé
#     reponse = imput()
#     #Assigner char a la valeur de imput 
#     char = imput()
#     #répéter une boucle tant que char n'égale pas reponse
#     while (char != reponse):
#         #Assigner char a la valeur de imput
#         char = imput()
#     #si char égale réponse alors :
#     if (char == reponse):
#         #return et print "j'aime les dinosaure "
#         return print("JAIME LES DINOSAURES")


# initialisation de x
x=0
#création du jeux
def jeu1(x):
    #demande joueur la lettre demandé
    reponse = input("rentrez une lettre: ")
    #Assigner char a la valeur de imput 
    char ='h'
    #si char n'est pas égale a la réponse demander alors :
    if (char != reponse):
        # rajouté + 1 à x
        x = x+1
        # return a jeu 1 et envoyer x:
        return jeu1(x)
        # si char == reponse
    else:
        # assigner b a x pour sauvegardé le nombre de tour
        b = x
        # remmetre x a 0 pour la prochaine partie
        x = 0
        # remmetre a null reponse pour la prochaine partie
        reponse = "a"
        # return et envoyé un print avec un message + le nombre de tour qu'il a fait !
        return print("jaime les dinosaures","nombre de tour fait :",b)

tableau = [0,54,8,22,5,7,6,1,9,87,2]

# on veux récupe 8

print(tableau[2]) #affiche 2

len(tableau) #renvoie la taille de tableau

prenom = "Alexandre"
nom = "Camandona"
identite = nom + prenom #problème pas d'espace
identite = nom + '' + prenom
*
integerValuer = 554 #renvoie 554
stringIntergerValue = str(554) #renvoie "554"






