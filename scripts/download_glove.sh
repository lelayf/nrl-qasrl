#!/bin/sh

wget http://nlp.stanford.edu/data/glove.6B.zip
mkdir ../data/glove
mv glove.6B.zip ../data/glove
cd  ../data/glove
unzip glove.6B.zip
gzip glove.6B.100d.txt

