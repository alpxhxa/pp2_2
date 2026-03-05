import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Исправленный паттерн: 
    # Ищем номер (например "1."), затем название до строки с ценой "X,XXX x XXX,XX"
    # Мы используем (?:...) для незахватывающих групп, чтобы не путать findall
    item_pattern = r"(\d+)\.\n(.*?)\n(?:\\s*)?(\d+,\d+)\s*x\s*([\d\s,]+)\n([\d\s,]+)"
    
    items_raw = re.findall(item_pattern, content, re.DOTALL)
    
    products = []
    for item in items_raw:
        # Очистка данных: убираем лишние пробелы и меняем запятые на точки для Python
        idx, name, qty, price, total = item
        products.append({
            "id": idx,
            "name": name.replace('\n', ' ').strip(),
            "quantity": float(qty.replace(',', '.')),
            "price_per_unit": float(price.replace(' ', '').replace(',', '.')),
            "total_price": float(total.replace(' ', '').replace(',', '.'))
        })

    # Извлечение даты и времени
    date_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s*\d{2}:\d{2}:\d{2})", content)
    receipt_date = date_match.group(1) if date_match else "Не найдено"

    # Извлечение итоговой суммы
    total_match = re.search(r"ИТОГО:\n([\d\s,]+)", content)
    total_amount = float(total_match.group(1).replace(' ', '').replace(',', '.')) if total_match else 0.0

    # Определение метода оплаты
    payment_method = "Банковская карта" if "Банковская карта" in content else "Наличные"

    return {
        "metadata": {
            "date_time": receipt_date,
            "total_sum": total_amount,
            "payment_method": payment_method
        },
        "products": products
    }

if __name__ == "__main__":
    try:
        data = parse_receipt('raw.txt')
        print(json.dumps(data, ensure_ascii=False, indent=4))
    except Exception as e:
        print(f"Произошла ошибка: {e}")