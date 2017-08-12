in wordcut folder
- lexitron:	dictionary file use in lexto
- LongLexTo.java: main longlexto file
- Trie.java and LongParseTree.java: class used in lexto

- folder sample: sample test for longlexto
- folder wordcut: sample output for longlexto
- unknownWord.txt: unknownWord output for longlexto

- use lexto: 	javac -encoding "UTF-8" Trie.java
		javac -encoding "UTF-8" LongParseTree.java
		javac -encoding "UTF-8" LongLexTo.java
		java -Dfile.encoding=UTF8 LongLexTo [input text file] [wordcut file]
- you can change lexitron file and unknown file input in LongLexTo.java

- genWordCutFromSample.sh: use to run wordcut from sample

in nounphrase folder
- nounphrase.py: nounphrase detector file
  use: python nounphrase.py [input from lexto] [output file]
- patterns.py: pattern generator
- patterns.txt : detect nounphrase pattern

- folder sample: sample test for longlexto
- folder wordcut: sample output for longlexto and input for nounphrase.py
- folder nounphrase: sample output for nounphrase.py

-genNounphrase.sh: test run sample
