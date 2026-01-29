
#负责计算功能的实现
def calcuate(num1, num2, op):
    print("您输入的是：",num1, op, num2)

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
       return num1 * num2
    elif op == "/":
        if num2 == 0:
            return  "❌输入错误，不能除以0"
        else:
           return num1 / num2
    elif op == "%":
        return num1 % num2
    elif op == "**":
        return num1 ** num2
    else:
        return "❌不支持该运算符"

#处理字符串
def calculate_express(expr):
    parts = expr.split()
    
    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
        op = parts[1]
        #float:把字符串变成数字（支持小数
    except ValueError:
        print("❌请输入有效的数字")
        print(num1, num2, op)
    
    return calcuate(num1, num2, op)

