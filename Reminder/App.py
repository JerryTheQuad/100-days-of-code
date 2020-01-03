import time

print('What shall I remind you about?')
text = str(input())

print('In how many minutes?')
#Multiplying the next variable by 60 because time.sleep counts in seconds
local_time = float(input()) * 60

time.sleep(local_time)

print(text)
