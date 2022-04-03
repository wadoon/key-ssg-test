---
id: 2052
title: 'KeY Setup Instructions'
date: '2018-11-26T10:10:20+01:00'
author: 'Dominic Steinhöfel'
layout: revision
guid: 'https://www.key-project.org/2018/11/26/2013-autosave-v1/'
permalink: '/?p=2052'
---

The instructions in this page should help you setting up the KeY development environment for the HacKeYthon. In case of any problems, please contact [Dominic Steinhöfel](https://www.key-project.org/about/people/) before the event. The goal is that every participant has a working development environment set up before the HacKeYthon.

<div class="wp-block-advgb-summary alignnone"><div class="advgb-toc-header collapsed">Table of Contents</div>- [General Instructions](#advgb-toc-2d31dc09-b701-4462-b514-32702818bda2)
- [Download Eclipse, Check Out the Git Repository, Install Plugins, Import Projects](#advgb-toc-ff070dc5-65f1-4f7d-a8d9-f685bd1938f7)
- [Linux 64 bit, Script \[recommended\]](#advgb-toc-150b674d-2f79-43b0-8b90-b0e90251fa60)
- [Manual Process](#advgb-toc-027c021a-912a-4726-a40b-6b959a2eee63)
- [Troubleshooting Compilation errors](#advgb-toc-5a4c231a-6bbe-4592-9301-df0a1dd6d351)
- [Code Convention Settings](#advgb-toc-f370bdb7-d038-40a5-b5b8-4f68266e5b56)
- [Code Formatter](#advgb-toc-ad7e32e8-0eb7-4e7b-84be-60c98e2bb39e)
- [User Name in Comments](#advgb-toc-778428ad-555b-4a94-bc54-8c87d8865518)
- [Configure Auto Save Actions](#advgb-toc-2bb36ce7-fe58-44a5-a0a7-6296ab88f762)
- [Run KeY and the Test Suite](#advgb-toc-b8fd47a3-84a5-4302-ab91-f50d1669c055)

</div>## General Instructions

1. Download the [KeY bootstrap archive](https://www.key-project.org/material/KeYBootstrap.zip). This archive contains the recommended file structure, a script for starting Eclipse with the right parameters, and a convenience script for Linux 64bit systems for performing most actions outlined in the following automatically.
2. Extract the contents of the archive to the destination where you want your shiny new KeY workspace to appear, for instance in your home directory (such that you have the folder “key-workspace” in “/home/yourusername/”).
3. Make sure you have Git installed on your system. For Windows, there is [Git for Windows](https://git-scm.com/download/win), on Debian-like systems, you can run “sudo apt-get install git” from a shell.
4. Also make sure you have access to the [KeY GitLab](https://git.key-project.org). You should furthermore have created an SSH key on your system which you registered there. Instructions are available at the [GitLab help page](https://docs.gitlab.com/ee/ssh/) (sections “Generating a new SSH key pair” and “Adding an SSH key to your GitLab account”).

## Download Eclipse, Check Out the Git Repository, Install Plugins, Import Projects  


The following subsections are mutually exclusive; please choose the one that applies to you.

### Linux 64 bit, Script \[recommended\]

1. Run the script “setup.sh” by calling “./setup.sh” from the command line in the directory to which you unzipped the archive.

### Manual Process

The following instructions should apply to all operating systems. Windows users should interpret “/” as “\\” for the directory separators.

1. Download the “Eclipse IDE for Java Developers” package which applies to your system from the [Eclipse download page](https://www.eclipse.org/downloads/packages/).
2. Extract the contents of the archive to “key-workspace/Tools/eclipse/”. Inside this directory you should find the Eclipse executable.
3. Change to the directory “key-workspace/GIT/”.
4. There, run “git clone git@git.key-project.org:key/key.git”.
5. Open eclipse via the scripts “eclipse” or “eclipse.bat” (Windows) in the directory “key-workspace/Development/KeY/eclipse”.
6. Install the following plugins via “Help &gt; Install New Software”, selecting the update site “2018-09 – http://download.eclipse.org/releases/2018-09”: 
    1. “EMF – Eclipse Modeling Framework SDK”,
    2. “OCL Classic SDK: Ecore/UML Parsers,Evaluator,Edit”,
    3. “Graphical Modeling Framework (GMF) Runtime SDK”,
    4. “GEF Common SDK”,
    5. “SWTBot for Eclipse Testing”,
    6. “SWTBot for GEF Testing”,
    7. “SWTBot for SWT Testing”,
    8. “SWTBot IDE Features”,
    9. “Graphiti (Incubation)”
7. Restart when prompted.
8. Import all KeY eclipse projects via “File &gt; Import &gt; General &gt; Existing Projects into Workspace”, selecting “key-workspace/GIT/key/” as the root directory (choose “Select All”).

## Troubleshooting Compilation errors  


Please open eclipse via the scripts “eclipse” or “eclipse.bat” (Windows) in the directory “key-workspace/Development/KeY/eclipse”. You might encounter various compilation problems that I try to address in the following.

Since you imported all projects (either automatically or manually), there will also be the project “BankJML” which shows various errors. Just remove it (without deleting it from the workspace), you won’t need it.

In the class “JDTUtil”, you could observe an error like “Access restriction: The method ‘JavaElementLabelComposerCore.appendTypeLabel(IType, long)’ is not API …”. Resolve this by navigating to the problematic file, clicking on the error and choosing the quick fix (Ctrl + 1, “Configure Problem Severity”), clicking on “Configure Project Settings”, and then setting the rule for “Forbidden reference” to “Warning”. This should solve it.

If you are reported errors like missing projects “key.util” which are though not missing, try to remove the projects from the workspace (choose to not delete them from the disk) and importing them again (from the directory “key-workspace/GIT/”). Don’t import BankJML again.

If you encounter a compilation error in the “key.core.test” package, because of the missing folder “genSrc”, resolve this by moving to the directory “key-workspace/GIT/key/key/key.core.test/” and running “ant generateproofcollectionparser”. You can also run this ant goal via the eclipse ant view (Window &gt; Show View &gt; Other &gt; Ant), then you don’t need to use the command line.

After and between those steps, try a “Project -&gt; Clean” with “Clean all projects” set. You might have to run the aforementioned ant command again. Now you hopefully don’t see any more errors…

## Code Convention Settings

Now, the time has come to apply some settings contributing to the conformance of your newly written code with the KeY coding guidelines.

### Code Formatter

Open “Window &gt; Preferences”, choose “Java &gt; Code Style &gt; Formatter”. In the dialog, choose “Import” for importing a new profile, navigate to “key-workspace/GIT/key/key/doc” and choose “KeYCodeStyle.xml”. I personally edited the style to allow for “on/off” tags in the code that are spared by auto formatting, such that commented out code or extraordinary code snippets with special formatting are not messed up. For that, choose “Edit”, “Off/on Tags”, “Enable Off/On tags”.

### User Name in Comments

In the preferences dialog, go to “Java &gt; Code Style &gt; Code Templates”, choose “Comments &gt; Types” there and edit the style by replacing the “${user}” placeholder with your real name (without German Umlauts or other special characters!).

### Configure Auto Save Actions

There are some things which can automatically be done when saving which increase the code quality a little. In the preferences window, navigate to “Java &gt; Editor &gt; Save Actions” and check “Perform the selected actions on save”. Then check “Organize imports” and “Additional actions” (don’t check “Format source code”, since it’s bad for version control when you’re editing previously existing classes), and click on “configure”. In the appearing dialog, check “Remove trailing whitespace” and “Correct indentation”. Make absolutely sure that you *don’t* check “Sort members” since it’s a nightmare for version control. Everything else should be left as-is.

Click “Apply and Close” in the preferences window.

## Run KeY and the Test Suite

Once you set up KeY, you should try to run the KeY GUI and the default test suite. For this, first open the class “de.uka.ilkd.key.core.Main” in the “key.ui” project and run it as a Java application; this should produce you the KeY GUI. After that, try out “de.uka.ilkd.key.suite.TestKey” in “key.core.test” (run as JUnit test suite).