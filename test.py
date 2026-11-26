def series_sum(n):
    k = 1
    
    for i in range(1, n):
        k += 1/(1 + n*3)
    return round(k, 2)

print(series_sum(5))