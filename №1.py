def  average_grade(a, b, c):
    return (a+b+c)/3
a1=int(input())
b1=int(input())
c1=int(input())
res=average_grade(a1,b1,c1)
print(res)
def grade_message(res):
    if res>=4.5:
        return("отлично")
    elif res<4.5 and res>=3.5:
        return("хорошо")
    elif res<3.5:
        return("нужно повторить материал")
mes=grade_message(res)
print(mes)

a2=5
b2=4
c2=5
res2=average_grade(a2,b2,c2)
mes2=grade_message(res2)
print(res2)
print(mes2)

a3=3
b3=4
c3=3
res3=average_grade(a3,b3,c3)
mes3=grade_message(res3)
print(res3)
print(mes3)