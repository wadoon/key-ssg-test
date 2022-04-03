---
id: 2536
title: 'Safer Parallelization'
date: '2020-05-29T20:17:43+01:00'
author: 'Dominic Steinhöfel'
layout: revision
guid: 'https://www.key-project.org/2020/05/29/2478-revision-v1/'
permalink: '/?p=2536'
---

This page supplies additional material for the paper “*Safer Parallelization”*, submitted to ISoLA 2020.

**Abstract.** Adapting sequential legacy software to parallel environments not only saves time and money, but additionally avoids losing valuable domain knowledge hidden in existing code. One useful parallelization approach is the detection of standardized parallel design patterns which allow making best use of parallel programming interfaces like OpenMP. When these patterns are not literally present, it can be necessary to apply code transformations to suitably re-shape the input program. In this paper, we describe how we used Abstract Execution, a semi-automatic program proving technique for second-order program properties, to formally prove conditional correctness of the restructuring techniques CU Elimination, Loop Splitting and Geometric Decomposition – for all input programs. The former two techniques require an advanced modeling technique based on families of abstract location sets.

- [<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> Download KeY/REFINITY and Restructuring Models](/material/SaferParallelization/REFINITY-RestructuringModels.zip)

## REFINITY and Restructuring Models

The archive linked above contains the current KeY version with REFINITY, the three transformation models discussed in the paper, as well as a (Linux) script `replayProofs.sh` to replay all closed proofs in batch mode. REFINITY models have the file ending ".aer", proof (bundles) the ending ".zproof". REFINITY models can be opened from within KeY and the REFINITY window, proofs have to be loaded directly in KeY. For instructions on how to run KeY/REFINITY and system prerequisites, we refer to the [REFINITY webpage](https://www.key-project.org/refinity/).

*Note:* When loading longer proofs, such as the one for Geometric Decomposition, it might happen that you get a StackOverflowError. This is an uncritical bug related to recent versions of the KeY user interface, and should not prevent the system from completely loading and displaying the chosen proof, and being fully functional afterward.

## Proof Statistics

In the following, we show the detailed statistics for the proofs of our transformation schemata. "Block/Loop Contract apps" are in fact applications of constraints defined in the models; internally, they are encoded as "block contracts".

Concerning interactive (manual) applications, "instAll" and "allLeftHide" are both quantifier instantiations for universal assumptions. Case distinctions on the truth values of formulas are realized using "cut\_direct" applications. Real, user-defined cuts (on-the fly lemmas) are introduced by "cut" applications.

### CU Elimination

| **Nodes** | 994 |
|---|---|
| **Branches** | 9 |
| **Interactive steps** | 0 |
| **Symbolic execution steps** | 28 |
| **Automode time** | 6,054 ms |
| **Avg. time per step** | 6.096 ms |
| **Rule applications** |
| **Quantifier instantiations** | 1 |
| **One-step Simplifier apps** | 0 |
| **SMT solver apps** | 0 |
| **Dependency Contract apps** | 0 |
| **Operation Contract apps** | 0 |
| **Block/Loop Contract apps** | 2 |
| **Loop invariant apps** | 0 |
| **Abstract Execution apps** | 4 |
| **Merge Rule apps** | 0 |
| **Total rule apps** | 993 |

### Loop Splitting

| **Nodes** | 15,599 |
|---|---|
| **Branches** | 86 |
| **Interactive steps** | 23 |
| **Symbolic execution steps** | 158 |
| **Automode time** | 295.9s |
| **Automode time** | 29,5965 ms |
| **Avg. time per step** | 18.974 ms |
| **Rule applications** |
| **Quantifier instantiations** | 113 |
| **One-step Simplifier apps** | 0 |
| **SMT solver apps** | 0 |
| **Dependency Contract apps** | 0 |
| **Operation Contract apps** | 0 |
| **Block/Loop Contract apps** | 10 |
| **Loop invariant apps** | 3 |
| **Abstract Execution apps** | 5 |
| **Merge Rule apps** | 0 |
| **Total rule apps** | 15,598 |
| **Details on Interactive Apps** |
| **cut** | 8 |
| **instAll** | 7 |
| **hide\_left** | 5 |
| **hide\_right** | 2 |
| **allLeftHide** | 1 |

### Geometric Decomposition

| **Nodes** | 84,209 |
|---|---|
| **Branches** | 360 |
| **Interactive steps** | 215 |
| **Symbolic execution steps** | 175 |
| **Automode time** | 38min |
| **Automode time** | 2337083ms |
| **Avg. time per step** | 27.753ms |
| **Rule applications** |
| **Quantifier instantiations** | 173 |
| **One-step Simplifier apps** | 0 |
| **SMT solver apps** | 0 |
| **Dependency Contract apps** | 0 |
| **Operation Contract apps** | 0 |
| **Block/Loop Contract apps** | 8 |
| **Loop invariant apps** | 3 |
| **Abstract Execution apps** | 3 |
| **Merge Rule apps** | 0 |
| **Total rule apps** | 84,208 |
| **Details on Interactive Apps** |
| **hide\_left** | 36 |
| **cut\_direct** | 29 |
| **instAll** | 24 |
| **cut** | 23 |
| **hide\_right** | 21 |
| **ifthenelse\_true** | 17 |
| **jdiv\_axiom\_inline** | 17 |
| **replace\_known\_left** | 17 |
| **div\_axiom\_positive** | 6 |
| **applyEqRigid** | 4 |
| **allLeftHide** | 2 |
| **allRight** | 2 |
| **applyEqReverse** | 2 |
| **concrete\_and\_3** | 2 |
| **concrete\_or\_4** | 2 |
| **hideAuxiliaryEqConcrete** | 2 |
| **andRight** | 1 |
| **applyEq** | 1 |
| **auto\_int\_induction\_geqZero** | 1 |
| **concrete\_and\_1** | 1 |
| **concrete\_or\_2** | 1 |
| **ifthenelse\_split\_for** | 1 |
| **orLeft** | 1 |
| **pullOut** | 1 |
| **replace\_known\_right** | 1 |