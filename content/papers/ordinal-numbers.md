---
id: 1074
title: 'Ordinal Numbers'
date: '2017-03-31T09:21:17+01:00'
author: 'Richard Bubel'
layout: page
guid: 'https://www.key-project.org/?page_id=1074'
ampforwp-amp-on-off:
    - default
ampforwp_custom_content_editor:
    - ''
ampforwp_custom_content_editor_checkbox:
    - null
ampforwp_custom_sidebar_select:
    - none
---

v

## KeY Version with Ordinal Number Support (For Tableaux 2017 Reviewers Only)

<div class="row"><div class="col-md-8">### Download or Start

KeY requires Java version 8 or newer and is tested on Linux, OS X and Microsoft Windows.

- Instant Start: [Web Start](https://formal.iti.kit.edu/key/tableaux17/webstart/KeY.jnlp)
- Binary Version: [KeY](https://formal.iti.kit.edu/key/tableaux17/key-2.5_d2d1b7463a24ad5aab7d217e8ab9e5ca13a01496.zip)
- Source Code: [KeY-src.zip](https://formal.iti.kit.edu/key/tableaux17/key-src-2.5_d2d1b7463a24ad5aab7d217e8ab9e5ca13a01496.zip)
- [GoodsteinBig.java](https://formal.iti.kit.edu/pschmitt/Tableau2017/GoodsteinBig.java) This program computes Goodstein sequences using Java’s BigInteger class. This program is not mentioned in the paper.
- [Goodstein.java](https://formal.iti.kit.edu/pschmitt/Tableau2017/Goodstein.java) The file “Goodstein.java” contains the Java program that is analysed in the paper. It does not correctly compute Goodstein sequences once they grow beyond maxInt. But, since in the default setting KeY treats Java integers as mathematical integer the performed analysis is correct.  
     In the paper the JML annotations of “Goodstein.java” have been reduced to the essential core. Here the full annotation is shown. Also the auxiliary method for computing exponentials “intPow” is included
- [Program Correctness Proofs](https://formal.iti.kit.edu/pschmitt/Tableau2017/ProgrammProofs.tar) This tarfile contains the proofs of the contracts of the three methods in “Goodstein.java”. Proof files can be loaded in the KeY system the same way as annotated Java programs: in the pull-down menue “file” choose “load” and select the wanted proof file. After loading you may inspect the finished proof. To keep things simple the unpacked proof files should be placed in the same directory as Goodstein.java.
- The [technical report](https://www.key-project.org/wp-content/uploads/2017/06/Ord.pdf) contains more material than could be covered in the page resticted paper.
- The program correctness proofs use a number of lemmas on ordinals, the embedding of positive integers into ordinals, and termination functions introduced for Goodstein sequences. Proofs of these lemmas are contained in the zip-files [OrdProofs1](https://www.key-project.org/wp-content/uploads/2017/06/OrdProofs1.zip) [OrdProofs2](https://www.key-project.org/wp-content/uploads/2017/06/OrdProofs2.zip) [OrdProofs3](https://www.key-project.org/wp-content/uploads/2017/06/OrdProofs3.zip) respectively. The files in these zip-archives use KeY internal names. The correspondence between the lemma whose proof you want to inspect and the name of the proof file can be retrieved from [Fml2Taclet](https://www.key-project.org/wp-content/uploads/2017/06/Fml2Taclets.pdf). To inspect the proofs, start the KeY system and select in the pull-down menue “file” subitem “load” the wanted proof file. Proof files come with extensions .key or .proof. The user will not note any difference after loading them. The .proof files contain saved finished proofs. The .key files contain commands of a simple, experimental scripting language that construct the proof on the fly. In some rare cases the proof in a .key file does not complete. It has to be completed manually, which is in all cases trivial if you know how to handle the prover. This phenomenon is due to deficiencies of the scripting language.
 
 </div><div class="col-md-4"> [<span class="glyphicon glyphicon-play"></span> Run KeY via Webstart ](http://formal.iti.kit.edu/key/tableaux17/webstart/KeY.jnlp) </div></div>