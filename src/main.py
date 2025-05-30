def calculate(expression: str) -> float:
    """
    Evalúa una expresión aritmética que incluye las operaciones básicas:
    suma (+), resta (-), multiplicación (*) y división (/), y soporta el uso de paréntesis.
    
    Parámetros:
      expression: str - Cadena con la expresión aritmética (por ejemplo, "2 + 2").

    Retorna:
      float - Resultado de la evaluación.

    Lanza:
      SyntaxError si la sintaxis es incorrecta.
      ValueError si se encuentra un carácter inválido.
      ZeroDivisionError si se intenta dividir por cero.
    """
    s = expression.strip()
    if s == "":
        raise ValueError("Entrada vacía")

    i = 0  # Índice actual en la cadena

    def skip_whitespace():
        nonlocal i
        while i < len(s) and s[i].isspace():
            i += 1

    def parse_number() -> float:
        nonlocal i
        skip_whitespace()
        start = i
        if i < len(s) and not (s[i].isdigit() or s[i] == '.'):
            raise ValueError(f"Carácter inválido en la posición {i}.")
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            i += 1
        if start == i:
            raise SyntaxError("Sintaxis inválida: se esperaba un número.")
        return float(s[start:i])

    def parse_factor() -> float:
        nonlocal i
        skip_whitespace()
        if i < len(s) and s[i] == "(":
            i += 1  # omite el paréntesis abierto
            result = parse_expression()
            skip_whitespace()
            if i < len(s) and s[i] == ")":
                i += 1  # omite el paréntesis cerrado
            else:
                raise SyntaxError("Sintaxis inválida: se esperaba ')'.")
            return result
        else:
            return parse_number()
                
    def parse_term() -> float:
        nonlocal i
        result = parse_factor()
        while True:
            skip_whitespace()
            if i < len(s) and s[i] in "*/":
                op = s[i]
                i += 1
                right = parse_factor()
                if op == "*":
                    result *= right
                else:
                    result /= right
            else:
                break
        return result
    
    def parse_expression() -> float:
        nonlocal i
        result = parse_term()
        while True:
            skip_whitespace()
            if i < len(s) and s[i] in "+-":
                op = s[i]
                i += 1
                right = parse_term()
                if op == "+":
                    result += right
                else:
                    result -= right
            else:
                break
        return result

    result = parse_expression()
    skip_whitespace()
    if i != len(s):
        raise ValueError("Entrada inválida: quedan caracteres sin procesar.")
    return result
