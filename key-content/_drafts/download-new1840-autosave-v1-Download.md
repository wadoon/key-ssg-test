---
id: 1844
title: Download
date: '2018-09-30T22:32:29+01:00'
author: weigl
layout: revision
guid: 'https://www.key-project.org/2018/09/30/1840-autosave-v1/'
permalink: '/?p=1844'
---

<div class="row"><div class="col-md-9 col-md-pull-3">## KeY 2

<div class="row"><div class="col-md-8">KeY 2.6.3 is the latest stable release, released on October 11th, 2017.  
The versions KeY 2.6.x accompany the second [KeY Book](https://www.key-project.org/thebook/).

For major new features (like state merging etc.), please checkout the nightly build.

KeY 2 differs significantly from the previous [KeY 1.6](http://www.key-project.org/download/key16.html) release.  
The last KeY 1.6 release is [KeY 1.6.5](http://www.key-project.org/download/key16.html) (released  
on April 18, 2013) and only provided for legacy reasons.

KeY Hoare has its own dedicated download page.

In case of questions about KeY please contact: <support@key-project.org>.

### Download or Start

KeY requires Java version 7 or newer and is tested on Linux, OS X and Microsoft Windows.

- Instant Start: [Web Start](https://formal.iti.kit.edu/key/releases/2.6/webstart/KeY.jnlp)
- Binary Version: [KeY-2.6.3.zip](https://formal.iti.kit.edu/key/releases/2.6.3/key-2.6.3_7d3deab0763c88edee4f7a08e604661e0dbdd450.zip)
- Source Code: [KeY-2.6.3-src.tgz](https://formal.iti.kit.edu/key/releases/2.6.3/key-src-2.6.3_7d3deab0763c88edee4f7a08e604661e0dbdd450.zip)


</div><div class="col-md-4">[<span aria-hidden="true" class="glyphicon glyphicon-play"></span> Run KeY 2.6 via Webstart](http://formal.iti.kit.edu/key/download/releases/2.6/webstart/KeY.jnlp)</div></div>### Supported Java and JML Features

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

Detailed information about the provided Eclipse extensions can be found [here](/eclipse/).  
To install KeY 2.6.3 for [Eclipse 4.7 Oxygen](http://www.eclipse.org/oxygen) (other 4.x versions (Luna/Mars/Neon) should work  
as well)

<div class="table-responsive">| Update Site Name: | KeY Eclipse Extensions |
|---|---|
| Update Site URL: | <https://formal.iti.kit.edu/key/download/releases/2.6/eclipse/> |

</div>#### Known issues

If no items are shown in the “Install” wizard, please deselect the checkbox “Group items by category”.

## Unstable Development Versions (Nightly Builds)

You can download current snapshot of the KeY development.

<div class="row"><div class="col-md-4">[  
<span aria-hidden="true" class="glyphicon glyphicon-play"></span>  
Webstart (Nighlty Build)](https://formal.iti.kit.edu/key/download/nightly/webstart/KeY.jnlp)<small>Have a look at the section [Webstart Problems](#webstart)  
if you have trouble starting KeY via Webstart</small>

</div><div class="col-md-4">[  
<span aria-hidden="true" class="glyphicon glyphicon-download"></span>  
fatJar distribution  ](https://formal.iti.kit.edu/key/download/nightly/dist/latest.php)<small>Just downdload and start with `java -jar key*-exe.jar`</small>

</div><div class="col-md-4">[  
<span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span>  
Source and binary artefacts](http://i12www.ira.uka.de/~key/download/nightly/)<small>Classical KeY distribution with single jar of components, sources and javadoc.</small>

</div></div>**Attention: The nightly builds require a JRE/JDK with JavaFX!** JavaFX is included in the Oracle JRE/JDK until Java11. In case of OpenJDK it depends on your distribution, i.e. for Ubuntu: please install openjfx via <span style="font-family: 'courier new', courier, monospace;">sudo apt-get install openjfx</span>; for Fedora install `java-1.8.0-openjdk-openjfx`.

No support is provided for development versions.

## Webstart Problems

These issues are most likely only of concern if you are using webstart for the nighlty builds.

If you get an error dialog stating that the execution of the application was blocked due to your Java security settings, you have three options.  
You can either

- download and run the binary versions using the links provided above,
- add the website `http://i12www.ira.uka.de/` to the exception list of your Java installation, or
- import our certificate with which the Jar was signed.


### Adding our website to the exception list

First, you have to start the *Java Control Panel*. This can be accomplished via running `javaws -viewer` in a terminal. Two windows should open: The “Java Cache Viewer” (close this window) and the Java Control Panel. Click  
on the “Security” tab in the control panel and choose to edit the site list; then, click on “Add” and enter the URL `http://i12www.ira.uka.de/`.

### Import the KeY certificate

[Download the file “KEY.cer”](/KEY.cer) which contains our certificate. Open the Java Control Panel via running `javaws -viewer` and close the cache viewer. Click on the “Security” tab and choose to manage certificates.  
Then, click on “import”, change the file filter to “All Files”, navigate to the directory where you stored the KEY.cer file, choose it and press OK.

If the two solutions outlined above should fail for you, please resort to downloading and using the compiled binary version.

## Known Problems &amp; Workarounds

### Strings “don’t work” in projects with auto-generated stubs

<div class="row"><div class="col-md-4">#### Problem description

When using the (otherwise very practical!) feature of the KeY eclipse plugin which automatically generates stubs (empty methods with default specifications) for included library methods, it might happen that **symbolic execution of Java programs gets stuck** at a place like `str = "foo";`, where `str` is a variable of type String.

</div><div class="col-md-4">#### Reason

Normally, String assignments just work, since this behavior is defined in some files shipped with KeY (JavaRedux). However, **when generating stubs** (that are included via the “bootclasspath” option), the **default behavior is overidden** by the dummy behavior, resulting in certain elementary things not working.

</div><div class="col-md-4">#### Workaround

The workaround is to **replace the content of the file “String.java”** in the folder “**stubs/java/lang/**” with the content of the “**[String.java](/wp-content/uploads/2018/01/String.java)**” originally shipped with KeY, and to furthermore **add a file “[String.key](/wp-content/uploads/2018/01/String.key)“** in the same directory (*click on the links to download current versions of those files as of 2018/01/25*). Now, String assignments should work again.

</div></div>### Other Problems

If you encounter problems not described here, please have a look into [our “Getting Help” section](/getting-started/).

</div></div>