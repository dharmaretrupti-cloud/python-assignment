

attendance = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# count = sum(attendance)
# print("present_days=:",count)
# output :7

# absent_count = len(attendance) - sum(attendance)
# print("absent_days=:", absent_count)
# output :3

# attendance_percentage = (sum(attendance)/len(attendance)) *100
# print("Attendance percentage=:",attendance_percentage)
# output : 70.0


attendance_percentage = (sum(attendance) / len(attendance)) * 100
if attendance_percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")


# Longest present streak
max_streak = 0
current_streak = 0

for day in attendance:
    if day == 1:
        current_streak += 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
        current_streak = 0

if current_streak > max_streak:
    max_streak = current_streak

print("Longest present streak:", max_streak)
