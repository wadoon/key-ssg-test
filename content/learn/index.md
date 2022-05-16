---
id: 1535
title: 'Learn KeY'
date: '2017-10-09T13:30:38+01:00'
author: 'Dominic Steinhöfel'
layout: page
---

## Getting Started 

### Download KeY

- Download [KeY 2.10](https://www.key-project.org/dist/2.10.0/key-2.10.0-exe.jar) as
  single click jar and double click the jar file <small>(or use
  `java -jar key-2.8.0-exe.jar` on the command line)</small>
- Alternatively, download one of the
- [KeY 2.10.0 stable binaries](https://www.key-project.org/dist/2.10.0/key-2.10.0.zip) or
- [development versions](https://www.key-project.org/nightly/)


### The KeY Book(s) 


TODO 

### Documentation 


A good starting point is the [tutorial on formal verification with
KeY](https://link.springer.com/chapter/10.1007/978-3-319-49812-6_16)
in the [KeY book.](/thebook2/) The [examples from the
book](/thebook2/examples-from-the-book/) are available
[here](/thebook2/examples-from-the-book/).

### KeY as a Library

You can use KeY as a library in your own project: Make use of its
capabilities as a first-order prover or symbolic execution engine. We
provide some starting points for you in the [“KeY for Your Own
Research Projects”
section](https://www.key-project.org/applications/key-for-your-own-research-projects/).
[Download the KeY nightly source code distribution
here](http://i12www.ira.uka.de/~key/download/nightly/) and have a look
at our [Javadoc
documentation](http://i12www.ira.uka.de/~key/download/nightly/api/) if
you want to extend KeY or understand how things work under the hood.





### Getting Help

The preferred way for getting help, in particular when you want to use
KeY as a library or want to change or extend the source code, is to
use
[StackOverflow](https://stackoverflow.com/questions/tagged/key-formal-verification).
Be sure to tag your question with the
<kbd>key-formal-verification</kbd> tag, so that your question is not
lost amongst all the questions on StackOverflow. Alternatively, you
can write an email to our mailing list support@key-project.org.


### Tutorials & Examples

Load an example from the list presented in the dialog that pops up
when starting KeY. Good choices are, e.g.: - “Quicktour” for program
verification

- “Transitivity of Subset” for first-order logic
- “Declassification – Sum” for information flow analysis

## Tutorials

### Video Tutorial: Interactive Verification with the Symbolic Execution Debugger (SED)

{{< youtube IV-dEnpCLkI >}}


### Video Tutorial: Proof Attempt Inspection with the Symbolic Execution Debugger

{{< youtube 8e-q9Jf1h_w >}}

### Formal Verification with KeY: A Tutorial (2016)

By Bernhard Beckert, Reiner Hähnle, Martin Hentschel and Peter H.
Schmitt Book chapter of the [KeY
book](https://www.key-project.org/thebook2/). This chapter gives
a systematic tutorial introduction on how to perform formal program
verification with the KeY system. It illustrates a number of
complications and pitfalls, notably programs with loops, and shows how
to deal with them. After working through this tutorial, you should be
able to formally verify with KeY the correctness of simple Java
programs, such as standard sorting algorithms, gcd, etc. 

[Find this tutorial on SpringerLink](https://link.springer.com/chapter/10.1007/978-3-319-49812-6_16)

**Note:** The following tutorials may require older versions of KeY.

### Verifying Object-Oriented Programs with KeY: A Tutorial (2007)

By Wolfgang Ahrendt, Bernhard Beckert, Reiner Hähnle, Philipp Rümmer,
and Peter H. Schmitt. 

> **Abstract.** This paper is a tutorial on
> performing formal specification and semi-automatic verification of
> Java programs with the formal software development tool KeY. This
> tutorial aims to fill the gap between elementary introductions using
> toy examples and state-of-art case studies by going through
> a self-contained, yet non-trivial, example. It is hoped that this
> contributes to explain the problems encountered in verification of
> imperative, object-oriented programs to a readership outside the
> limited community of active researchers.

[Download this tutorial](/wp-content/uploads/2016/12/fmco06post.pdf). 

### KeY: The Sequent Calculus of the KeY Tool (2015)

Tutorial at [CADE-25](http://conference.mi.fu-berlin.de/cade-25/home)
by [Reiner Hähnle](http://www.se.tu-darmstadt.de/se/group-members/reiner-haehnle/) and
[Peter H. Schmitt](http://lfm.iti.kit.edu/english/pschmitt.php) 

You can download [part I](/wp-content/uploads/2016/12/Design_Space_Calculus.pdf) and [part
II](/wp-content/uploads/2016/12/TutorialSlidesPart2.pdf) of the slides
of this tutorial as well as the [corresponding KeY proofs](/wp-content/uploads/2016/12/proofs.zip). 



