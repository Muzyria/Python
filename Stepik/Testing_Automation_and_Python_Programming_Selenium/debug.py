from datetime import datetime, timedelta

dt = datetime.now() + timedelta(days=10)

print(str(dt.strftime('%d/%m/%Y')))