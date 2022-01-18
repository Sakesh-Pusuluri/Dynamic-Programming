class Solution:
    def carPooling(self, trips, capacity):
        trips = sorted(trips, key=lambda x: x[1])
        heap = []
        rem_cap = 0

        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                 rem_cap -= heappop(heap)[-1]

            rem_cap += trip[0]
            if rem_cap > capacity:
                return False
            trip = (trip[2], trip[1], trip[0])
            heappush(heap, trip)

        return True
