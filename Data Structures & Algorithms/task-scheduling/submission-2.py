class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1
        
        task_heap = []
        wait_queue = deque()

        for task, count in task_count.items():
            heapq.heappush_max(task_heap, count)

        t = 0
        while wait_queue or task_heap:
            t += 1
            # If element at front of the queue has waited enough,
            # add it back to the heap
            if wait_queue and t - wait_queue[0][1] > n:
                count, _ = wait_queue.popleft()
                heapq.heappush_max(task_heap, count)
                
            # If heap is empty, there are no tasks ready to be run
            # This is a wasted CPU cycle
            if task_heap:
                count = heapq.heappop_max(task_heap)
                # If this task needs to run again, add it to queue
                if count > 1:
                    wait_queue.append((count - 1, t))
            else:
                t = wait_queue[0][1] + n
            #     task = '-'
            
            # print(f'{t} {task}')
        
        return t
            
