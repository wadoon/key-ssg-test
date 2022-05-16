---
title: 'Program Verification'
date: '2021-12-23T17:59:59+01:00'
author: 'Wolfram Pfeifer'
---


The core feature of KeY is a theorem prover for Java Dynamic Logic
based on a sequent calculus. It allows for full functional
verification of sequential Java (without floats, garbage collection
and multithreading, see the [section below](#supported-features)) and
Java Card 2.2.x programs. Properties can be specified in the [Java
Modelling Language (JML)](http://www.jmlspecs.org) or in Java Dynamic
Logic directly. To try out KeY for program verification, go to the
[download](http://key-project.org/download/) page and follow the
instructions. Upon start of KeY, you can select among several examples
in menu “File &gt; Load Examples”. Read the corresponding descriptions
and try out what looks most interesting to you. Alternatively, have
a look at our [tutorials section](#Tutorials).

## Supported Java Features

Java is a very complex language which massively evolved over the time.
KeY does not support all Java features. Some of those, like
floating-point arithmetic, are in principle hard to handle from
a theorem-proving point of view; others, like Generics and Lambdas,
could be considered in future versions of the system. The following
(incomplete) table gives an overview about the state of selected Java
features in the current KeY version. Features shaded in green are
supported, those in red are unsupported; features in yellow are in
principle not supported, but can be treated with restrictions by
a workaround supplied by KeY. A list of [supported JML
features](/jml-support-in-key/) is available
[here](/jml-support-in-key/).


| Feature                                          | State                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basic Java 1.2 features                          | KeY supports Integer arithmetic (for both mathematical Integers and actual Integer types with overflows), Strings, inheritance, dynamic dispatch, loops, recursion, …                                                                                                                                                                    |
| Enhanced “for” loops                             | Supported.                                                                                                                                                                                                                                                                                                                               |
| Library methods                                  | KeY will throw an error when you use libraries the code of which is not in KeY’s classpath. However, we have a plugin in our eclipse extension which can create stubs with default contracts for library methods such that you can directly start proving properties about your code, or manually refine the stub specifications before. |
| Generics                                         | Unsupported; However, a tool to statically remove Generics from the code can be downloaded [here](https://www.key-project.org/download/).                                                                                                                                                                                                |
| Floating point types                             | Unsupported.                                                                                                                                                                                                                                                                                                                             |
| Multithreading                                   | Unsupported.                                                                                                                                                                                                                                                                                                                             |
| try-with-resources and multi-catch (both Java 7) | Unsupported.                                                                                                                                                                                                                                                                                                                             |
| Java 8 features (lambdas etc.)                   | Unsupported.                                                                                                                                                                                                                                                                                                                             |


### Relevant blog posts

