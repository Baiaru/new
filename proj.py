def list(x):
    list_second = ["Крещение Руси", "Отмена Крепостного права", "Куликовская битва"]
    final_list = []
    final_list = dict(zip(x, list_second))
    print(final_list)


def main():
    x = [988, 1861, 1380]
    list(x)

if __name__ == '__main__':
    main()