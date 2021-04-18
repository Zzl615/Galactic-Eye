def calculate_air_alert(today_data):
    return False


def calculate_rain_alert(today_weather):
    return False


def calculate_cloth_alert(his_temp, today_temp):
    return False


def calculate_alert(his_data: dict, today_data: dict):
    # 关于未来24h的温度  最高温度、最低温度、8~9点（室外）、20~21点（室外）
    cloth_alert = calculate_cloth_alert(his_data, today_data)
    # 关于 空气污染
    air_alert = calculate_air_alert(today_data)
    # 关于降水情况
    rain_alert = calculate_rain_alert(today_data)

    alert = cloth_alert or air_alert or rain_alert

    return alert
