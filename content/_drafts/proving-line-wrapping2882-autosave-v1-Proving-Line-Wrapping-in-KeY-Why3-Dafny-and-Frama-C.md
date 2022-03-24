---
id: 2898
title: 'Proving Line Wrapping in KeY, Why3, Dafny and Frama-C'
date: '2021-04-13T12:11:06+01:00'
author: 'Mattias Ulbrich'
layout: revision
guid: 'https://www.key-project.org/?p=2898'
permalink: '/?p=2898'
---

This is a short comparison report about a verification task solved with KeY, [Why3](https://why3.lri.fr), [Dafny](https://github.com/dafny-lang/dafny) and [Frama-C](https://frama-c.com/).

The original challenge comes from a real-world situation. There is no particular “trick” needed for the specification and verification; it is rather straightforward. Yet, the required annotations to achieve the specification are not too few – making the example a good opportunity to compare different specification languages.

## Motivation

The original problem is a GUI bug in KeY where tooltips suffered from very long lines. A routine to wrap these tooltips had to be written. To make it correct, it has been formally proven in KeY (yielding the first KeY-proven code inside KeY!). [Jean-Christophe](https://www.lri.fr/~filliatr/) and [Andrei](http://tertium.org/) from the Why3 team then kindly contributed a provenly correct solution in Why3. A literal translation of the KeY solution to Dafny gives us a third comparison partner in Dafny. [Lionel](https://formal.iti.kit.edu/~blatter) provided a version in Frama-C.

[![](https://www.key-project.org/wp-content/uploads/2021/03/tooltip1-300x191.png)](https://www.key-project.org/wp-content/uploads/2021/03/tooltip1.png) [![](https://www.key-project.org/wp-content/uploads/2021/03/tooltip2-300x203.png)](https://www.key-project.org/wp-content/uploads/2021/03/tooltip2.png)

A simpler version of this example has been proposed as [the microchallenge in a recent KeY tutorial.](https://www.key-project.org/2021/03/26/key-tutorial-at-verifythis-2021/)

## Informal specification

Implement a method `wrapLines` that wrap lines such that a maximum line length is not exceeded. It receives a string in form of a mutable character array and a positive desired length of lines. The array may already contain newline-characters when the method is called.

1. `wrapLines` does not raise any runtime error and always terminates (normally).
2. `wrapLines` changes at most entries in the array, and only replaces spaces by newline characters.
3. If, after `wrapLines` terminates, there are more than `lineLength` characters in a row without newline characters among them, then there are also no spaces among them. (Impossible to break ...)
4. If `wrapLines` introduces a newline character at index `k`, then there is no possibility that the line terminated at `k` could have been made longer without exceeding the desired length of lines.

## Solutions

| *Tool* | *Languages* | *Simple challenge* | *Challenge* | *Code Language* |
|---|---|---|---|---|
| KeY | Java + JML | [Link](https://www.key-project.org/wp-content/uploads/2021/03/WrapUtilsSolution.java) | [Link](https://www.key-project.org/wp-content/uploads/2021/04/WrapUtils.java) | Java |
| [Why3](http://why3.lri.fr) | WhyML | [Link](https://gitlab.inria.fr/why3/why3/-/blob/master/examples/wrap_lines.mlw#L40) | [Link](https://gitlab.inria.fr/why3/why3/-/blob/master/examples/wrap_lines.mlw#L74) | OCaml |
| [Dafny](https://github.com/dafny-lang/dafny) | Dafny |  | [Link](https://formal.iti.kit.edu/~ulbrich/pub/wrap.dfy) | C# |
| [Frama-C](https://frama-c.com/) | ACSL + C | [Link](https://github.com/lyonel2017/VerifyThis-2017/blob/master/2021/microchallenge/WrapLine.c#L42) |  | C |

*Simple Challenge* refers to the microchallenge in the tutorial.  
*Code Language* refers to the language for the executable version of the specified code.