from pizza_store.store import(
    NYPizzaStore,
    ChicagoPizzaStore
)

def main():

    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print('Haeseok ordered a {}'.format(pizza.get_name()))
    print()
    pizza = chicago_store.order_pizza('cheese')
    print('Haeseok ordered a {}'.format(pizza.get_name()))
    
    
if __name__ == '__main__':
    main()