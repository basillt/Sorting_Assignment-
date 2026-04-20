# Sorting_Assignment

**Student Name(s):**
* DEMA MOHAMED - 212931380
* BASIL TAHA - 214656852

## Chosen Algorithms

For this assignment, I chose to focus on three different sorting algorithms to demonstrate a variety of performance and approaches:

*   **Bubble Sort:** I chose this because it's one of the simplest and most basic algorithms to understand. It's not particularly efficient, but it's excellent for demonstrating how slower algorithms behave as the amount of data grows. It serves as our "reference point" for a less optimal algorithm.

*   **Merge Sort:** This is an efficient and stable "Divide and Conquer" algorithm. It always operates in O(n log n) time, making it a good choice when consistent and efficient performance is desired, regardless of the initial order of the data. It represents the group of more efficient algorithms.

*   **Quick Sort:** Also a "Divide and Conquer" algorithm, it is considered one of the fastest sorting algorithms in practice for most cases. I chose it to show the potential for high speed, although in some cases (like nearly sorted arrays) it can be less efficient than Merge Sort. It represents the faster and more complex algorithms.

## Experiment Results

### result1.png: Sorting Algorithm Comparison (Random Arrays)

![Sorting Algorithm Comparison (Random Arrays)](https://private-us-east-1.manuscdn.com/sessionFile/dJMRjijqXD6DqkC3sy2c7Q/sandbox/L0REniuHKkHQNJr4sn6XyK-images_1776690569671_na1fn_L2hvbWUvdWJ1bnR1L3Jlc3VsdDE.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZEpNUmppanFYRDZEcWtDM3N5MmM3US9zYW5kYm94L0wwUkVuaXVIS2tIUU5KcjRzbjZYeUstaW1hZ2VzXzE3NzY2OTA1Njk2NzFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxjM1ZzZERFLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=fPbR1EQ2QAYUMrbeo2m7m4kfrrMuTeSWM3vBDzUruz4u8Itizr64ObXXMXozbNnGzgYq~B3VaxaW9GLy3M7cSY7Ar8DHOFbIhAvMnmfI-MZw2CSvxTafRiuYQvYzFwwY7Ogd474NZpbHXMDInEX9RK9KmF0xCAvlxSBgo6d8-TmOm4Wkjx18juyRyua2TI6Ffp-1hVw~qbETW034sTVDwM4uzgjb963BF75Wys~WX6dnwvVD9VkV~LNDmAR8AATxsS4tQfhgEp9XDdEkY8yBNrabD9644wRZAS0q1sz4HsCusDNHUbiKAQMfcNTNnKcWXVLHRcGIiWwQhwoVJyufOA__)

In this graph, we see how the three chosen algorithms handle arrays filled with random numbers. It's clear that Bubble Sort is the slowest – as the array size increases, its running time jumps dramatically. This is exactly what we expected from an algorithm with O(n^2) complexity. In contrast, Merge Sort and Quick Sort are much faster and more efficient. Their running times increase more moderately, consistent with their O(n log n) complexity. This graph shows us how important it is to choose the right algorithm when working with large amounts of data.

### result2.png: Sorting Algorithm Comparison (Nearly Sorted Arrays, with 5% Noise)

![Sorting Algorithm Comparison (Nearly Sorted Arrays, with 5% Noise)](https://private-us-east-1.manuscdn.com/sessionFile/dJMRjijqXD6DqkC3sy2c7Q/sandbox/L0REniuHKkHQNJr4sn6XyK-images_1776690569671_na1fn_L2hvbWUvdWJ1bnR1L3Jlc3VsdDI.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZEpNUmppanFYRDZEcWtDM3N5MmM3US9zYW5kYm94L0wwUkVuaXVIS2tIUU5KcjRzbjZYeUstaW1hZ2VzXzE3NzY2OTA1Njk2NzFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxjM1ZzZERJLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=bq-cEMTZhA1sry5yun26GlcV4S1lo~0P-nmypeTre2WXcgRNcbUYuHwk7K4hVQQ97f39rNnXgO3dpiir6JArSsH30rBpffdeqAVwNOMOzOsCoQnqgKsVUx9Ute~hY8UZx3d8tPwgurRF9u56rqiNwnBuTHzmCGmuxAeu~dDtKcXjP2gCj6gNe0pPU5OVmmttNkXPgpkd5c0WM-gCawLUlr7E4Lnw9A5BuvubKlOS4JKbxvOZcfV0LMKXaZzKp6c3kR1rhWu8OxLF~bHZajGRgi3z~1CG6sLIlkOda1lp3nBjx5q6vPV7yg-KOZZv~rVJq~N~73sUVVNK74jGkG1Wlw__)

 The second graph presents a slightly different scenario: what happens when the array is already almost sorted, with only a small amount of "noise" (in this case, 5% of elements swapped randomly)? Here, we see that Bubble Sort is still slow, but perhaps slightly less so than with completely random arrays. Merge Sort and Quick Sort continue to be fast and efficient, almost to the same extent as with random arrays. This shows that they are not overly affected by the initial order of the data, as long as the noise is small. This highlights their strength as general-purpose and effective algorithms for most situations.

In summary, these experiments help us understand not only how each algorithm works, but also when to use it, and how the type of data can influence its actual performance.
