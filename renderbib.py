import pybtex.database as pdb

from pybtex import PybtexEngine

db = pdb.parse_file("publications.bib")

engine = PybtexEngine()
result = engine.format_from_file("publications.bib", "plain", output_backend="md")
print(result)
