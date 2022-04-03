---
id: 1534
title: 'Coverage of Formal Specifications'
date: '2017-10-09T10:44:04+01:00'
author: 'Dominic Steinhöfel'
layout: revision
guid: 'https://www.key-project.org/2017/10/09/1274-revision-v1/'
permalink: '/?p=1534'
---

<div class="row"><div class="col-md-3 col-md-push-9"><div class="no_bullets" id="toc_container">Contents

- [Source code and Strongest Specification for “find”](#Source_code_and_Strongest_Specification_for_8220find8221)
- [Different Specifications for “find”](#Different_Specifications_for_8220find8221)
- [Coverage Results for “find” Specifications](#Coverage_Results_for_8220find8221_Specifications)
- [Tool Download and Usage Instructions](#Tool_Download_and_Usage_Instructions)

</div> </div><div class="col-md-9 col-md-pull-3"> <span aria-hidden="true" class="glyphicon glyphicon-info-sign"></span> This page supplies additional material for the extended abstract “*Assessing the Coverage of Formal Specifications*“, submitted to the PhD symposium “Algorithms, Tools and Applications” at iFM 2017.

 In the extended abstract, we discussed a simple “find” method trying to discover an element in an integer array and returning its index, or -1 if the element was not present. In the section below, you find the source code of the method, along with the strongest JML specification that we discovered using our tool. Afterward, we present several specifications and the results produced for them by the tool. Finally, we provide an executable of the prototype with some usage instructions.

 **Update** (2017/10/09): There is a new version of the tool which deviates in its output from the one discussed in the extended abstract. You find it [here](https://www.key-project.org/wp-content/uploads/2017/10/SpecCov.zip). The category of “use case facts” has been removed, the output is more verbose, and it features the possibility of interaction with the generated proof (e.g., to manually recover from prover incapacities). Also, the GUI has been improved.

## <span id="Source_code_and_Strongest_Specification_for_8220find8221">Source code and Strongest Specification for “find”</span>

 https://gist.github.com/rindPHI/c0bf00c371e9491a7598840ec5063f91 ## <span id="Different_Specifications_for_8220find8221">Different Specifications for “find”</span>

The following table shows the different specification versions for “find” which we studied, ordered by increasing strenght / coverage.

<div class="table-responsive"> | Name | Post Condition | Loop Invariant | Ghost variable | Ghost field |
|---|---|---|---|---|
| SimplePost | ```    \result == -1 \|\| arr[\result] == n ``` | ``` true ``` | X | X |
| StrongerInv | ```    \result == -1 \|\| arr[\result] == n ``` | ```    result == -1 \|\| arr[result] == n ``` | X | X |
| StrongerInvCaseDist | ```    \result == -1 \|\| arr[\result] == n ``` | ```    i >= 0 && i <= arr.length && (   result != -1     \|\| (\forall int k; k >= 0 && k < i; arr[k] != n)) && (   result == -1     \|\| arr[result] == n) ``` | X | X |
| StrongerInvConcreteResult | ```    \result == -1 \|\| arr[\result] == n ``` | ```    i >= 0 && i <= arr.length && (   result != -1     \|\| (\forall int k; k >= 0 && k < i; arr[k] != n)) && (   result == -1     \|\| arr[result] == n && result == i-1) ``` | X | X |
| StrongerPost | ```    ((\exists int i; i >= 0                  && i < arr.length;                     arr[i] == n)        ==> arr[\result] == n) && ((\forall int i; i >= 0                  && i < arr.length;                     arr[i] != n)        ==> \result == -1) ``` | ```    i >= 0 && i <= arr.length && (   result != -1     \|\| (\forall int k; k >= 0 && k < i; arr[k] != n)) && (   result == -1     \|\| arr[result] == n && result == i-1) ``` | X | X |
| InvWithLastRun | ```    ((\exists int i; i >= 0                  && i < arr.length;                     arr[i] == n)        ==> arr[\result] == n) && ((\forall int i; i >= 0                  && i < arr.length;                     arr[i] != n)        ==> \result == -1) ``` | ```    i >= 0 && i <= arr.length && i = iLastRun + 1 && (   result != -1     \|\| (\forall int k; k >= 0 && k < i; arr[k] != n)) && (   result == -1     \|\| arr[result] == n && result == i-1) ``` | ``` ghost int iLastRun = i - 1; ``` | X |
| PostWithLastRun | ```    ((\exists int i; i >= 0                  && i < arr.length;                     arr[i] == n)        ==>    arr[\result] == n            && \result == f_iLastRun) && ((\forall int i; i >= 0                  && i < arr.length;                     arr[i] != n)        ==> \result == -1) ``` | ```    i >= 0 && i <= arr.length && i = f_iLastRun + 1 && (   result != -1     \|\| (\forall int k; k >= 0 && k < i; arr[k] != n)) && (   result == -1     \|\| arr[result] == n && result == i-1) ``` | X | ``` ghost int f_iLastRun = i - 1; ``` |

 </div>## <span id="Coverage_Results_for_8220find8221_Specifications">Coverage Results for “find” Specifications</span>

The following table depicts the results produced by our implementation for the specification versions outlined above. “**Strength 1**” is a percentage coverage of *covered* and *abstractly covered* post condition, loop body and use case facts. “**Strength 2**” *only* considers *covered* post condition and loop body facts (so, *no* use case facts). “**Strength 3**” is an extension of “Strength 2” which also considers abstractly covered post condition and loop body facts. The values for “Strength 1” and “Strength 3” are *only monotonic from the third line on*, since in “SimplePost” and “StrongerInv”, there are *exception / use case facts uncovered* which makes it easier to abstractly cover facts (for instance, “true” abstractly covers all possible facts, but does not exclude any exception and usually does not imply any non-trivial method post condition).

<div class="table-responsive"> |  |  |  | Post Condition Facts | Loop Body Facts |  |  |  |
|---|---|---|---|---|---|---|---|
| Name | \# Uncovered Exception Facts | \# Uncovered Use Case Facts | Abstractly | Uncovered | Abstractly | Uncovered | Strength 1 | Strength 2 | Strength 3 |
| SimplePost | **1** | **1** | 1 | 1 | 1 | 1 | 30.00% | 0.00% | 37.50% |
| StrongerInv | **1** | 0 | 2 | 0 | 4 | 0 | 57.14% | 0.00% | 50.00% |
| StrongerInvCaseDist | 0 | 0 | 2 | 0 | 0 | 4 | 42.86% | 0.00% | 33.33% |
| StrongerInvConcreteResult | 0 | 0 | 2 | 0 | 0 | 2 | 57.14% | 33.33% | 50.00% |
| StrongerPost | 0 | 0 | 0 | 0 | 0 | 2 | 72.22% | 50.00% | 58.33% |
| InvWithLastRun | 0 | 0 | 0 | 1 | 0 | 0 | 95.45% | 87.50% | 93.75% |
| PostWithLastRun | 0 | 0 | 0 | 0 | 0 | 0 | 100% | 100% | 100% |

 </div>The chart below illustrates the progession of the strength measures.

 <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.min.js" type="text/javascript"></script>

<div style="position:relative"><canvas id="specStrChart"></canvas></div> <script type="text/javascript">
			var ctx = $("#specStrChart");
			var myLineChart = new Chart(
				ctx,
				{
					"type": "line",
					"data": {
						"labels":[
							"SimplePost",
							"StrongerInv",
							"StrongerInvCaseDist",
							"StrongerInvConcreteResult",
							"StrongerPost",
							"InvWithLastRun",
							"PostWithLastRun"
						],
						"datasets":[{
							"label": "Strength 1",
							"data": [30,57.14,42.85,57.14,72.22,95.45,100],
							"fill": false,
							"borderColor": "rgb(75, 192, 192)",
							"lineTension": 0.1
						},{
							"label": "Strength 2",
							"data": [0,0,0,33.33,50,85.5,100],
							"fill": false,
							"borderColor": "rgb(0, 255, 90)",
							"lineTension": 0.1
						},{
							"label": "Strength 3",
							"data": [37.5,50,33.33,50,58.33,93.75,100],
							"fill": false,
							"borderColor": "rgb(255, 162, 0)",
							"lineTension": 0.1
						}]
					},
					options: {
						scales: {
							xAxes: [{
								ticks: {
									"stepSize": 1,
									"min": 0,
									"autoSkip": false
								}
							}],
							yAxes: [{
								ticks: {
									// Include a dollar sign in the ticks
									callback: function(value, index, values) {
										return value + '%';
									}
								}
							}]
						}
					}
				});
		</script>## <span id="Tool_Download_and_Usage_Instructions">Tool Download and Usage Instructions</span>

[<span aria-hidden="true" class="glyphicon glyphicon glyphicon-download-alt"></span> Download the executable of the prototype](https://www.key-project.org/wp-content/uploads/2017/06/key-2.7_6492e8152c01b127137b403e8d24ee7521eb42e2.zip)

 After downloading the above ZIP file, just unzip it anywhere on your drive. A Java Runtime Environment of version 8 or higher is required to start the KeY version linked on this page.

 To execute the strength analysis CLI, run `java -cp KeY.jar de.tud.cs.se.ds.specstr.cli.Main`, which will display the following help:

 ```

===========================================
            This is  SpecStr v0.1          
a tool for assessing the strength of formal
  specifications using symbolic execution  
===========================================


usage: java -cp KeY.jar de.tud.cs.se.ds.specstr.cli.Main
            [input Java file]
            [fully qualified method name]
 -h,--help                   Display help (this text) and terminate
 -o,--out-file <arg>         Save output to this file
 -p,--proof-out-file <arg>   Save proof to this file
```

 For instance, starting it on the “find” method with the specification SimplePost (by executing `java -cp KeY.jar de.tud.cs.se.ds.specstr.cli.Main /path/to/Find.java "Find::find([II)I"`), we obtain as output

 ```

=====================
Unhandled Exceptions:
=====================

Unclosed exception node "Index Out of Bounds (_arr_0 != null, but i Out of Bounds!)", path condition: "result_1_0 = -1 & ( arr_0.length > i_0 & (arr_0.length <= i_0 | i_0 < 0))"

================
Uncovered Facts:
================

Post condition implies final state fact, Path condition "!result_1_0 = -1"
result = result_1_0

Loop use case fact, Path condition "!result_1_0 = -1"
arr_0[result_1_0]@heap[anon({}, anon_heap_LOOP)] = n

=========================
Abstractly Covered Facts:
=========================

Post condition implies final state fact, Path condition "result_1_0 = -1 & arr_0.length <= i_0"
result = -1

Loop body fact, Path condition "result_1_0 = -1 & (arr_0.length > i_0 & !arr_0[i_0] = n)"
i = 1 + i_0

Loop body fact, Path condition "result_1_0 = -1 & (arr_0.length > i_0 & arr_0[i_0] = n)"
i = 1 + i_0

Covered 3 (0 concretely, 3 abstractly) out of 5 facts
Overall Strength:          30,00%
Concrete Effects Strength: 0,00%
Abstract Effects Strength: 37,50%
```

The output can be written to a text file using the “-o” flag. With the “-p” flag, you can export the KeY proof tree (which is basically an extension of the symbolic execution tree) on which our analysis works. Then, you can start KeY by just running `java -jar KeY.jar` and loading the “.proof” file, and inspect the details of the analysis. Basically, everything is handled by dedicated proof rules which are prefixed by “Analyze…”, so you can search in the tree by pressing <kbd><kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>f</kbd></kbd>, entering “Analyze” and jumping from match to match.

 </div></div>