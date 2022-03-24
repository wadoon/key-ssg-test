---
id: 382
title: 'KeY Resources'
date: '2016-12-21T20:57:05+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'http://key-project.se.informatik.tu-darmstadt.de/2016/11/30/376-autosave-v1/'
permalink: '/?p=382'
---

KeY Resources provides the “KeY project” with automatic background proofs. Such projects extends the functionality of a Java project by maintaining automatically proofs in background. This means that the tool tries to do proofs automatically whenever files in a project change. Markers are used to show the proof result directly in the source editor.

The following sections illustrate the main features of KeY Resources using screenshots. Each section contains numbered screenshots that explain a usage scenario step by step. Clicking on each picture produces a more detailed view. The screenshots may differ from the latest release.

### Prerequisites

KeY Resources is compatible with [Eclipse](http://www.eclipse.org/) Mars or newer.

Required update-sites and installation instructions are available in the [download](http://key-project.se.informatik.tu-darmstadt.de/download/) area.

### Create a KeY Project

<div class="row"><div class="col-md-4"> ![Create a KeY Project](/uploads/2016/11/create01-300x174.png)1\. Open new project wizard via Package Explorer context menu item “New, Project…”

 </div><div class="col-md-4"> ![Select  KeY Project](/uploads/2016/11/create02-300x174.png)2\. Select “KeY Project”

</div></div><div class="row"><div class="col-md-8" style="text-align: center; vertical-align: top;"> ![Define project](/uploads/2016/11/create03-300x174.png)3\. Define project name and finish the wizard

</div></div>### Work with a KeY Project

<div class="row"><div class="col-md-4"> ![Edit & Save source code](/uploads/2016/11/work01-300x174.png)1\. Edit source code as normal and save it

</div><div class="col-md-4"> ![Proofs are performed during build](/uploads/2016/11/work02-300x174.png)2\. During build proofs are automatically executed and results are shown via marker

</div></div><div class="row"><div class="col-md-4"> ![Proofs managed by IDE (folder proofs)](/uploads/2016/11/work03-300x174.png)3\. Proofs are automatically maintained in folder “proofs”

</div><div class="col-md-4"> ![Tooltip over proof marker](/uploads/2016/11/work04-300x174.png)4\. Tooltip of a marker explains the proof state and give hints how to continue

</div></div><div class="row"><div class="col-md-8" style="text-align: center; vertical-align: top;"> ![Debug or open proofs](/uploads/2016/11/work05-300x174.png)5\. Proof files can be opend in KeY or the KeYIDE via a marker by selecting “Open proof” to inspect and finish the proof. In addition, a proof can be inspected in the SED via marker menu item “Debug proof”

</div></div>### Inspect verification status

<div class="row"><div class="col-md-4"> ![Select Other Views](/uploads/2016/11/status01-300x174.png)1\. Select main menu item “Window, Show View, Other…”

</div><div class="col-md-4"> [![Open view "Verification Status"](/uploads/2016/11/status02-300x174.png)](/uploads/2016/11/status02.png)2\. Open view “Verification Status”

</div></div><div class="row"><div class="col-md-4"> ![Status colors](/uploads/2016/11/status03-300x174.png)3\. Colors of tree items indicate verification statuses

 </div><div class="col-md-4"> ![HTML report](/uploads/2016/11/status04-300x174.png) 4. HTML report lists tasks and assumptions used by proofs

</div></div>### Inspect verification log

<div class="row"><div class="col-md-4"> ![log01](/uploads/2016/11/log01-300x174.png)1\. Select main menu item “Window, Show View, Other…”

 </div><div class="col-md-4"> ![log02](/uploads/2016/11/log02-300x174.png)2\. Open view “Verification Log”

</div></div><div class="row"><div class="col-md-8" style="text-align: center; vertical-align: middle;"> ![log03](/uploads/2016/11/log03-300x174.png)3\. Table shows used settings and times of performed verification tasks

 </div></div>### Customize build settings

[![](http://key-project.se.informatik.tu-darmstadt.de/wp-content/uploads/2016/11/custom01-300x174.png)](http://key-project.se.informatik.tu-darmstadt.de/wp-content/uploads/2016/11/custom01.png)<div class="row"><div class="col-md-4"> ![Customize build settings](/uploads/2016/11/custom01-300x174.png "Customize build settings")1\. Open project properties of a KeY project via context menu item “Properties”.

 </div><div class="col-md-4"> ![Customize build settings](/uploads/2016/11/custom02-300x174.png "Customize build settings")2\. Select properties page “KeY, KeY Proof Management” and customize build settings. E.g. enable counter example and test case generation.

 </div> </div>### Generated Test Cases

 <figure>[![Generated Test Cases](http://www.key-project.org/eclipse/KeYResources/images/testGeneration01thumb.png "Generated Test Cases")](http://www.key-project.org/eclipse/KeYResources/images/testGeneration01.png)<figcaption>1. Generated test cases are maintained in an additional Java project.  
In addition, a test suite which executes all test cases is generated.</figcaption></figure>### Inspect a counter example

 <figure>[![Inspect a counter example](http://www.key-project.org/eclipse/KeYResources/images/counterExample01thumb.png "Inspect a counter example")](http://www.key-project.org/eclipse/KeYResources/images/counterExample01.png)<figcaption>1. Counter examples can be opend via a marker by selecting “Show Counter Examples”.</figcaption></figure><figure>[![Inspect a counter example](http://www.key-project.org/eclipse/KeYResources/images/counterExample02thumb.png "Inspect a counter example")](http://www.key-project.org/eclipse/KeYResources/images/counterExample02.png)<figcaption>2. Inspect the opened counter example.</figcaption></figure>### Convert a Java Project into a KeY Project

 <figure>[![Convert a Java Project into a KeY Project](http://www.key-project.org/eclipse/KeYResources/images/convert01thumb.png "Convert a Java Project into a KeY Project")](http://www.key-project.org/eclipse/KeYResources/images/convert01.png)<figcaption>1. Select “Convert to KeY Project” in the context menu of a Java project.</figcaption></figure><figure>[![Convert a Java Project into a KeY Project](http://www.key-project.org/eclipse/KeYResources/images/convert02thumb.png "Convert a Java Project into a KeY Project")](http://www.key-project.org/eclipse/KeYResources/images/convert02.png)<figcaption>2. Proofs are automatically maintained  
after conversion.</figcaption></figure>### KeY basics in Eclipse and troubleshooting

- [KeY basics in Eclipse (Cross-project Functionality)](http://www.key-project.org/eclipse/CrossProject/index.html)
    - [Create an example project](http://www.key-project.org/eclipse/CrossProject/index.html#example)
    - [Change taclet options](http://www.key-project.org/eclipse/CrossProject/index.html#taclet)
    - [Define class path used by KeY](http://www.key-project.org/eclipse/CrossProject/index.html#KeYsClassPath)
- [Troubleshooting](http://www.key-project.org/eclipse/CrossProject/index.html#troubleshooting)
    - [Unresolved classtype (support for API classes)](http://www.key-project.org/eclipse/CrossProject/index.html#API)