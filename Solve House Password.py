def checkio(data: str) -> bool:
  
  #Initially set the conditions as false
    dig = False
    upper = False
    lower = False
    
    if(len(data) >= 10):
        x = [a for a in data]
        for a in x:
            if a.isdigit():
                dig = True
            if a.islower():
                lower = True
            if a.isupper():
                upper = True
        if(dig == True and upper == True and lower == True):
            return True
    return False
