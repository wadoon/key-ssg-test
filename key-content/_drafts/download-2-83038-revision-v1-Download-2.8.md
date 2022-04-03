---
id: 3062
title: Download-2.8
date: '2021-12-23T22:22:31+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'https://www.key-project.org/?p=3062'
permalink: '/?p=3062'
---

<div class="wp-block-advgb-summary alignnone"><div class="advgb-toc-header collapsed">Contents</div>- [KeY 2](#advgb-toc-53a71a5e-ad5c-4cb6-ba7e-d149a1a5b8d3)
- [Previous KeY versions](#we-still-provide-some-older-versions-of-key-5ebb794b-b4fc-4195-85ff-c51c01acd4c3)
- [Download or Start](#advgb-toc-4b899c46-5d4b-4876-a97f-892bee6a55c3)
- [Supported Java and JML Features](#advgb-toc-888cc9fd-499d-4cb2-a147-165cdc609375)
- [New Features in 2.8](#advgb-toc-7b8e64cc-1d88-47b4-9c24-fd8593910875)
- [KeY-Based Eclipse Projects](#advgb-toc-ee33c5ea-a453-489f-b5da-0698a263ffe9)
- [Unstable Development Versions (Nightly Builds)](#advgb-toc-2ed2d934-6196-427f-80ec-05e9162e6ccb)
- [Maven Repository](#maven-repository-3e16d08d-fcc9-4483-be77-e8837e2b3166)
- [Example Project](#use-with-maven-6979c951-6c0b-4ee7-8efe-5e51857090d0)
- [Use with Maven](#use-with-maven-6979c951-6c0b-4ee7-8efe-5e51857090d0)
- [Use with Gradle](#use-with-gradle-ce7559f3-183b-4a2a-90ac-ab493e157e96)
- [Using the Public Repository](#use-with-gradle-ce7559f3-183b-4a2a-90ac-ab493e157e96)
- [Known Problems &amp; Workarounds](#problems-using-key)
- [Strings “don’t work” in projects with auto-generated stubs](#advgb-toc-179b2df8-56dd-4e0f-85db-095931ddf746)
- [Other Problems](#advgb-toc-37818112-01ea-425d-a398-b35b79e7908a)

</div>## KeY 2

**KeY 2.8** is the latest stable release and has been published on December 18th, 2020. It comes with an overhauled user interface and many new features.

In case of questions about KeY please contact: <support@key-project.org>.

### Previous KeY versions

We provide still some previous versions:   
The versions [KeY 2.6.x](http://www.key-project.org/download-26/) accompany the second [KeY Book](https://www.key-project.org/thebook2/). You can find the KeY 2.6.x versions [here](https://www.key-project.org/download-26). The last KeY 1.6 release is [KeY 1.6.5](https://www.key-project.org/download/key16.html) (released on April 18, 2013) and only provided for legacy reasons. KeY Hoare has its own dedicated download page.

### Download or Start

KeY requires Java version 8 or newer and is tested on Linux, OS X and Microsoft Windows.

- Single Click Jar: [KeY-2.8.0.jar](https://www.key-project.org/dist/2.8.0/key-2.8.0-exe.jar) (officially supported install version)
    - Download and start via `java -jar key-2.8.0-exe.jar`  
         or via a simple double click on the jar file
- Binary Version: [KeY-2.8.0.zip](https://www.key-project.org/dist/2.8.0/key-2.8.0.zip)
- Source Code: [KeY-2.8.0-src.zip](https://www.key-project.org/dist/2.8.0/key-2.8.0-src.zip)

### Supported Java and JML Features

- [Supported Java features](https://www.key-project.org/applications/program-verification/)
- [Supported JML features](https://www.key-project.org/jml-support-in-key/)

### New Features in 2.8

- Support for bounded sums
- Innovative and improved treatment of loops via loop contracts and a new loop invariant rule based on loop scopes
- Proof bundles: Saving proofs incl. resources into one zip file
- Source code view with highlight for symbolically executed statements
- Origin Labels: Track the origin of the formulas (e.g. if they stem from a precondition, postcondition or loop invariant)
- Heatmaps (know which formulas have been modified recently)
- Interaction Logging
- Flexible and configurable layout, Improved search, proof exploration, etc.
- New proof script command
- Full [changelog](https://www.key-project.org/wp-content/uploads/2020/12/changelog-KeY-2.8.0.txt)

## KeY-Based Eclipse Projects

**The Eclipse based projects are not yet updated to KeY 2.8.0. The linked versions are still based on KeY 2.6.3.**

Detailed information about the provided Eclipse extensions can be found [here](https://www.key-project.org/eclipse/). To install KeY 2.6.3 for [Eclipse 4.7 Oxygen](http://www.eclipse.org/oxygen) (other 4.x versions (Luna/Mars/Neon) should work as well).

| **Update Site Name:** | KeY Eclipse Extensions |
|---|---|
| **Update Site URL:** | <https://formal.iti.kit.edu/key/download/releases/2.6/eclipse/> |

## Unstable Development Versions (Nightly Builds)

You can download a current snapshot of the KeY development version below.

<figure class="wp-block-table wp-block-advgb-table advgb-table-frontend">| [ <span aria-hidden="true" class="glyphicon glyphicon-download-alt"> FatJar Distribution </span>](https://www.key-project.org/nightly/dist/latest.php) | Just download and start via `java -jar key*-exe.jar`. |
|---|---|
| [ <span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> Source and Binary Artefacts ](https://www.key-project.org/nightly/) | The classical KeY distribution containing a single jar file with all components, sources and JavaDoc files. |

</figure>## Maven Repository

If you intend to use KeY as a (Java) library and want to access its API, you can include KeY as a dependency in Maven, gradle, sbt (or similar managers). We provide a Maven repository that contains the artifcats for the KeY packages mentioned below. The repository contains the current official release and is irregularly updated with the stable nightly-build version.

The Maven repository is hosted at our [Gitlab instance](https://git.key-project.org/key-public/key/-/packages). For using KeY you should include [key.core](https://git.key-project.org/key-public/key/-/packages/76) or [key.ui](https://git.key-project.org/key-public/key/-/packages/77) into your build script.

| URL | https://git.key-project.org/api/v4/projects/35/packages/maven |
|---|---|
| Group Id | org.key\_project |
| Artifacts Id | key.core   key.ui |
| Version: | 2.8.0 *(current release)*   2.6.3 *(old release)*   2.9.0-SNAPSHOT *(weekly-published nightly build)* |

Other artifacts are also exported, and are included transitively if required.

#### Example Project

You can find an example project on how to use KeY with Gradle here: <https://github.com/KeYProject/key-java-example>

#### Use with Maven

```
<pre class="gl-font-monospace" data-testid="multiline-instruction"><repositories>
  <repository>
    <id>gitlab-maven</id>
    <url>https://git.key-project.org/api/v4/projects/35/packages/maven</url>
  </repository>
</repositories>
```

#### Use with Gradle

```
<pre class="wp-block-preformatted">repositories { 
  maven { 
    url  "https://git.key-project.org/api/v4/projects/35/packages/maven"    
  }
}
```

#### Using the Public Repository

Beside of the zipped distribution you have access to a mirror of the internal Git repository. The mirror contains the stable (tested and validated master) and release branches of KeY. You can find the repository here:

<https://git.key-project.org/key-public/key/>

Using the public repository is the best choice, if you use (a) gradle for building your project and (b) you plan to make changes to KeY. Then you should add KeY as a submodule to your project:

```
$ git submodule add https://git.key-project.org/key-public/key.git
```

And add to your settings.gradle:

```
includeBuild 'key/key'
```

## Known Problems &amp; Workarounds

### Strings “don’t work” in projects with auto-generated stubs

| **Problem description** | **Reason** | **Workaround** |
|---|---|---|
| When using the (otherwise very practical!) feature of the KeY eclipse plugin which automatically generates stubs (empty methods with default specifications) for included library methods, it might happen that **symbolic execution of Java programs gets stuck** at a place like `str = "foo";`, where `str` is a variable of type String. | Normally, String assignments just work, since this behavior is defined in some files shipped with KeY (JavaRedux). However, **when generating stubs** (that are included via the “bootclasspath” option), the **default behavior is overidden** by the dummy behavior, resulting in certain elementary things not working. | The workaround is to **replace the content of the file “String.java”** in the folder “**stubs/java/lang/**” with the content of the “**[String.java](https://www.key-project.org/wp-content/uploads/2018/01/String.java)**” originally shipped with KeY, and to furthermore **add a file “[String.key](https://www.key-project.org/wp-content/uploads/2018/01/String.key)“** in the same directory (*click on the links to download current versions of those files as of 2018/01/25*). Now, String assignments should work again. |

### Other Problems

If you encounter problems not described here, please have a look into [our “Getting Help” section](https://www.key-project.org/getting-started/).