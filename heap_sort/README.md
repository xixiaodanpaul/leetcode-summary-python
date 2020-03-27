# Heap Sort

The following questions, I prefer to solve by using Heap Sort. It may have the optimal method, please check the discussion in LeetCode.  

* [Min-Heap](##Min-Heap)
* [Max-Heap](##Max-Heap)

## Min-Heap

This type of problem includes: find the kth smallest problem, find the kth rare problem， find minimum cost problem

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 373 | https://leetcode.com/problems/find-k-pairs-with-smallest-sums/ | |
| 1167 | https://leetcode.com/problems/minimum-cost-to-connect-sticks/ | |
| 1167* | https://leetcode.com/discuss/interview-question/344677| [this link](../python_practice/amazon/min_cost_to_connect_ropes.py) |  

## Max-Heap

This type of problem includes: find the kth largest problem, find the kth frequently problem, find maximum profit problem

Since Python's heapq implementation does not have built in support for max heap, we can just invert the values stored into the heap so it functions as a max heap. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 347 | https://leetcode.com/problems/top-k-frequent-elements/ | |
| 692 | https://leetcode.com/problems/top-k-frequent-words/ | |
| 692* | https://leetcode.com/discuss/interview-question/542597/ | [this link](../python_practice/amazon/top_k_frequently_mentioned_keywords.py) |