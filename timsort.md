---
id: 874
title: 'TimSort (Tools and Proofs of JAR submission)'
date: '2017-01-09T13:02:06+01:00'
author: 'Richard Bubel'
layout: page
guid: 'http://www.key-project.org/?page_id=874'
ampforwp-amp-on-off:
    - default
---

The file [TimSortProofs.zip](http://i12www.ira.uka.de/key/timsort/TimSortProofs.zip) contains the KeY Tool, the TimSort source file as well as the saved proofs of the TimSort case study. After unzipping you find the following directory structure

- **bin/**This directory contains the used version of the KeY Tool. You can start KeY with the command
    
    <center>`java -Xmx<memory>G -jar KeY.jar`</center>(assuming you are in the directory `bin` otherwise you need to specify the full path to the file `KeY.jar`).
    
    **Attention: You need Java 8 to run KeY.**
    
    For most of the proofs to load you need to replace `<memory>` by `2` (i.e., `java -Xmx2G KeY.jar`). The following table provides the required memory allocations:
    
    <center>| Method | Memory |  |
    |---|---|---|
    | newMergeCollapse | 4G |
    |
    | mergeHi | 8G |
    | mergeLo | 16G | (you might want to start KeY in addition with `-XX:+UseG1GC` before the memory parameter) |
    | all others | 2G |
    
    </center>
- **sorting/**This directory contains the KeY project setup incl. the source code and specification of TimSort
    - The file **src/java/util/TimSort.java** contains the TimSort implementation and its JML specification
    - The subdirectory **proof/new\_proofs/finished/** contains the proofs in zipped form. You need to unzip them manually before loading. After starting KeY you can load the unzipped proofs via the menu `File | Load `.
    - If you want to verify TimSort yourself, you need to select the file `Sort.key` in menu `File | Load`

The shell script `autoRun.sh` replays all proofs automatically (without starting KeY’s GUI) and outputs some statistics into the directory `replayResults/`