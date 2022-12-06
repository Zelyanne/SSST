from SSST_interfaceproto import ssstInterface as SSST


boso = SSST()



while True:
    print (""" Entrez le chiffre correspondant a votre requete 

1 - Ajouter une entreprise a SSST
2 - Ajouter un employe pour l une des entreprise 
3 - Supprimer une entreprise 

""")
    reponse = int(input())
    if reponse == 1:
        boso.generate_database()
        boso.generate_table()
    elif reponse == 2:
        boso.Add_Employe_to_Database()
    elif reponse == 3:
        boso.remove_database()
    else :
        print ("yare yare da vous devez choisir entre les nonbres proposes")
    
    print ( "Si vous voulez faire une autre requete appuyez y sinn tapez entree")
    reponse = input()
    if reponse != 'y' :
        break


#So102gxIAh5q