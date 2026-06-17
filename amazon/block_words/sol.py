
"""
    n = number of blocks
    m = length of word
    
    - Time complexity: O(n^m)
        - Building candidates: O(m * n)
        - Sorting cnadidates: O(mlogm)
        - Backtracking (worst case): O(n^m)
        
    - Space complexity: O(m * n)
        - used: O(n)
        - Recursion stack: O(m)
        - total: O(m * n)
        
    Let n be the number of blocks and m be the length of the word. Building the candidate list takes O(mn). The backtracking step is exponential in the worst case, up to O(n^m), because each character may try many unused blocks. The space complexity is O(mn) for the candidate lists, plus O(n) for the used array and O(m) for the recursion stack, so overall O(mn).
"""
def can_spell(blocks: list[tuple[str, str]], word: str) -> bool:
    """
        Each block can be used at most once.
        So if the word has more characters than the number of blocks,
        it is impossible to spell the word.
    """
    if len(word) > len(blocks):
        return False

    """
        For each character in the word, I want to know which blocks can
        be used to make that character.
        For example, if the word is "BABY", candidates[i] will store the
        list of block indices that can make word[i].
    """
    candidates = []

    for ch in word:
        possible_blocks = []

        """
            Check every block and see whether this character appears on
            that block.
            If it does, this block is a possible choice for this character.
        """
        for i, block in enumerate(blocks):
            if ch in block:
                possible_blocks.append(i)
        """
            If no block contains this character at all,
            then there is no way to spell the word.
        """
        if not possible_blocks:
            return False

        candidates.append(possible_blocks)

    """
        This is an optimization for backtracking.
        I try to place the most constrained characters first.
        For example, if one character can only be made by 1 block,
        and another character can be made by 5 blocks, it is better to
        handle the 1-block case first because it reduces branching.
        This does not change correctness. It only changes the order we search.
    """
    candidates.sort(key=len)

    """
        used[i] tells me whether block i has already benn used.
        Since each block can only be used once, we cannot reuse a block
        for multiple characters.
    """
    used = [False] * len(blocks)

    def backtrack(pos: int) -> bool:
        """
            If pos reaches the end of canadidates, that means we
            successfully assigned one unused block to every character in
            the word.
        """
        if pos == len(candidates):
            return True

        """
            candidates[pos] is the list of blocks that can make the
            current character. 
            We try each possible block and see if it leads to a valid solution.
        """
        for block_index in candidates[pos]:
            """
                If this block is already used for another character, we
                cannot use it again.
            """
            if used[block_index]:
                continue

            # Choose this block for the current character.
            used[block_index] = True

            """
                Recursively try to assign blocks for the remaining
                characters.
                If that works, we found a valid spelling.
            """
            if backtrack(pos + 1):
                return True

            """
                If choosing this block did not work, undo the choice and
                try another possible block.
            """
            used[block_index] = False

        """
            If none of the possible blocks worked for this character,
            then this path cannot spell the word.
        """
        return False

    # Start assigning blocks from the first character candidate.
    return backtrack(0)
