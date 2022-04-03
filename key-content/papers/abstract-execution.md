---
id: 2141
title: 'Abstract Execution'
date: '2019-03-07T12:15:16+01:00'
author: 'Dominic Steinhöfel'
layout: page
guid: 'https://www.key-project.org/?page_id=2141'
---

This page supplies additional material for the paper “*Abstract Execution*“, accepted for FM 2019.

**Table of Contents**

- [KeY-AE and Refactoring Models](#advgb-toc-6b0c8634-f029-4436-96ff-9c0cd13b0a0f)
- [Proof Statistics](#advgb-toc-8ece6dda-7db8-4e6c-bb63-f6fc5d899f3b)
- [Syntactic Desugaring](#advgb-toc-0af0dc8e-01af-4c78-8918-4f8512cfae6e)
- [How To Write New Refactoring Models](#advgb-toc-64f8c47c-84db-4427-b9f5-c1226efbd925)
- [Abstract Execution Taclets](#advgb-toc-c81f3b24-f48e-4404-91e9-53fca70b1ef0)

**Abstract.** We propose a new static software analysis principle called *Abstract Execution*, generalizing *Symbolic Execution*: While the latter analyzes all possible execution paths of a *specific program*, Abstract Execution analyzes a *partially unspecified program* by permitting *abstract symbols* representing unknown contexts. For each abstract symbol, we faithfully represent each possible concrete execution resulting from its substitution with concrete code. There is a wide range of applications of Abstract Execution, especially for verifying *relational properties* of schematic programs. We implemented Abstract Execution in a deductive verification framework and proved correctness of eight well-known statement-level refactoring rules, including two with loops. For each refactoring we characterize the preconditions that make it semantics-preserving. Most preconditions are not mentioned in the literature.

- [<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> Download Preprint](/material/AbstractExecution/AbstractExecution.pdf)
- [<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> Download Appendix](/material/AbstractExecution/AbstractExecution-Appendix.pdf)
- [<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> Download KeY and Supplementary Files](/material/AbstractExecution/AbstractExecution.zip)

You can download a [preprint of the paper](http://key-project.org/material/AbstractExecution/AbstractExecution.pdf), or download the[ appendix only](http://key-project.org/material/AbstractExecution/AbstractExecution-Appendix.pdf).

## KeY-AE and Refactoring Models

The [archive with additional files](http://key-project.org/material/AbstractExecution/AbstractExecution.zip) for the paper contains a **KeY version implementing Abstract Execution** as well as **all refactoring models** (abstract Java programs, KeY problem files and proof scripts for refactorings with loops). There is also a **README.md file** in which you find information about the file structure and advice on how to **start KeY** or a **test suite running all refactoring equivalence proofs**. For running the test suite (of which you find the corresponding Java files in the src/ directory) or starting KeY, you need to have **at least Java 8 installed** (and ant for building the test project automatically).

You can conveniently **load most AE examples** with KeY’s “**Load Example**” dialog. This includes only correctly specified examples, not those for which the proofs do not close. The latter are included as additional soundness validation checks, and for demonstrating the functionality of our type checker for Abstract Placeholder Statement specifications, in the above mentioned archive. For loading an AE example, choose “File &gt; Load Example” and scroll to the “Abstract Execution” folder at the bottom of the examples list. For the examples not including loops, click on the “Play” button at the upper left of the window to start the automatic strategy execution. The loop-based examples come with proof scripts that start automatically. For some examples, we also have finished proofs available which you can reload by choosing “Load Proof” instead of “Load Example”. All examples should “work”, i.e. the proofs close without any further interaction.

<div class="wp-block-image"><figure class="aligncenter is-resized">![Screenshot of the "Load Example" dialog in KeY, with the Remove Control Flag example chosen.](https://www.key-project.org/wp-content/uploads/2019/04/AE-Screenshot-1024x675.png)<figcaption>Screenshot of the “Load Example” dialog in KeY, with the Remove Control Flag example chosen.</figcaption></figure></div>## Proof Statistics

The below table shows some details about the proof statistics mentioned in the paper.

<style type="text/css">
    table#stats-table th {
        text-align: center;
        border: 0;
        padding: 0;
    } 
    table#stats-table thead {
        border-top: 2px solid #ddd;
        border-bottom: 1px solid #ddd;
    }
    table#stats-table thead tr:first-child th {
        padding-top: 8px;
    }
    table#stats-table thead tr:last-child th {
        padding-bottom: 8px;
    }
    table#stats-table td {
        text-align: right;
    }
    table#stats-table td:first-child {
        text-align: left;
    }
</style><div class="table-responsive">| Refactoring Technique | Nodes | Auto mode time \[ms\] | \#APS |
|---|---|---|---|
| Move Statements to Callers | 2,896 | 6,637 | 3 |
| Extract Method (with field) | 2,974 | 11,487 | 3 |
| Extract Method | 3,022 | 10,769 | 3 |
| Cond.Dupl.Cond.Fragm. (Prefix) | 3,845 | 12,526 | 4 |
| Cond.Dupl.Cond.Fragm. (Postfix) | 3,874 | 9,372 | 4 |
| Cond.Dupl.Cond.Fragm. (Try Catch Postfix) | 4,527 | 12,255 | 4 |
| Cond.Dupl.Cond.Fragm. (Try Catch Postfix, no finally) | 5,065 | 19,314 | 4 |
| Cond.Dupl.Cond.Fragm. (complex abstract expression) | 6,964 | 20,040 | 5 |
| Decompose Conditional | 6,017 | 26,026 | 4 |
| Slide Statements | 7,284 | 31,961 | 5 |
| Remove Control Flag (Manuall Unrolling) | 9,004 | 42,123 | 2 |
| Remove Control Flag (Unrolling Inv Rule) | 9,012 | 32,013 | 2 |
| Replace Exception with Test (Single Variable Rollback) | 14,251 | 50,659 | 4 |
| Replace Exception with Test (Skolem Locset Rollback) | 18,685 | 63,693 | 4 |
| Split Loop | 39,980 | 333,805 | 8 |
|  |
| **Mean** | 10,709 | 54,482 |  |
| **Median** | 7,124 | 28,994 |  |
| **MIN** | 2,896 | 6,637 |  |
| **MAX** | 39,980 | 333,805 |  |

</div>## Syntactic Desugaring

The paper mentions some syntactic elements of APS specifications that are not yet implemented in KeY. All those have to be desugared to standard Java DL terms which are declared in the .key problem files. The following table explains how to do so. We plan to implement the syntactic additions in the future such that they directly can be used.

<div class="table-responsive">| Specification Construct | How to Desugar |
|---|---|
| `locals(P)` | - Replace by `\dl_localsP` - Add `LocSet localsP;` to the `\functions { ... }` block of the problems file |
| `final(skolemLocSet)` (in a `declares` clause) | - Replace by `\dl_final(\dl_skolemLocSet)` - Add `LocSet skolemLocSet;` to the `\functions { ... }` block of the problems file |
| `hasTo(loc)` | - Replace by `\dl_hasTo(loc)` |
| `throwsExc(ID)`, `returns(ID)` | - Replace by `\dl_throwsExcID` / `\dl_returnsID` - Add `boolean throwsExcID;`, `boolean returnsID;` to the `\functions { ... }` block of the problems file |
| `axiom mutex { term1, term2, ..., termN };` (for boolean terms term1, …, termn) | Add a premise to the `\problem { ... }` part of the .key problem file. You can either directly encode the mutex property as a first-order formula, or add a premise `mutuallyExclusiveN(term1, term2, ..., termN) ->` and add a rule to the problems file using the `#mutualExclusionFormulaN` (replace the “N” by your particular one). Check the problem file in the resources subdirectory “ConsolidateDuplicateConditionalFragementAsSlideStatementsCorrect” to see an example. |

</div>## How To Write New Refactoring Models

The [archive with additional files](http://key-project.org/material/AbstractExecution/AbstractExecution.zip) for the AE paper contains a skeleton Java and problem definition file in the directory <tt>resources/SKELETON/</tt>. There are comments in the contained files “problem.key” and “Refactor.java” that provide hints on how to extend the Skeleton to create a new refactoring model. Please use the unsugared syntax described above; examples for this are also contained in the Skeleton. For checking your new example, load the “problem.key” file into KeY and press the “Play” button to start the automatic proof search.

## Abstract Execution Taclets

Taclets (“Schematic, Theory-Specific Rules”) are sequent calculus rules declared in a special, domain-specific language tailored in particular to symbolic execution rules. Most rules in KeY are written as taclets. The most complicated ones, like method contract or loop invariant rules, so far have been implemented as Java-only “built-in” rules. Our Abstract Execution taclets, as well as the new loop invariant taclets that we especially implemented for Abstract Execution, are an exception to that rule. We think that writing rules as taclets makes them more transparent and better maintainable; nevertheless, we had to add new features to the taclet language and to implement special variable conditions and term transformers for our AE taclets.

Below, you find the Abstract Execution taclet for Abstract Placeholder Statements within a loop scope and a non-void method.

```
<pre class="wp-block-code">```
abstractExecutionNonVoidLoopScope {
    // All Skolem symbols are "fresh for" the abstract program, such that
    // the same program occurring twice directly encodes the same behavior.
    \schemaVar \formula [nonrigid] C;
    \schemaVar \update U;
    \schemaVar \skolemTerm java.lang.Throwable exc \freshFor(#absProg);
    \schemaVar \skolemTerm boolean returns \freshFor(#absProg);
    \schemaVar \skolemTerm any result \freshFor(#absProg);
    \schemaVar \skolemTerm boolean breaks \freshFor(#absProg);
    \schemaVar \skolemTerm boolean continues \freshFor(#absProg);

    \find (\modality{#allmodal}{ .. #absProg ... }\endmodality(post))

    // Check that we're inside a loop scope               
    \varcond(\prefixContainsElement("LoopScopeBlock"))
    // Check that we're inside a method frame (otherwise returning makes no sense)
    \varcond(\prefixContainsElement("MethodFrame"))
    
    // Check that we're in a non-void method, extract result variable
    \varcond(\storeResultVarIn(#v))
    \varcond(\isDefined(#v))
    
    // Surrounding block labels 
    \varcond(\storeContextLabelsIn(#labels))
    // Surrounding loop labels 
    \varcond(\storeContextLoopLabelsIn(#labels1))
    // Booleans modeling breaks to those labels. Fresh for the abstract program.
    \varcond(\instantiateVarsFresh(#vars, #labels, "breaks", boolean \freshFor(#absProg)))
    \varcond(\instantiateVarsFresh(#vars1, #labels1, "continues", boolean \freshFor(#absProg)))
    
    // Program variables for modeling irregular termination
    \varcond(\newPV(#exc, "exc", java.lang.Throwable \freshFor(#absProg)))
    \varcond(\newPV(#returns, "returns", boolean \freshFor(#absProg)))
    \varcond(\newPV(#result, "result", \typeof(#v) \freshFor(#absProg)))
    \varcond(\newPV(#breaks, "breaks", boolean \freshFor(#absProg)))
    \varcond(\newPV(#continues, "continues", boolean \freshFor(#absProg)))
    
    // Parametric Skolem update and path condition initialization.
    //
    // The update receives two location sets as parameters; the first one for its
    // assignable, and the second one for its accessible locations (similar to a
    // normal update, just with sets). The path condition receives as argument the
    // location set of its accessible values, including the exception, returns, 
    // result, breaks and continues flags.
    \varcond(\initializeParametricSkolemUpdate(U, #absProg))
    \varcond(\initializeParametricSkolemPathCondition(C, #absProg))

    // Index variables for foreach loop 
    \varcond(\new(#v1, boolean))
    \varcond(\newLabel(#label))
    
    \replacewith ( 
         {U}{   #exc:=exc || #returns:=returns
             || #result:=#addCast(result,#result)
             || #breaks:=breaks || #continues:=continues}
           (  C 
            & #mutualExclusionFormula5(#returns, #exc, #breaks, #continues, #vars) 
            & #returnSpec(#absProg, #returns)
            & #excSpec(#absProg, #exc)
            & #breaksSpec(#absProg, #breaks)
            & #continuesSpec(#absProg, #continues)
           ) ->
         {U}{   #exc:=exc || #returns:=returns
             || #result:=#addCast(result,#result)
             || #breaks:=breaks || #continues:=continues}
           \modality{#allmodal}{ ..
               if (#returns) {
                   return #result;
               }
               if (#exc != null) {
                   throw #exc;
               }
               if (#continues) {
                   continue;
               }
               if (#breaks) {
                   break;
               }
               #foreach (#v1, #label in #vars, #labels) { 
                   if (#v1) {
                       break #label;
                   }
               }
               #foreach (#v1, #label1 in #vars1, #labels1) { 
                   if (#v1) {
                       continue #label1;
                   }
               }
           ... }\endmodality(post))
    
    \heuristics(abstractExecution, simplify_prog)
};
```
```