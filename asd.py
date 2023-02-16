from datetime import date, timedelta

date_point = date.today() - timedelta(100)
if date_point > date.today():
    print("vece")
else:
    print("manje je")
