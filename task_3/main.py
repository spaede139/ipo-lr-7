
import json
import os
print("start code")
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'main.json')
cout=0
while True:
    print(f"1- вывести все записи \n2- Вывести запись по полю \n3- Добавить запись\n4- Удалить запись по полю\n5- Выйти из программы")
    choice=input("ВЫБЕРИТЕ ОДИН ИЗ 5 ПУНКТОВ  :")
    if choice!=1 or 2 or 3 or 4 or 5:
        print("введите число от 1 до 5 вы НЕВЕРНО УКАЗАЛИ ЧИСЛО!")
    if choice=="1" :
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
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
        cout+=1
    if choice == "2":
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        search_id=int(input("введите id нужного поля :"))
        index=1
        for item in data:
            search_id_flag=False
            if item.get('id')==search_id:
                print(f"ID: {item.get('id')}")
                print(f"Город: {item.get('name')}")
                print(f"Страна: {item.get('country')}")
                if item.get('is_big'):
                    big_status = "Да"
                else:
                    big_status = "Нет"  
                print(f"Большой: {big_status}")
                print(f"Население: {item.get('people_count')}")
                print(f"номер записи {index}")
                search_id_flag=False
            index+=1
        cout+=1
        if not search_id_flag:
            print("запись не найдена")
    if choice=="3":
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
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
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        cout+=1
    if choice=="4":
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        del_id=int(input("введите id записи которую хотите удалить :"))
        del_flag=False
        index_del = -1 
        for index,item in enumerate(data):
            if item['id']==del_id: 
                index_del=index
                del_flag=True
                break
        del data[index_del]          
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        cout+=1
        if not del_flag:
            print("запись не найдена")
        
    if choice == "5":
        
        print(f"выполнино операций{cout}")
        print("программа завершена")
        break

