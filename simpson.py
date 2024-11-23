import math

def simpson (a,b,f,n):
    
    if n % 2 != 0:
        raise ValueError("تعداد زیربازه‌ها باید زوج باشد.")

    h = (b - a) / n
    list_x = []
    for i in range(n+1):
        x = a + i * h
        list_x.append(x)
    
    list_y = []    
    for j in list_x :
        y = f(j)
        list_y.append(y)
        
    antg = list_y[0] + list_y[-1]
    for i in range(1, n, 2):
        antg += 4 * list_y[i]
    for i in range(2, n - 1, 2):
        antg += 2 * list_y[i]

    
    answer = (h/3)*antg
    return round(answer, 5) 


# a = حد پایین انتگرال
a = int(input("enter a : "))

# b = حد بالای انتگرال

b = int(input("enter b : "))

# n = تعداد تقسیم بندی ها 

n = int(input("enter n : "))

# F(x) = تابع مد نظر

f = lambda x: x * math.sin(x)

print("the answer is = ",simpson(a,b,f,n))