---
id: 354
title: SED
date: '2016-11-30T20:24:50+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'http://key-project.se.informatik.tu-darmstadt.de/2016/11/30/351-revision-v1/'
permalink: '/?p=354'
---

## Symbolic Execution Debugger (SED)

The Symbolic Execution Debugger (SED) is a platform for symbolic execution in general and allows to interactively debug programs based on symbolic execution. Symbolic execution discovers all possible execution paths simultaneously. This is achieved by the use of symbolic in lieu of concrete values resulting in a symbolic execution tree. Each node in the symbolic execution tree provides the full state and related information such as the symbolic call stack or the path conditions under which the node is reached.

Execution can start at any method or at any statement without setting up a context. Navigation is realized using classic debugger functionality, including stepwise execution or breakpoints.

The screenshots of the following sections illustrate the main features of SED using KeY as symbolic execution engine. Each section contains numbered screenshots that explain a usage scenario step by step. Clicking on each picture produces a more detailed view. The screenshots may differ from the latest release. At the end of this webpage we briefly describe the architecture of SED and the theory behind it.

### <a name="prerequisites"></a>Prerequisites

The Symbolic Execution Debugger is compatible with [Eclipse](http://www.eclipse.org/) Mars or newer.

Required update-sites and installation instructions are available in the [download](http://www.key-project.org/download/index.html#eclipse) area.

As getting started guide for new users we recommend the [tutorial](http://www.key-project.org/eclipse/SED/tutorial.html) using the [SED examples](http://www.key-project.org/eclipse/SED/index.html#example).  
In addition, participation in the [evaluations](http://www.key-project.org/eclipse/SED/index.html#evaluations) allows you to try out the SED in a guided way by hand of different examples.

### <a name="screencast"></a>Screencast: Symbolic Execution Debugger (SED)

<iframe allowfullscreen="allowfullscreen" frameborder="0" height="360" loading="lazy" src="https://www.youtube.com/embed/xvKGVyU92MY" width="640"></iframe>### <a name="screencast"></a>Screencast: Proof Attempt Inspection

<iframe allowfullscreen="allowfullscreen" frameborder="0" height="360" loading="lazy" src="https://www.youtube.com/embed/8e-q9Jf1h_w" width="640"></iframe>### <a name="screencast"></a>Screencast: Interactive Verification

<iframe allowfullscreen="allowfullscreen" frameborder="0" height="360" loading="lazy" src="https://www.youtube.com/embed/IV-dEnpCLkI" width="640"></iframe>### <a name="launch"></a>Debug any method or any statement(s) symbolically

<div class="highslide-gallery"><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch01thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch01.png)<figcaption>1. Select the method or the statements to debug.</figcaption></figure><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch02thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch02.png)<figcaption>2. Launch selection via main menu item  
“Run, Debug As, Symbolic Execution Debugger (SED)”.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch03thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch03.png)<figcaption>3. Switch to perspective “Symbolic Debug”.</figcaption></figure><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch04thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch04.png)<figcaption>4. Perform symbolic execution interactively.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch05thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch05.png)<figcaption>5. Inspect all possible execution paths.</figcaption></figure><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch06thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch06.png)<figcaption>6. Inspect full state and related information of the selected node.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch07thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch07.png)<figcaption>7. Inspect constraints limiting the symbolic value of a variable.</figcaption></figure><figure>[![Debug any method or any statement(s) symbolically](http://www.key-project.org/eclipse/SED/images/launch08thumb.png "Debug any method or any statement(s) symbolically")](http://www.key-project.org/eclipse/SED/images/launch08.png)<figcaption>8. Source code reached during symbolic execution is highlighted and  
allows to jump to the corresponding node.</figcaption></figure></div>### <a name="grouping"></a>Collapse frames representing code blocks

<div class="highslide-gallery"><figure>[![Collapse frames representing code blocks](http://www.key-project.org/eclipse/SED/images/group01thumb.png)](http://www.key-project.org/eclipse/SED/images/group01.png)<figcaption>1. Select context menu item “Collapse”  
of a symbolic execution tree node which opens a frame.</figcaption></figure><figure>[![Collapse frames representing code blocks](http://www.key-project.org/eclipse/SED/images/group02thumb.png)](http://www.key-project.org/eclipse/SED/images/group02.png)<figcaption>2. In the collapsed state only the conditions  
under which the end of the code block is reached are shown.</figcaption></figure></div>### <a name="customization"></a>Limit execution paths by customizing the debug configuration

<div class="highslide-gallery"><figure>[![Limit execution paths by customizing the debug configuration](http://www.key-project.org/eclipse/SED/images/custom01thumb.png "Limit execution paths by customizing the debug configuration")](http://www.key-project.org/eclipse/SED/images/custom01.png)<figcaption>1. Edit debug configuration  
via main menu item   
“Run, Debug Configurations…”.</figcaption></figure><figure>[![Limit execution paths by customizing the debug configuration](http://www.key-project.org/eclipse/SED/images/custom02thumb.png "Limit execution paths by customizing the debug configuration")](http://www.key-project.org/eclipse/SED/images/custom02.png)<figcaption>2. Limit execution paths with a precondition or by a JML specification.</figcaption></figure><figure>[![Limit execution paths by customizing the debug configuration](http://www.key-project.org/eclipse/SED/images/custom03thumb.png "Limit execution paths by customizing the debug configuration")](http://www.key-project.org/eclipse/SED/images/custom03.png)<figcaption>3. Launch and debug as above.</figcaption></figure></div>### <a name="loopInvariants"></a>Use loop invariants to guarantee finite symbolic execution trees in presence of loops

<div class="highslide-gallery"><figure>[![Use loop invariants to guarantee finite symbolic execution trees in presence of loops](http://www.key-project.org/eclipse/SED/images/loop01thumb.png "Use loop invariants to guarantee finite symbolic execution trees in presence of loops")](http://www.key-project.org/eclipse/SED/images/loop01.png)<figcaption>1. Set loop treatment to “Invariant”.</figcaption></figure><figure>[![Use loop invariants to guarantee finite symbolic execution trees in presence of loops](http://www.key-project.org/eclipse/SED/images/loop02thumb.png "Use loop invariants to guarantee finite symbolic execution trees in presence of loops")](http://www.key-project.org/eclipse/SED/images/loop02.png)<figcaption>2. Launch and debug as above. The “Body Preserves Invariant” branch represents an arbitarary  
loop iteration and ends when the loop body is completely executed.  
Branch “Use Case” continues execution after the loop.</figcaption></figure></div>### <a name="contracts"></a>Use method contracts if the implementation of a called method is not of interest

<div class="highslide-gallery"><figure>[![Use method contracts if the implementation of a called method is not of interest](http://www.key-project.org/eclipse/SED/images/method01thumb.png "Use method contracts if the implementation of a called method is not of interest")](http://www.key-project.org/eclipse/SED/images/method01.png)<figcaption>1. Set method treatment to “Contract”.</figcaption></figure><figure>[![Use method contracts if the implementation of a called method is not of interest](http://www.key-project.org/eclipse/SED/images/method02thumb.png "Use method contracts if the implementation of a called method is not of interest")](http://www.key-project.org/eclipse/SED/images/method02.png)<figcaption>2. Launch and debug as above. If normal as well as exceptional behavior  
was specified in the method contract, symbolic execution will split after  
applying the contract to cover both possibilities.</figcaption></figure></div>### <a name="layouts"></a>Visualize all possible memory layouts of a node

<div class="highslide-gallery"><figure>[![Visualize all possible memory layouts of a node](http://www.key-project.org/eclipse/SED/images/configuration01thumb.png "Visualize all possible memory layouts of a node")](http://www.key-project.org/eclipse/SED/images/configuration01.png)<figcaption>1. Select “Visualize Memory Layouts”.</figcaption></figure><figure>[![Visualize all possible memory layouts of a node](http://www.key-project.org/eclipse/SED/images/configuration02thumb.png "Visualize all possible memory layouts of a node")](http://www.key-project.org/eclipse/SED/images/configuration02.png)<figcaption>2. Switch to perspective “State Visualization”.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Visualize all possible memory layouts of a node](http://www.key-project.org/eclipse/SED/images/configuration03thumb.png "Visualize all possible memory layouts of a node")](http://www.key-project.org/eclipse/SED/images/configuration03.png)<figcaption>3. Inspect memory layouts caused by aliasing.</figcaption></figure></div>### <a name="breakpoints"></a>Use breakpoints to find executions resulting in a specified state

<div class="highslide-gallery"><figure>[![Use Breakpoints to find executions resulting in a specified state](http://www.key-project.org/eclipse/SED/images/breakpoints01thumb.png "Use Breakpoints to find executions resulting in a specified state")](http://www.key-project.org/eclipse/SED/images/breakpoints01.png)<figcaption>1. Define a Line, Method or Java Exception breakpoint,  
a Watchpoint or a KeY Watchpoint as usual.</figcaption></figure><figure>[![Use Breakpoints to find executions resulting in a specified state](http://www.key-project.org/eclipse/SED/images/breakpoints02thumb.png "Use Breakpoints to find executions resulting in a specified state")](http://www.key-project.org/eclipse/SED/images/breakpoints02.png)<figcaption>2. Continue symbolic execution.</figcaption></figure><figure>[![Use Breakpoints to find executions resulting in a specified state](http://www.key-project.org/eclipse/SED/images/breakpoints03thumb.png "Use Breakpoints to find executions resulting in a specified state")](http://www.key-project.org/eclipse/SED/images/breakpoints03.png)<figcaption>3. Symbolic execution suspends  
when breakpoint is hit.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Use Breakpoints to find executions resulting in a specified state](http://www.key-project.org/eclipse/SED/images/breakpoints04thumb.png "Use Breakpoints to find executions resulting in a specified state")](http://www.key-project.org/eclipse/SED/images/breakpoints04.png)<figcaption>4. Continue symbolic execution if desired.</figcaption></figure></div>### <a name="proofAttempt"></a>Inspect any proof performed by KeY

<div class="highslide-gallery"><figure>[![Inspect any proof performed by KeY](http://www.key-project.org/eclipse/SED/images/proof01thumb.png)](http://www.key-project.org/eclipse/SED/images/proof01.png)<figcaption>1. Select the proof file to inspect and  
click on context menu item “Debug As, Symbolic Execution Debugger (SED)”.</figcaption></figure><figure>[![Inspect any proof performed by KeY](http://www.key-project.org/eclipse/SED/images/proof02thumb.png)](http://www.key-project.org/eclipse/SED/images/proof02.png)<figcaption>2. Symbolic execution tree explored by the proof  
is shown in view “Symbolic Execution Tree”.</figcaption></figure></div>### <a name="verifiyMethodContract"></a>Verify a method contract

<div class="highslide-gallery"><figure>[![Verify a method contract](http://www.key-project.org/eclipse/SED/images/verification01thumb.png)](http://www.key-project.org/eclipse/SED/images/verification01.png)<figcaption>1. Select “Use existing contract” in the debug configuration,   
use the “Browse” button to select one and click on “Debug”.</figcaption></figure><figure>[![Verify a method contract](http://www.key-project.org/eclipse/SED/images/verification02thumb.png)](http://www.key-project.org/eclipse/SED/images/verification02.png)<figcaption>2. Explore the program behavior as usual.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Verify a method contract](http://www.key-project.org/eclipse/SED/images/verification03thumb.png)](http://www.key-project.org/eclipse/SED/images/verification03.png)<figcaption>3. The source code is conform to the method contract if and only if  
all branches end in a termination node and no node in the full symbolic execution tree is red crossed out.</figcaption></figure></div>### <a name="traceTruthValues"></a>Trace truth values evaluated by KeY as part of a proof

<div class="highslide-gallery"><figure>[![Trace truth values evaluated by KeY as part of a proof](http://www.key-project.org/eclipse/SED/images/truthValueTracing01thumb.png)](http://www.key-project.org/eclipse/SED/images/truthValueTracing01.png)<figcaption>1. Enable “Truth Value Evaluation” in the debug configuration and launch it.</figcaption></figure><figure>[![Trace truth values evaluated by KeY as part of a proof](http://www.key-project.org/eclipse/SED/images/truthValueTracing02thumb.png)](http://www.key-project.org/eclipse/SED/images/truthValueTracing02.png)<figcaption>2. A red crossed out node offers a properties tab  
which shows the truth value tracing.</figcaption></figure></div>### <a name="slicing"></a>Slice a symbolic execution tree

<div class="highslide-gallery"><figure>[![Slice a symbolic execution tree](http://www.key-project.org/eclipse/SED/images/slicing01thumb.png)](http://www.key-project.org/eclipse/SED/images/slicing01.png)<figcaption>1. Select context menu item “Slice Symbolic Execution Tree”   
of a variable in view Variables.</figcaption></figure><figure>[![Slice a symbolic execution tree](http://www.key-project.org/eclipse/SED/images/slicing02thumb.png)](http://www.key-project.org/eclipse/SED/images/slicing02.png)<figcaption>2. Configure Slicing Algorithm.</figcaption></figure><figure>[![Slice a symbolic execution tree](http://www.key-project.org/eclipse/SED/images/slicing03thumb.png)](http://www.key-project.org/eclipse/SED/images/slicing03.png)<figcaption>3. Symbolic execution tree nodes  
part of the slice are highlighted.</figcaption></figure></div>### <a name="comments"></a>Add comments to symbolic execution tree nodes

<div class="highslide-gallery"><figure>[![Add comments to symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/comments01thumb.png)](http://www.key-project.org/eclipse/SED/images/comments01.png)<figcaption>1. Select symbolic execution tree node and  
switch to properties tab “Annotation Links”.  
Click then on “New Comment”.</figcaption></figure><figure>[![Add comments to symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/comments02thumb.png)](http://www.key-project.org/eclipse/SED/images/comments02.png)<figcaption>2. Enter comment.</figcaption></figure><figure>[![Add comments to symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/comments03thumb.png)](http://www.key-project.org/eclipse/SED/images/comments03.png)<figcaption>3. Comment is shown in properties tab “Annotation Links”.</figcaption></figure></div>### <a name="search"></a>Search text in the labels of symbolic execution tree nodes

<div class="highslide-gallery"><figure>[![Search text in the labels of symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/search01thumb.png)](http://www.key-project.org/eclipse/SED/images/search01.png)<figcaption>1. Select debug target or launch in view Debug  
and switch to properties tab “Annotations”.   
Click then on “Search”.</figcaption></figure><figure>[![Search text in the labels of symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/search02thumb.png)](http://www.key-project.org/eclipse/SED/images/search02.png)<figcaption>2. Define search criteria.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Search text in the labels of symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/search03thumb.png)](http://www.key-project.org/eclipse/SED/images/search03.png)<figcaption>3. Nodes part of the search are highlighted.</figcaption></figure><figure>[![Search text in the labels of symbolic execution tree nodes](http://www.key-project.org/eclipse/SED/images/search04thumb.png)](http://www.key-project.org/eclipse/SED/images/search04.png)<figcaption>4. Click on “Show annotation links” to list found nodes.</figcaption></figure></div>### <a name="example"></a>Create Java project with examples for the Symbolic Execution Debugger (Tutorial)

<div class="highslide-gallery"><figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](http://www.key-project.org/eclipse/SED/images/example01thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](http://www.key-project.org/eclipse/SED/images/example01.png)<figcaption>1. Open example wizard via main menu item “File, New, Example…”.</figcaption></figure><figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](http://www.key-project.org/eclipse/SED/images/example02thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](http://www.key-project.org/eclipse/SED/images/example02.png)<figcaption>2. Select “Symbolic Execution Debugger (SED), SED Examples”.</figcaption></figure></div><div class="highslide-gallery"><figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](http://www.key-project.org/eclipse/SED/images/example03thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](http://www.key-project.org/eclipse/SED/images/example03.png)<figcaption>3. Enter the project name.</figcaption></figure><figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](http://www.key-project.org/eclipse/SED/images/example04thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](http://www.key-project.org/eclipse/SED/images/example04.png)<figcaption>4. Have a look at the created example content.</figcaption></figure></div>### <a name="troubleshooting"></a>Configuration of KeY’s symbolic execution engine and troubleshooting

- [KeY basics in Eclipse (Cross-project Functionality)](http://www.key-project.org/eclipse/CrossProject/index.html)
    - [Create an example project](http://www.key-project.org/eclipse/CrossProject/index.html#example)
    - [Change taclet options](http://www.key-project.org/eclipse/CrossProject/index.html#taclet)
    - [Define class path used by KeY](http://www.key-project.org/eclipse/CrossProject/index.html#KeYsClassPath)
- [Troubleshooting](http://www.key-project.org/eclipse/CrossProject/index.html#troubleshooting)
    - [Unresolved classtype (support for API classes)](http://www.key-project.org/eclipse/CrossProject/index.html#API)

### <a name="evaluations"></a>Experimental Evaluations

The following evaluations were performed to evaluate different use cases of the Symbolic Execution Debugger (SED).  
**Participation is still recommended as starting point for new users.**  
Each evaluation explains the use of the SED and allows you to try it out on different examples.- [Reviewing Code Evaluation](http://www.key-project.org/eclipse/SED/ReviewingCode.html)
- [Understanding Proof Attempts Evaluation](http://www.key-project.org/eclipse/SED/UnderstandingProofAttempts.html)

### <a name="architecture"></a>Architecture

The Symbolic Execution Debugger (SED) extends [Eclipse](http://www.eclipse.org/) and can be added to existing Eclipse-based products. In particular, SED is compatible with the [Java Development Tools (JDT)](http://www.eclipse.org/jdt) that provide the functionality to develop Java applications in Eclipse. To achieve this and also a user interface that seamlessly integrates with Eclipse, SED consequently uses and extends the Eclipse platform as shown by the following graphic:

|  | KeY Debug Core | KeY Debug UI |  |
|---|:-:|:-:|---|
|  |  | Symbolic Debug Core | Visualization UI |  |  |
|  |  | Symbolic Debug UI |  |  |
| JDT Core/Debug | Debug Core | Debug UI | JDT UI |
| Workspace | Workbench |

The core of Eclipse is the *Workspace* managing projects and the user interface (*Workbench*) with editors, views and perspectives. Based on this, provides the [Debug Platform](http://www.eclipse.org/eclipse/debug) language independent facilities for debugging (*Debug Core* and *Debug UI*). Finally, JDT offers functionality to edit and debug Java programs (*JDT Core/Debug* and *JDT UI*).

*Symbolic Debug Core* extends the debug model of the Debug Platform for symbolic execution in general independent from languages and symbolic execution engines. Additional UI extensions (*Symbolic Debug UI*) and visualization capabilities (*Visualization UI*) are also available.

At last, *KeY Debug Core* implements the extended debug model for symbolic execution based on [KeY’s symbolic execution engine](http://www.key-project.org/eclipse/SED/index.html#SEE). The required extensions to the user interface to launch Java methods and statements symbolically are provided by *KeY Debug UI*.

The SED platform allows to integrate different symbolic execution engines with purpose of debugging, program understanding or to control analysis based on symbolic execution. All to be done is to realize the [extended debug model for symbolic execution](http://www.key-project.org/eclipse/SED/index.html#ExtendedDebugModel) and to offer user interface extensions to start symbolic execution. An example implementation showing how to integrate a symbolic execution engine into the Symbolic Execution Debugger, can be found [here](http://www.key-project.org/eclipse/SED/example.zip).

### <a name="ExtendedDebugModel"></a>The extended debug model for symbolic execution

The Eclipse [Debug Platform](http://www.eclipse.org/eclipse/debug) provides language independent facilities for debugging. This is achieved by a language independent debug model which is implemented for different languages like Java. Once a program is launched, it is represented as `ILaunch` and provides access to the debuggable execution context. The debuggable execution context is defined by `IDebugTarget` instances and allows for instance to list the currently running threads (`IThread`). For more details about the Debug Platform we refer to the article [How to write an Eclipse debugger](http://www.eclipse.org/articles/Article-Debugger/how-to.html).

The debug model reflects the structure of running programs and is not designed for symbolic execution by default. But it can be reused and extended for symbolic execution as the following image shows:

![](http://www.key-project.org/eclipse/SED/images/ExtendedDebugModel.png)

If something is launched symbolically (`ILaunch`), the debuggable execution context is defined by `ISEDDebugTarget` instances which is a subtype of `IDebugTarget`. It provides access to the root of a symbolic execution tree represented as `ISEDThread`instance. All nodes within a symbolic execution tree are subtypes of `ISEDDebugNode` that allows to access child nodes and the parent node. Beside the start node (`ISEDThread`) represent `ISEDStatement`, `ISEDBranchStatement`, `ISEDLoopStatement` and `ISEDLoopCondition` different kinds of statements. A method call treated by inlining is reprehend by an `ISEDMethodCall` and the return of the called method by `ISEDMethodReturn` or `ISEDExceptionalMethodReturn` instances. Alternatively, method calls can be treated by applying contracts (`ISEDMethodContract`) and loops by applying a loop invariant (`ISEDLoopInvariant`) instead of unrolling it. If execution splits into several branches `ISEDBranchCondition` nodes show the condition under which each path is taken. Finally, symbolic execution terminates normally (`ISEDTermination`) or exceptionally with an uncaught exception (`ISEDExceptionalTermination`). Branches executing only the loop body after an applied loop invariant end usually in an `ISEDLoopBodyTermination` node as long as the loop does not terminate abnormally.

### <a name="SEE"></a>KeY’s Symbolic Execution Engine

A general purpose symbolic execution engine based on KeY is developed together with the Symbolic Execution Debugger. It uses only Java functionality and can be used outside of an Eclipse setup.

KeY is a semi-automatic verification tool that proves the correctness of sequential Java programs (without garbage collection, dynamic class loading and floats) annotated with [JML](http://www.jmlspecs.org/) specifications. Within a proof, symbolic execution is mixed with the evaluation of logical formulas. KeY operates on the source code level and thus a static symbolic execution is performed meaning that the program is never actually executed.

KeY’s Symbolic Execution Engine constructs a proof and extracts the symbolic execution tree from it. The main difference to verification is that no specifications are needed at all. But if they are available, they can be used during symbolic execution. Loop invariants ensure finite proof trees in presence of loops. Method contracts allow to treat methods for which the source code is not available and guarantee finite proof trees in presence of recursive method calls.

A specific proof strategy ensures that the proofs from which the symbolic execution tree is extracted have a suitable shape. That strategy also guarantees that symbolic execution is done in the correct order of Java semantics.

The symbolic execution engine as such is fully automatic. In rare cases side proofs of logical formulas (e.g., the fulfillment of pre- and postconditions) may remain open if the strategy is not powerful enough to discharge them.