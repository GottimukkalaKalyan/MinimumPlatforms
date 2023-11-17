arrive = list(map(int, input().split()))
arrive.sort()
departure = list(map(int, input().split()))
departure.sort()
list_a = []
for i in range(len(arrive)):
    if i == 0:
        list_a.append(departure[i])
    else:
        for j in list_a:
            if arrive[i] > j:
                list_a.remove(j)
                list_a.append(departure[i])
                break
            else:
                list_a.append(departure[i])
                break
print(len(list_a))
