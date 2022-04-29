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