import csv
import random

def generate_unique_names(n, prefix="test_"):
    return [f"{prefix}{i:03d}" for i in range(1, n + 1)]

def resolve_device_model(prefix: str) -> str:
    if prefix == "L1":
        return "Utility Tablet - 10 Inch"
    else:
        return "Utility Tablet - YTR"

def generate_csv(rows: int, filename: str = "devices.csv"):
    headers = [
        "Device ID", "Device Model", "Cart Name", "Cart Model",
        "Last Moved", "Status", "ICCID"
    ]

    cart_models = [
        "Drive - DC with Controller Access",
        "Drive - AC with Full Controller Access",
        "Drive - Gas EFI with Controller Access"
    ]

    statuses = ["no fix", "active", "idle"]
    prefixes = ["L1",  "S1"]

    unique_cart_names = generate_unique_names(rows, prefix="test_")

    with open(filename, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)

        for i in range(rows):
            prefix = random.choice(prefixes)
            device_id = f"{prefix}{random.randint(1000000000000000, 9999999999999999)}"
            device_model = resolve_device_model(prefix)
            cart_name = unique_cart_names[i]
            cart_model = random.choice(cart_models)
            last_moved = str(random.randint(240000000000, 259999999999))
            status = random.choice(statuses)
            iccid = str(random.randint(8901000000000000000, 8999999999999999999))

            row = [
                device_id,
                device_model,
                cart_name,
                cart_model,
                last_moved,
                status,
                iccid
            ]

            writer.writerow(row)

    print(f"✅ Файл '{filename}' успешно создан. Device Model зависит от префикса, имена уникальны.")



generate_csv(10)