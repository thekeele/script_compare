#!/usr/bin/env python
from __future__ import division
import nltk
from nltk.corpus import stopwords

# script source: http://www.people.com/article/melania-trump-michelle-obama-similar-convention-speeches

# open
f_rnc = open('rnc_full.txt', 'r')
f_dnc = open('dnc_full.txt', 'r')

# read
rnc_full = f_rnc.read()
dnc_full = f_dnc.read()

# count
rnc_tokens = nltk.word_tokenize(rnc_full)
dnc_tokens = nltk.word_tokenize(dnc_full)

# normalize
stopwords = stopwords.words('english')

rnc_tokens = [w.lower() for w in rnc_tokens if w.isalpha()]
rnc_tokens = [w for w in rnc_tokens if w not in stopwords]

dnc_tokens = [w.lower() for w in dnc_tokens if w.isalpha()]
dnc_tokens = [w for w in dnc_tokens if w not in stopwords]

# calculation
fd_rnc = nltk.FreqDist(rnc_tokens)
fd_dnc = nltk.FreqDist(dnc_tokens)

# display
print "2016 RNC Transcript Frequency Distribution: "
fd_rnc.tabulate()

print "\n2008 DNC Transcript Frequency Distribution: "
fd_dnc.tabulate()

# set operation
union = fd_rnc & fd_dnc

print "\nMost Common Words Ranked by Frequency"
print union

print "\nNumber of Common Words: " + str(len(union))
print "RNC %: " + str(len(union) / len(fd_rnc) * 100) + " of " + str(len(fd_rnc))
print "DNC %: " + str(len(union) / len(fd_dnc) * 100) + " of " + str(len(fd_dnc))
