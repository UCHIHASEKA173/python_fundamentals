class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.order = Queue()

    def take_order(self, customer: str, flavor: str, scoops: int):
        if flavor not in self.flavors:
            print('Sorry, flavor unavailable.')
        
        elif scoops < 1 or scoops > 3:
            print('Choose 1, 2, or 3 scoops.')

        else:
            print('Order created!')
            order = {'customer': customer, 'flavor': flavor, 'scoops': scoops}
            self.order.enqueue(order)

    def show_all_orders(self):
        print('All orders in queue:')
        for i in self.order.items:
            print(i)

    def next_order(self):
        print('Next order', self.order.dequeue())



shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()


        





