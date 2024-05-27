from datetime import datetime, timedelta
import time

offset_seconds = int(input("Offset (seconds): "))
offset_milliseconds = int(input("Offset (milliseconds): "))
mode = input("Add or subtract seconds from the existing file? (add/sub): ").lower()

if mode not in ["add", "sub"]:
  mode = "add"

sub_file = input("Subtitle file name: ")
new_sub_file = input("New subtitle file name: ")

with open(sub_file, "r") as f:
  cont = f.readlines()
  new_cont = []
  for i, line in enumerate(cont):
    if len(line) > 2 and line[2] == ':':
      timestamps = line[:-1].split(' --> ')

      time_from = datetime.strptime(timestamps[0], '%H:%M:%S,%f')
      time_to = datetime.strptime(timestamps[1], '%H:%M:%S,%f')
      
      offset = timedelta(seconds=offset_seconds, milliseconds=offset_milliseconds)
      
      new_time_from = None
      new_time_to = None
      
      if mode == 'add':
        new_time_from = time_from + offset
        new_time_to = time_to + offset
      elif mode == 'sub':
        new_time_from = time_from - offset
        new_time_to = time_to - offset
      
      new_line = new_time_from.strftime('%H:%M:%S,%f')[:-3] + ' --> ' + new_time_to.strftime('%H:%M:%S,%f')[:-3] + '\n'

      new_cont.append(new_line)
      continue
      
    new_cont.append(line)
    
  with open(new_sub_file, "w") as f:
    f.write("".join(new_cont))
    print(f"New subtitle file created as {new_sub_file}")