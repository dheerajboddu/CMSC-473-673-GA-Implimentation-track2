# CMSC-473-673-GA-Implimentation-track2
NLP Graduate Assessment  DC32292


# Problem Statement: 
Implement the inside-outside and CKY algorithms for probabilistic context free grammars. For
probabilistic CKY, see chapter 14.2 of 3SLP. For inside-outside, while you may reference any resource in
compliance with the “Y” resources in the beginnning, you may also reference Michael Collins’s notes on
the inside-outside algorithm: http://www.cs.columbia.edu/˜mcollins/io.pdf. Consulting
these notes will not be an academic integrity violation. Use the inside-outside algorithm to train in a semisupervised manner (using the Penn Treebank sections 02-21 for supervised data, and the UD English EWT
training sentences for unsupervised data), and evaluate on the Penn Treebank (dev evaluation on section
22, test evaluation on section 23). Obtain parses using your CKY implementation, and evaluate using the
publicly available evalb script (https://nlp.cs.nyu.edu/evalb/EVALB.tgz).
