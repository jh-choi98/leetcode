# Data structures and algorithms

When it comes to coding, thinking out loud and creating a dialogue with
your interviewer is key.

## Data structures and algorithms overview

Your interviewer will ask you to solve a data structure oriented
problem. You will then write code using the appropriate data structure
to solve the problem. You'll also be expected to compare various
approaches and explain why the one you selected was the right one.

### What does the data structures and algorithms competency assess?

This competency measures your ability to choose the most efficient
run-time solutions. For example, different data structures are more
performant for reading data while others are more performant for
writing. Algorithms should be as fast as possible and, of course, solve
the problem correctly. Look out for edge cases for which your algorithm
fails to satisfy requirements.

### How should I best prepare for this competency?

- Consider runtimes for common operations and understand how they use memory.
- Understand data structures you encounter in core libraries (e.g., trees, hash maps, lists, arrays, queues, etc.)
- Understand common algorithms (e.g., traversals), divide and conquer, when to use breadth first vs. depth first recursion.
- Discuss runtimes, theoretical limitations, and basic implementation
  strategies for different cases of algorithms.

#### Suggested areas of refresh:

- Binary search tree data.
- Scalability methods—With the architecture, there are many techniques
  and methods which can be used in order to customize and improve the
  design of a system. Some of the most widely used are: redundancy,
  partitioning, caching, indexing, load balancing, and queues.

## How to best showcase data structures and algorithms

Here we give you a peek at what strong data structures and algorithms
skills looks like for Amazon SDEs, as well as tips from our interviewers
on how you can demonstrate these skills in your interview.

### Criteria and pro tips for addressing them

#### Optimization

Criteria: Use optimal data structures and algorithms to solve the problem.

Tips:

- Build a toolbox of what data structures would be useful in common scenarios such as efficient access by key/object/position, maintaining sort order, searching, and finding maximums/minimums. Also think about edge cases where your chosen data structure may not function as intended - for example with hash-based data structures what happens when there is a hash collision, or what a degenerate binary tree looks like and why.
- Be familiar with the features, data structures, and algorithms in your programming language(s) of choice. If you dive deep into these it might introduce you to data structures you may not normally see/use so you can expand your toolbox for solving problems.
- If you're comparing two data structures or algorithms that each have
  some drawback (very common!), pick one and give a justification for
  it. Remember to explain the benefit, operations, and time complexity.

#### Identity Shortcomings

Criteria: Identify potential shortcomings and discuss tradeoffs with different data structures and algorithms.

Tips:

- As a candidate make sure to clarify the shortcoming/issues you can expect by using the solution you are planning to implement. If you know a better DataStructure that can address those shortcomings but you are not confident in using it in your solution, make sure to mention and discuss this with your interviewer as well before you start with using the DS you are confident to use.
- Try to identify the pattern for the given problem, but don't
  overcomplicate it. Could it be solved using recursion, say specifically
  DFS? Could it fit into the bucket of dynamic programming? Can you
  achieve a solution using a linear data structure like array instead of a
  non-linear one like heap?

#### Justification

Criteria: Justify why the selected data structures and algorithm was used.

Tips:

- There is always more than one way to solve the problem. If you identify other solutions, explain why you are using the one you are, this shows a good understanding of the Algorithm and the problem.
- Be prepared to talk about your understanding of the data structures
  you choose and answer questions about how those data structures work
  under the hood. Do you know multiple ways of resolving collisions in
  hash maps? Why is heap insertion O (log n)? Answering these questions
  gives us confidence you understand the data structures and have not
  just memorized their answers.

#### Runtime and Space Tradeoffs

Criteria: Demonstrate a solid grasp of runtime and space complexity tradeoffs even if not perfectly accurate O(n) syntax.

Tip:

- If the interviewer asks you a real-world problem, first zoom out and think through all relevant possible data structures and algorithms that could be used to solve this problem. Before finalizing a solution, clarify problem constraints and consider multiple ways forward, see which are worth discussing before recommending one and going ahead with it.
