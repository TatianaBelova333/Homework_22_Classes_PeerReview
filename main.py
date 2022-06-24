from utils import Utils


def main():
    # Start message and prompt to Enter
    print('Привет! Программа симулирует движение товаров между складом и магазином\n'
          '\nДля отправки товаров нужно ввести сообщение\n'
          'Формат: Доставить [кол-во] [наименование] из [откуда] в [куда]\n'
          'Пример: Доставить 2 слон из склад в магазин\n'
          '\nДля остановки программы в любой момент введите "стоп"\n'
          'Для начала работы нажмите Enter')
    input()

    # Create and populate Shop, Store instances
    shop, store = Utils.create_instances()

    while True:
        # Display items in store and shop
        print(Utils.display_items(store=store, shop=shop))

        # Prompt user input and process it
        user_task = input('\nВведите задание: ')
        print(Utils.send_request(user_task, shop, store))


if __name__ == '__main__':
    main()
