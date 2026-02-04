
# LAB Operators and expressions
# this is one of the lab in my Python Essentials
# Goal is to identify the end time

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_start_minutes = hour * 60 + mins #convert hour to minutes so we can total and compute for the total minutes
total_end_minutes = total_start_minutes + dura # since duration is in minutes we can get the total minutes

end_hour = (total_end_minutes // 60) % 24
end_minutes = total_end_minutes % 60

print( "End time: " ,end_hour , ":",end_minutes)

