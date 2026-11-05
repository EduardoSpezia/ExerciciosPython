paisA = 90000000
paisB = 140000000
anos = 0

while paisA < paisB:
    paisA = (paisA * 1.035)
    paisB = (paisB * 1.01)
    anos += 1
print(anos, "Anos")