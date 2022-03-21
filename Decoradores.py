def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print(f"Haremos una {funcion_parametro.__name__}")
        funcion_parametro()
        print("Hemos terminado")
    return funcion_interior


@funcion_decoradora
def resta():
    print(50-25)

@funcion_decoradora
def suma():
    print(25+25)


suma()
resta()