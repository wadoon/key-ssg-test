---
id: 2107
title: 'Report about the 1st International HacKeYthon 2018'
date: '2018-12-17T11:39:52+01:00'
author: 'Dominic Steinhöfel'
excerpt: 'Two weeks ago, at the 6th and 7th of December, 2018, the 1st International HacKeYthon took place in the rooms of the KIT in Karlsruhe, Germany. In five groups consisting of 3 to 4 participants each we worked on small projects contributing to the overall good of the KeY system. The event was a great success: Many concrete results will soon be merged with our master branch. There will be more HacKeYthons in the future!'
layout: post
guid: 'https://www.key-project.org/?p=2107'
permalink: /2018/12/17/report-about-the-1st-international-hackeython-2018/
image: /wp-content/uploads/2018/10/hackeython-logo.png
categories:
    - Uncategorized
---

<div class="wp-block-advgb-summary alignnone"><div class="advgb-toc-header collapsed">Table of Contents</div>- [Results of the Subprojects](#advgb-toc-c0101fe0-b5c4-4e28-b0ac-0d86da3d773d)
- [Interaction logging](#advgb-toc-50a4d3c9-54d8-4b0c-a06e-f2f765308b7c)
- [Proof Management](#advgb-toc-cf64b3ea-8c44-4e31-a45f-b13999337446)
- [GUI Dialog Streamlining and Extensions for Easier Accessibility](#advgb-toc-7e00adf6-821c-4a1d-a4ed-85f3ed1d528e)
- [Parallelization: Simultaneous Proving of Distinct Branches](#advgb-toc-1a6ac678-316b-4a27-b20f-91fea5a97274)
- [Algebraic Data Types for KeY](#advgb-toc-c6afec49-6681-4f2a-8461-1563e72afbf2)
- [Students Award and Social Aspects](#advgb-toc-cb35ec8d-5eb1-4057-b230-b38780a46842)
- [The First HacKeYthon Will Not Be the Last](#advgb-toc-b111eb40-c5b7-4ae6-ac8f-7d844cbd3985)

</div>Two weeks ago, at the 6th and 7th of December, 2018, the [1st International HacKeYthon](https://www.key-project.org/1st-hackeython-2018/) took place in the rooms of the KIT in Karlsruhe, Germany. In five groups consisting of 3 to 4 participants each we worked on small projects contributing to the overall good of the KeY system. The projects were addressing properties such as usability and performance of the system which are frequently ignored or postponed since their direct value for research is limited.

The result of this experiment was a great success: Participants have been working intensely with the system and had fun doing so. Newer project members, among them many students, reported having learned a lot about the internal workings of KeY. And most importantly, there are concrete results that can be observed, lots of them currently in the process of being made ready to be merged with the master branch of KeY. The only major point of criticism was the lack of time. We decided that there will be more HacKeYthons in the future, which will then last for 2,5 instead of less than two days, such that there will be longer time periods in which participants can work on their projects without distraction.

## Results of the Subprojects

Here is a brief overview of the results that have been achieved in the individual HacKeYthon groups. Each group additionally has been working on an outlook for future extensions. The group speakers are responsible to ensure a sustainable development of their topic, such that the results can be presented to the user community soon.

### Interaction logging

- Proof interactions are logged into a named log file: Manual rule applications, changes to the settings, calls to strategies / macros.
- Possibility to save own notes.
- Log entries can be added to list of favorites.

### Proof Management

- Command line tool for checking cyclic proof dependencies has been developed.
- All files belonging to a project are saved in one bundle.
- Files in a bundle are checked for consistent proof settings.

### GUI Dialog Streamlining and Extensions for Easier Accessibility

- A set of novelties concerning the KeY GUI has been developed.
- Improvements in the taclet instantiation editor: Easier interaction possibilities with text boxes, pretty printing.
- Extension of the "show all active settings" dialog for better overview and as a basis for a future possibility of changing settings.
- Addition of a mechanism for refreshing selected proofs.

### Parallelization: Simultaneous Proving of Distinct Branches

- Already before the HacKeYthon, many performance bottlenecks have been tracked down and resolved to prepare for the topic, which led to large speedups.
- Dramatic improvement of prover speed for synthetic examples.
- Noticeable speed increase for average examples, ideas for further improvements have been sketched.
- Parallelization of proof branches as well as strategy evaluations envisioned and begun.

### Algebraic Data Types for KeY

- Development of ADT syntax, communication of it to leading members of the JML community.
- Extension of the KeY parsers for .key files for the new syntax.
- Development of data structures for ADTs, incl. some checks (rejection of syntactically corret, but semantically meaningless definitions).
- Ideas for generation of KeY logic symbols of ADTs have been developed.

## Students Award and Social Aspects

On the first evening, we had a very nice social dinner at the local brewery "Vogelbräu" (picture below). Events like this contribute very much to integrating the locally distributed team of KeY developers of all experience levels.

<div class="wp-block-advgb-image advgb-image-block" data-image="https://www.key-project.org/wp-content/uploads/2018/12/group-picture.jpg" style="background-image:url( https://www.key-project.org/wp-content/uploads/2018/12/group-picture.jpg);height:500px;width:500px;justify-content:flex-start;align-items:center"><a class="advgb-image-overlay" style="background-color:#313131" target="_blank"></a>
</div>The decision about whom to grant the student award for outstanding contributions to the HacKeYthon was a very hard one, since all participating students have been working and contributing fantastically. At the end, Wolfram Pfeifer, the group speaker of the Proof Management group, got the certificate as the only student leading a team. Still, all the other students received a cinema voucher to honor their contributions. We are really happy about the big number of motivated KIT students who helped a lot in making this event a success!

## The First HacKeYthon Will Not Be the Last  


The first HacKeYthon, even in its limited time frame, gave rise to so many smaller and bigger innovations to KeY that it might be called incomparable to anything else in the long history of the project. Therefore, the first HacKeYthon will not be the last one. We will try to establish this type of event as a reoccurring one, maybe even biannually, who knows! Thanks to all our motivated and skillful participants who joined this experiment and contributed to its success!