names = ['Manouchehr', 'Alisan', 'Elina']
pepole =  {
    'Manouchehr':{'sen': 38 , 'ghad': 174},
    'Alisan': {'sen': 4 , 'ghad': 30}
}
for name in names:
    if name in pepole:
        # we have this person
        # lets print the sen
        print(f"I Have {name} and sen is {pepole[name]['sen']}")
    else:
        print(f"ooooh I have no data for {name}")
