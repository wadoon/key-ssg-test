---
title: '(Symbolic) Debugging'
date: '2016-12-08T10:30:33+01:00'
author: 'Dominic Steinhöfel'
---

The Symbolic Execution Debugger (SED) is a platform for symbolic
execution in general and allows to interactively debug programs based
on symbolic execution. Symbolic execution discovers all possible
execution paths simultaneously. This is achieved by the use of
symbolic in lieu of concrete values resulting in a symbolic execution
tree. Each node in the symbolic execution tree provides the full state
and related information such as the symbolic call stack or the path
conditions under which the node is reached.

Execution can start at any method or at any statement without setting
up a context. Navigation is realized using classic debugger
functionality, including stepwise execution or breakpoints.

The screenshots of the following sections illustrate the main features
of SED using KeY as symbolic execution engine. Each section contains
numbered screenshots that explain a usage scenario step by step.
Clicking on each picture produces a more detailed view. The
screenshots may differ from the latest release. At the end of this
webpage we briefly describe the architecture of SED and the theory
behind it.

### Prerequisites

The Symbolic Execution Debugger is compatible with
[Eclipse](http://www.eclipse.org) Indigo (3.7) or newer.

Required update-sites and installation instructions are available in
the [download](../../download/index.html#eclipse) area.

As getting started guide for new users we recommend the
[tutorial](tutorial.html) using the [SED examples](#example). In
addition, participation in the [evaluations](#evaluations) allows you
to try out the SED in a guided way by hand of different examples.

### Screencast: Symbolic Execution Debugger (SED)

{{< youtube xvKGVyU92MY >}} 

### Screencast: Proof Attempt Inspection

{{< youtube 8e-q9Jf1h_w >}} 

### Screencast: Interactive Verification

{{< youtube IV-dEnpCLkI >}} 

### Debug any method or any statement(s) symbolically

{{< fig src="images/launch01.png" caption="Debug any method or any statement(s) symbolically" >}}

<div class="highslide-caption">1\. Select the method or the statements to debug.</div>

<figcaption>1\. Select the method or the statements to debug.</figcaption>

</figure>

<figure>[![Debug any method or any statement(s) symbolically](images/launch02thumb.png "Debug any method or any statement(s) symbolically")](images/launch02.png) 

<div class="highslide-caption">2\. Launch selection via main menu item "Run, Debug As, Symbolic Execution Debugger (SED)".</div>

<figcaption>2\. Launch selection via main menu item  
"Run, Debug As, Symbolic Execution Debugger (SED)".</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Debug any method or any statement(s) symbolically](images/launch03thumb.png "Debug any method or any statement(s) symbolically")](images/launch03.png) 

<div class="highslide-caption">3\. Switch to perspective "Symbolic Debug".</div>

<figcaption>3\. Switch to perspective "Symbolic Debug".</figcaption>

</figure>

<figure>[![Debug any method or any statement(s) symbolically](images/launch04thumb.png "Debug any method or any statement(s) symbolically")](images/launch04.png) 

<div class="highslide-caption">4\. Perform symbolic execution interactively.</div>

<figcaption>4\. Perform symbolic execution interactively.</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Debug any method or any statement(s) symbolically](images/launch05thumb.png "Debug any method or any statement(s) symbolically")](images/launch05.png) 

<div class="highslide-caption">5\. Inspect all possible execution paths.</div>

<figcaption>5\. Inspect all possible execution paths.</figcaption>

</figure>

<figure>[![Debug any method or any statement(s) symbolically](images/launch06thumb.png "Debug any method or any statement(s) symbolically")](images/launch06.png) 

<div class="highslide-caption">6\. Inspect full state and related information of the selected node.</div>

<figcaption>6\. Inspect full state and related information of the selected node.</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Debug any method or any statement(s) symbolically](images/launch07thumb.png "Debug any method or any statement(s) symbolically")](images/launch07.png) 

<div class="highslide-caption">7\. Inspect constraints limiting the symbolic value of a variable.</div>

<figcaption>7\. Inspect constraints limiting the symbolic value of a variable.</figcaption>

</figure>

<figure>[![Debug any method or any statement(s) symbolically](images/launch08thumb.png "Debug any method or any statement(s) symbolically")](images/launch08.png) 

<div class="highslide-caption">8\. Source code reached during symbolic execution is highlighted and allows to jump to the corresponding node.</div>

<figcaption>8\. Source code reached during symbolic execution is highlighted and  
allows to jump to the corresponding node.</figcaption>

</figure>

</div>

### <a name="grouping">Collapse frames representing code blocks</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Collapse frames representing code blocks](images/group01thumb.png)](images/group01.png) 

<div class="highslide-caption">1\. Select context menu item "Collapse" of a symbolic execution tree node which opens a frame.</div>

<figcaption>1\. Select context menu item "Collapse"  
of a symbolic execution tree node which opens a frame.</figcaption>

</figure>

<figure>[![Collapse frames representing code blocks](images/group02thumb.png)](images/group02.png) 

<div class="highslide-caption">2\. In the collapsed state only the conditions under which the end of the code block is reached are shown.</div>

<figcaption>2\. In the collapsed state only the conditions  
under which the end of the code block is reached are shown.</figcaption>

</figure>

</div>

### <a name="customization">Limit execution paths by customizing the debug configuration</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Limit execution paths by customizing the debug configuration](images/custom01thumb.png "Limit execution paths by customizing the debug configuration")](images/custom01.png) 

<div class="highslide-caption">1\. Edit debug configuration via main menu item "Run, Debug Configurations...".</div>

<figcaption>1\. Edit debug configuration  
via main menu item  
"Run, Debug Configurations...".</figcaption>

</figure>

<figure>[![Limit execution paths by customizing the debug configuration](images/custom02thumb.png "Limit execution paths by customizing the debug configuration")](images/custom02.png) 

<div class="highslide-caption">2\. Limit execution paths with a precondition or by a JML specification.</div>

<figcaption>2\. Limit execution paths with a precondition or by a JML specification.</figcaption>

</figure>

<figure>[![Limit execution paths by customizing the debug configuration](images/custom03thumb.png "Limit execution paths by customizing the debug configuration")](images/custom03.png) 

<div class="highslide-caption">3\. Launch and debug as above.</div>

<figcaption>3\. Launch and debug as above.</figcaption>

</figure>

</div>

### <a name="loopInvariants">Use loop invariants to guarantee finite symbolic execution trees in presence of loops</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Use loop invariants to guarantee finite symbolic execution trees in presence of loops](images/loop01thumb.png "Use loop invariants to guarantee finite symbolic execution trees in presence of loops")](images/loop01.png) 

<div class="highslide-caption">1\. Set loop treatment to "Invariant".</div>

<figcaption>1\. Set loop treatment to "Invariant".</figcaption>

</figure>

<figure>[![Use loop invariants to guarantee finite symbolic execution trees in presence of loops](images/loop02thumb.png "Use loop invariants to guarantee finite symbolic execution trees in presence of loops")](images/loop02.png) 

<div class="highslide-caption">2\. Launch and debug as above. The "Body Preserves Invariant" branch represents an arbitrary loop iteration and ends when the loop body is completely executed. Branch "Use Case" continues execution after the loop.</div>

<figcaption>2\. Launch and debug as above. The "Body Preserves Invariant" branch represents an arbitarary  
loop iteration and ends when the loop body is completely executed.  
Branch "Use Case" continues execution after the loop.</figcaption>

</figure>

</div>

### <a name="contracts">Use method contracts if the implementation of a called method is not of interest</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Use method contracts if the implementation of a called method is not of interest](images/method01thumb.png "Use method contracts if the implementation of a called method is not of interest")](images/method01.png) 

<div class="highslide-caption">1\. Set method treatment to "Contract".</div>

<figcaption>1\. Set method treatment to "Contract".</figcaption>

</figure>

<figure>[![Use method contracts if the implementation of a called method is not of interest](images/method02thumb.png "Use method contracts if the implementation of a called method is not of interest")](images/method02.png) 

<div class="highslide-caption">2\. Launch and debug as above. If normal as well as exceptional behavior was specified in the method contract,  
symbolic execution will split after applying the contract to cover both possibilities.</div>

<figcaption>2\. Launch and debug as above. If normal as well as exceptional behavior  
was specified in the method contract, symbolic execution will split after  
applying the contract to cover both possibilities.</figcaption>

</figure>

</div>

### <a name="layouts">Visualize all possible memory layouts of a node</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Visualize all possible memory layouts of a node](images/configuration01thumb.png "Visualize all possible memory layouts of a node")](images/configuration01.png) 

<div class="highslide-caption">1\. Select "Visualize Memory Layouts".</div>

<figcaption>1\. Select "Visualize Memory Layouts".</figcaption>

</figure>

<figure>[![Visualize all possible memory layouts of a node](images/configuration02thumb.png "Visualize all possible memory layouts of a node")](images/configuration02.png) 

<div class="highslide-caption">2\. Switch to perspective "State Visualization".</div>

<figcaption>2\. Switch to perspective "State Visualization".</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Visualize all possible memory layouts of a node](images/configuration03thumb.png "Visualize all possible memory layouts of a node")](images/configuration03.png) 

<div class="highslide-caption">3\. Inspect memory layouts caused by aliasing.</div>

<figcaption>3\. Inspect memory layouts caused by aliasing.</figcaption>

</figure>

</div>

### <a name="breakpoints">Use breakpoints to find executions resulting in a specified state</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Use Breakpoints to find executions resulting in a specified state](images/breakpoints01thumb.png "Use Breakpoints to find executions resulting in a specified state")](images/breakpoints01.png) 

<div class="highslide-caption">1\. Define a Line, Method or Java Exception breakpoint, a Watchpoint or a KeY Watchpoint as usual.</div>

<figcaption>1\. Define a Line, Method or Java Exception breakpoint,  
a Watchpoint or a KeY Watchpoint as usual.</figcaption>

</figure>

<figure>[![Use Breakpoints to find executions resulting in a specified state](images/breakpoints02thumb.png "Use Breakpoints to find executions resulting in a specified state")](images/breakpoints02.png) 

<div class="highslide-caption">2\. Continue symbolic execution.</div>

<figcaption>2\. Continue symbolic execution.</figcaption>

</figure>

<figure>[![Use Breakpoints to find executions resulting in a specified state](images/breakpoints03thumb.png "Use Breakpoints to find executions resulting in a specified state")](images/breakpoints03.png) 

<div class="highslide-caption">3\. Symbolic execution suspends when breakpoint is hit.</div>

<figcaption>3\. Symbolic execution suspends  
when breakpoint is hit.</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Use Breakpoints to find executions resulting in a specified state](images/breakpoints04thumb.png "Use Breakpoints to find executions resulting in a specified state")](images/breakpoints04.png) 

<div class="highslide-caption">4\. Continue symbolic execution if desired.</div>

<figcaption>4\. Continue symbolic execution if desired.</figcaption>

</figure>

</div>

### <a name="proofAttempt">Inspect any proof performed by KeY</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Inspect any proof performed by KeY](images/proof01thumb.png)](images/proof01.png) 

<div class="highslide-caption">1\. Select the proof file to inspect and click on context menu item "Debug As, Symbolic Execution Debugger (SED)".</div>

<figcaption>1\. Select the proof file to inspect and  
click on context menu item "Debug As, Symbolic Execution Debugger (SED)".</figcaption>

</figure>

<figure>[![Inspect any proof performed by KeY](images/proof02thumb.png)](images/proof02.png) 

<div class="highslide-caption">2\. Symbolic execution tree explored by the proof is shown in view "Symbolic Execution Tree".</div>

<figcaption>2\. Symbolic execution tree explored by the proof  
is shown in view "Symbolic Execution Tree".</figcaption>

</figure>

</div>

### <a name="verifiyMethodContract">Verify a method contract</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Verify a method contract](images/verification01thumb.png)](images/verification01.png) 

<div class="highslide-caption">1\. Select "Use existing contract" in the debug configuration, use the "Browse" button to select one and click on "Debug".</div>

<figcaption>1\. Select "Use existing contract" in the debug configuration,  
use the "Browse" button to select one and click on "Debug".</figcaption>

</figure>

<figure>[![Verify a method contract](images/verification02thumb.png)](images/verification02.png) 

<div class="highslide-caption">2\. Explore the program behavior as usual.</div>

<figcaption>2\. Explore the program behavior as usual.</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Verify a method contract](images/verification03thumb.png)](images/verification03.png) 

<div class="highslide-caption">3\. The source code is conform to the method contract if and only if all branches end in a termination node and no node in the full symbolic execution tree is red crossed out.</div>

<figcaption>3\. The source code is conform to the method contract if and only if  
all branches end in a termination node and no node in the full symbolic execution tree is red crossed out.</figcaption>

</figure>

</div>

### <a name="traceTruthValues">Trace truth values evaluated by KeY as part of a proof</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Trace truth values evaluated by KeY as part of a proof](images/truthValueTracing01thumb.png)](images/truthValueTracing01.png) 

<div class="highslide-caption">1\. Enable "Truth Value Evaluation" in the debug configuration and launch it.</div>

<figcaption>1\. Enable "Truth Value Evaluation" in the debug configuration and launch it.</figcaption>

</figure>

<figure>[![Trace truth values evaluated by KeY as part of a proof](images/truthValueTracing02thumb.png)](images/truthValueTracing02.png) 

<div class="highslide-caption">2\. A red crossed out node offers a properties tab which shows the truth value tracing.</div>

<figcaption>2\. A red crossed out node offers a properties tab  
which shows the truth value tracing.</figcaption>

</figure>

</div>

### <a name="slicing">Slice a symbolic execution tree</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Slice a symbolic execution tree](images/slicing01thumb.png)](images/slicing01.png) 

<div class="highslide-caption">1\. Select context menu item "Slice Symbolic Execution Tree" of a variable in view Variables.</div>

<figcaption>1\. Select context menu item "Slice Symbolic Execution Tree"  
of a variable in view Variables.</figcaption>

</figure>

<figure>[![Slice a symbolic execution tree](images/slicing02thumb.png)](images/slicing02.png) 

<div class="highslide-caption">2\. Configure Slicing Algorithm.</div>

<figcaption>2\. Configure Slicing Algorithm.</figcaption>

</figure>

<figure>[![Slice a symbolic execution tree](images/slicing03thumb.png)](images/slicing03.png) 

<div class="highslide-caption">3\. Symbolic execution tree nodes part of the slice are highlighted.</div>

<figcaption>3\. Symbolic execution tree nodes  
part of the slice are highlighted.</figcaption>

</figure>

</div>

### <a name="comments">Add comments to symbolic execution tree nodes</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Add comments to symbolic execution tree nodes](images/comments01thumb.png)](images/comments01.png) 

<div class="highslide-caption">1\. Select symbolic execution tree node and switch to properties tab "Annotation Links". Click then on "New Comment".</div>

<figcaption>1\. Select symbolic execution tree node and  
switch to properties tab "Annotation Links".  
Click then on "New Comment".</figcaption>

</figure>

<figure>[![Add comments to symbolic execution tree nodes](images/comments02thumb.png)](images/comments02.png) 

<div class="highslide-caption">2\. Enter comment.</div>

<figcaption>2\. Enter comment.</figcaption>

</figure>

<figure>[![Add comments to symbolic execution tree nodes](images/comments03thumb.png)](images/comments03.png) 

<div class="highslide-caption">3\. Comment is shown in properties tab "Annotation Links".</div>

<figcaption>3\. Comment is shown in properties tab "Annotation Links".</figcaption>

</figure>

</div>

### <a name="search">Search text in the labels of symbolic execution tree nodes</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Search text in the labels of symbolic execution tree nodes](images/search01thumb.png)](images/search01.png) 

<div class="highslide-caption">1\. Select debug target or launch in view Debug and switch to properties tab "Annotations". Click then on "Search".</div>

<figcaption>1\. Select debug target or launch in view Debug  
and switch to properties tab "Annotations".  
Click then on "Search".</figcaption>

</figure>

<figure>[![Search text in the labels of symbolic execution tree nodes](images/search02thumb.png)](images/search02.png) 

<div class="highslide-caption">2\. Define search criteria.</div>

<figcaption>2\. Define search criteria.</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Search text in the labels of symbolic execution tree nodes](images/search03thumb.png)](images/search03.png) 

<div class="highslide-caption">3\. Nodes part of the search are highlighted.</div>

<figcaption>3\. Nodes part of the search are highlighted.</figcaption>

</figure>

<figure>[![Search text in the labels of symbolic execution tree nodes](images/search04thumb.png)](images/search04.png) 

<div class="highslide-caption">4\. Click on "Show annotation links" to list found nodes.</div>

<figcaption>4\. Click on "Show annotation links" to list found nodes.</figcaption>

</figure>

</div>

### <a name="example">Create Java project with examples for the Symbolic Execution Debugger (Tutorial)</a>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](images/example01thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](images/example01.png) 

<div class="highslide-caption">1\. Open example wizard via main menu item "File, New, Example...".</div>

<figcaption>1\. Open example wizard via main menu item "File, New, Example...".</figcaption>

</figure>

<figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](images/example02thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](images/example02.png) 

<div class="highslide-caption">2\. Select "Symbolic Execution Debugger (SED), SED Examples".</div>

<figcaption>2\. Select "Symbolic Execution Debugger (SED), SED Examples".</figcaption>

</figure>

</div>

<div class="highslide-gallery" style="display: table; border-spacing: 5px;">

<figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](images/example03thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](images/example03.png) 

<div class="highslide-caption">3\. Enter the project name.</div>

<figcaption>3\. Enter the project name.</figcaption>

</figure>

<figure>[![Create Java project with examples for the Symbolic Execution Debugger (Tutorial)](images/example04thumb.png "Create Java project with examples for the Symbolic Execution Debugger (Tutorial)")](images/example04.png) 

<div class="highslide-caption">4\. Have a look at the created example content.</div>

<figcaption>4\. Have a look at the created example content.</figcaption>

</figure>

</div>

### <a name="troubleshooting">Configuration of KeY's symbolic execution engine and troubleshooting</a>

*   [KeY basics in Eclipse (Cross-project Functionality)](../CrossProject/index.html)
    *   [Create an example project](../CrossProject/index.html#example)
    *   [Change taclet options](../CrossProject/index.html#taclet)
    *   [Define class path used by KeY](../CrossProject/index.html#KeYsClassPath)
*   [Troubleshooting](../CrossProject/index.html#troubleshooting)
    *   [Unresolved classtype (support for API classes)](../CrossProject/index.html#API)

### <a name="evaluations">Experimental Evaluations</a>

The following evaluations were performed to evaluate different use cases of the Symbolic Execution Debugger (SED).  
**Participation is still recommended as starting point for new users.**  
Each evaluation explains the use of the SED and allows you to try it out on different examples.

*   [Reviewing Code Evaluation](ReviewingCode.html)
*   [Understanding Proof Attempts Evaluation](UnderstandingProofAttempts.html)

### <a name="architecture">Architecture</a>

The Symbolic Execution Debugger (SED) extends [Eclipse](http://www.eclipse.org) and can be added to existing Eclipse-based products. In particular, SED is compatible with the [Java Development Tools (JDT)](http://www.eclipse.org/jdt) that provide the functionality to develop Java applications in Eclipse. To achieve this and also a user interface that seamlessly integrates with Eclipse, SED consequently uses and extends the Eclipse platform as shown by the following graphic:

<table border="0" cellspacing="10" cellpadding="20">

<tbody>

<tr>

<td></td>

<td colspan="2" bgcolor="#b1d3ec" align="center">KeY Debug Core</td>

<td colspan="2" bgcolor="#b1d3ec" align="center">KeY Debug UI</td>

<td></td>

</tr>

<tr>

<td></td>

<td></td>

<td rowspan="2" bgcolor="#b1d3ec" align="center">Symbolic Debug Core</td>

<td bgcolor="#b1d3ec" align="center">Visualization UI</td>

<td></td>

<td></td>

</tr>

<tr>

<td></td>

<td></td>

<td bgcolor="#b1d3ec" align="center">Symbolic Debug UI</td>

<td></td>

<td></td>

</tr>

<tr>

<td colspan="2" bgcolor="#4e9ad6" align="center">JDT Core/Debug</td>

<td bgcolor="#4e9ad6" align="center">Debug Core</td>

<td bgcolor="#4e9ad6" align="center">Debug UI</td>

<td colspan="2" bgcolor="#4e9ad6" align="center">JDT UI</td>

</tr>

<tr>

<td colspan="3" bgcolor="#4e9ad6" align="center" width="50%">Workspace</td>

<td colspan="3" bgcolor="#4e9ad6" align="center" width="50%">Workbench</td>

</tr>

</tbody>

</table>

The core of Eclipse is the _Workspace_ managing projects and the user interface (_Workbench_) with editors, views and perspectives. Based on this, provides the [Debug Platform](http://www.eclipse.org/eclipse/debug) language independent facilities for debugging (_Debug Core_ and _Debug UI_). Finally, JDT offers functionality to edit and debug Java programs (_JDT Core/Debug_ and _JDT UI_).

_Symbolic Debug Core_ extends the debug model of the Debug Platform for symbolic execution in general independent from languages and symbolic execution engines. Additional UI extensions (_Symbolic Debug UI_) and visualization capabilities (_Visualization UI_) are also available.

At last, _KeY Debug Core_ implements the extended debug model for symbolic execution based on [KeY's symbolic execution engine](#SEE). The required extensions to the user interface to launch Java methods and statements symbolically are provided by _KeY Debug UI_.

The SED platform allows to integrate different symbolic execution engines with purpose of debugging, program understanding or to control analysis based on symbolic execution. All to be done is to realize the [extended debug model for symbolic execution](#ExtendedDebugModel) and to offer user interface extensions to start symbolic execution. An example implementation showing how to integrate a symbolic execution engine into the Symbolic Execution Debugger, can be found [here](example.zip).

### <a name="ExtendedDebugModel">The extended debug model for symbolic execution</a>

The Eclipse [Debug Platform](http://www.eclipse.org/eclipse/debug) provides language independent facilities for debugging. This is achieved by a language independent debug model which is implemented for different languages like Java. Once a program is launched, it is represented as `ILaunch` and provides access to the debuggable execution context. The debuggable execution context is defined by `IDebugTarget` instances and allows for instance to list the currently running threads (`IThread`). For more details about the Debug Platform we refer to the article [How to write an Eclipse debugger](http://www.eclipse.org/articles/Article-Debugger/how-to.html).

The debug model reflects the structure of running programs and is not designed for symbolic execution by default. But it can be reused and extended for symbolic execution as the following image shows:

![](images/ExtendedDebugModel.png)

If something is launched symbolically (`ILaunch`), the debuggable
execution context is defined by `ISEDDebugTarget` instances which is
a subtype of `IDebugTarget`. It provides access to the root of
a symbolic execution tree represented as `ISEDThread` instance. All
nodes within a symbolic execution tree are subtypes of `ISEDDebugNode`
that allows to access child nodes and the parent node. Beside the
start node (`ISEDThread`) represent `ISEDStatement`,
`ISEDBranchStatement`, `ISEDLoopStatement` and `ISEDLoopCondition`
different kinds of statements. A method call treated by inlining is
reprehend by an `ISEDMethodCall` and the return of the called method
by `ISEDMethodReturn` or `ISEDExceptionalMethodReturn` instances.
Alternatively, method calls can be treated by applying contracts
(`ISEDMethodContract`) and loops by applying a loop invariant
(`ISEDLoopInvariant`) instead of unrolling it. If execution splits
into several branches `ISEDBranchCondition` nodes show the condition
under which each path is taken. Finally, symbolic execution terminates
normally (`ISEDTermination`) or exceptionally with an uncaught
exception (`ISEDExceptionalTermination`). Branches executing only the
loop body after an applied loop invariant end usually in an
`ISEDLoopBodyTermination` node as long as the loop does not terminate
abnormally.

### KeY's Symbolic Execution Engine

A general purpose symbolic execution engine based on KeY is developed
together with the Symbolic Execution Debugger. It uses only Java
functionality and can be used outside of an Eclipse setup.

KeY is a semi-automatic verification tool that proves the correctness
of sequential Java programs (without garbage collection, dynamic class
loading and floats) annotated with [JML](http://www.jmlspecs.org)
specifications. Within a proof, symbolic execution is mixed with the
evaluation of logical formulas. KeY operates on the source code level
and thus a static symbolic execution is performed meaning that the
program is never actually executed.

KeY's Symbolic Execution Engine constructs a proof and extracts the
symbolic execution tree from it. The main difference to verification
is that no specifications are needed at all. But if they are
available, they can be used during symbolic execution. Loop invariants
ensure finite proof trees in presence of loops. Method contracts allow
to treat methods for which the source code is not available and
guarantee finite proof trees in presence of recursive method calls.

A specific proof strategy ensures that the proofs from which the
symbolic execution tree is extracted have a suitable shape. That
strategy also guarantees that symbolic execution is done in the
correct order of Java semantics.

The symbolic execution engine as such is fully automatic. In rare
cases side proofs of logical formulas (e.g., the fulfillment of pre-
and postconditions) may remain open if the strategy is not powerful
enough to discharge them.
