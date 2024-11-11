places = {'X': ["ottawa", "hawaii"],
          'Y': ["delhi","nainital"],
          'Z':['panaji','mumbai']

}
for names,info in places.items():
    print(f"fav place of {names}")
    for places in info:
        print(places)

