---
title: 'KeY for Your Own Research Projects'
date: '2017-10-10T12:22:20+01:00'
author: 'Dominic Steinhöfel'
---

KeY’s symbolic execution API: The source code version includes the
project <tt>key.core.symbolic\_execution.example</tt> which provides
a usage example of KeY’s symbolic execution engine.
- Verifying with KeY: The source code version includes the project
  <tt>key.core.example</tt> which creates all proof obligations for
  a given Java project and tries to verify them automatically using
  KeY’s prover.
 

## Source code sample: Symbolic Execution API

 The following code snippet shows how to access the symbolic execution API programmatically.

https://gist.github.com/rindPHI/eb909f1c8e382604e2f60be62cd084aa


## Source code sample: Program verification

The following code snippet shows how to programatically prove
a program correct, i.e., by calling KeY from inside source code rather
then using the CLI/GUI.

https://gist.github.com/rindPHI/70b9a4b2ee3159f4f55f59ea2198637a

## Relevant blog posts

[![](https://www.key-project.org/wp-content/uploads/2017/02/key-applications-150x150.png)](https://www.key-project.org/2017/02/20/successful-usage-of-key/)
[How researchers from UPM and IMDEA used KeY as
backend](https://www.key-project.org/2017/02/20/successful-usage-of-key/)
- Researchers (Julio Mariño Raúl, N. N. Alborodo, Lars-Åke Fredlund
and Ángel Herranz) from UPM and IMDEA (both Madrid, Spain) developed
a methodology to synthesize verifiable concurrent Java components from
formal models.
