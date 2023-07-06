def f(x):
  return x**3 + x

N = int(input())

Left = 0.0
Right = 100.0
for i in range(20):
  Mid = (Left + Right) / 2
  val = f(Mid)
  
  if val > N:
    Right = Mid
  else:
    Left = Mid

print(Mid)
