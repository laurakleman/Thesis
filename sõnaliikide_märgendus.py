import re
import sys
import os
import csv
from glob import glob

corpus_file = sys.argv[1]
mapping_file = sys.argv[2]
out_file = sys.argv[3]


def read_mapping(mapping_file):

	mapping = {}
	

	with open(mapping_file, 'r', encoding="utf-8") as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)

		for row in reader:
			mapping[row[1].strip()] = (row[0].strip(),row[2].strip()) 
	return mapping
	
mapping = read_mapping(mapping_file)

#failirida = re.compile("^{n}\t{word}\t{lemma}\t{upostag}\t{xpostag}\t{feats}\t{head}\t{deprel}\t{deps}\t{misc}$")
failirida = re.compile(r'^(?P<number>[0-9]+?)\t(?P<word>[^\t]*)\t(?P<lemma>[^\t]*)\t(?P<upostag>[^\t]*)\t(?P<xpostag>[^\t]*)\t(?P<feats>[^\t]*)\t(?P<head>[^\t]*)\t(?P<deprel>[^\t]*).*$')

def teisendus(fail):
	conllu_line_str = "{n}\t{word}\t{lemma}\t{upostag}\t{xpostag}\t{feats}\t{head}\t{deprel}\t{deps}\t{misc}"

	n = 1

	for line in open(corpus_file, encoding="utf-8"):
		m = failirida.match(line.rstrip())
		if m is not None:
			word,lemma,upostag,xpostag,feats,head,deprel=m.group('word'), m.group('lemma'), m.group('upostag'), m.group('xpostag'),m.group('feats'),m.group('head'),m.group('deprel') 
			
		
			for k in feats.split('|'):
				
				if k in mapping:
				
					feats = feats.replace(k,mapping[k][0]+"="+mapping[k][1])

			conllu_line = conllu_line_str.format(

				n=n,

				word=word,

				lemma=lemma,

				upostag=upostag,

				xpostag=xpostag,

				feats=feats,

				head=head,

				deprel=deprel,

				deps="_",

				misc="_"

            )

			n += 1

		else:

			conllu_line = ""

			n = 1

		yield conllu_line	

with open(out_file, 'w', encoding='utf-8') as outf:

	prw, n = None, 0

	for line in teisendus(corpus_file):

		if line == "" and (n == 0 or prw == ""):

			continue

		print(line, file=outf)

		prw = line

		n += 1

	print(file=outf)