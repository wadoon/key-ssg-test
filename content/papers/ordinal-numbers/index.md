---
title: 'A Mechanizable First-Order Theory of Ordinals'
date: '2017-09-06T12:00:00+01:00'
author: Peter H. Schmitt
---

> Peter H. Schmitt: A Mechanizable First-Order Theory of Ordinals. In:
> Schmidt, Renate A.; Nalon, Claudia (Ed.): Automated Reasoning with
> Analytic Tableaux and Related Methods - 26th International
> Conference, {TABLEAUX} 2017, Brasilia, Brazil, September 25-28,
> 2017, Proceedings, pp. 331–346, Springer, 2017, ISBN:
> 978-3-319-66901-4

## Abstract

We present a first-order theory of ordinals without resorting to set
theory. The theory is implemented in the KeY program verification
system which is in turn used to prove termination of a Java program
computing the Goodstein sequences.

[doi:10.1007/978-3-319-66902-1\_20](https://dx.doi.org/10.1007/978-3-319-66902-1_20)

## KeY Version with Ordinal Number Support

KeY requires Java version 8 or newer and is tested on Linux, OS X and
Microsoft Windows.

- Instant Start: [Web Start](https://formal.iti.kit.edu/key/tableaux17/webstart/KeY.jnlp)
- Binary Version: [KeY](https://formal.iti.kit.edu/key/tableaux17/key-2.5_d2d1b7463a24ad5aab7d217e8ab9e5ca13a01496.zip)
- Source Code: [KeY-src.zip](https://formal.iti.kit.edu/key/tableaux17/key-src-2.5_d2d1b7463a24ad5aab7d217e8ab9e5ca13a01496.zip)
- [GoodsteinBig.java](https://formal.iti.kit.edu/pschmitt/Tableau2017/GoodsteinBig.java)
  This program computes Goodstein sequences using Java’s BigInteger
  class. This program is not mentioned in the paper.
- [Goodstein.java](https://formal.iti.kit.edu/pschmitt/Tableau2017/Goodstein.java)
  The file `Goodstein.java` contains the Java program that is analysed
  in the paper. It does not correctly compute Goodstein sequences once
  they grow beyond maxInt. But, since in the default setting KeY
  treats Java integers as mathematical integer the performed analysis
  is correct.

  In the paper the JML annotations of “Goodstein.java” have been
  reduced to the essential core. Here the full annotation is shown. Also
  the auxiliary method for computing exponentials “intPow” is included
  
- [Program Correctness Proofs](https://formal.iti.kit.edu/pschmitt/Tableau2017/ProgrammProofs.tar)
  This tarfile contains the proofs of the contracts of the three
  methods in “Goodstein.java”. Proof files can be loaded in the KeY
  system the same way as annotated Java programs: in the pull-down
  menue “file” choose “load” and select the wanted proof file. After
  loading you may inspect the finished proof. To keep things simple
  the unpacked proof files should be placed in the same directory as
  Goodstein.java.
- The [technical report](/wp-content/uploads/2017/06/Ord.pdf) contains
  more material than could be covered in the page resticted paper.
- The program correctness proofs use a number of lemmas on ordinals,
  the embedding of positive integers into ordinals, and termination
  functions introduced for Goodstein sequences. Proofs of these lemmas
  are contained in the zip-files
  [OrdProofs1](/wp-content/uploads/2017/06/OrdProofs1.zip)
  [OrdProofs2](/wp-content/uploads/2017/06/OrdProofs2.zip)
  [OrdProofs3](/wp-content/uploads/2017/06/OrdProofs3.zip)
  respectively. The files in these zip-archives use KeY internal
  names. The correspondence between the lemma whose proof you want to
  inspect and the name of the proof file can be retrieved from
  [Fml2Taclet](/wp-content/uploads/2017/06/Fml2Taclets.pdf).
  To inspect the proofs, start the KeY system and select in the
  pull-down menue “file” subitem “load” the wanted proof file. Proof
  files come with extensions .key or .proof. The user will not note
  any difference after loading them. The .proof files contain saved
  finished proofs. The .key files contain commands of a simple,
  experimental scripting language that construct the proof on the fly.
  In some rare cases the proof in a .key file does not complete. It
  has to be completed manually, which is in all cases trivial if you
  know how to handle the prover. This phenomenon is due to
  deficiencies of the scripting language.
 
- [Run KeY via Webstart ](http://formal.iti.kit.edu/key/tableaux17/webstart/KeY.jnlp)
 


## BibTeX

```
@inproceedings{Schmitt2017,
  title = {A Mechanizable First-Order Theory of Ordinals},
  author = {Peter H. Schmitt},
  editor = {Renate A. Schmidt and Claudia Nalon},
  url = {https://www.key-project.org/papers/ordinal-numbers},
  doi = {10.1007/978-3-319-66902-1_20},
  isbn = {978-3-319-66901-4},
  year  = {2017},
  date = {2017-09-06},
  urldate = {2017-09-06},
  booktitle = {Automated Reasoning with Analytic Tableaux and Related Methods - 26th
               International Conference, {TABLEAUX} 2017, Brasilia, Brazil, September 25-28, 2017, Proceedings},
  volume = {10501},
  pages = {331--346},
  publisher = {Springer},
  series = {Lecture Notes in Computer Science},
  abstract = {We present a first-order theory of ordinals without resorting to set theory. The theory is implemented in the
              KeY program verification system which is in turn used to prove termination of a Java program computing 
              the Goodstein sequences.},
  keywords = {theorem proving},
  pubstate = {published},
  tppubtype = {inproceedings}
}
```
