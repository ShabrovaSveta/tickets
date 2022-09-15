tickets = dict()
ticket_count = int(input("Введите кол-во билетов: "))

for i in range(ticket_count):
    age = int(input(f"Введите возраст для билета {i+1}: "))
    if age < 18:
        tickets[i] = 0
    elif 18 <= age < 25:
        tickets[i] = 990
    elif age >= 25:
        tickets[i] = 1390

summa = sum(tickets.values())
skidka = summa * 0.1
print("Сумма:", summa)

if ticket_count > 3:
    print("Сумма со скидкой 10%:", summa - skidka)

"""
1. range(ticket_count) для например ticket_count = 3 вернёт в цикле 0, 1, 2
2. сохраняем цены в словарь tickets.
3. словарь возвращает список ключей методом keys(), а список значений методом values()
Ключи словаря будут номер билета. Он не нужен, а нужны значения для суммирования. 
Чтобы получить сумму значений получим их через values()
и суммируем методом sum()
4. надеюсь правильно считает процент скидки :)
