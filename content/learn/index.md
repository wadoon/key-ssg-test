---
id: 1535
title: 'Learning KeY'
date: '2021-05-23T02:10:38+01:00'
author: 'Alexander Weigl'
wide: true
---

<!--
<div class="p-5 mb-4 bg-light rounded-3">
<div class="container-fluid py-5">
<h1 class="display-5 fw-bold">Custom jumbotron</h1>
    <p class="col-md-8 fs-4">Using a series of utilities, you can create this jumbotron, just like the one in previous versions of Bootstrap. Check out the examples below for how you can remix and restyle it to your liking.</p>
<button class="btn btn-primary btn-lg" type="button">Example button</button>
</div>
</div>
-->

<div class="row">
      <div class="col-md-6">
        <div class="h-100 p-5 text-white bg-dark rounded-3">
          <h2>Download KeY</h2>

Download <a class="text-white" href="https://www.key-project.org/dist/2.10.0/key-2.10.0-exe.jar">KeY 2.10</a> as
  single click jar and double click the jar file (or use `java -jar
  key-2.8.0-exe.jar` on the command line)
  
  <p>
<a class="btn btn-outline-light" type="button"
href="https://www.key-project.org/dist/2.10.0/key-2.10.0.zip">Stable
binaries</a> or <a class="btn btn-outline-light"
href="https://www.key-project.org/nightly/">development versions</a>
</p>

</div>
</div>

<div class="col-md-6">
<div class="h-100 p-5 bg-light border rounded-3">
<h2>Developer and User Documenation</h2>
<p>Or, keep it light and add a border for some added definition to the boundaries of your content. Be sure to look under the hood at the source HTML here as we've adjusted the alignment and sizing of both column's content for equal-height.</p>
<button class="btn btn-outline-secondary" type="button">Example button</button>
</div>
</div>
</div>
<hr>
<div class="row">
<div class="col-md-6">
<div class="h-100 p-5 text-bg-warning border rounded-3">
<h2>A starting point</h2>
<p>

A good starting point is the [tutorial on formal verification with
KeY](https://link.springer.com/chapter/10.1007/978-3-319-49812-6_16)
in the [KeY book.](/thebook2/) The [examples from the
book](/thebook2/examples-from-the-book/) are available
[here](/thebook2/examples-from-the-book/).

</p>
<button class="btn btn-primary" type="button">Example button</button>
</div>
</div>


<div class="col-md-6">
<div class="h-100 p-5 text-bg-light border rounded-3">
<h2>Getting Help</h2>
<p>

The preferred way for getting help, in particular when you want to use
KeY as a library or want to change or extend the source code, is to
use
[StackOverflow](https://stackoverflow.com/questions/tagged/key-formal-verification).
Be sure to tag your question with the
<kbd>key-formal-verification</kbd> tag, so that your question is not
lost amongst all the questions on StackOverflow. Alternatively, you
can write an email to our mailing list support@key-project.org.

</p>
</div>
</div>
</div>


### Getting Help



### The KeY Book(s) 

<div class="row">
<div class="col-md-4">
<div class="card">
<img src="/2020/12/the-new-book-has-arrived/bookFuturePerspectivesLarge.png" style="width:16rem" class="card-img-top" alt="...">
<div class="card-body">
<h5 class="card-title">
    Deductive Software Verification: Future Perspectives
</h5>
<p class="card-text">
The LNCS volume 12345* “Deductive Software Verification: Future
Perspectives” contains a collection of articles – reflections on the
occasion of 20 years of KeY.
</p>
<a href="#" class="btn btn-primary">Go somewhere</a>
</div>
</div>
</div>
<div class="col-md-4">
<div class="card  text-bg-dark">
<img src="/wp-content/uploads/2016/11/BookCover-197x300.jpg"  style="width:16rem" class="card-img-top" alt="...">
<div class="card-body">
<h5 class="card-title">Deductive Software Verification — The KeY Book From Theory to Practice</h5>
<p class="card-text">

The new book covers deductive software verification as realised by the
KeY approach. It constitutes the ultimate source for the KeY tool
since version 2.x. It also features a general (not KeY specific)
chapter on the Java Modeling Language which provides a thorough
introduction into the specification language.

</p>
<a href="/thebook2/" class="btn btn-primary">Book Page</a>
</div>
</div>
</div>
<div class="col-md-4">
<div class="card text-bg-light">
<img src="/wp-content/uploads/2016/04/keybook-196x300.png" class="card-img-top" 
    style="width:16rem" alt="...">
<div class="card-body">
<h5 class="card-title">Verification of Object-Oriented Software: The KeY Approach</h5>
<p class="card-text">
    The definitive source for all information related to the KeY project. 
</p>
<a href="/thebook/" class="btn btn-primary">Book Page</a>
</div>
</div>
</div>



</div>

## Tutorials & Examples

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



Load an example from the list presented in the dialog that pops up
when starting KeY. Good choices are, e.g.: - “Quicktour” for program
verification

- “Transitivity of Subset” for first-order logic
- “Declassification – Sum” for information flow analysis

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


## Video Tutorial (SED): Interactive Verification with the Symbolic Execution Debugger (SED)

{{< youtube IV-dEnpCLkI >}}


## Video Tutorial (SED): Proof Attempt Inspection with the Symbolic Execution Debugger

{{< youtube 8e-q9Jf1h_w >}}

