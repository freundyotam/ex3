
def parse_file(filename):
    file = open(filename, 'r')
    inventory = {}

    lines = file.read().splitlines()
    for line in lines:
        args = line.split()

        if (args[0] == 'add'):
            if args[2] not in inventory.keys():
                inventory[args[2]] = {'price': float(args[3]), 'amount': float(args[4]),'profit': 0}

        elif(args[0] == 'change'):
            inventory[args[2]]['amount'] += float(args[3])

        elif(args[0] == 'ship'):
            item_string = line[11:]
            order_items = item_string.split(' -- ')
            
            for item_pair in order_items:
                item = item_pair.split(', ')
                try:
                    item_amount = float(item[1])
                    if inventory[item[0]]['amount'] >= item_amount:
                        inventory[item[0]]['profit'] += inventory[item[0]]['price']*item_amount
                        inventory[item[0]]['amount'] -= item_amount
                except:
                    pass


    return inventory




def find_best_selling_product(file_name):
    cur_best_selling = ('', 0)
    try:
        for name, item_data in parse_file(file_name).items():
                if item_data['profit'] > cur_best_selling[1]:
                    cur_best_selling = (name, item_data['profit'])

    except:
        pass
    return cur_best_selling
    

def find_k_most_expensive_products(file_name, k):
    result_list = []
    try:
        items = sorted(parse_file(file_name).items())
        price_sorted_items = sorted(items, key= lambda kv: kv[1]['price'], reverse= True)
        for i in range(k):
            try:
                result_list.append(price_sorted_items[i][0])
            except:
                pass
    except:
        pass
    return result_list