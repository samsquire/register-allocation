instructions = [
  # expression, operation, source_var, operand, target_var
  ("a = 3", "set", "a", 3, "a"),
  ("a = a + 2", "add", "a", "2", "a"),
  
  ("b = a * 2", "multiply", "a", "2", "b"),
  ("d = 7", "set", "d", "7", "d")
]

def merge_ranges(ranges):
  merged_range = []
  left_position = 0
  right_position = 1
  while right_position < len(ranges):
    left = ranges[left_position]
    right = ranges[right_position]
    if left[0] == right[0]:
      # print("found variable")
      if left[2] + 1 == right[1]:
        merged = (left[0], left[1], right[2])
        merged_range.append(merged)
        print("merged range", merged)
      else:
        merged_range.append(left)
        merged_range.append(right)
    else:
      merged_range.append(left)
      merged_range.append(right)
    left_position = left_position + 2
    right_position = right_position + 2

  if len(ranges) % 2 == 1:
    merged_range.append(ranges[len(ranges) - 1])
 
  return merged_range

def live_ranges(vars, instructions):
  ranges = []
  for var in vars:
    stack = []
    for pc, instruction in enumerate(instructions):
      if instruction[2] == var or instruction[4] == var:
        stack.append(pc)
        if len(stack) == 2:
          end, start = stack.pop(), stack.pop()
          ranges.append((var,  start, end ))
          print("appending range", start, end)
    if len(stack) > 0:
        for item in stack:
          end, start = item, item
          ranges.append((var,  start, end ))
  print(ranges)
  current_length = len(ranges)
  previous_length = -1
  while previous_length != current_length:
    previous_length = current_length
    ranges = merge_ranges(ranges)
    current_length = len(ranges)
    print(current_length)
  return ranges

print(live_ranges(["a", "b", "d"], instructions))