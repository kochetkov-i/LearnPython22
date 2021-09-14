def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except ValueError:
        print("Value error in convert input params")
        exit()
    except TypeError:
        print("Type error in convert input params")
        exit()

    if max_discount >= 100:
        print("Слишком большая максимальная скидка")
        exit()
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
