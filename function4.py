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



def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL +=key + "=" + user[key] + "&"
    return strURL

print(userURIBuilder("credu.com", "80", id="kim", passwd="1234",
name="mike"))
#람다함수
g=lambda x,y:x*y
print(g(3,4))
print((lambda x:x*x)(3))



print( globals())