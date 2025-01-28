a = 3
b = 2
c = a + b
print(a, b, c)


numList = {
    "1",
    "2",
    "3"
}
#배열
shop = ["수박", "사과", "참외"]
print(shop[-1])

#딕션어리(map) 키 값
obj = {
    "name" : "이선호",
    "age" : 22,
}
#print(obj["name"])

people = [
    {
        "name" : "나인혁",
        "age" : 22,
    },
    {
        "name" : "B",
        "age" : 22,
    },
]

#print(people[0]['name'])

# 함수
# function -> def
#   함수명(파라미터) :
def sum(a, b):
    return a + b
print(sum(3, 4))

def is_adult(age) :
    if age > 20 :
        print("성인")
    else :
        print("청소년")

is_adult(21)



#반복문
fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
count = 0
for fruit in fruits:
    if fruit == '사과' :
        count += 1
print(count)


def count_fruits(fruit_nmae):
    fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
    count = 0
    for f in fruits:
        if f == fruit_nmae :
            count += 1
    return count

print(count_fruits("배"))
people_info = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def get_age(name) :
    for p in people_info:
        if p["name"] == name:
            return p["age"]
    return "그런 이름은 존재하지 않습니다."

print("=====")
print(get_age("bob"))
print(get_age("john"))
print(get_age("smith2"))


class Person:
    def __init__(self, name):
        self.name = name
    def sayhello(self, towhom):
        print(f"Hello, {towhom}. i am {self.name}")

person = Person("apple")
person.sayhello("john")


