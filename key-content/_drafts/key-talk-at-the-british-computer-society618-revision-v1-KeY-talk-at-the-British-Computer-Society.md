---
id: 621
title: 'KeY talk at the British Computer Society'
date: '2016-12-19T10:40:59+01:00'
author: 'Dominic Steinhöfel'
layout: revision
guid: 'http://key-project.se.informatik.tu-darmstadt.de/2016/12/19/618-revision-v1/'
permalink: '/?p=621'
---

Prof. Reiner Hähnle will give an invited talk at the British Computer Society at **May 4th, 2017**: “[The KeY Formal Verification Tool](http://www.bcs.org/content/ConWebDoc/57115)“.

 ### Synopsis

 KeY is a deductive verification tool for sequential Java programs. It is based on a rich program logic for Java source code. KeY can perform functional verification of Java programs annotated with with specifications in the Java Modeling language. Specification elements include class invariants and method contracts. The rules of KeY's program logic realize a symbolic execution engine for Java. Verification proceeds method-wise, unbounded loops are approximated by invariants, method calls by contracts. KeY incorporates state-of-art proof search and an auto-active mode that in many cases results in fully automatic proofs. Otherwise, the user can perform interactive steps or ask the system to search for a counter example. KeY has been successfully used to verify complex legacy code, such as the JDK's sort method, where a subtle bug was found and subsequently fixed. I will explain some of the theoretical underpinnings and design principles of KeY. I will also give a live demonstration of some of KeY's capabilities.