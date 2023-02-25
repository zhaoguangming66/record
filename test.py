import time



def change_time_to_beijin_time(str_time):
    year_month_day = str_time.split('T')[0]
    hour_time = (str_time.split('T')[1]).split('+')[0]
    time_ =  f'{year_month_day} {hour_time}'
    t_time = time.localtime(int(time.mktime(time.strptime(time_, "%Y-%m-%d %H:%M:%S"))) + 3600 * 1)
    beijin_time = time.strftime("%Y-%m-%d %H:%M:%S", t_time)
    return beijin_time


if __name__ == '__main__':
    # print(get_date_str("2023-01-05T10:00:00+01:00"))
    ss="""# https://magazine.interencheres.com/actualites/
    # https://magazine.interencheres.com/tendances/
    # https://magazine.interencheres.com/coulisses-des-encheres/
    # https://magazine.interencheres.com/art-mobilier/
    # https://magazine.interencheres.com/vehicules/
    # https://magazine.interencheres.com/materiels-professionnels/"""
    ''.replace("# ",'')
    print([s.strip().replace("# ",'') for s in ss.split("\n")])