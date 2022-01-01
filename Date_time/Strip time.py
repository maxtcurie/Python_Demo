from datetime import datetime

dt_string = "12/11/2018 09:15:32"

datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")