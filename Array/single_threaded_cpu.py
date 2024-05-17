# You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the ith task will be available to process at enqueueTimei and will take processingTimei to finish processing.

# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.

class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key=lambda x: x[0])

        idx = 0
        minHeap = []
        current_time = tasks[0][0]
        final_arr = []
        while minHeap or idx < len(tasks):
            while idx < len(tasks) and tasks[idx][0] <= current_time:
                heapq.heappush(minHeap, [tasks[idx][1], tasks[idx][2]])
                idx += 1

            if not minHeap:  # when its empty
                current_time = tasks[idx][0]
            else:
                curr_val, i = heapq.heappop(minHeap)
                current_time += curr_val
                final_arr.append(i)

        return final_arr
