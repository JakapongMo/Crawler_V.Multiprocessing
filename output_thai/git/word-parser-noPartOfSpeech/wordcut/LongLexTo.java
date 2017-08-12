/**
 * Licensed under the CC-GNU Lesser General Public License, Version 2.1 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://creativecommons.org/licenses/LGPL/2.1/
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// LongLexTo: Tokenizing Thai texts using Longest Matching Approach
//   Note: Types: 0=unknown  1=known  2=ambiguous  3=English/digits  4=special characters
//
// Public methods:
//   1) public LongLexTo(File dictFile);  //Constructor with a dictionary file
//   2) public void addDict(File dictFile);     //Add dictionary (e.g., unknown-word file)
//   3) public void wordInstance(String text);  //Word tokenization
//   4) public void lineInstance(String text);  //Line-break tokenization
//   4) public Vector getIndexList();
//   5) Iterator's public methods: hasNext, first, next
//
// Author: Choochart Haruechaiyasak
// Last update: 28 March 2006

import java.io.*;
import java.util.*;

public class LongLexTo {

	//Private variables
	private Trie dict;               //For storing words from dictionary
	private LongParseTree ptree;     //Parsing tree (for Thai words)

	//Returned variables
	private Vector indexList;  //List of word index positions
	private Vector lineList;   //List of line index positions
	private Vector typeList;   //List of word types (for word only)
	private Iterator iter;     //Iterator for indexList OR lineList (depends on the call)

	private static String dictFileName = "lexitron.txt";
	public static ArrayList<String> words = new ArrayList<String>();

	/*******************************************************************/
	/*********************** Return index list *************************/
	/*******************************************************************/
	public Vector getIndexList() {
		return indexList; }

	/*******************************************************************/
	/*********************** Return type list *************************/
	/*******************************************************************/
	public Vector getTypeList() {
		return typeList; }

	/*******************************************************************/
	/******************** Iterator for index list **********************/
	/*******************************************************************/
	//Return iterator's hasNext for index list
	public boolean hasNext() {
		if(!iter.hasNext())
			return false;
		return true;
	}

	//Return iterator's first index
	public int first() {
		return 0;
	}

	//Return iterator's next index
	public int next() {
		return((Integer)iter.next()).intValue();
	}

	/*******************************************************************/
	/********************** Constructor (default) **********************/
	/*******************************************************************/
	@SuppressWarnings("unchecked")
	public LongLexTo() throws IOException {
		csvReader(dictFileName);

		dict=new Trie();
		File dictFile=new File(dictFileName);
		if(dictFile.exists())
			addDict(dictFile);
		else
			System.out.println(" !!! Error: Missing default dictionary file, lexitron.txt");
		indexList=new Vector();
		lineList=new Vector();
		typeList=new Vector();
		ptree=new LongParseTree(dict, indexList, typeList);

	} //Constructor

	/*******************************************************************/
	/************** Constructor (passing dictionary file ) *************/
	/*******************************************************************/
	@SuppressWarnings("unchecked")
	public LongLexTo(File dictFile) throws IOException {
		csvReader(dictFileName);
		dict=new Trie();
		if(dictFile.exists())
			addDict(dictFile);
		else
			System.out.println(" !!! Error: The dictionary file is not found, " + dictFile.getName());
		indexList=new Vector();
		lineList=new Vector();
		typeList=new Vector();
		ptree=new LongParseTree(dict, indexList, typeList);
		
	} //Constructor

	/*******************************************************************/
	/**************************** addDict ******************************/
	/*******************************************************************/
	@SuppressWarnings("unchecked")
	public void addDict(File dictFile) throws IOException {

		// Read words from dictionary
		for (String temp : words) {
			dict.add(temp.replaceAll("\u00A0", ""));
		}
	} 

	/****************************************************************/
	/************************** wordInstance ************************/
	/****************************************************************/
	@SuppressWarnings("unchecked")
	public void wordInstance(String text) {

		indexList.clear();
		typeList.clear();
		int pos, index;
		String word;
		boolean found;
		char ch;

		pos=0;
		while(pos<text.length()) {

			//Check for special characters and English words/numbers
			ch=text.charAt(pos);

			//English
			if(((ch>='A')&&(ch<='Z'))||((ch>='a')&&(ch<='z'))) {
				while((pos<text.length())&&(((ch>='A')&&(ch<='Z'))||((ch>='a')&&(ch<='z'))))
					ch=text.charAt(pos++);
				if(pos<text.length())
					pos--;
				indexList.addElement(new Integer(pos));
				typeList.addElement(new Integer(3));
			}
			//Digits
			else if(((ch>='0')&&(ch<='9'))||((ch>='๐')&&(ch<='๙'))) {
				while((pos<text.length())&&(((ch>='0')&&(ch<='9'))||((ch>='๐')&&(ch<='๙'))||(ch==',')||(ch=='.')))
					ch=text.charAt(pos++);
				if(pos<text.length())
					pos--;
				indexList.addElement(new Integer(pos));
				typeList.addElement(new Integer(3));
			}
			//Special characters
			else if((ch<='~')||(ch=='ๆ')||(ch=='ฯ')||(ch=='')||(ch=='')||(ch==',')) {
				pos++;
				indexList.addElement(new Integer(pos));
				typeList.addElement(new Integer(4));
			}
			//Thai word (known/unknown/ambiguous)
			else
				pos=ptree.parseWordInstance(pos, text);
		} //While all text length
		iter=indexList.iterator();
	} //wordInstance

	/****************************************************************/
	/************************** lineInstance ************************/
	/****************************************************************/
	@SuppressWarnings("unchecked")
	public void lineInstance(String text) {

		int windowSize=10; //for detecting parentheses, quotes
		int curType, nextType, tempType, curIndex, nextIndex, tempIndex;
		lineList.clear();
		wordInstance(text);
		int i;
		for(i=0; i<typeList.size()-1; i++) {
			curType=((Integer)typeList.elementAt(i)).intValue();
			curIndex=((Integer)indexList.elementAt(i)).intValue();

			if((curType==3)||(curType==4)) {
				//Parenthesese
				if((curType==4)&&(text.charAt(curIndex-1)=='(')) {
					int pos=i+1;
					while((pos<typeList.size())&&(pos<i+windowSize)) {
						tempType=((Integer)typeList.elementAt(pos)).intValue();
						tempIndex=((Integer)indexList.elementAt(pos++)).intValue();
						if((tempType==4)&&(text.charAt(tempIndex-1)==')')) {
							lineList.addElement(new Integer(tempIndex));
							i=pos-1;
							break;
						}
					}
				}
			
				//Single quote
				else if((curType==4)&&(text.charAt(curIndex-1)=='\'')) {
					int pos=i+1;
					while((pos<typeList.size())&&(pos<i+windowSize)) {
						tempType=((Integer)typeList.elementAt(pos)).intValue();
						tempIndex=((Integer)indexList.elementAt(pos++)).intValue();
						
						if((tempType==4)&&(text.charAt(tempIndex-1)=='\'')) {
							lineList.addElement(new Integer(tempIndex));
							i=pos-1;
							break;
						}
					}
				}
			
				//Double quote
				else if((curType==4)&&(text.charAt(curIndex-1)=='\"')) {
					int pos=i+1;
					while((pos<typeList.size())&&(pos<i+windowSize)) {
						tempType=((Integer)typeList.elementAt(pos)).intValue();
						tempIndex=((Integer)indexList.elementAt(pos++)).intValue();
			
						if((tempType==4)&&(text.charAt(tempIndex-1)=='\"')) {
							lineList.addElement(new Integer(tempIndex));
							i=pos-1;
							break;
						}
					}
				}
				else
					lineList.addElement(new Integer(curIndex));
			}
			
			else {
				nextType=((Integer)typeList.elementAt(i+1)).intValue();
				nextIndex=((Integer)indexList.elementAt(i+1)).intValue();
				if((nextType==3)||
					((nextType==4)&&((text.charAt(nextIndex-1)==' ')||(text.charAt(nextIndex-1)=='\"')||
					(text.charAt(nextIndex-1)=='(')||(text.charAt(nextIndex-1)=='\''))))
					
					lineList.addElement(new Integer(((Integer)indexList.elementAt(i)).intValue()));
				
				else if((curType==1)&&(nextType!=0)&&(nextType!=4))
					lineList.addElement(new Integer(((Integer)indexList.elementAt(i)).intValue()));
			}
		}
		if(i<typeList.size())
			lineList.addElement(new Integer(((Integer)indexList.elementAt(indexList.size()-1)).intValue()));
		iter=lineList.iterator();
	} //lineInstance

	/****************************************************************/
	/*************************** Demo *******************************/
	/****************************************************************/
	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {
		if(args.length != 2) {
			System.out.println("usage: java LongLexTo [input text file] [output csv file]");
			System.exit(1);
		}
		LongLexTo tokenizer = new LongLexTo(new File(dictFileName));		
		Vector typeList;
		String text="", line, inFileName, outFileName;
		char ch;
		int begin, end, type;

		File inFile, outFile;
		FileReader fr;
		BufferedReader br;
		FileWriter fw;

		BufferedReader streamReader = new BufferedReader(new InputStreamReader(System.in));

		System.out.println("*******************************");
		System.out.println("*** LexTo: Lexeme Tokenizer ***");
		System.out.println("*******************************");


		//Get input file name
		// do {
			inFileName = args[0].replaceAll("\u00A0", "");
			inFile=new File(inFileName);			
		// } while(!inFile.exists());

		if(!inFile.exists()){
			System.out.println("There are no input file.");
			System.out.println("Exit");
			System.exit(1);
		}

		//Get output file name
		outFileName=args[1].trim();
		outFile=new File(outFileName);

		fr=new FileReader(inFile);
		br=new BufferedReader(fr);
		fw=new FileWriter(outFile);

		fw.write("word\n");
		
		while((line=br.readLine())!=null) {
			line=line.replaceAll("\u00A0", "");
			// line = line.trim();
			if(line.length() > 0) {
				tokenizer.wordInstance(line);
				typeList=tokenizer.getTypeList();
				begin=tokenizer.first();
				int i = 0;
				while(tokenizer.hasNext()) {
					end=tokenizer.next();
					type=((Integer)typeList.elementAt(i++)).intValue();
					if(type != 4) {
						String ans = line.substring(begin, end).replaceAll("\u00A0", "");
						fw.write("\"" + ans + "\"\n");
						// System.out.println(ans + " " + type);
					}

						begin=end;

				}
			}
		} //while all line

		fr.close();
		fw.close();
		System.out.println("\n *** Status: Use Text Editor to view result: " + outFileName);
	} 

	//read csv dict file into list
	private static void csvReader(String csvFile) {
		BufferedReader br = null;
		String line = "";

		try {

			br = new BufferedReader(new FileReader(csvFile));
			while ((line = br.readLine()) != null) {
				String[] splitLine = line.split("\\|");
				String[] emptyArr = {""};

				words.add(splitLine[0].replaceAll("\u00A0", ""));
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}

	private static void printArr(String[] arr) {
		for(int i=0; i<arr.length; i++)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	public static void printArrListString(ArrayList<String> arr) {
		for(int i = 0; i < arr.size(); i++) {
			String ele = arr.get(i);
			System.out.println(ele);
		}
	}

	private static String stringArr(String[] arr) {
		String res = "\"";
		for(int i=0; i<arr.length; i++){
			res += arr[i];
			if(i != arr.length-1)
				res += ",";
		}
		return res + "\"";
	}

	private static void clearFile(String filename) {
		try {
			FileWriter fw = new FileWriter(filename,false); //the true will append the new data
			fw.write("");          
			fw.close();
		}
		catch(IOException ioe) {
			System.err.println("IOException: " + ioe.getMessage());
		}
	}
	
	private static void writeFile(String word,String filename) {
		try {
			FileWriter fw = new FileWriter(filename,true); //the true will append the new data
			fw.write(word + "\n");          
			fw.close();
		}
		catch(IOException ioe) {
			System.err.println("IOException: " + ioe.getMessage());
		}
	}
}