# CP_project
This project was a collaboration between me and three other classmates for a coding class at university in 2022. We had one month to complete the project. The primary goal was to find the original DNA sequence using a given list of DNA fragments. 
Our professor had provided us the following information to kickstart the project : 

We made several assumptions for this:

1. No errors in the fragments (missing or altered symbols)
2. The direction of the fragments is always the same
3. No large blocks of repeating sequences
4. Complete coverage of the sequence
5. Considering only maximal overlaps between sequences
   
The approach we took involved creating an "overlap graph" where each node is a DNA fragment. An edge exists from one fragment 'w' to another fragment 'w'' with a weight 'k' if a suffix of 'w' is a prefix of 'w'' with length 'k'. Edges with weight 0 are ignored. We also discard any fragment that appears entirely within another, as it doesn't provide any alignment information.

The paths in the overlap graph produce alignments of the nodes in the path. Since we aim to align all fragments without repetition, we're looking for Hamiltonian paths—paths that visit each node exactly once. The goal is to find the Hamiltonian path with the maximum overlap, thus producing the smallest consensus sequence.

Finding this path is computationally challenging, and there's no efficient algorithm for it. Therefore, we used a probabilistic approach with a greedy bias. At each node, the algorithm selects the next node with the highest overlap with high probability. This process restarts multiple times to explore various paths randomly. The algorithm keeps track of the Hamiltonian path with the highest overlap found during all the restarts and returns this value.





