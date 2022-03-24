---
id: 3096
title: 'JML Support in KeY'
date: '2022-01-13T15:30:04+01:00'
author: 'Wolfram Pfeifer'
layout: revision
guid: 'https://www.key-project.org/?p=3096'
permalink: '/?p=3096'
---

This page documents the state of support for the [Java Modeling Language](http://www.eecs.ucf.edu/~leavens/JML//index.shtml) (JML) in KeY releases 1.6.5 and 2.4.1 as well in the release candidate for KeY 2.6.0. We also list some KeY-specific extensions to JML here. We do not explain JML itself here, please refer to the reference manual for that.

<div class="table-responsive">| JML Feature | KeY 1.6.5 | KeY 2.4.1 | KeY 2.6 | KeY 2.10 | Comments |
|---|---|---|---|---|---|
| **ghost field/variable** | yes | yes | yes | yes |  |
| **model field** | no | yes | yes | yes |  |
| **model method** | no | yes | yes | yes |  |
| **class invariant** | yes | yes | yes | yes | [see note below](http://key-project.se.informatik.tu-darmstadt.de/jml-support-in-key/#note-inv) |
| **history constraint** | no | no | no | no |  |
| **initially clause** | no | yes | yes | yes |  |
| **axiom clause** | no | yes | yes | yes |  |
| **represents clause** | no | yes | yes | yes |  |
| **requires clause** | yes | yes | yes | yes |  |
| **ensures clause** | yes | yes | yes | yes |  |
| **signals clause** | yes | yes | yes | yes |  |
| **signals\_only clause** | yes | yes | yes | yes |  |
| **diverges clause** | yes | yes | yes | yes |  |
| **measured\_by clause** | no | yes | yes | yes |  |
| **assignable clause** | yes | yes | yes | yes |  |
| **accessible clause** | no | yes | yes | yes |  |
| **redundancy** | yes | yes | yes | yes | treated as non-redundant |
| **set statement** | yes¹ | yes¹ | yes¹ | yes | ¹known issue: must not be last statement in block |
| **assert statement** | no | yes² | yes² | yes | ²known issue: must be followed by non-empty block |
| **assume statement** | no | no | no | yes |  |
| **visibility modifiers** | yes | yes | yes | yes |  |
| **helper modifier** | no | yes | yes | yes |  |
| **pure modifier** | [see note](#note-pure) | yes | yes | yes | [see note below](#note-pure) |
| **math modifiers** | no | no | no | no | used integer semantics can be set globally via Taclet options |
| **\\bigint type** | no | yes³ | yes | yes | ³KeY 2.4 uses Euclidean division, mod |
| **\\real type** | no | parsable | parsable | parsable | no reasoning about reals |
| **\\TYPE type** | no | no | no | no |  |
| **\\index** and **\\values** | no | yes | yes | yes | JML extension also used in OpenJML |
| **\\invariant\_for** | no | yes | yes | yes |  |
| **\\old** | yes | partially | yes | yes | known issue: not available for parameters in 2.4 |
| **\\forall** and **\\exists** | yes | yes | yes | yes |  |
| **\\sum**, **\\num\_of** and **\\product** | no | yes | yes | yes | reasoning only about bounded sums and products, e.g. (\\sum int i; a&lt;=i&lt;b; f(i)) |
| **\\min** and **\\max** | no | no | parsable | parsable |  |
| **\\fresh** | yes | yes | yes | yes |  |
| **\\reach** | no | partially | partially | partially | TODO |
| **\\typeof** | yes | yes | yes | yes |  |
| **\\is\_initialized** | yes | yes | yes | yes |  |
| **expression associativity** | right | right | standard | standard | [see note below](#note-assoc) |

</div>### Notes

#### <a name="note-inv"></a>Class Invariants

KeY does not require invariants to hold in every *visible* state. In *KeY 1.6.5 or older*, invariants are required to hold in the post state. The user has to select in the GUI which invariants are assumed for each method. In *KeY 2.0.0 or later*, invariants are not generally assumed in pre conditions or required in post conditions. The only exception are invariants of the class (or a superclass) in which the method under test is declared. This behavior can be disabled using the <tt>helper</tt>modifier. Invariants can be explicitly added to any specification clause using the <tt>\\invariant\_for</tt> expression. #### <a name="note-pure"></a>Purity

In *KeY 1.6.5 or older*, the <tt>pure</tt> modifier means *strong purity* (no changes to the heap at all). In *KeY 2.0.0 or later*, it means weak purity as described in the JML reference manual. For strong purity use the <tt>strictly\_pure</tt> modifier instead (KeY-specific extension). #### <a name="note-assoc"></a>Expression Associativity

The JML reference manual declares all operators to be left-associative (as in Java), with the exception of the forward implication, which is right-associative. Only KeY versions from 2.6.0 on respect this. In earlier versions, all operators are right-associative. When using those, remember that KeY is not a replacement for a JML syntax/type checker.