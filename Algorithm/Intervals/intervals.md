## 1. What is an Intervals

An interval represents a range of values, usually defined by a start point and an end point

- **Representation:** usually an array or object: `[start, end]`
- **Mathematical Notation:** [a, b] where a ≤ b

## 2. Core Relationships Between Intervals

When you have two intervals, **A** `[a_start, a_end]` and **B** `[b_start, b_end]`, there are only a few ways they can interact.

### The Three Main Cases

Assume we have sorted the intervals so that `a_start <= b_start`

1. Non-Overlapping (Disjoint):

   `b_start > a_end`

   _Logic:_ They are separate. You usually move to the next pair.

2. Overlapping (Mergeable):

   `b_start <= a_end`

   _Logic:_ You often need to merge them. The new end becomes the maximum of the two ends

3. Completely Nested (Subset):

   `b_start >= a_start` AND `b_end <= a_end`

   _Logic:_ Usually, you keep the larger interval (A) or discard the smaller one (B), depending on the problem goal

## 3. The "Golden Rule" of Interval Problems

> Sort by Start Time

Almost 90% of interval problems require you to sort the input array based on the **start time** as the first step.

- **Why?** If the intervals are sorted, you only need to compare the current interval with the _previous_ one. You don't need to compare every interval with every other interval.
- **Complexity:** This sets the time complexity to **O(N log N)** (due to sorting).

## 4. Common Algorithmic Patterns

- The "Merge" Pattern (Greedy)

  1. **Sort** intervals by start time
  2. Create a `result` list and add the first interval
  3. Iterate through the rest
  4. Compare the `current` interval with the `last` interval in the result list
     - **If Overlap:** Update the `last` interval's end time to `max(last.end, current.end)`
     - **If No Overlap:** Push the `current` interval into the `result` list.

- The "Sweep Line" Pattern
  Used for problems like **Meeting Rooms II** (finding the maximum number of concurrent events).
  1. Separate all start times and end times into two arrays.
  2. **Sort** both arrays.
  3. Use two pointers (one for starts, one for ends).
     - If `start_time < end_time`: A meeting has started. Increment count (`+1`). Move start pointer.
     - If `start_time >= end_time`: A meeting has ended. Decrement count (`1`). Move end pointer.
