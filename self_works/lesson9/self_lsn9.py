import json
import csv
import openpyxl

s1, s2, s3, s4 = [input() for _ in range(4)]


def write_two_string(string1, string2):
    with open('lesson.txt', 'a+') as file:
        file.write(string1 + '\n')
        file.write(string2 + '\n')


write_two_string(s1, s2)
write_two_string(s3, s4)

data = {
    123456: ('Max', 24),
    123457: ('Sam', 22),
    123458: ('Bob', 34),
    123459: ('Tom', 55),
    123450: ('Joe', 10),
}


def get_json():
    with open('data.json', 'w') as file:
        json.dump(data, file)


def get_csv():
    with open('data.json', 'r') as file:
        json_file = json.load(file)

    for id_, info in json_file.items():
        info.append(f'+{id_} 327675')

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        writer.writerow(['id', 'name', 'age', 'phone'])

        for id_, info in json_file.items():
            name, age, phone = info
            writer.writerow([id_, name, age, phone])


def get_pyxl():
    wb = openpyxl.Workbook()
    ws = wb['Sheet']
    ws.append({k + 1: f'person{k}' for k in range(1, 6)})

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        id_ = []
        name = []
        phone = []
        for i in reader:
            id_.append(i[0])
            name.append(i[1])
            phone.append(i[3])
    ws.append(id_)
    ws.append(name)
    ws.append(phone)

    wb.save('test.xlsx')


get_json()
get_csv()
get_pyxl()
