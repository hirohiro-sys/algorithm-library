s = input()
stack = []
for i in range(len(s)):
  if s[i]=="(":
    stack.append(i+1)
  else:
    print(stack.pop(),i+1)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dx
"""
