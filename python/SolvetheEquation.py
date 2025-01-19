"""
Решите заданное уравнение и верните значение 'x' в виде строки "x=#value". 
Уравнение содержит только операции '+', '-', переменную 'x' и ее коэффициент. 
Вы должны вернуть "No solution", если для уравнения нет решения, или "Infinite solutions", 
если для уравнения существует бесконечное количество решений. 
Если для уравнения существует ровно одно решение, мы убеждаемся, что значение 'x' является целым числом.
"""

# Input: s = "*"
# Output: 9

def solveEquation(equation: str) -> str:
    def parse(equ):
        coeff, const = 0, 0
        num, sign = 0, 1
        i = 0
        while i < len(equ):
            if equ[i] == '+':
                sign = 1
                i += 1
            elif equ[i] == '-':
                sign = -1
                i += 1
            elif equ[i].isdigit():
                num = 0
                while i < len(equ) and equ[i].isdigit():
                    num = num * 10 + int(equ[i])
                    i += 1
                if i < len(equ) and equ[i] == 'x':
                    coeff += sign * num
                    i += 1
                else:
                    const += sign * num
            elif equ[i] == 'x':
                coeff += sign
                i += 1
        return coeff, const
    
    left, right = equation.split('=')
    left_coeff, left_const = parse(left)
    right_coeff, right_const = parse(right)
    
    coeff = left_coeff - right_coeff
    const = right_const - left_const
    
    if coeff == 0:
        return "Infinite solutions" if const == 0 else "No solution"
    return f"x={const // coeff}"

if __name__ == "__main__":
    result = solveEquation(s = "*")
    print(result)
