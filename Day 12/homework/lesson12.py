score - int(input("ტესტში რა ქულა მიიღე?:  "))

if score > 90 and score < 100:
    print("თქვენ დაგიფინანსდებათ სწავლა სრულიად")

elif score > 70 and score < 80:
    print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით")

elif score > 40 and score < 70:
    print("თქვენ დაგიფინანსდებატ სწავლა 500 ლარით")

elif score < 40:
    print("თქვენ არ დაგიფინანსდებატ სწავლის პროცესი")

else:
    print("შენ შეიყვანე არასწორი ქულა")
