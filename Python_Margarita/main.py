a = True
while a:
    ps = input("Напиши пароль")
    if len(ps) < 8:
        print("Короткий")
    else:
        print("ОК")
        a = False
print("Пароль отличный")

