---
id: 2234
title: 'Loop Scope Invariant Rule'
date: '2019-04-10T16:19:41+01:00'
author: 'Dominic Steinhöfel'
layout: revision
guid: 'https://www.key-project.org/2019/04/10/936-revision-v1/'
permalink: '/?p=2234'
---

<div class="row"><div class="col-md-3 col-md-push-9"><div class="no_bullets" id="toc_container">Contents

- [Complete Statistics Table](#Complete_Statistics_Table)
- [Complementary Files](#Complementary_Files)
    - [Loop Scope Invariant Rule](#Loop_Scope_Invariant_Rule)
    - [State Merging in Loops](#State_Merging_in_Loops)

</div></div><div class="col-md-9 col-md-pull-3"><span aria-hidden="true" class="glyphicon glyphicon-info-sign"></span>This page supplies additional material for the paper “*A New Invariant Rule for the Analysis of Loops with Non-standard Control Flows*“, accepted for iFM 2017.

The [extended technical report](https://tubiblio.ulb.tu-darmstadt.de/105053/) based on the iFM submission can be found [here](https://tubiblio.ulb.tu-darmstadt.de/105053/). The technical report additionally contains material that we had to leave out in the submission for space reasons. ## <span id="Complete_Statistics_Table">Complete Statistics Table</span>

<style type="text/css">
            table#stats-table th {<br />
                text-align: center;<br />
                border: 0;<br />
                padding: 0;<br />
            }<br />
           table#stats-table thead {<br />
                border-top: 2px solid #ddd;<br />
                border-bottom: 1px solid #ddd;<br />
            }            table#stats-table thead tr:first-child th {<br />
                padding-top: 8px;<br />
            }<br />
            table#stats-table thead tr:last-child th {<br />
                padding-bottom: 8px;<br />
            }<br />
            table#stats-table td {<br />
                text-align: right;<br />
            }<br />
            table#stats-table td:first-child {<br />
                text-align: left;<br />
            }<br />
            table#stats-table .egood {<br />
                color: green;<br />
            }<br />
            table#stats-table .ebad {<br />
                color: red;<br />
            }<br />
            table#stats-table .emedium {<br />
                color: gray;<br />
            }<br />
        </style><div class="table-responsive">| Problem | Proof Nodes | % Diff. | Symb.Ex.Steps | % Difference |
|---|---|---|---|---|
|  | Old Rule | Loop Scope Rule | \# Nodes | Old Rule | New Rule | \# Symb.Ex.Steps |
| coincidence\_count | 14.199 | 50.957 | <span class="ebad">258.88</span> | 210 | 153 | <span class="egood">-27.14</span> |
| ArrayList.remove.1 | 12.269 | 14.575 | <span class="ebad">18.80</span> | 258 | 191 | <span class="egood">-25.97</span> |
| saddleback\_search | 30.119 | 32.203 | <span class="ebad">6.92</span> | 235 | 181 | <span class="egood">-22.98</span> |
| list\_recursiveSpec | 5.243 | 5.557 | <span class="ebad">5.99</span> | 184 | 170 | <span class="egood">-7.61</span> |
| removeDups | 19.891 | 19.736 | <span class="emedium">-0.78</span> | 373 | 308 | <span class="egood">-17.43</span> |
| ArrayList\_add | 6.451 | 6.380 | <span class="emedium">-1.10</span> | 458 | 444 | <span class="egood">-3.06</span> |
| polishFlagSort | 4.299 | 4.242 | <span class="emedium">-1.33</span> | 93 | 83 | <span class="egood">-10.75</span> |
| ArrayList\_concatenate | 23.205 | 22.585 | <span class="emedium">-2.67</span> | 641 | 564 | <span class="egood">-12.01</span> |
| list\_recursiveSpec | 6.131 | 5.937 | <span class="egood">-3.16</span> | 216 | 184 | <span class="egood">-14.81</span> |
| BinarySearch\_search | 4.462 | 4.269 | <span class="egood">-4.33</span> | 182 | 149 | <span class="egood">-18.13</span> |
| Simple\_square | 840 | 794 | <span class="egood">-5.48</span> | 53 | 42 | <span class="egood">-20.75</span> |
| MemoryAllocator\_alloc | 1.067 | 1.003 | <span class="egood">-6.00</span> | 90 | 77 | <span class="egood">-14.44</span> |
| reverseArray | 5.348 | 4.997 | <span class="egood">-6.56</span> | 151 | 139 | <span class="egood">-7.95</span> |
| Node\_search | 7.768 | 7.256 | <span class="egood">-6.59</span> | 97 | 57 | <span class="egood">-41.24</span> |
| gcdHelp-post | 2.634 | 2.456 | <span class="egood">-6.76</span> | 39 | 28 | <span class="egood">-28.21</span> |
| ExampleSubject\_addObserver | 4.557 | 4.241 | <span class="egood">-6.93</span> | 168 | 133 | <span class="egood">-20.83</span> |
| Queens\_isConsistent | 3.677 | 3.420 | <span class="egood">-6.99</span> | 167 | 135 | <span class="egood">-19.16</span> |
| ArrayList.enlarge | 3.051 | 2.824 | <span class="egood">-7.44</span> | 106 | 79 | <span class="egood">-25.47</span> |
| ArrayList.contains | 2.414 | 2.225 | <span class="egood">-7.83</span> | 98 | 60 | <span class="egood">-38.78</span> |
| UpdateAbstraction\_ex9\_secure | 1.457 | 1.319 | <span class="egood">-9.47</span> | 183 | 162 | <span class="egood">-11.48</span> |
| MemoryAllocator\_alloc\_unsigned | 1.362 | 1.232 | <span class="egood">-9.54</span> | 91 | 78 | <span class="egood">-14.29</span> |
| ArrayList\_enlarge | 2.764 | 2.499 | <span class="egood">-9.59</span> | 152 | 125 | <span class="egood">-17.76</span> |
| arrayMax | 1.921 | 1.734 | <span class="egood">-9.73</span> | 97 | 72 | <span class="egood">-25.77</span> |
| arrayFillNonAtomic | 5.376 | 4.852 | <span class="egood">-9.75</span> | 294 | 268 | <span class="egood">-8.84</span> |
| ArrayList\_enlarge | 3.195 | 2.871 | <span class="egood">-10.14</span> | 157 | 130 | <span class="egood">-17.20</span> |
| SumAndMax\_sumAndMax | 4.101 | 3.676 | <span class="egood">-10.36</span> | 140 | 114 | <span class="egood">-18.57</span> |
| ArrayList.add | 2.302 | 2.060 | <span class="egood">-10.51</span> | 144 | 131 | <span class="egood">-9.03</span> |
| LinkedList\_get\_normal | 6.889 | 6.160 | <span class="egood">-10.58</span> | 184 | 159 | <span class="egood">-13.59</span> |
| segsum | 822 | 727 | <span class="egood">-11.56</span> | 64 | 51 | <span class="egood">-20.31</span> |
| removeDups\_arrayPart | 1.735 | 1.533 | <span class="egood">-11.64</span> | 102 | 89 | <span class="egood">-12.75</span> |
| reverseArray2 | 2.224 | 1.964 | <span class="egood">-11.69</span> | 134 | 110 | <span class="egood">-17.91</span> |
| selection\_sort | 5.512 | 4.829 | <span class="egood">-12.39</span> | 278 | 205 | <span class="egood">-26.26</span> |
| ArrayList.remFirst | 2.485 | 2.175 | <span class="egood">-12.47</span> | 168 | 133 | <span class="egood">-20.83</span> |
| loop2 | 1.032 | 892 | <span class="egood">-13.57</span> | 83 | 57 | <span class="egood">-31.33</span> |
| AddAndMultiply\_add | 1.351 | 1.165 | <span class="egood">-13.77</span> | 109 | 83 | <span class="egood">-23.85</span> |
| oldForParams | 544 | 469 | <span class="egood">-13.79</span> | 48 | 37 | <span class="egood">-22.92</span> |
| cubicSum | 909 | 775 | <span class="egood">-14.74</span> | 64 | 53 | <span class="egood">-17.19</span> |
| permissions\_method3 | 1.656 | 1.401 | <span class="egood">-15.40</span> | 91 | 57 | <span class="egood">-37.36</span> |
| contains | 1.021 | 863 | <span class="egood">-15.48</span> | 73 | 49 | <span class="egood">-32.88</span> |
| sum0 | 769 | 646 | <span class="egood">-15.99</span> | 85 | 58 | <span class="egood">-31.76</span> |
| project | 6.137 | 5.088 | <span class="egood">-17.09</span> | 433 | 293 | <span class="egood">-32.33</span> |
| for\_ReferenceArray | 664 | 550 | <span class="egood">-17.17</span> | 70 | 44 | <span class="egood">-37.14</span> |
| for\_Array | 827 | 684 | <span class="egood">-17.29</span> | 95 | 68 | <span class="egood">-28.42</span> |
| ArrayList\_get | 1.830 | 1.496 | <span class="egood">-18.25</span> | 157 | 121 | <span class="egood">-22.93</span> |
| loopInvFree | 403 | 329 | <span class="egood">-18.36</span> | 56 | 44 | <span class="egood">-21.43</span> |
| sum2 | 785 | 631 | <span class="egood">-19.62</span> | 100 | 58 | <span class="egood">-42.00</span> |
| sum1 | 939 | 753 | <span class="egood">-19.81</span> | 85 | 58 | <span class="egood">-31.76</span> |
| sum3 | 820 | 646 | <span class="egood">-21.22</span> | 100 | 58 | <span class="egood">-42.00</span> |
| ArrayList\_contains\_dep | 6.069 | 4.393 | <span class="egood">-27.62</span> | 396 | 213 | <span class="egood">-46.21</span> |
| ArrayList.remove.0 | 3.689 | 2.473 | <span class="egood">-32.96</span> | 186 | 69 | <span class="egood">-62.90</span> |
| jml-information-flow | 48.215 | 31.659 | <span class="egood">-34.34</span> | 474 | 369 | <span class="egood">-22.15</span> |
| Simple\_unnecessaryLoopInvariant | 110 | 71 | <span class="egood">-35.45</span> | 27 | 13 | <span class="egood">-51.85</span> |
| lcp | 3.132 | 1.927 | <span class="egood">-38.47</span> | 235 | 104 | <span class="egood">-55.74</span> |
| for\_Iterable | 622 | 300 | <span class="egood">-51.77</span> | 130 | 58 | <span class="egood">-55.38</span> |

</div>## <span id="Complementary_Files">Complementary Files</span>

Below you find the versions of KeY needed to reproduce the examples mentioned in the paper, as well as the problem (`.key`) and proof (`.proof`) files representing the examples. You can download the KeY versions using the green buttons. After downloading and unzipping the linked files, start KeY by running `java -jar KeY.jar` in the newly created directory. A Java Runtime Environment of version 8 or higher is required to start the KeY versions linked on this page. **If a file won’t load, please check that there has not been an absolute directory path accidentally left over** (`.key` and `.proof` files are plain text files, just open them with an editor if there is a problem). *If you have questions regarding or problems with running KeY or loading the provided examples, please feel free to contact “steinhoefel (a-t) cs.tu-darmstadt.de” .*### <span id="Loop_Scope_Invariant_Rule">Loop Scope Invariant Rule</span>

Below you find the KeY version including the loop scope invariant rule, as well as the examples mentioned in the paper, once for the old and once for the new rule. When loading an existing `.proof` (or `.key`) file, the information about which invariant rule to use is already encoded in the file header. Otherwise, you can switch between the invariant rules by setting the desired value for “Loop treatment” in the “Proof Search Strategy” tab of KeY. Please use the corresponding KeY versions when loading `.proof` files for the examples with the old and the new rule. [<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> KeY version with the Loop Scope Invariant Rule](/material/loopscopes/key-2.7_loopScopeInvRule.zip)[<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> KeY version with the old invariant rule](/material/loopscopes/key-2.7_oldInvRule.zip)[<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> KeY input files for the new rule](/material/loopscopes/loopScopeExamples.zip)[<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> KeY input files for the old rule](/material/loopscopes/oldInvRuleExamples.zip)The archives with example files may contain more files than actually referenced in the paper. The `.proof` files relevant for the paper are: ```
<pre style="height: 300px;">/heap/block_contracts/Simple__unnecessaryLoopInvariant.key.proof
/heap/coincidence_count/project.key.proof
/heap/comprehensions/bprodSplit.key.proof
/heap/comprehensions/segsum.key.proof
/heap/comprehensions/sum0.key.proof
/heap/comprehensions/sum1.key.proof
/heap/comprehensions/sum2.key.proof
/heap/comprehensions/sum3.key.proof
/heap/fm12_01_LRS/lcp.key.proof
/heap/javacard/arrayFillNonAtomic.key.proof
/heap/list/ArrayList_concatenate.key.proof
/heap/list/ArrayList_contains_dep.key.proof
/heap/list/ArrayList_enlarge.key.proof
/heap/list_ghost/ArrayList_enlarge.key.proof
/heap/list/LinkedList_get_normal.key.proof
/heap/list_recursiveSpec/ListOperationsNonNull_getNextNN_normal_behavior.key.proof
/heap/list_recursiveSpec/ListOperationsNonNull_setValueAt_normal_behavior.key.proof
/heap/list_seq/ArrayList.contains.key.proof
/heap/list_seq/ArrayList.enlarge.key.proof
/heap/list_seq/ArrayList.remove.0.key.proof
/heap/list_seq/ArrayList.remove.1.key.proof
/heap/observer/ExampleSubject_addObserver.key.proof
/heap/permissions/permissions_method3.key.proof
/heap/removeDups/arrayPart.key.proof
/heap/removeDups/contains.key.proof
/heap/removeDups/removeDup.key.proof
/heap/saddleback_search/Saddleback_search.key.proof
/heap/SemanticSlicing/project.key.proof
/heap/simple/loop2.key.proof
/heap/simple/oldForParams.key.proof
/heap/simple/selection_sort.key.proof
/heap/SmansEtAl/ArrayList_add.key.proof
/heap/vacid0_01_SparseArray/MemoryAllocator_alloc.key.proof
/heap/vacid0_01_SparseArray/MemoryAllocator_alloc_unsigned.key.proof
/heap/vstte10_01_SumAndMax/SumAndMax_sumAndMax.key.proof
/heap/vstte10_03_LinkedList/Node_search.key.proof
/heap/vstte10_04_Queens/Queens_isConsistent.key.proof
/heap/WeideEtAl_01_AddAndMultiply/AddAndMultiply_add.key.proof
/heap/WeideEtAl_02_BinarySearch/BinarySearch_search.key.proof
/newBook/09.list_modelfield/ArrayList.add.key.proof
/newBook/09.list_modelfield/ArrayList.remFirst.key.proof
/standard_key/arith/cubicSum.key.proof
/standard_key/arith/euclidean/gcdHelp-post.key.proof
/standard_key/arith/gemplusDecimal/add.key.proof
/standard_key/java_dl/arrayMax.key.proof
/standard_key/java_dl/java5/for_Array.key.proof
/standard_key/java_dl/java5/for_Iterable.key.proof
/standard_key/java_dl/java5/for_ReferenceArray.key.proof
/standard_key/java_dl/jml-free/loopInvFree.key.proof
/standard_key/java_dl/jml-information-flow.key.proof
/standard_key/java_dl/polishFlagSort.key.proof
/standard_key/java_dl/reverseArray2.key.proof
/standard_key/java_dl/reverseArray.key.proof
```

For the manually improved outlier proofs discussed in the paper, the additionally relevant files are `/heap/coincidence_count/project.key.manually-optimized.proof` (in the archive with files for the new rule) and `./standard_key/java_dl/jml-information-flow.key.manually-improved.proof` (in the archive for the old rule). ### <span id="State_Merging_in_Loops">State Merging in Loops</span>

Below you find the KeY version which additionally includes an (experimental) implementation of the discussed state merging approach for loops. There is a “Taclet Option” for setting this technique on or off; it’s accessible by “Options” &gt; “Taclet Options” &gt; “mergeAfterLoopScope”. When loading an existing `.key` or `.proof` file, the option is set according to the specification in the file. The examples contain several `.key` files for starting from scratch with the “partially unrolled find” method discussed in the paper based on different settinsg, as well as finished `.proof` files. [<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> KeY version for state merging in loops](/material/loopscopes/key-2.7_loopScopeInvRule-StateMerging.zip)[<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> KeY input files for state merging](/material/loopscopes/LoopScopeInvRule-StateMerging-ProofsAndKeYFiles.zip)</div></div>