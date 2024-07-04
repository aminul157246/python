# weight = input('What is your weight : ')
# kg_or_lbs = input('kg or lbs :')

# if(kg_or_lbs == "kg" or "KG" or "Kg"):
#     kg = int(weight) * 0.453
#     print('your age is : ', kg  , 'kg')
# elif(kg_or_lbs == 'lbs' or 'LBS' or 'Lbs') : 
#     lbs = int(weight) / 0.453
#     print('your age is : ', + lbs)
# else:
#     print('Nothing')



weight = input('What is your weight : ')
kg_or_lbs = input('kg or lbs :')

# kg to lbs 
if(kg_or_lbs.upper() == 'lbs'):
    kg = int(weight) * 0.453
    print(f'you are {kg} kg')

# lbs to kg  
else:
    lbs = int(weight) / 0.453
    print(f'you are {lbs} pound')