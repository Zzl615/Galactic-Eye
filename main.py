# import pandas as pd
import json
import datetime
from alert import calculate_alert
from source.binstd import fetch_today_weather_data
from source.sqlite import get_previous_weather_data, save_weather_date
from network.notify import notify_alert

if __name__ == "__main__":
    today = datetime.date()
    today_data = fetch_today_weather_data(today)
    save_weather_date(today_data)
    his_data = get_previous_weather_data()
    alert_res = calculate_alert(his_data, today_data)
    if alert_res:
        notify_alert()
