a= float(input("Enter the Gross Income ",))
b= int(input("Enter the Number of Dependents ",))
taxRate= .20
standardDeduction = 10000
dependentDeduction= 3000
taxableIncome= a-standardDeduction-(b*dependentDeduction)
tax= taxableIncome*taxRate
print("The Tax is ",tax)