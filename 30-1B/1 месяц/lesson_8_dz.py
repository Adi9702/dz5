with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\nabc\n30\nxyz\n40\n")

def process_numbers_file(filename="numbers.txt"):
    numbers = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    num = float(line.strip())
                    numbers.append(num)
                except ValueError:
                    print(f"Предупреждение: Строка {line_num} пропущена: не число.")
    except FileNotFoundError:
        print("Файл не найден.")
        return

    if not numbers:
        print("Нет корректных чисел для подсчета.")
        return

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Сумма: {total_sum}")
    print(f"Среднее: {average}")
process_numbers_file()
 

