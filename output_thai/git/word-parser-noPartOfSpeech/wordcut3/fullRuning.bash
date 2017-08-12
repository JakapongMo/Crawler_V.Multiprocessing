javac -encoding "UTF-8" Trie.java
echo "******** finished compile Trie ********"
javac -encoding "UTF-8" LongParseTree.java
echo "**** finished compile LongParseTree ***"
javac -encoding "UTF-8" LongLexTo.java
echo "****** finished compile LongLexTo *****"
java -Dfile.encoding=UTF8 LongLexTo .\simple0.txt .\sample\result.txt