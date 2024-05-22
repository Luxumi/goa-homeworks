goa = "goa is the best"
goas = "goas is the best"

for i in range(len(goa)):
    if i == 0:
        goa = goa[:i] + goas[i] + goa[i+1:]
    else:
        goa = goa[:i] + goas[i-1:i+1] + goa[i+1:]

print(goa)