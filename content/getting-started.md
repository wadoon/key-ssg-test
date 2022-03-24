---
id: 1535
title: 'Getting Started'
date: '2017-10-09T13:30:38+01:00'
author: 'Dominic Steinhöfel'
layout: page
guid: 'https://www.key-project.org/?page_id=1535'
ampforwp_custom_content_editor:
    - ''
ampforwp_custom_content_editor_checkbox:
    - null
ampforwp_custom_sidebar_select:
    - none
ampforwp-amp-on-off:
    - default
---

<style type="text/css">
    .circle {<br />
        border-radius: 50%;<br />
        background: #3cc47c;<br />
        height: 47px;<br />
        width: 47px;<br />
        font-size: 20px;<br />
        padding-top: 6px;<br />
        padding-left: 1px;<br />
        font-weight: 700;<br />
        text-align: center;<br />
        vertical-align: middle;<br />
        color: white;<br />
    }
<p>	a.download-button {<br />
		background-color: orange;<br />
		border-color: orange;<br />
		color: white;<br />
		padding: 8px 27px;<br />
	}
<p>	@media screen and (min-width: 980px) /* Desktop */ {<br />
		.circle {<br />
			margin-left: auto;<br />
			margin-right: auto;<br />
			margin-top: -24px;<br />
		}
<p>		.dots {<br />
			border-top: 1px dotted #3cc47c;<br />
			margin-top: 24px;<br />
		}<br />
	}
<p>	@media screen and (max-width: 979px) /* Tablet */ {<br />
		.circle {<br />
			float: left;<br />
		}
<p>		h3 {<br />
			line-height: 39px;<br />
			margin-left: 55px;<br />
		}
<p>		.dots p {<br />
			clear: both;<br />
		}<br />
	}<br />
</style></head><body><div class="row dots"><div class="col-md-3"><div class="circle">1</div>### Download KeY

- Download [KeY 2.10](https://www.key-project.org/dist/2.10.0/key-2.10.0-exe.jar) as single click jar and double click the jar file <small>(or use `java -jar key-2.8.0-exe.jar` on the command line)</small>
- Alternatively, download one of the
- [KeY 2.10.0 stable binaries](https://www.key-project.org/dist/2.10.0/key-2.10.0.zip) or
- [development versions](https://www.key-project.org/nightly/)


</div><div class="col-md-3"><div class="circle">2</div>### Tutorials &amp; Examples

Load an example from the list presented in the dialog that pops up when starting KeY. Good choices are, e.g.: - “Quicktour” for program verification
- “Transitivity of Subset” for first-order logic
- “Declassification – Sum” for information flow analysis

Have a look at our [tutorials section](/applications/program-verification/#Tutorials) for program verification. A good starting point is the [tutorial on formal verification with KeY](https://link.springer.com/chapter/10.1007/978-3-319-49812-6_16) in the [KeY book.](/thebook2/) The [examples from the book](/thebook2/examples-from-the-book/) are available [here](/thebook2/examples-from-the-book/). </div><div class="col-md-3"><div class="circle">3</div>### KeY as a Library

You can use KeY as a library in your own project: Make use of its capabilities as a first-order prover or symbolic execution engine. We provide some starting points for you in the [“KeY for Your Own Research Projects” section](https://www.key-project.org/applications/key-for-your-own-research-projects/). [Download the KeY nightly source code distribution here](http://i12www.ira.uka.de/~key/download/nightly/) and have a look at our [Javadoc documentation](http://i12www.ira.uka.de/~key/download/nightly/api/) if you want to extend KeY or understand how things work under the hood. </div><div class="col-md-3"><div class="circle">4</div>### Getting Help

The preferred way for getting help, in particular when you want to use KeY as a library or want to change or extend the source code, is to use [StackOverflow](https://stackoverflow.com/questions/tagged/key-formal-verification). Be sure to tag your question with the <kbd>key-formal-verification</kbd> tag, so that your question is not lost amongst all the questions on StackOverflow. Alternatively, you can write an email to our mailing list <span id="ede197f99a149cd1fa2e1adb23c261f6"></span><script type="text/javascript">
                    var t=[51,9,88,-56,160,-46,147,-45,106,-72,181,-84,189,-81,197,-86,144,-106,141,-92,141,-88,147,-109,144,-95,144,-89,148,-110,145,-96,145,-95,154,-116,151,-102,151,-101,160,-122,157,-108,157,-108,167,-129,164,-115,164,-112,171,-133,168,-119,168,-114,173,-135,170,-116,168,-109,147,-112,161,-113,168,-109,147,-112,161,-113,162,-103,141,-106,155,-105,154,-95,133,-98,150,-97,156,-118,153,-104,153,-103,162,-124,159,-110,159,-107,166,-128,163,-114,163,-114,173,-135,170,-121,169,-115,174,-136,171,-122,170,-121,180,-142,177,-120,177,-118,156,-121,170,-121,175,-116,154,-119,171,-117,176,-138,173,-124,173,-124,183,-145,180,-131,180,-128,187,-149,184,-135,183,-132,191,-157,219,-104,221,-109,221,-110,224,-108,172,-65,166,-45,90,22,92,19,87,14,85,31,15,96,18,85,-25,72,25,37];
                    var toAppend = '';
                    for (var i=1; i<t.length; i++)
                    {
                    	toAppend+=String.fromCharCode(t[i]+t[i-1]);
                    }
                    document.getElementById('ede197f99a149cd1fa2e1adb23c261f6').innerHTML = toAppend;
                </script><noscript>Please enable JavaScript to see this field.</noscript>. </div></div>