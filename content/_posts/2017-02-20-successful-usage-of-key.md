---
id: 1592
title: 'KeY for Your Own Research Projects'
date: '2017-10-10T12:22:20+01:00'
author: 'Dominic Steinhöfel'
layout: revision
guid: 'https://www.key-project.org/2017/10/10/992-revision-v1/'
permalink: '/?p=1592'
---

<div class="row"><div class="col-md-3 col-md-push-9"><div class="no_bullets" id="toc_container">Contents

- [Source code sample: Symbolic Execution API](#Source_code_sample_Symbolic_Execution_API)
- [Source code sample: Program verification](#Source_code_sample_Program_verification)
- [Relevant blog posts](#Relevant_blog_posts)

</div> </div><div class="col-md-9 col-md-pull-3">- KeY’s symbolic execution API: The source code version includes the project <tt>key.core.symbolic\_execution.example</tt> which provides a usage example of KeY’s symbolic execution engine.
- Verifying with KeY: The source code version includes the project <tt>key.core.example</tt> which creates all proof obligations for a given Java project and tries to verify them automatically using KeY’s prover.
 
## <span id="Source_code_sample_Symbolic_Execution_API">Source code sample: Symbolic Execution API</span>

 The following code snippet shows how to access the symbolic execution API programmatically.

https://gist.github.com/rindPHI/eb909f1c8e382604e2f60be62cd084aa

## <span id="Source_code_sample_Program_verification">Source code sample: Program verification</span>

 The following code snippet shows how to programatically prove a program correct, i.e., by calling KeY from inside source code rather then using the CLI/GUI.

https://gist.github.com/rindPHI/70b9a4b2ee3159f4f55f59ea2198637a

## <span id="Relevant_blog_posts">Relevant blog posts</span>

<div class="display-posts-listing"><div class="listing-item">[![](https://www.key-project.org/wp-content/uploads/2017/02/key-applications-150x150.png)](https://www.key-project.org/2017/02/20/successful-usage-of-key/) [How researchers from UPM and IMDEA used KeY as backend](https://www.key-project.org/2017/02/20/successful-usage-of-key/) <span class="excerpt-dash">-</span> <span class="excerpt">Researchers (Julio Mariño Raúl, N. N. Alborodo, Lars-Åke Fredlund and Ángel Herranz) from UPM and IMDEA (both Madrid, Spain) developed a methodology to synthesize verifiable concurrent Java components from formal models.</span></div></div> </div>  </div> 