def seasons_and_months():
    month=input("ENTER THE MONTH: ")
    if month in str('february,march'):
        print("spring")
    elif month in str('april,may,june'):
        print("summer")
    elif month in str('july,august,september,'):
        print("rainy")
    elif month in str('october,november'):
        print("autumn")
    elif month in str('december,january'):
        print("winter")
seasons_and_months()    
