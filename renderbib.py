import argparse

import pybtex.database as pdb

from pprint import *

def print_section_year(year):
    print(f'<h2 id="year{year}">{year}</h2>')



PERSON_LINK = {
    'Weigl, Alexander': 'https://formal.iti.kit.edu/weigl',
    "Beckert, Bernhard"              : "https://formal.iti.kit.edu//&#126;beckert/",
    "Blatter, Lionel"                : "https://formal.iti.kit.edu/&#126;blatter/",
    "Herda, Mihai"                   : "https://formal.iti.kit.edu/&#126;herda/",
    "Kirsten, Michael"               : "https://formal.iti.kit.edu/&#126;kirsten/",
    "Klamroth, Jonas"                : "https://formal.iti.kit.edu/&#126;klamroth/",
    "Lanzinger, Florian"             : "https://formal.iti.kit.edu/&#126;lanzinger/",
    "Pfeifer, Wolfram"               : "https://formal.iti.kit.edu/&#126;pfeifer/",
    "Schiffl, Jonas"                 : "https://formal.iti.kit.edu/&#126;schiffl/",
    "Ulbrich, Mattias"               : "https://formal.iti.kit.edu/&#126;ulbrich/",

    "Bormer, Thorsten"               : "https://formal.iti.kit.edu//&#126;bormer/",
    "Bruns, Daniel"                  : "https://formal.iti.kit.edu//&#126;grahl/",
    "Gladisch, Christoph"            : "https://formal.iti.kit.edu//&#126;gladisch/",
    "Gladisch, Christoph David"      : "https://formal.iti.kit.edu//&#126;gladisch/",
    "Grahl, Daniel"                  : "https://formal.iti.kit.edu//&#126;grahl/",
    "Grebing, Sarah"                 : "https://formal.iti.kit.edu//&#126;grebing/",
    "Grebing, Sarah Caecilia"        : "https://formal.iti.kit.edu//&#126;grebing/",
    "Greiner, Simon"                 : "https://formal.iti.kit.edu//&#126;greiner/",
    "Klebanov, Vladimir"             : "https://formal.iti.kit.edu/&#126;klebanov/",
    "Liu, Tianhai"                   : "https://formal.iti.kit.edu/&#126;liu/",

    "Ahrendt, Wolfgang"              : "http://www.cse.chalmers.se/&#126;ahrendt/",
    "Bubel, Richard"                 : "https://www.se.tu-darmstadt.de/se/group-members/richard-bubel/",
    "Hentschel, Martin"              : "https://www.se.tu-darmstadt.de/se/group-members/martin-hentschel/",
    r'H\"{a}hnle, Reiner'                 : "https://www.se.tu-darmstadt.de/se/group-members/reiner-haehnle/",
    "Menzel, Wolfram"                : "http://www.wolfram-menzel.de/",
    "Mostowski, Wojciech"            : "http://ceres.hh.se/mediawiki/Wojciech_Mostowski",
    "Huy Quoc Do"                   : "https://www.se.tu-darmstadt.de/se/group-members/huy-quoc-do/",
    "Rümmer, Philipp"                : "http://www.philipp.ruemmer.org/",
    "Scheben, Christoph"             : "https://lfm.iti.kit.edu/scheben.php",
    "Schmitt, Peter. H"              : "/&#126;schmitt/",
    "Weiß, Benjamin"                 : "https://lfm.iti.kit.edu/bweiss.php",

    # "Simon Bischof"                 : "https://pp.ipd.kit.edu/person.php?id=148",
    # "Matthias Budde"                : "https://www.teco.edu/people/budde/",
    # "Richard Gay"                   : "http://www.mais.informatik.tu-darmstadt.de/Richard_Gay.html",
    # "Aboubakr Achraf El Ghazi"      : "https://dbis.ipd.kit.edu/english/2284.php",
    # "Rajeev Goré"                   : "https://users.cecs.anu.edu.au/&#126;rpg/",
    # "Rajeev Gor&eacute;"            : "https://users.cecs.anu.edu.au/&#126;rpg/",
    # "Tony Hoare"                    : "https://www.cs.ox.ac.uk/people/tony.hoare/",
    # "Dennis Hofheinz"               : "https://crypto.iti.kit.edu/index.php?id=hofheinz",
    # "Marieke Huisman"               : "http://wwwhome.cs.utwente.nl/~marieke/",
    # "Marko Kleine Büning"           : "https://verialg.iti.kit.edu/687.php",
    # "Marko Kleine B&uuml;ning"      : "https://verialg.iti.kit.edu/687.php",
    # "Marko Xing Kleine Büning"      : "https://verialg.iti.kit.edu/687.php",
    # "Marko Xing Kleine B&uuml;ning" : "https://verialg.iti.kit.edu/687.php",
    # "Alexander Koch"                : "https://crypto.iti.kit.edu/staff_alexander_koch.php",
    # "Anne Koziolek"                 : "https://are.ipd.kit.edu/people/anne-koziolek/",
    # "Ralf Küsters"                  : "https://sec.uni-stuttgart.de/people/kuesters",
    # "Ralf K&uuml;sters"             : "https://sec.uni-stuttgart.de/people/kuesters",
    # "Heiko Mantel"                  : "http://www.mais.informatik.tu-darmstadt.de/Heiko_Mantel.html",
    # "Anne Martens"                  : "https://are.ipd.kit.edu/people/anne-koziolek/",
    # "Rosemary Monahan"              : "https://www.cs.nuim.ie/users/dr-rosemary-monahan",
    # "Martin Mohr"                   : "https://pp.ipd.kit.edu/person.php?id=121",
    # "Erik Pescara"                  : "https://www.teco.edu/people/pescara/",
    # "Jörn Müller-Quade"             : "https://crypto.iti.kit.edu/index.php?id=mueller-quade",
    # "J&ouml;rn M&uuml;ller-Quade"   : "https://crypto.iti.kit.edu/index.php?id=mueller-quade",
    # "Jörg Raczkowsky"               : "https://www.ipr.kit.edu/english/staff_109.php",
    # "J&ouml;rg Raczkowsky"          : "https://www.ipr.kit.edu/english/staff_109.php",
    # "Ralf Reussner"                 : "http://sdq.ipd.kit.edu/people/ralf_reussner/",
    # "Peter Sanders"                 : "https://algo2.iti.kit.edu/sanders.php",
    # "Enrico Scapin"                 : "https://sec.uni-stuttgart.de/people/scapin",
    # "Ina Schäfer"                   : "https://www.tu-braunschweig.de/isf/team/schaefer",
    # "Ina Sch&auml;fer"              : "https://www.tu-braunschweig.de/isf/team/schaefer",
    # "Ina Schaefer"                  : "https://www.tu-braunschweig.de/isf/team/schaefer",
    # "Andrea Schankin"               : "https://www.teco.edu/people/schankin/",
    # "Luzie Schreiter"               : "https://www.ipr.kit.edu/english/staff_1247.php",
    # "Carsten Schürmann"             : "https://www.itu.dk/people/carsten/",
    # "Carsten Sch&uuml;rmann"        : "https://www.itu.dk/people/carsten/",
    # "Carsten Schuermann"            : "https://www.itu.dk/people/carsten/",
    # "Carsten Sinz"                  : "https://verialg.iti.kit.edu/353.php",
    # "Gregor Snelting"               : "https://pp.ipd.kit.edu/personhp/gregor_snelting.php",
    "Taghdiri, Mana"                 : "https://www.horus.biz/author/manataghdiri/",
    # "Walter F. Tichy"               : "https://ps.ipd.kit.edu/176_376.php",
    "Tyszberowicz, Shmuel"           : "https://www.int.mta.ac.il/StaffDirectoryMTA/Prof.-Tyszberowicz-Shmuel",
    # "Shmuel S. Tyszberowicz"        : "https://www.int.mta.ac.il/StaffDirectoryMTA/Prof.-Tyszberowicz-Shmuel",
    # "Melanie Volkamer"              : "https://secuso.aifb.kit.edu/Team_Volkamer.php",
    # "Heinz Wörn"                    : "https://www.ipr.kit.edu/english/staff_96.php",
    # "Heinz W&ouml;rn"               : "https://www.ipr.kit.edu/english/staff_96.php",
    # "Martina Zitterbart"            : "https://telematics.tm.kit.edu/staff_zitterbart.php"
}


def print_persons(authors, kind='author'):
    def print_author(a):
        #print(dir(a))
        link = PERSON_LINK.get(str(a), None)
        if link:
            return f'<span class="{kind}"><a href="{link}">{text(a)}</a></span>'
        else:
            return f'<span class="{kind}">{text(a)}</span>'

    for idx, p in enumerate(authors):
        print(print_author(p), end="")
        if idx == len(authors) - 2:
            print(" and ")
        elif idx < len(authors) - 1:
            print(", ")
    print("; ")


def print_links(e, fields):
    preprint = ""
    long_version = ""
    url = ""
    software = ""
    doi = ""

    if 'doi' in fields:
        p = fields['doi']
        doi = f'<a href="https://dx.doi.org/{p}"><img style="height:.8em" src="/img/DOI_logo.svg"/>{p}</a>'

    if 'preprint' in fields:
        p = fields['preprint']
        preprint = f'<a href="{p}">Preprint</a>'

    if 'long_version' in fields:
        p = fields['long_version']
        long_version = f'<a href="{p}">Long Version</a>'

    if 'software' in fields:
        p = fields['long_version']
        software = f'<a href="{p}">Software</a>'

    if 'url' in fields:
        p = fields['url']
        url = f'<a href="{p}">URL</a>'

    perm=f'<a href="#{e.key}">[PERMA]</a>'


    print(f'<div class="links">{perm} {url} {doi} {long_version} {software}</div>')

def print_place(type, fields):
    journal = fields.get('journal', "")
    booktitle = fields.get('booktitle', "")
    volume =  fields.get('volume', "")
    number = fields.get('number', "")
    pages = fields.get('pages', "").replace("--", "&ndash;")
    school = fields.get('school', "")
    year = fields['year']
    series = fields.get('series',"")

    match type:
        case 'book':
             print(f'In {series}, {volume}, {year}')
        case "article":
             print(f'{journal}, {number}({volume}), pp. {pages}')
        case 'inproceedings':
             print(f'{booktitle}, {number}({volume}), pp. {pages}')
        case 'techreport':
             institute=fields.get('institution',"")
             print(f'{series}, {number}, {institute}, {year}')
        case 'phdthesis':
             print(f'PhD thesis, {school}, {year}')
        case _:
             print("XXX", fields)


def text(txt):
    if isinstance(txt, str):
        return txt.replace(r'\"{o}', 'ö')\
                   .replace(r'\"{a}', 'ä')\
                   .replace(r'\"{u}', 'ü')\
                   .replace(r'\"{O}', 'Ö')\
                   .replace(r'\"{A}', 'Ä')\
                   .replace(r'\"{U}', 'Ü')
    elif isinstance(txt, pdb.Person):
        #print(dir(txt))
        return text(' '.join(txt.first_names+txt.last_names))
    else:
        return text(str(txt))

def print_entry(e):
    #print(dir(e), dir(e.fields))
    typ = e.type
    fields = e.fields
    #print(fields.keys(), e)
    abstract = e.fields.get('abstract',None)

    authors = e.persons.get('author', None)
    editors = e.persons.get('editor', None)

    print(f'<div class="bib-entry bib-{typ}" id="{e.key}">')
    if authors:
        print_persons(authors)
    else:
        print_persons(editors, 'editor')
    title = text(fields['title'])
    print(f'<span class="title">{title}</span>; ')
    print_place(typ, fields)
    print_links(e, fields)

    if abstract:
        print(f'<details class="abstract">')
        print('<summary>Abstract</summary>')
        print(f'<p>{abstract}</p>')
        print('</details>')

    print(f'<details class="abstract">')
    print('<summary>Bibtex</summary>')
    b = e.to_string('bibtex')
    print(f'<p><code><pre>{b}</pre></code></p>')
    print('</details>')

    print("</div>")


if __name__ == '__main__':
    cli = argparse.ArgumentParser("renderbib.py", description="Renders a Bibtex file into a HTML website")
    cli.add_argument("--keyword", "-k")
    cli.add_argument("file")
    args = cli.parse_args()
    db = pdb.parse_file(args.file)

    # This would be nice and easy, but did not support html or links ...
    # We need to write something on our own.
    # engine = PybtexEngine()
    # result = engine.format_from_file("publications.bib", "plain", output_backend="md")
    # print(result)

    entries = [x for x in db.entries.values() if 'year' in x.fields]
    get_year = lambda e: -int(e.fields['year'])
    entries = sorted(entries, key = get_year)


    print("""---\ntitle: Publications\n---\n\n
<style>
 .bib-entry {
   padding:.5em;
   font-size:80%;
 }

 span.author {
   font-style:italic;
 }

 span.title {
   font-weight:bold;
 }
</style>
\n\n""")




    current_year = None

    for v in entries:
        if v.type == 'proceedings':
            continue

        year = v.fields['year']
        if year != current_year:
            print_section_year(year)
            current_year = year


        print_entry(v)
