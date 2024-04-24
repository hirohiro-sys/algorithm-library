queue = []
for i in range(int(input())):
  a = input().split()
  if a[0]=="1":
    queue.append(a[1])
  elif a[0]=="2":
    print(queue[0])
  else:
    queue.pop(0)


"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_az
"""
