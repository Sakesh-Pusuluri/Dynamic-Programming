import heapq

class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

def find_max_cpu_load(jobs):
  # TODO: Write your code here
  jobs.sort(key = lambda x:x.start)
  minHeap=[(jobs[0].end,jobs[0].start,jobs[0].cpu_load)]
  heapq.heapify(minHeap)
  maxCapacity = jobs[0].cpu_load
  ans=0
  for i in range(1,len(jobs)):
    if(jobs[i].start<=minHeap[0][0]):
      maxCapacity+=jobs[i].cpu_load
      heapq.heappush(minHeap,(jobs[i].end,jobs[i].start,jobs[i].cpu_load))
    else:
      while minHeap and minHeap[0][0] <= jobs[i].start:
        a,b,c = heapq.heappop(minHeap)
        maxCapacity-=c
      maxCapacity+=jobs[i].cpu_load
      heapq.heappush(minHeap,(jobs[i].end,jobs[i].start,jobs[i].cpu_load))
    ans=max(ans,maxCapacity)
  return ans

def main():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()


# Time complexity - O(NlogN)
# Space complexity - O(N)

