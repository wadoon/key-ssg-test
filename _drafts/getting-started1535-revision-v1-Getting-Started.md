---
id: 3102
title: 'Getting Started'
date: '2022-01-29T16:29:32+01:00'
author: 'Richard Bubel'
layout: revision
guid: 'https://www.key-project.org/?p=3102'
permalink: '/?p=3102'
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

The preferred way for getting help, in particular when you want to use KeY as a library or want to change or extend the source code, is to use [StackOverflow](https://stackoverflow.com/questions/tagged/key-formal-verification). Be sure to tag your question with the <kbd>key-formal-verification</kbd> tag, so that your question is not lost amongst all the questions on StackOverflow. Alternatively, you can write an email to our mailing list <span id="3bf6ab6ab33023099c102d3fc95bcb83"></span><script type="text/javascript">
                    var t=[78,-18,115,-83,187,-73,174,-72,133,-99,208,-111,216,-108,224,-113,171,-133,168,-119,168,-115,174,-136,171,-122,171,-116,175,-137,172,-123,172,-122,181,-143,178,-129,178,-128,187,-149,184,-135,184,-135,194,-156,191,-142,191,-139,198,-160,195,-146,195,-141,200,-162,197,-143,195,-136,174,-139,188,-140,195,-136,174,-139,188,-140,189,-130,168,-133,182,-132,181,-122,160,-125,177,-124,183,-145,180,-131,180,-130,189,-151,186,-137,186,-134,193,-155,190,-141,190,-141,200,-162,197,-148,196,-142,201,-163,198,-149,197,-148,207,-169,204,-147,204,-145,183,-148,197,-148,202,-143,181,-146,198,-144,203,-165,200,-151,200,-151,210,-172,207,-158,207,-155,214,-176,211,-162,210,-159,218,-184,246,-131,248,-136,248,-137,251,-135,199,-92,193,-72,117,-5,119,-8,114,-13,112,4,42,69,45,58,2,45,52,10];
                    var toAppend = '';
                    for (var i=1; i<t.length; i++)
                    {
                    	toAppend+=String.fromCharCode(t[i]+t[i-1]);
                    }
                    document.getElementById('3bf6ab6ab33023099c102d3fc95bcb83').innerHTML = toAppend;
                </script><noscript>Please enable JavaScript to see this field.</noscript>. </div></div>