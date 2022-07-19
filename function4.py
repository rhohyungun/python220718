def times(a=10, b=20):
    return a*b

print(times())
print(times(5))


def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result


print(union("ham","egg"))
print(union("ham","egg","spam"))
