---
id: 2468
title: 'Structured Validation of Abstract Programs'
date: '2020-04-20T08:27:04+01:00'
author: 'Dominic Steinhöfel'
layout: post
guid: 'https://www.key-project.org/?p=2468'
permalink: '/?p=2468'
categories:
    - Applications
    - 'Features of KeY'
tags:
    - 'Abstract Execution'
    - 'Abstract Programs'
    - Checklist
    - Validation
---

1. **How can the AS complete** (exception etc.), and does this have unintended effects on my surrounding program?
2. **What parts of the state can the AS change, and what may it read**? Is this choice sensible, i.e., can I imagine a sensible instance that uses at most that frame/footprint? (or exactly instead of at most, if it’s hasTo”)
3. Does the **frame/footprint also make sense** in the **case of abrupt completion** (with overapproximation semantics, i.e., parts not marked as hasTo don’t have to be assigned)? In particular, **are there too restrictive hasTos**?
4. Are **preconditions and postconditions sensible**? Also,
    1. Are **preconditions mutually exclusive**?
    2. Is the **precondition for normal\_behavior empty**? (It will anyway be ignored!)
    3. **Can postconditions be enforced** by instances, taking into consideration also the frames and footprints?