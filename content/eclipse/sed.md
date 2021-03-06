---
id: 351
title: 'Symbolic Execution Debugger (SED)'
date: '2016-11-30T20:23:22+01:00'
author: 'Richard Bubel'
layout: page
guid: 'http://key-project.se.informatik.tu-darmstadt.de/?page_id=351'
ampforwp-amp-on-off:
    - default
---

The Symbolic Execution Debugger (SED) is a platform for symbolic execution in general and allows to interactively debug programs based on symbolic execution. Symbolic execution discovers all possible execution paths simultaneously. This is achieved by the use of symbolic in lieu of concrete values resulting in a symbolic execution tree. Each node in the symbolic execution tree provides the full state and related information such as the symbolic call stack or the path conditions under which the node is reached. Execution can start at any method or at any statement without setting up a context. Navigation is realized using classic debugger functionality, including stepwise execution or breakpoints. The screenshots of the following sections illustrate the main features of SED using KeY as symbolic execution engine. Each section contains numbered screenshots that explain a usage scenario step by step. Clicking on each picture produces a more detailed view. The screenshots may differ from the latest release. At the end of this webpage we briefly describe the architecture of SED and the theory behind it.

### <a name="prerequisites"></a>Prerequisites

The Symbolic Execution Debugger is compatible with [Eclipse](http://www.eclipse.org/) Mars or newer. Required update-sites and installation instructions are available in the [download](https://www.key-project.org/download/) area. As getting started guide for new users we recommend the [tutorial](http://www.key-project.org/eclipse/SED/tutorial.html) using the [SED examples](http://www.key-project.org/eclipse/SED/index.html#example). In addition, participation in the [evaluations](http://www.key-project.org/eclipse/SED/index.html#evaluations) allows you to try out the SED in a guided way by hand of different examples. ### <a name="screencast"></a>Screencasts

| ####  Symbolic Execution Debugger (SED)  <iframe allowfullscreen="allowfullscreen" frameborder="0" height="180" loading="lazy" src="https://www.youtube.com/embed/xvKGVyU92MY" width="320"></iframe> | #### Proof Attempt Inspection  <iframe allowfullscreen="allowfullscreen" frameborder="0" height="180" loading="lazy" src="https://www.youtube.com/embed/8e-q9Jf1h_w" width="320"></iframe> | #### Interactive Verification  <iframe allowfullscreen="allowfullscreen" data-mce-fragment="1" frameborder="0" height="180" loading="lazy" src="https://www.youtube.com/embed/IV-dEnpCLkI" width="320"></iframe> |
|---|---|---|

### <a name="troubleshooting"></a>Configuration of KeY???s symbolic execution engine and troubleshooting

- [KeY basics in Eclipse (Cross-project Functionality)](http://www.key-project.org/eclipse/CrossProject/index.html)
    - [Create an example project](http://www.key-project.org/eclipse/CrossProject/index.html#example)
    - [Change taclet options](http://www.key-project.org/eclipse/CrossProject/index.html#taclet)
    - [Define class path used by KeY](http://www.key-project.org/eclipse/CrossProject/index.html#KeYsClassPath)
- [Troubleshooting](http://www.key-project.org/eclipse/CrossProject/index.html#troubleshooting)
    - [Unresolved classtype (support for API classes)](http://www.key-project.org/eclipse/CrossProject/index.html#API)

### <a name="evaluations"></a>Experimental Evaluations

<span>The following evaluations were performed to evaluate different use cases
of the Symbolic Execution Debugger (SED).</span>**Participation is still
recommended as starting point for new users.**<span>Each evaluation explains the
use of the SED and allows you to try it out on different examples.</span>-
[Reviewing Code
Evaluation](http://www.key-project.org/eclipse/SED/ReviewingCode.html)
- [Understanding Proof Attempts Evaluation](http://www.key-project.org/eclipse/SED/UnderstandingProofAttempts.html)

### <a name="architecture"></a>Architecture

The Symbolic Execution Debugger (SED) extends [Eclipse](http://www.eclipse.org/)
and can be added to existing Eclipse-based products. In particular, SED is
compatible with the [Java Development Tools (JDT)](http://www.eclipse.org/jdt)
that provide the functionality to develop Java applications in Eclipse. To
achieve this and also a user interface that seamlessly integrates with Eclipse,
SED consequently uses and extends the Eclipse platform as shown by the following
graphic: ![](https://www.key-project.org/wp-content/uploads/2016/11/SEDArchitecture-300x129.png)<div
style="text-align: justify;">The core of Eclipse is the *Workspace* managing
projects and the user interface (*Workbench*) with editors, views and
perspectives. Based on this, provides the [Debug
Platform](http://www.eclipse.org/eclipse/debug) language independent facilities
for debugging (*Debug Core* and *Debug UI*). Finally, JDT offers functionality
to edit and debug Java programs (*JDT Core/Debug* and *JDT UI*).</div><div
style="text-align: justify;">*Symbolic Debug Core* extends the debug model of
the Debug Platform for symbolic execution in general independent from languages
and symbolic execution engines. Additional UI extensions (*Symbolic Debug UI*)
and visualization capabilities (*Visualization UI*) are also available.</div>At
last, *KeY Debug Core* implements the extended debug model for symbolic
execution based on [KeY???s symbolic execution
engine](http://www.key-project.org/eclipse/SED/index.html#SEE). The required
extensions to the user interface to launch Java methods and statements
symbolically are provided by *KeY Debug UI*. The SED platform allows to
integrate different symbolic execution engines with purpose of debugging,
program understanding or to control analysis based on symbolic execution. All to
be done is to realize the [extended debug model for symbolic
execution](http://www.key-project.org/eclipse/SED/index.html#ExtendedDebugModel)
and to offer user interface extensions to start symbolic execution. An example
implementation showing how to integrate a symbolic execution engine into the
Symbolic Execution Debugger, can be found
[here](http://www.key-project.org/eclipse/SED/example.zip). ### <a
name="ExtendedDebugModel"></a>The extended debug model for symbolic execution

The Eclipse [Debug Platform](http://www.eclipse.org/eclipse/debug) provides language independent facilities for debugging. This is achieved by a language independent debug model which is implemented for different languages like Java. Once a program is launched, it is represented as `ILaunch` and provides access to the debuggable execution context. The debuggable execution context is defined by `IDebugTarget` instances and allows for instance to list the currently running threads (`IThread`). For more details about the Debug Platform we refer to the article [How to write an Eclipse debugger](http://www.eclipse.org/articles/Article-Debugger/how-to.html). The debug model reflects the structure of running programs and is not designed for symbolic execution by default. But it can be reused and extended for symbolic execution as the following image shows: ![](https://www.key-project.org/wp-content/uploads/2016/11/ExtendedDebugModel-300x191.png)If something is launched symbolically (`ILaunch`), the debuggable execution context is defined by `ISEDDebugTarget` instances which is a subtype of `IDebugTarget`. It provides access to the root of a symbolic execution tree represented as `ISEDThread`instance. All nodes within a symbolic execution tree are subtypes of `ISEDDebugNode` that allows to access child nodes and the parent node. Beside the start node (`ISEDThread`) represent `ISEDStatement`, `ISEDBranchStatement`, `ISEDLoopStatement` and `ISEDLoopCondition` different kinds of statements. A method call treated by inlining is reprehend by an `ISEDMethodCall` and the return of the called method by `ISEDMethodReturn` or `ISEDExceptionalMethodReturn` instances. Alternatively, method calls can be treated by applying contracts (`ISEDMethodContract`) and loops by applying a loop invariant (`ISEDLoopInvariant`) instead of unrolling it. If execution splits into several branches `ISEDBranchCondition` nodes show the condition under which each path is taken. Finally, symbolic execution terminates normally (`ISEDTermination`) or exceptionally with an uncaught exception (`ISEDExceptionalTermination`). Branches executing only the loop body after an applied loop invariant end usually in an `ISEDLoopBodyTermination` node as long as the loop does not terminate abnormally.

### <a name="SEE"></a>KeY???s Symbolic Execution Engine

A general purpose symbolic execution engine based on KeY is developed
together with the Symbolic Execution Debugger. It uses only Java
functionality and can be used outside of an Eclipse setup. KeY is
a semi-automatic verification tool that proves the correctness of
sequential Java programs (without garbage collection, dynamic class
loading and floats) annotated with [JML](http://www.jmlspecs.org/)
specifications. Within a proof, symbolic execution is mixed with the
evaluation of logical formulas. KeY operates on the source code level
and thus a static symbolic execution is performed meaning that the
program is never actually executed. KeY???s Symbolic Execution Engine
constructs a proof and extracts the symbolic execution tree from it.
The main difference to verification is that no specifications are
needed at all. But if they are available, they can be used during
symbolic execution. Loop invariants ensure finite proof trees in
presence of loops. Method contracts allow to treat methods for which
the source code is not available and guarantee finite proof trees in
presence of recursive method calls. A specific proof strategy ensures
that the proofs from which the symbolic execution tree is extracted
have a suitable shape. That strategy also guarantees that symbolic
execution is done in the correct order of Java semantics. The symbolic
execution engine as such is fully automatic. In rare cases side proofs
of logical formulas (e.g., the fulfillment of pre- and postconditions)
may remain open if the strategy is not powerful enough to discharge
them.
