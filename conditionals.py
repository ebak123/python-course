price = 1.2
province = "nunavut"

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)


if 1 == 1.00:
    print("É igual")
else:
    print("Não é igual")

if province == "alberta":
    tax = .05
elif province == "ontario":
    tax = .13
else:
    tax= .15
print(tax)


if province == "alberta" or province == 'nunavut':
    tax = .05
elif province == "ontario":
    tax = .13
else:
    tax = .15
print(tax)

if province in("alberta", "nunavut", "yukon"):
    tax=.05
elif province == 'ontario':
    tax = .13