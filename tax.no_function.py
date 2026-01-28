## tax.no_function.py
def calculate_price_with_tax():
    price = float(input('What is the price '))
    tax = float(input('What is the tax rate? '))
    calculated_price = price * (100 + tax) / 100
    print(f'The calculated price is {calculated_price}')

def get_inputs():
    sentinel = str.upper(input(f'Enter Q for quit or any other key to compute tax '))
    return sentinel

done = False
while not done:
    sentinel = get_inputs()
    if sentinel == 'Q':
        done = True
        print(sentinel,done)
        continue
    else:
        print("Compute tax")
    calculate_price_with_tax()




