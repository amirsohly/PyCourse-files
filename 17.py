a = [80,40,60,20,10,30]

'''for i in a:
    print(i)'''

#پاک کردن عنصر
#روش 1
a.remove(60)
#روش 2
a.pop(1)

#اضافه کردن عنصر
#روش 1
a.append(500)
#روش 2
a.insert(3,800)

#معکوس کردن عناصر آرایه
a.reverse()

#مرتب‌سازی
a.sort()

print(len(a))