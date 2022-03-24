---
id: 2360
title: 'Automatically Proving the Correctness of Refactoring Rules with Abstract Execution and REFINITY'
date: '2019-11-14T12:48:56+01:00'
author: 'Dominic Steinhöfel'
layout: page
guid: 'https://www.key-project.org/?page_id=2360'
uagb_style_timestamp-css:
    - '1575026547'
---

## Documentation

[Online documentation for REFINITY](https://www.key-project.org/material/REFINITYDoc/) (*under ongoing development*) is available.

## Downloads

<div class="wp-block-columns"><div class="wp-block-column"><div class="wp-block-advgb-button alignright is-style-squared">[Download KeY with REFINITY](https://www.key-project.org/material/AbstractExecution/key-2.7-AE.jar)</div></div><div class="wp-block-column"><div class="wp-block-advgb-button alignleft is-style-squared">[Get Support](mailto:steinhoefel@cs.tu-darmstadt.de)</div></div></div>You need **at least a [Java Development Kit (JDK) 11](https://adoptopenjdk.net/)** to run the Jar above. Then, just run “`java -jar key-2.7-AE.jar`“. Have a look at the descriptions below to get started.

## Example

To see an abstract program model for the equivalence proof of a refactoring in action, download and run KeY-AE and load the example “Extract Prefix” (see screenshot below) from the examples dialog. This will open the REFINITY window for inspection of the model (see screenshots section further down). To edit the model, save it to another place. By clicking the “Play” button in REFINITY’s toolbar, a proof obligation will be created and loaded in the KeY main window. Proof search will start automatically. In the lower right of the status bar in REFINITY, you get some information about the current proof status. You can also directly inspect the status in the KeY main window, which is especially useful if a proof does not close (e.g., because the model is not correct, or because of a prover incapacity).

<div class="wp-block-image"><figure class="aligncenter">[![](https://www.key-project.org/wp-content/uploads/2019/11/Screenshot-Path-To-Example.png)](https://www.key-project.org/wp-content/uploads/2019/11/Screenshot-Path-To-Example.png)<figcaption>Path in the Examples Dialog to the “Extract Prefix” Example.   
All “Abstract Execution” examples will start the REFINITY user interface.</figcaption></figure></div>## Screenshots

<figure class="wp-block-image">[![](https://www.key-project.org/wp-content/uploads/2019/11/KeY-AE-Button-Screenshot-1024x621.png)](https://www.key-project.org/wp-content/uploads/2019/11/KeY-AE-Button-Screenshot.png)<figcaption>The Button for Starting REFINITY</figcaption></figure><figure class="wp-block-image">[![](https://www.key-project.org/wp-content/uploads/2019/11/Screenshot-REFA-1-1024x739.png)](https://www.key-project.org/wp-content/uploads/2019/11/Screenshot-REFA-1.png)<figcaption>The REFINITY User Interface</figcaption></figure>## Changelog

```
<pre class="wp-block-code">```
## 2020-10-21 (v0.9.7) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Syntax checking for APE specifications
  * Instantiation checking: Check whether a concrete program is an instance of
    an abstract one. Early testing face, only programmatic access.
  * Bugfixes (e.g., no saving necessary before validating a proof)

## 2020-06-12 (v0.9.6) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Added certificate checking: Validate a saved proof bundle for a model.

## 2020-06-05 (v0.9.5) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Automatic addition of empty block { ; } after ae_constraint. Manual addition of empty block
    therefore no longer necessary.

## 2020-04-24 (v0.9.4) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Supporting postconditions via standard "ensures" for break and continue behavior
  * Stability fixes in the user interface
  * Saving recently opened REFINITY models
  * New \field and \progvar JML types for advanced framing conditions
  * Support for abstract location sets with parameters (like, e.g., "subFrame(int)")
    
    NOTE: This change breaks backwards compatibility of .aer files, as abstract location
    sets can now be parametrized and are realized as function declarations (what they
    in fact always were).

## 2019-12-29 (v0.9.3) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Changed AE rules: Initialization of result and exception objects in abstract update scope. Breaks
    backwards compatibility with existing proofs!
  * Adapted Strategies: Simplification of abstract updates has now same priority as simplification of
    concrete update. Leads to a performance boost.

## 2019-12-06 (v0.9.2) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Bug fixes in conversion to KeY file
  * Different behavior when pressing Ctrl+S for yet unsaved model: Show dialog instead of status message
  * Fixed bug in pre- postcondition relation fields about unrecognized symbols which actually have been added

## 2019-12-06 (v0.9.1) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * Supporting relational preconditions
  * Better heap simplification (abstract update simplification for select expressions, removing 
    ineffective anonymizations) 

## 2019-12-05 (v0.9) Dominic Steinhoefel <steinhoefel@cs.tu-darmstadt.de>

  * JML Support for relation to verify
  * Fixed compilation bug when using Java 8
  * Started KeY-independent versioning, displaying version number in title
```
```