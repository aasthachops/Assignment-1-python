#question1
a= int(input("Enter the value of a",))
b= int(input("Enter the value of b",))
c= int(input("Enter the value of c",))

avg= (a+b+c)/3
print("The average of 3 numbers entered is ",avg)


#question2
a= float(input("Enter the Gross Income ",))
b= int(input("Enter the Number of Dependents ",))
taxRate= .20
standardDeduction = 10000
dependentDeduction= 3000
taxableIncome= a-standardDeduction-(b*dependentDeduction)
tax= taxableIncome*taxRate
print("The Tax is ",tax)

#question 3
list= [21108019, 'Aastha Chopra', 'F', 'Python', 9.5]
print(list)

#question4
Marks =[90, 54, 48, 69, 21]
Marks.sort()
print(Marks)


#Question:5(a)

list= ['Red', 'Green', 'Whte','Black','Pink','Yellow']
new_list = []
for index, value in enumerate(list):
    if index not in [4]:
        new_list.append(value)
print(new_list)

#Question 5(B)
new_list[3]='Purple'
print(new_list)