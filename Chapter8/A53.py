import heapq

prio_queue = []
for _ in range(int(input())):
    query = input().split()
    if query[0]=="1":
        heapq.heappush(prio_queue,int(query[1]))
    elif query[0]=="2":
        print(prio_queue[0])
    else:
        heapq.heappop(prio_queue)


"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ba
"""
