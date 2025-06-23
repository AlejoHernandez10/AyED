def division(dividendo, divisor):
    try:
        dividendo = float(dividendo)
        divisor = float(divisor)

    except:
        print("no se puede convertir a numero")
        return None
    


    if divisor == 0:
        raise ZeroDivisionError
    else:
        return float(dividendo) / float(divisor)
    
numero1 = input("Dividendo: ") 
numero2 = input("Divisor: ")

print(division(numero1, numero2))
