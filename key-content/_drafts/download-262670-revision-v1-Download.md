---
id: 2675
title: Download
date: '2020-12-18T15:03:44+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'https://www.key-project.org/2020/12/18/2670-revision-v1/'
permalink: '/?p=2675'
---

<div class="wp-block-advgb-summary alignnone"><div class="advgb-toc-header collapsed">Contents</div>- [KeY 2](#advgb-toc-53a71a5e-ad5c-4cb6-ba7e-d149a1a5b8d3)
- [Download or Start](#advgb-toc-4b899c46-5d4b-4876-a97f-892bee6a55c3)
- [Supported Java and JML Features](#advgb-toc-888cc9fd-499d-4cb2-a147-165cdc609375)
- [New Features in 2.x](#advgb-toc-7b8e64cc-1d88-47b4-9c24-fd8593910875)
- [KeY-Based Eclipse Projects](#advgb-toc-ee33c5ea-a453-489f-b5da-0698a263ffe9)
- [Unstable Development Versions (Nightly Builds)](#advgb-toc-2ed2d934-6196-427f-80ec-05e9162e6ccb)
- [Maven Repository](#maven-repository-3e16d08d-fcc9-4483-be77-e8837e2b3166)
- [Use with Maven](#use-with-maven-6979c951-6c0b-4ee7-8efe-5e51857090d0)
- [Use with Gradle](#use-with-gradle-ce7559f3-183b-4a2a-90ac-ab493e157e96)
- [Webstart Problems](#webstart)
- [Adding our website to the exception list](#advgb-toc-bc7847f7-d75c-467c-bad3-6cc4703ee965)
- [Import the KeY certificate](#advgb-toc-e53a3ca0-5469-4a6e-9ca9-eefd83dcb6cd)
- [Known Problems &amp; Workarounds](#problems-using-key)
- [Strings “don’t work” in projects with auto-generated stubs](#advgb-toc-179b2df8-56dd-4e0f-85db-095931ddf746)
- [Other Problems](#advgb-toc-37818112-01ea-425d-a398-b35b79e7908a)

</div>## KeY 2

KeY 2.6.3 is the latest stable release. The versions KeY 2.6.x accompany the second [KeY Book](https://www.key-project.org/thebook/). For major new features (like state merging etc.), please checkout the nightly build. KeY 2 differs significantly from the previous [KeY 1.6](https://www.key-project.org/download/key16.html) release. The last KeY 1.6 release is [KeY 1.6.5](https://www.key-project.org/download/key16.html) (released on April 18, 2013) and only provided for legacy reasons. KeY Hoare has its own dedicated download page. In case of questions about KeY please contact: <support@key-project.org>.

<div style="margin: 0 auto; width: 261px">[<span aria-hidden="true" class="glyphicon glyphicon-play"></span> Run KeY 2.6 via Webstart](http://formal.iti.kit.edu/key/download/releases/2.6/webstart/KeY.jnlp)</div>### Download or Start

KeY requires Java version 8 or newer and is tested on Linux, OS X and Microsoft Windows.

- Instant Start: [Web Start](https://formal.iti.kit.edu/key/releases/2.6/webstart/KeY.jnlp)
- Binary Version: [KeY-2.6.3.zip](https://formal.iti.kit.edu/key/releases/2.6.3/key-2.6.3_7d3deab0763c88edee4f7a08e604661e0dbdd450.zip)
- Source Code: [KeY-2.6.3-src.tgz](https://formal.iti.kit.edu/key/releases/2.6.3/key-src-2.6.3_7d3deab0763c88edee4f7a08e604661e0dbdd450.zip)

### Supported Java and JML Features

- [Supported Java features](https://www.key-project.org/applications/program-verification/)
- [Supported JML features](https://www.key-project.org/jml-support-in-key/)

### New Features in 2.x

- Explicit Heap Model and Dynamic Frames
- Verification of Recursive Methods
- Further Enhancend JML Support ([Details](https://www.key-project.org/jml-support-in-key/))
- Simplified representation of integers
- GUI improvements (refreshed appearance, improved search, keyboard shortcuts)
- Counter Example Generation &amp; Test Generation
- Calculus for Information Flow Reasoning
- Full support for shift-operations and partially for other binary operators
- Various bugfixes

## KeY-Based Eclipse Projects

Detailed information about the provided Eclipse extensions can be found [here](https://www.key-project.org/eclipse/). To install KeY 2.6.3 for [Eclipse 4.7 Oxygen](http://www.eclipse.org/oxygen) (other 4.x versions (Luna/Mars/Neon) should work as well).

| **Update Site Name:** | KeY Eclipse Extensions |
|---|---|
| **Update Site URL:** | <https://formal.iti.kit.edu/key/download/releases/2.6/eclipse/> |

## Unstable Development Versions (Nightly Builds)

You can download a current snapshot of the KeY development version below.

<figure class="wp-block-table wp-block-advgb-table advgb-table-frontend">| [ <span aria-hidden="true" class="glyphicon glyphicon-download"></span> FatJar Distribution ](https://formal.iti.kit.edu/key/download/nightly/dist/latest.php) | Just download and start via `java -jar key*-exe.jar`. |
|---|---|
| [ <span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span> Source and Binary Artefacts ](https://www.key-project.org/nightly/) | The classical KeY distribution containing a single jar file with all components, sources and JavaDoc files. |

</figure>## Maven Repository

We provide a Maven repository via Bintray. The repository is irregularly updated with our current stable version.

| URL | <https://dl.bintray.com/key/stable-snapshots/> |
|---|---|
| Group Id | org.key\_project |
| Artifacts Id | key.core.example   key.core.proof\_references   key.core.symbolic\_execution.example   key.core.symbolic\_execution   key.core.testgen   key.core   key.removegenerics   key.ui   key.util   keyext.interactionlog   rifl |
| Version: | 2.7.0.YYYYMMDD |

You also need recoder:

```
<pre class="wp-block-preformatted" id="block-029c3021-982d-4981-ae3d-2248871928fb">key-project:recoderKey:1.0
```

#### Use with Maven

```
<pre class="wp-block-preformatted"><repository><br></br>   <snapshots><enabled>false</enabled></snapshots><br></br>   <id>bintray-key-stable-snapshots</id><br></br>   <name>bintray</name><br></br>   <url>https://dl.bintray.com/key/stable-snapshots</url><br></br></repository>
 
```

#### Use with Gradle

```
<pre class="wp-block-preformatted">repositories {     
  maven {        
    url  "https://dl.bintray.com/key/stable-snapshots"    
  } 
}         
```

## Webstart Problems

If you get an error dialog stating that the execution of the application was blocked due to your Java security settings, you have three options. You can either

- download and run the binary versions using the links provided above,
- add the website `http://i12www.ira.uka.de/` to the exception list of your Java installation, or
- import our certificate with which the Jar was signed.

### Adding our website to the exception list

First, you have to start the *Java Control Panel*. This can be accomplished via running `javaws -viewer` in a terminal. Two windows should open: The “Java Cache Viewer” (close this window) and the Java Control Panel. Clickon the “Security” tab in the control panel and choose to edit the site list; then, click on “Add” and enter the URL `http://i12www.ira.uka.de/`.

### Import the KeY certificate

[Download the file “KEY.cer”](https://www.key-project.org/KEY.cer) which contains our certificate. Open the Java Control Panel via running `javaws -viewer` and close the cache viewer. Click on the “Security” tab and choose to manage certificates.Then, click on “import”, change the file filter to “All Files”, navigate to the directory where you stored the KEY.cer file, choose it and press OK.

If the two solutions outlined above should fail for you, please resort to downloading and using the compiled binary version.

## Known Problems &amp; Workarounds

### Strings “don’t work” in projects with auto-generated stubs

| **Problem description** | **Reason** | **Workaround** |
|---|---|---|
| When using the (otherwise very practical!) feature of the KeY eclipse plugin which automatically generates stubs (empty methods with default specifications) for included library methods, it might happen that **symbolic execution of Java programs gets stuck** at a place like `str = "foo";`, where `str` is a variable of type String. | Normally, String assignments just work, since this behavior is defined in some files shipped with KeY (JavaRedux). However, **when generating stubs** (that are included via the “bootclasspath” option), the **default behavior is overidden** by the dummy behavior, resulting in certain elementary things not working. | The workaround is to **replace the content of the file “String.java”** in the folder “**stubs/java/lang/**” with the content of the “**[String.java](https://www.key-project.org/wp-content/uploads/2018/01/String.java)**” originally shipped with KeY, and to furthermore **add a file “[String.key](https://www.key-project.org/wp-content/uploads/2018/01/String.key)“** in the same directory (*click on the links to download current versions of those files as of 2018/01/25*). Now, String assignments should work again. |

### Other Problems

If you encounter problems not described here, please have a look into [our “Getting Help” section](https://www.key-project.org/getting-started/).