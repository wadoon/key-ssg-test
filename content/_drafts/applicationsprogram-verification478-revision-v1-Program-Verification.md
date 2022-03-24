---
id: 1136
title: 'Program Verification'
date: '2017-04-20T20:39:23+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'https://www.key-project.org/2017/04/20/478-revision-v1/'
permalink: '/?p=1136'
---

<span aria-hidden="true" class="glyphicon glyphicon-road"></span> This page is under construction

<div class="row"><div class="col-md-3 col-md-push-9"><div class="no_bullets" id="toc_container">Contents

- [Supported Java Features](#Supported_Java_Features)
- [Tutorials](#Tutorials)
- [Literature](#Literature)

</div> </div><div class="col-md-9 col-md-pull-3"> The core feature of KeY is a theorem prover for Java Dynamic Logic based on a sequent calculus. It allows for full functional verification of sequential Java (without floats, garbage collection and multithreading, see the [section below](#supported-features)) and Java Card 2.2.x programs. Properties can be specified in the [Java Modelling Language (JML)](http://www.jmlspecs.org) or in Java Dynamic Logic directly.

 To try out KeY for program verification, go to the [download](http://key-project.org/download/) page and follow the instructions. Upon start of KeY, you can select among several examples in menu “File &gt; Load Examples”. Read the corresponding descriptions and try out what looks most interesting to you. Alternatively, have a look at our [tutorials section](#Tutorials).

## <span id="Supported_Java_Features">Supported Java Features</span>

 Java is a very complex language which massively evolved over the time. KeY does not support all Java features. Some of those, like floating-point arithmetic, are in principle hard to handle from a theorem-proving point of view; others, like Generics and Lambdas, could be considered in future versions of the system.

 The following (incomplete) table gives an overview about the state of selected Java features in the current KeY version. Features shaded in green are supported, those in red are unsupported; features in yellow are in principle not supported, but can be treated with restrictions by a workaround supplied by KeY.

A list of [supported JML features](/jml-support-in-key/) is available [here](/jml-support-in-key/).

<div class="table-responsive"> | Feature | State |
|---|---|
| Basic Java 1.2 features | KeY supports Integer arithmetic (for both mathematical Integers and actual Integer types with overflows), Strings, inheritance, dynamic dispatch, loops, recursion, … |
| Enhanced “for” loops | Supported. |
| Library methods | KeY will throw an error when you use libraries the code of which is not in KeY’s classpath. However, we have a plugin in our eclipse extension which can create stubs with default contracts for library methods such that you can directly start proving properties about your code, or manually refine the stub specifications before. |
| Generics | Unsupported; However, the eclipse extension comes along with a plugin to statically remove Generics from the code. <span>In Eclipse with KeY installed, open the context menu on a project in the package explorer and select Remove Generics.</span> |
| Floating point types | Unsupported. |
| Multithreading | Unsupported. |
| try-with-resources and multi-catch (both Java 7) | Unsupported. |
| Java 8 features (lambdas etc.) | Unsupported. |

 </div>## <span id="Tutorials">Tutorials</span>

<a id="tutorials"></a><div class="row"><div class="col-sm-6">### Video Tutorial: Interactive Verification with the Symbolic Execution Debugger (SED)

<div class="embed-responsive embed-responsive-16by9"> <iframe class="embed-responsive-item" height="150" loading="lazy" src="https://www.youtube.com/embed/IV-dEnpCLkI" width="300"></iframe> </div> </div><div class="col-sm-6">### Video Tutorial: Proof Attempt Inspection with the Symbolic Execution Debugger

<div class="embed-responsive embed-responsive-16by9"> <iframe class="embed-responsive-item" height="150" loading="lazy" src="https://www.youtube.com/embed/8e-q9Jf1h_w" width="300"></iframe> </div> </div> </div>**Note:** The following tutorials may require older versions of KeY.

<div class="row"><div class="col-sm-6">### KeY: The Sequent Calculus of the KeY Tool

 Tutorial at [CADE-25](http://conference.mi.fu-berlin.de/cade-25/home) by [Reiner Hähnle](http://www.se.tu-darmstadt.de/se/group-members/reiner-haehnle/) and [Peter H. Schmitt](http://lfm.iti.kit.edu/english/pschmitt.php)

 You can download [part I](/wp-content/uploads/2016/12/Design_Space_Calculus.pdf) and [part II](/wp-content/uploads/2016/12/TutorialSlidesPart2.pdf) of the slides of this tutorial as well as the [corresponding KeY proofs](/wp-content/uploads/2016/12/proofs.zip).

 </div><div class="col-sm-6">### Verifying Object-Oriented Programs with KeY: A Tutorial

By Wolfgang Ahrendt, Bernhard Beckert, Reiner Hähnle, Philipp Rümmer, and Peter H. Schmitt.

 **Abstract.** This paper is a tutorial on performing formal specification and semi-automatic verification of Java programs with the formal software development tool KeY. This tutorial aims to fill the gap between elementary introductions using toy examples and state-of-art case studies by going through a self-contained, yet non-trivial, example. It is hoped that this contributes to explain the problems encountered in verification of imperative, object-oriented programs to a readership outside the limited community of active researchers.

[Download this tutorial](/wp-content/uploads/2016/12/fmco06post.pdf).

 </div> </div>## <span id="Literature">Literature</span>

<div class="teachpress_pub_list"><form method="get" name="tppublistform"><a id="tppubs" name="tppubs"></a>[Show all](https://www.key-project.org/?p=1136?#tppubs "Show all")

</form><div class="teachpress_message_error">Sorry, no publications matched your criteria.

</div></div> </div></div>