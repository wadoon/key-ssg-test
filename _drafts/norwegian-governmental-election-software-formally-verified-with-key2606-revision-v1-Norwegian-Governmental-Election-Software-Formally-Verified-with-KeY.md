---
id: 2613
title: 'Norwegian Governmental Election Software Formally Verified with KeY'
date: '2020-10-06T13:29:02+01:00'
author: 'Dominic Steinhöfel'
excerpt: 'In his recently finished Master''s thesis, Henrik Torland Klev verified (parts of) EVA, the main support system for elections in municipalities and counties in Norway, using the KeY prover.'
layout: revision
guid: 'https://www.key-project.org/2020/10/06/2606-revision-v1/'
permalink: '/?p=2613'
---

In his [recently finished Master’s thesis](https://www.duo.uio.no/handle/10852/79576?show=full), Henrik Torland Klev verified (parts of) EVA, the *main support system for elections in municipalities and counties in Norway*, using the KeY prover.

The EVA system records the basic data needed to conduct elections in Norway, including the parties' list proposals and the electoral figure. Election results are reported to EVA by municipalities and constituencies. Giving the importance of the system for Norwegian elections, increasing the trust in it by means of formal verification is an endeavor whose importance cannot be overestimated. The primary verification target in the scope of this thesis is a central algorithm implemented in the system, *Sainte-Laguë's modified method*.

Specifying EVA components in JML required writing non-trivial contracts and auxiliary specifications, in particular complicated loop invariants. Occasionally, the EVA implementation had to be adapted to a version more suitable for formal verification with KeY<sup>1</sup>.

As a result of the thesis, "most central methods" of EVA were proved to conform to their specifications. Some methods methods could not be proved within this case study due to their complexity. In addition, Klev reports some problems he had with KeY.

The KeY team very much appreciates the work of Henrik Torland Klev and is grateful for the feedback. We encourage all users of KeY, both those who use the platform as a library and those using it as a verification tool in case studies, to reach out to us in case of problems like those mentioned above; please use [our support channels](https://www.key-project.org/getting-started/) to that end. Furthermore, we are always happy to [be contacted](https://www.key-project.org/about/contact/) and informed about new projects realized using KeY.

- - - - - -

<sup>1)</sup> This is not always the case, also for real-world case studies: For the [verification of TimSort](http://www.envisage-project.eu/proving-android-java-and-python-sorting-algorithm-is-broken-and-how-to-fix-it/) and [Dual Pivot QuickSort](https://www.key-project.org/2017/08/17/dual-pivot/), the original implementation was verified.