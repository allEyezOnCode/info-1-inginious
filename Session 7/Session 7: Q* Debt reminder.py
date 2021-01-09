def give_money(borrowed_money, from_person, to_person, amount):
    if from_person == to_person or type(from_person) != str or type(to_person) != str or type(borrowed_money) != dict or (type(amount) != int and type(amount) != float):
        raise ValueError
    for person in [from_person, to_person]:
        if person not in borrowed_money:
            borrowed_money[person] = {}
        for person2 in [from_person, to_person]:
            if person2 not in borrowed_money[person] and person2 != person:
                borrowed_money[person][person2] = 0
    print(borrowed_money)
    borrowed_money[from_person][to_person] -= amount
    borrowed_money[to_person][from_person] += amount
def total_money_borrowed(borrowed_money):
    if type(borrowed_money) != dict: raise ValueError
    total_sum = 0
    for value in borrowed_money.values():
        for el in value.values():
            if el > 0: total_sum += el
    return total_sum

borrowed_money = {}
give_money(borrowed_money, "Mark", "Bill", 2000000)
give_money(borrowed_money, "Mark", "Steve", 2000000)
give_money(borrowed_money, "Serguei", "Bill", 5000000)
give_money(borrowed_money, "Bill", "Larry", 6000000)
give_money(borrowed_money, "Larry", "Linus", 5.5)
give_money(borrowed_money, "Steve", "Mark", borrowed_money["Steve"]["Mark"])
