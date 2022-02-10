def three2one(prot, sep=None):
""" translate a protein sequence from 3 to 1 letter codesep - separator if not one of the whitespace characters"""
code = {"GLY" : "G", "ALA" : "A", "LEU" : "L", "ILE" : "I",
"ARG" : "R", "LYS" : "K", "MET" : "M", "CYS" : "C",
"TYR" : "Y", "THR" : "T", "PRO" : "P", "SER" : "S",
"TRP" : "W", "ASP" : "D", "GLU" : "E", "ASN" : "N",
"GLN" : "Q", "PHE" : "F", "HIS" : "H", "VAL" : "V"}
newprot = ""
for aa in prot.split(sep):
newprot += code.get(aa, "?")
return newprot
