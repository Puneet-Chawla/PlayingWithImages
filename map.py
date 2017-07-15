import heapq
income = [10, 20, 30]

def double(a):
    return a*2

new_income =list(map(double, income))
print(new_income)

grades = [12,123,345,11,132]

print(heapq.nlargest(2, grades))
