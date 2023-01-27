
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def for_hour(time):
    if(time%12 == 0):
        return 12
    else:
        return time%12
def get_day(cirs,time):
    if(cirs == 'PM'):
        return (time + 12)//24
    else:
        return time//24
def get_cirs(cirs,time):
    if(cirs == 'PM'):
        if((time +12)%24 > 12):
            return 'PM'
        else:
            return 'AM'
    else:
        if((time%24) >= 12):
            return 'PM'
        else:
            return 'AM'
def get_name_day(n_day,position):
    return days[((position +  n_day)%7)-1]
def get_formatage(time,minute,cir,n_day,day=None):
    if(n_day > 0):
        if(n_day==1):
            if(day):
                return "{}:{:02d} {}, {} (next day)".format(time,minute,cir,day)
            return  "{}:{:02d} {}, (next day)".format(time,minute,cir)
        else:
            if(day):
                return "{}:{:02d} {}, {} ({} days later)".format(time,minute,cir,day,n_day)
            return  "{}:{:02d} {}, ({} days later)".format(time,minute,cir,n_day)
    else:
        if(day):
            return "{}:{:02d} {}, {}".format(time,minute,cir,day)
        return  "{}:{:02d} {}".format(time,minute,cir)


def add_time(start, duration,optional = None):
    start_infos = start.split(" ")
    start_hour,start_minute = start_infos[0].split(":")
    duration_hour,duration_minute = duration.split(":")
    start_hour = int(start_hour);start_minute = int(start_minute)
    duration_hour = int(duration_hour);duration_minute = int(duration_minute)
    hour = start_hour + duration_hour + int((start_minute + duration_minute)/60)
    minute = (start_minute + duration_minute)%60;time= for_hour(hour);n_day = get_day(start_infos[1],hour);cirs=get_cirs(start_infos[1],hour)
    if(optional):
        day = get_name_day(n_day,days.index(optional.capitalize())+1)
        return get_formatage(time,minute,cirs,n_day,day) 
    return get_formatage(time,minute,cirs,n_day) 
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("8:16 PM", "466:02"))
print(add_time("11:59 PM", "24:05"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:40 AM", "0:25"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:55 AM", "3:12"))
print(add_time("3:30 PM", "2:12"))
print(add_time("5:01 AM", "0:00"))
