def get_result(param) :
    param = param.replace(" ", "")
    operations = ["+", "-", "*", "/"]
    param_operation = [] # 파라미터 내 수식을 담을 배열
    param_number = [] # 파라미터내 숫자만 담을 배열
    result = ""

    for data in param:
        if data.isdigit() :
            param_number.append(data)
        else :
            for operation in operations:
                if operation == data:
                    param_operation.append(operation)
                    break

    for i in range(len(param_operation)) :
        result += param_number[i] + param_operation[i]

    result += param_number[-1]
    return result

# get_result("2 3 + 5 *")