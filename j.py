dict = { 'druhi' :
        {'language': 'french',
         'hobby':'coding'
         },
         'drishi' :
         {'language': 'finnish',
         'hobby':'music'}
}
for name,ask in dict.items():
    print(f"{name}'s Fav are : ")
    for qus,ans in ask.items():
        print(qus)
        print(ans)
