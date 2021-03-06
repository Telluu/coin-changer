#!/usr/bin/env python3


def main():
    print('#####################################')
    print('--------Coin Changer by Tellu--------')
    print('#####################################\n')

    while True:
        print('##############################')

        cost = numVal('Enter total cost: ')
        cash = numVal('Enter amount of cash given by the client: ')

        change(cash, cost)

        print('##############################\n\n\n')


def change(cash, cost):
    prefix = '$'
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

    change = round(cash - cost, 2)
    change_show = format(abs(change), ',.2f')

    if change > 0:
        print('--------------------')
        print(f'Change: {prefix}{change_show}')
        print('--------------------')

        for denomination in denominations:
            quantity = 0
            while change >= denomination:
                change = round(change - denomination, 2)
                quantity += 1
            if quantity > 0:
                if denomination < 1:
                    prefix = ''
                    denomination = f'{int(denomination * 100)}¢'
                if quantity > 1:
                    denomination = f'{denomination} - x{quantity}'
                print(f'{prefix}{denomination}')

    elif change == 0:
        print('----------------')
        print('# No change! #')
        print('----------------')

    elif change < 0:
        print(
            '-----------------------------------------------------------------------')
        print(
            f'Not enough money! {prefix}{change_show} is missing!')
        print(
            '-----------------------------------------------------------------------')
    else:
        return


# Input sanitizing
def numVal(prompt):
    while True:
        # Take user input
        value = str(input(prompt))

        # And check if its a float
        try:
            float(value)
        except ValueError:
            print('Error! Only numbers are allowed! Decimals after the dot.')
            continue

        # Then separate integer from decimal, count both and check conditions
        check = value.split('.')
        if len(check[0]) > 8:
            print('Error! Value cannot be larger than 100 million!')
            continue
        elif len(check) > 1 and len(check[1]) > 2:
            print('Error! There cannot be more than 2 decimal numbers!')
            continue

        # Finally if it passes all the checks, give it back
        return float(value)


if __name__ == '__main__':
    main()
