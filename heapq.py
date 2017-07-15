import heapq

stocks = [
    {'tinker':'APPL','price':123},
    {'tinker': 'APP', 'price': 3},
    {'tinker': 'APL', 'price': 12},
    {'tinker': 'AL', 'price': 23},
    {'tinker': 'PPL', 'price': 13}
]

print(heapq.nsmallest(2, stocks ,key= lambda stock :stock['price']))
