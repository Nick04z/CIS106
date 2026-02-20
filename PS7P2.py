#Nicholas Rodriguez - 2/19/2026 - PS7P2
#process
fibValA = 1
fibValB = 1

print(fibValA)
print(fibValB)


for count in range (0, 18, 1):
    fibValC = fibValA + fibValB
    print(fibValC)
    fibValA = fibValB
    fibValB = fibValC 