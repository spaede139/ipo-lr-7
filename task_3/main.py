
import json
import os

def show_menu():
    print("\n==================================================")
    print("МЕНЮ ПРОГРАММЫ:")
    print("1 - Показать все города")
    print("2 - Найти город по ID")
    print("3 - Добавить новый город")
    print("4 - Удалить город по ID")
    print("5 - Выйти из программы")
    print("==================================================")

def users_choice():
    choice=(input("ВЫБЕРИТЕ ОДИН ИЗ 5 ПУНКТОВ  :"))
    if len(choice) == 1 and choice in "12345":
            return choice
    else:
        print("ОШИБКА: Введите число от 1 до 5!")
def all_records(data):
    for item in data:
        print(f"ID: {item.get('id')}")
        print(f"Город: {item.get('name')}")
        print(f"Страна: {item.get('country')}")
        if item.get('is_big'):
            big_status = "Да"
        else:
            big_status = "Нет"  
            print(f"Большой: {big_status}")
            print(f"Население: {item.get('people_count')}")
def find_record(data):
    search_id= input("Введите ID: ")
    if not search_id.isdigit():
        print("ОШИБКА: ID должен быть числом!")
        return
    index=1
    found = False    
    for index, item in enumerate(data, 1):  
        if item.get('id') == int(search_id):
            found = True
            print(f"\n=== НАЙДЕНА ЗАПИСЬ #{index} ===")
            print(f"ID: {item.get('id')}")
            print(f"Город: {item.get('name')}")
            print(f"Страна: {item.get('country')}")
            if item.get('is_big'):
                big_status = "Да"
            else:
                big_status = "Нет"
            print(f"Большой: {big_status}")
            print(f"Население: {item.get('people_count')}")
            print("=" * 40)
            
            break  
    if not found:
        print(f"\nЗапись с ID {search_id} не найдена!")
def add_record_by_id(data):
    id=int(input("введите id новой записи :"))
    name = input("Введите название города: ")
    country = input("Введите название страны: ")    
    people_count =int(input("Введите население города: "))
    if people_count > 100000:
        is_big = True
    else:
        is_big = False
    new_item={
        "id": id,
        "name": name,
        "country": country,
        "is_big": is_big,
        "people_count": people_count
        }
    data.append(new_item)
def del_record(data):
    del_id=int(input("введите id записи которую хотите удалить :"))
    del_flag=False
    index_del = -1 
    for index,item in enumerate(data):
        if item['id']==del_id: 
            index_del=index
            del_flag=True
            break
    del data[index_del]
    if not del_flag:
            print("запись не найдена")
def path_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'main.json')
    return file_path
def file_open(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def file_save(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def main():
    print("start code")
    cout=0
    file_path=path_file()
    while True:
        show_menu()

        choice = users_choice() 
        if choice=="1" :
            data =file_open(file_path)
            all_records(data)
            cout+=1
        if choice == "2":
            data =file_open(file_path)
            find_record(data)
            cout+=1
        if choice=="3":
            data =file_open(file_path)
            add_record_by_id(data)
            file_save(file_path,data)
            cout+=1
        if choice=="4":
            wdata =file_open(file_path)
            del_record(data)          
            file_save(file_path,data)
            cout+=1
        if choice == "5":
            
            print(f"выполнино операций{cout}")
            print("программа завершена")
            print("code finish")
            break
main()

