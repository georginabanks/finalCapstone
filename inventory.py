class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # return cost
    def get_cost(self):
        return self.cost

    # return quantity
    def get_quantity(self):
        return self.quantity

    # return product name
    def get_product(self):
        return self.product

    # return product code
    def get_code(self):
        return self.code

    # print product details
    def __str__(self):
        output = ''
        output += '\n────────────────────────────────────\n'
        output += f'Product: {self.product}\n'
        output += f'Country: {self.country}\n'
        output += f'Code: {self.code}\n'
        output += f'Cost: {self.cost}\n'
        output += f'Quantity: {self.quantity}\n'
        output += '────────────────────────────────────'
        return output


#=============Shoe list===========
list_shoes = []


#==========Functions outside the class==============
# read shoe data from inventory
def read_shoes_data():
    # read data from file
    f = open('inventory.txt', 'r')
    inventory = f.readlines()
    f.close()

    # append data to shoe list
    n = 0
    for line in inventory:
        line = line.replace('\n', '').split(',')

        if n == 0:
            n += 1
            continue
        else:
            list_shoes.append(Shoes(line[0], line[1], line[2], line[3], line[4]))
            n += 1


# add new shoe data to list
def capture_shoes():
    read_shoes_data()

    # user inputs product details
    country = input('Country: ')
    code = input ('Product code: ')
    product = input('Product name: ')
    cost = input('Cost: ')
    quantity = input('Quantity in stock: ')

    # append data to shoe list
    new_shoe = Shoes(country, code, product, cost, quantity)
    list_shoes.append(new_shoe)

    # add product to inventory
    new_product = f'\n{country},{code},{product},{cost},{quantity}'
    f = open('inventory.txt', 'a')
    f.write(new_product)
    f.close()


# view all products
def view_all():
    for item in list_shoes:
        print(item)


# restock product
def re_stock():
    f = open('inventory.txt', 'r')
    inventory = f.readlines()
    f.close()

    qty = 0
    n = 0

    # find product with lowest quantity
    for line in inventory:
        if n == 0:
            n += 1
            continue
        else:
            line = line.split(',')
            i_qty = int(line[4])
            if i_qty < qty:
                qty = i_qty
            else:
                continue
            n += 1

    # print details of product with least stock
    sects = inventory[n].split(',')

    output = ''
    output += '\n────────────────────────────────────────────────────────\n'
    output += f'The product with the lowest stock is {sects[2]}'
    output += '\n────────────────────────────────────────────────────────\n'
    print(output)

    # add stock to quantity
    while True:
        add_qty = int(input('Add quantity: '))

        # restock
        if type(add_qty) == int:
            sects[4] = str(int(sects[4]) + add_qty)
            new_data = ','.join(sects)
            break
        else:
            print('Invalid quantity. Please try again.')
            continue

    inventory[n] = new_data

    # write data to inventory
    f = open('inventory.txt', 'w')
    for line in inventory:
        f.write(line)
    f.close()


# user searches for product via code
def search_shoe():
    shoe_code = input('Product code: ')

    while True:

        for item in list_shoes:
            code = item.get_code()
            if code == shoe_code:
                print(item)
                break
            else:
                continue

        # print error if code not in inventory
        else:
            print('That code does not exist.')
            break

        break


# display stock value for each product
def value_per_item():
    read_shoes_data()

    output = ''

    for item in list_shoes:
        qty = item.get_qty()
        cost = item.get_cost()
        value = qty * cost
        output += f'{item[0]}: £{value}\n'

    return output


# display product with highest quantity in stock
def highest_qty():
    f = open('inventory.txt', 'r')
    inventory = f.readlines()
    f.close()

    # identify product with highest quantity in stock
    qty = 0
    n = 0

    for line in inventory:
        if n == 0:
            n += 1
            continue
        else:
            line = line.split(',')
            i_qty = int(line[4])
            if i_qty > qty:
                qty = i_qty
            else:
                continue
            n += 1

    # print details
    sects = inventory[n].split(',')

    output = ''
    output += '\n────────────────────────────────────────────────────────────────────────\n'
    output += f'The product with the highest quantity in stock is {sects[2]}.\n'
    output += f'There are {sects[4]} items in stock.\n'
    output += '\n────────────────────────────────────────────────────────────────────────\n'
    print(output)


#==========Main Menu=============
while True:
    read_shoes_data()

    menu = input("""
Please choose one of the following options:
1 - Add new product
2 - View all products
3 - Restock product
4 - Search product    
5 - View product with highest quantity in stock
6 - Exit
""")

    # add new product
    if menu == '1':
        capture_shoes()
        output = ''
        output += '\n────────────────────────────────────\n'
        output += 'Product has been added to inventory.'
        output += '\n────────────────────────────────────'
        print(output)
        continue

    # view all products
    elif menu == '2':
        view_all()
        continue

    # restock product
    elif menu == '3':
        re_stock()
        continue

    # search for product
    elif menu == '4':
        search_shoe()
        continue

    # display product with highest quantity in stock
    elif menu == '5':
        highest_qty()
        continue

    # exit
    elif menu == '6':
        output = ''
        output += '\n────────────────\n'
        output += '\tGoodbye.'
        output += '\n────────────────'
        print(output)
        exit()

    # invalid input error
    else:
        print('Invalid menu choice. Please try again.')
        continue
