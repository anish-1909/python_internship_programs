#prog 5 Time Conversion
total_seconds=int(input("Enter time duration in seconds: "))
hours=total_seconds//3600
minutes= (total_seconds%3600)//60
seconds=total_seconds%60
print(f"\n Time duration of {total_seconds} seconds in HH:MM:SS format is {hours:02d}:{minutes:02d}:{seconds:02d}")