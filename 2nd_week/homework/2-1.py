def get_result_new(param) :
    param = param.split()

    stack = [] # 계산을 위한 스택

    for data in param:
        if data.isdigit() :
            stack.append(int(data))
        else :
            b = stack.pop()
            a = stack.pop()

            if data == "+":
                stack.append(a + b)
            elif data == "-":
                stack.append(a - b)
            elif data == "*":
                stack.append(a * b)
            elif data == "/":
                stack.append(int(a / b))
    return stack[0]

print(get_result_new("2 3 + 5 *"))  # 출력: 25
print(get_result_new("4 2 / 3 - 2 *"))  # 출력: -2