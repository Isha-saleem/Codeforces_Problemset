
# #677A
n, h = map(int, input().split())
heights = list(map(int, input().split()))
width = 0
for i in heights:
  if i > h:
    width += 2
  else:
    width += 1
print(width)
