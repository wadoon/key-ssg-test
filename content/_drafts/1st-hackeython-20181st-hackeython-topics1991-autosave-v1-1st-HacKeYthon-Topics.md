---
id: 2001
title: '1st HacKeYthon Topics'
date: '2018-11-09T19:38:17+01:00'
author: 'Michael Kirsten'
layout: revision
guid: 'https://www.key-project.org/2018/11/09/1991-autosave-v1/'
permalink: '/?p=2001'
---

During the [first HacKeYthon](https://www.key-project.org/1st-hackeython-2018/), we will together approach the following list of topics, each of which will be assigned a team of 3 to 5 participants, one of which will be the group speaker.

<div class="wp-block-columns has-2-columns"><div class="wp-block-column"></div><div class="wp-block-column"></div></div><div class="wp-block-advgb-summary alignnone"><div class="advgb-toc-header collapsed">Table of Contents</div>- [Interaction Logging](#advgb-toc-d89ae4cf-76a8-4c43-804f-39b0e24727a9)
- [Our Motivation](#advgb-toc-f45d1116-02eb-4212-9145-79458de2c5cf)
- [Our Goal](#advgb-toc-20c92ea4-da17-42a6-8c69-c08780057eeb)
- [Our Objectives](#advgb-toc-745dd69f-0e1c-4942-bc12-594037e7e435)
- [First Goal](#advgb-toc-a3842049-58c5-403a-a741-f0fefb19a4b5)
- [Second goal](#advgb-toc-02fbc5f8-8bad-492d-bed3-9ff365ea2be4)
- [Proof Management](#advgb-toc-f6fd4f32-028e-4863-a2e2-55e9eda6bd08)
- [GUI Dialog Streamlining and Extensions for Easier Accessibility ](#advgb-toc-5800c142-51ad-49bf-967f-54cdee94fcaf)
- [Parallelization: Simultaneous Proving of Distinct Branches](#advgb-toc-37f0ddb8-0eca-44ba-80ff-453d17d29456)
- [Abstract Data Types for KeY](#advgb-toc-5180c24e-d3f4-4bf3-a3ff-00ed94ce9d69)

</div>## Interaction Logging

**Group Speaker**: Alexander Weigl

### Our Motivation

“How long did you need for the proof?” is the most typical advisor question at the end of a thesis about proofing the correctness of software with KeY. Beside, the concrete numbers of the proof tree metrics and prover run-time, we do not have any measurements of the under taking interactions on the proof and in the tool. Although, interactions are the key aspect of KeY and proofs of complex software rely on them.

### Our Goal

Our goal is split into two areas:

- First, we will capture the interactive rule applications. This allows a simpler and smaller storage format for proves and also an export of proof-scripts (Ulbrich- or KPS-style).
    - This sub-goal tries to close a gap between KeY and PSDBG, and also makes a proof more comprehensible.
- Second, we will introduces quantitative metrics for measuring the labour and interaction complexity of the proof construction.
- How long was KeY focused?
- How often was the proof reloaded?
- Number of interactive prunes, quantifications, cuts, …?
- Time until a new branch was closed.
- …

### Our Objectives

Following working points have been identified. Note, preparations can be found in [https://git.key-project.org/key/key/merge\_requests/84](https://git.key-project.org/key/key/merge_requests/84).

#### First Goal

- Finding the crosspoints for injection of interaction recording. (Crosspoints found for macros and rules).
- View of current logged interactions.
- Saving the user interaction along the proof.
- Export into a new proof storage format and proof reconstruction.
- Export into proof scripts.

#### Second goal

- Defining a framework for UI metrics
    - flexible model classes
    - storing and loading of UI metrics
    - add actions to the UI
- Defining and Implementing the UI metrics.  
    Following list is a suggestion:
    - Focus time of KeY and the prove
    - Number of proof reloads
    - Number of proof switches
    - Number of interactive rule and macro applications by type.
    - Life span of a branch
    - Number of focus switches

## Proof Management

**Group speaker**: Wolfram Pfeifer

We aim to develop a project-based display of the total proof state of a system. This should answer the question of when a system actually can be categorized as being proven, and furthermore provide a visualization of finished and open proofs for all proof obligations associated to the system for a better overview and usability of KeY for larger systems. One key point is the checking cyclic dependencies between contracts, since this signals a soundness issue.

## GUI Dialog Streamlining and Extensions for Easier Accessibility 

**Group speaker**: Michael Kirsten

- Concerns GUI of KeY tool
- Systematic conceptual rework of (type of) availability of current settings and switches in GUI dialogues
- Possibly (better) integration of currently badly-integrated or poorly-available settings and display options in uniform GUI dialogues
- Generally (more) uniform look and feel etc.
- Generally making proof settings more robust
- Possibly (better) integration of taclet options such that no loaded proof goal is needed (which currently makes them non-available in KeY files)
- Possibly creating a small proof macro toolkit (in KeY’s GUI) using, currently only via KeY’s source code available, abstract proof macros

## Parallelization: Simultaneous Proving of Distinct Branches

**Group speaker**: Richard Bubel

As KeY is based on a sequent calculus which leads to proofs quickly branching into subtrees, it is a natural optimization to parallelize the proving of the subtrees within the system. We believe that this would signify an immense performance boost for KeY, making it possible to approach larger programs within acceptable time (well, if there’s sufficient memory). This is though a non-trivial undertaking since KeY hasn’t been built for this, which is why some refactoring will be needed to accomplish this goal. On the other hand, recent changes regarding decentralized handling of namespaces within KeY already should make it simpler to parallelize processing of individual goals. This project will enable you to deeply dive into the system and achieve a major improvement in case of success.

## Abstract Data Types for KeY

**Group speaker**: Dominic Steinhöfel

Abstract data types are an easy-to-use and concise technique for implementing and specifying programs. So far, KeY supports the definition of sorts and functions on sorts that can be used in problem statements and specifications. We aim to extend this in two ways: First, provide a nice concrete syntax for defining abstract datatypes within .key files in the flavor of Haskell, Coq etc. and integrate this well with the system, and second, also make it possible to directly specify and use them within JML (where so far, you cannot define sorts and function symbols). In this project, we’ll deal with KeY’s parsers and very basic building blocks like sorts, functions, namespaces etc. One goal is to also elaborate some nice examples where ADTs help in specifying a problem.