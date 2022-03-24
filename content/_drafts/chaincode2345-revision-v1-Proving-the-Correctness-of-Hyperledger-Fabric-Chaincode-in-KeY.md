---
id: 2357
title: 'Proving the Correctness of Hyperledger Fabric Chaincode in KeY'
date: '2019-11-12T09:58:44+01:00'
author: 'Jonas Schiffl'
layout: revision
guid: 'https://www.key-project.org/2019/11/12/2345-revision-v1/'
permalink: '/?p=2357'
---

Smart contracts are programs that run on distributed ledger platforms, and they usually manage resources representing valuable assets. Moreover, their source code is visible to potential attackers, they are distributed, and bugs are hard to fix. Thus, they are susceptible to attacks exploiting programming errors. Their vulnerability makes a rigorous formal analysis of the functional correctness of smart contracts highly desirable.

This is where KeY comes into play. In a recent [case study](https://formal.iti.kit.edu/biblio/?lang=en&key=BeckertHerdaKirstenEA2018), we extended KeY to reason about the correctness of [Hyperledger Fabric](https://www.hyperledger.org/projects/fabric) smart contracts.

To do that, we modeled the distributed ledger as a sequence of assignments. The API methods of Hyperledger Fabric were annotated accordingly.

Furthermore, we had to deal with serialization and persistent storage of data. To be able to reason about this in KeY, we automatically create an abstract KeY data type for each type of object that gets stored on the ledger, so that we can express reading from and writing to the ledger as equivalent operations on a sequence of the corresponding abstract data types.

## Paper

In a recent workshop paper, we discuss our notion of smart contract verification. We propose an abstraction of smart contract platforms that yields itself usefully to deductive program verification, and we discuss different types of correctness properties of smart contracts, and how to verify them.

[Preprint](https://www.key-project.org/wp-content/uploads/2019/11/sc-verification.pdf)

The paper has been published in LNCS, available at springerlink.

## Sources and Proof Files

#### Extended KeY version

[key-2.7\_2d2a68348e607ba00900a9ecfaee13afec14c614-exe.jar](https://www.key-project.org/wp-content/uploads/2019/11/key-2.7_2d2a68348e607ba00900a9ecfaee13afec14c614-exe.jar)

#### Java Source Files

[Java source files](https://www.key-project.org/wp-content/uploads/2019/11/java-sources.zip)

#### Proofs

[createPlayer.proof](https://www.key-project.org/wp-content/uploads/2019/11/createPlayer.proof)  
[evaluate.proof](https://www.key-project.org/wp-content/uploads/2019/11/evaluate.proof)