import json
print("start code")
file = open('dump.json','r',encoding='utf-8')
data = json.load(file)
file.close()

search_code = input("Введите номер квалификации: ").strip()
for item in data:
    if item['model']=="data.specialty" and item["fields"]["code"]==search_code:
        fields=item["fields"]
        print(f"{"-"*20}Найденно{"-"*20}")
        print(f"{fields['code']}>>Специальность{fields['title']},{fields["c_type"]}")
    elif item['model=datf.skill'] and item["fields"]["code"]==search_code:
        print(f"{"-"*20}Найденно{"-"*20}")
        print(f"{fields['code']}>>Специальность{fields['title']}")
    else:
        print(f"{"-"*20}Не найденно{"-"*20}")
print("end code")