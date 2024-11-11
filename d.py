dict = {
    'Druhi':{
        'language':'coding',
         'sports':'lawntennis',
         },
    'Drishi':{
         'language':'poding',
         'sports':'tennis',
         },
}
print(dict)
for name,info in dict.items():
    print(f'Fav of {name} is : ')
    lang = info['language']
    sport = info['sports']
    print(f"Fav lang is {lang} and Fav sports is {sport}")
