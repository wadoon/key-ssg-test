---
id: 2103
title: 'Proving JDK’s Dual Pivot Quicksort Correct'
date: '2018-12-08T14:28:52+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'https://www.key-project.org/2018/12/08/1387-revision-v1/'
permalink: '/?p=2103'
---

*by Bernhard Beckert, Jonas Schiffl, Peter H. Schmitt and Mattias Ulbrich*Sorting is a fundamental functionality in libraries, for which efficiency is crucial. Correctness of the highly optimized implementations is often taken for granted. [De Gouw et al.](http://envisage-project.eu/wp-content/uploads/2015/02/sorting.pdf) have shown that this certainty is deceptive by revealing [a bug in the Java Development Kit (JDK) implementation of TimSort](http://www.envisage-project.eu/proving-android-java-and-python-sorting-algorithm-is-broken-and-how-to-fix-it/). We have now formally analysed the *other* implementation of sorting in the JDK standard library: A highly efficient implementation of a dual pivot quicksort algorithm. We were able to deductively prove that the algorithm implementation is correct. However, a loop invariant which is annotated to the source code does not hold. This post reports on the successful case study in which KeY was applied to a non-trivial real-world implementation of a non-trivial algorithm. [**Please find all details in the paper.**](https://formal.iti.kit.edu/biblio/?lang=en&key=BeckertSchifflEA2017)## Target of the Verification Task

### Algorithm

<figure aria-describedby="caption-attachment-1397" class="wp-caption aligncenter" id="attachment_1397" style="width: 663px">![Illustration of a dual pivot partition](https://www.key-project.org/wp-content/uploads/2017/08/dual-pivot-quicksort.png)<figcaption class="wp-caption-text" id="caption-attachment-1397">Illustration of a dual pivot partition</figcaption></figure>While the worst-case runtime complexity of comparison-based sorting algorithms is known to be in the class O(n log(n)), there have been numerous attempts to reduce their “practical” complexity. In 2009, [Vladimir Yaroslavskiy suggested a variation of the quicksort algorithm](http://codeblab.com/wp-content/uploads/2009/09/DualPivotQuicksort.pdf) that uses two pivot elements. The figure above exemplarily illustrates the arrangement of the array elements after the partitioning step. The pivot elements are shown as hatched bars. The first part (green in the figure) contains all elements smaller than the smaller pivot element, the middle part (blue) contains all elements between the pivots (inclusively), and the third part (red) consists of all elements greater than the larger pivot. The algorithm proceeds by sorting the three parts recursively by the same principle. Extensive benchmarking led to the adoption of Yaroslavskiy’s Dual Pivot Quicksort implementation as the OpenJDK 7 standard sorting function for primitive data type arrays in 2011. Conclusive explanations for its superior performance appear to be surprisingly hard to find, but evidence points to cache effects. Wild et al. conclude: > “The efficiency of Yaroslavskiy’s algorithm in practice is caused by advanced features of modern processors. In models that assign constant cost contributions to single instructions – i.e., locality of memory accesses and instruction pipelining are ignored – classic Quicksort is more efficient.”

### Implementation

We formally analysed the class `<a href="http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/8-b132/java/util/DualPivotQuicksort.java">java.util.DualPivotQuicksort</a>` contained both in Oracle's JDK and in OpenJDK 8. Like many modern programming languages, the standard library of Java uses a portfolio of various sorting algorithms in different contexts. This class, consisting of more than 3000 lines of code, makes use of no less than four different algorithms: Merge sort, insertion sort, counting sort, and quicksort. For the `byte`, `char`, and `short` data types, counting sort is used. Arrays of other primitive data types are first scanned once to determine whether they consist of a small number of already sorted sequences; if that is the case, merge sort is used, taking advantage of the existing sorted array parts. For arrays with less than 47 entries, [insertion sort](#insertion-sort) is used. In all other cases, quicksort is used (e.g., for large integer arrays that are not partially sorted). This “default” option is the subject of our correctness proof. ## Verification Task

### Toplevel Specification

<style>
pre.java .keyword { color: darkblue; }<br />
</style>```
<pre class="java"><span class="keyword">class</span> DualPivotQuicksort {
 // ...
 
 /*@ <span class="keyword">public normal_behavior</span>
   @ <span class="keyword">ensures</span> (<span class="keyword">\forall int</span> i; 0 <= i && i < a.<span class="keyword">length</span>;
   @          (\<span class="keyword">forall int</span> j; 0 < j && j < a.<span class="keyword">length</span>; 
   @           i < j ==> a[i] <= a[j]));
   @ <span class="keyword">ensures</span> \seqPerm(\array2seq(a), \old(\array2seq(a)));
   @ <span class="keyword">assignable</span> a[*]; 
   @*/
 <span class="keyword">void</span> sort(<span class="keyword">int</span>[] a) { ... }
}
```

This JML specification covers the following aspects of the behaviour of the method sort: 1. On termination, the array is sorted in increasing order (lines 5–7).
2. On termination, the array contains a permutation of the initial array content (line 8).
3. The implementation does not modify any existing memory location except the entries of the array (line 9).
4. The method always terminates (this is the default for JML if a diverges clause has not been specified).
5. The method does not throw an exception. This is implied since the contract is declared normal behavior.

### Managing the Task

To modularise the problem, we broke down the code into smaller units by refactoring the large sort method into smaller new methods. Besides disentangling the different sorting algorithms, it significantly reduced the complexity of the individual proof obligations. The parts of the code that suggested themselves for method extraction were the partitioning implementation, the initial sorting of the five chosen elements, and several small loops for moving the indices used in the partitioning algorithm. Besides this modularisation into smaller sub-problems, we also reduced complexity by separating three parts of the requirement specification 1. the sortedness property,
2. the permutation property, and
3. the absence of integer overflows.

## Annotated Sources and Proof Files

**Sortedness Property:**- [DualPivotQuicksort\_sort.java](https://www.key-project.org/wp-content/uploads/2017/08/DualPivotQuicksort_sort.java)
- [SwapValues\_sort.java](https://www.key-project.org/wp-content/uploads/2017/08/SwapValues_sort.java)
- [SinglePivotPartition\_sort.java](https://www.key-project.org/wp-content/uploads/2017/08/SinglePivotPartition_sort.java)

**Permutation Property:**- [DualPivotQuicksort\_perm.java](https://www.key-project.org/wp-content/uploads/2017/08/DualPivotQuicksort_perm.java)
- [SwapValues\_perm.java](https://www.key-project.org/wp-content/uploads/2017/08/SwapValues_perm.java)
- [SinglePivotPartition\_perm.java](https://www.key-project.org/wp-content/uploads/2017/08/SinglePivotPartition_perm.java)

**Integer Overflow:**- [](https://www.key-project.org/wp-content/uploads/2017/08/SinglePivotParition_overflow.java)[DualPivotQuicksort\_overflow.java](https://www.key-project.org/wp-content/uploads/2017/08/DualPivotQuicksort_overflow.java)[](https://www.key-project.org/wp-content/uploads/2017/08/SinglePivotParition_overflow.java)
- [SinglePivotParition\_overflow.java](https://www.key-project.org/wp-content/uploads/2017/08/SinglePivotParition_overflow.java)
- [DualPivotQuicksort\_CBMC.java](https://www.key-project.org/wp-content/uploads/2017/08/DualPivotQuicksort_CBMC.java):This file was proved via the software bounded model checker [CBMC](http://www.cprover.org/cbmc/).

**ZIP files with all sources and proofs:**- [](https://www.key-project.org/wp-content/uploads/2017/08/DualPivot_KeY_Proofs.zip)all source: [DualPivot\_KeY\_Sources.zip](https://www.key-project.org/wp-content/uploads/2018/03/DualPivot_KeY_Sources.zip)
- all files: [DualPivot\_KeY\_Proofs.zip](https://www.key-project.org/wp-content/uploads/2017/08/DualPivot_KeY_Proofs.zip)
- employed KeY version: [key-2.7\_9c003....zip](https://www.key-project.org/wp-content/uploads/2017/08/key-2.7_9c003bb729fff7c922d356f50f89bff669d8a8da.zip)

## <a name="insertion-sort"></a>Extension: Pair Insertion Sort

If the list contains at most 47 Elements, the portfolio engine falls back to insertion sort – in spite of its worse average-case performance – to avoid the comparatively large overhead of quicksort or merge sort. To be more efficient, a variant in which two elements are sorted at a time is used in this case. The challenge to verify the algorithm has been put forth at the VerifyThis competition 2017. Michael Kirsten carried out a verification of the actual implementation using KeY. - [PairInsertionSort\_sort](https://www.key-project.org/wp-content/uploads/2017/08/PairInsertionSort.java)
- [PairInsertionSort\_sort\_proof](https://www.key-project.org/wp-content/uploads/2017/08/PairInsertionSort_sort_proof.zip)