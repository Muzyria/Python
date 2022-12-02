from datetime import datetime, timedelta

dt = datetime.now() + timedelta(days=10)

print(dt.strftime('%d/%m/%Y'))