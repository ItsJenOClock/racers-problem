def non_winners(races):
    # Write your solution here!
    # steps:
    # initialize empty set of 'losers'(2nd and 3rd place) that I will add to and will return the final set
    # create another set of winners (1st place people in the dictionary)
    # iterate through via for loop via values (tuples and skip index 0)
    # append those to that earlier set 'losers' that will be returned

    losers = set()
    winners = set()
    for top_three in races.values():
        winners.add(top_three[0])
    
    for top_three in races.values():
        if top_three[1] not in winners:
            losers.add(top_three[1])
        if top_three[2] not in winners:
            losers.add(top_three[2])

    return losers

races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()

print("All tests passed! Discuss time/space complexity if time remains")