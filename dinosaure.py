#DEBUT
# print ("BONJOUR MONDE")

# def retournerSixPlusTrois():
#     return 6+3
# def retournerSixPlusX(x):
#     return 6 + x

# print(retournerSixPlusX(444444444444444444444444444444444444444444))
#--------------------------------------------------------------------------------------------------
# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def multiply(x,y):
#     return x*y

# def divide(x,y):
#     return x/y

# def modulo(x,y):
#     return x%y

def CalculsalaireSalaireSeconde(s,day,heur):
    return (s/(day*max(0,min(heur,24))*3600))*12

print(CalculsalaireSalaireSeconde(12000,235,8))
#FIN
