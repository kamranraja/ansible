#!/usr/bin/python
# Kamran Raja
# 1/5/2015
# This utility will organize your Ansible inventory files in alphabetical order
# Arguments: Provide the file name as the only argument 

import sys

file_name = sys.argv[1]

lines = []
groups = []

try: 
  file = open(file_name,'r+w')
  for line in file:
    lines.append(line.strip())
  # Throw in a white space at the end, just in case there isn't one already
  lines.append('\r')
except Exception as e:
  print e
finally:
  file.seek(0,0)

# Strip out the group names
for i in lines:
  if '[' in i:
    groups.append(i.strip('[').strip(']'))

# Iterate over each group alphabetically
for group in sorted(groups):
  group_name = "[{:s}]".format(group)
  found = False

  # Iterate over every line in the file
  for line in lines:
    # When we find that group  name
    if group_name in line or found is True:
      found = True
      # After removing whitespace, if the line is not blank (indicting the end of a group definition
      if line.strip():
        file.write(str(line + '\n'))
      # This is probably the end of this groups definition
      else:
        file.write('\n')
        break

file.close()
