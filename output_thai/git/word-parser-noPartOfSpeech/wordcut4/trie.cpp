#include <iostream>
#include <stdio.h>
#include <string>
#define childrenSize 26
using namespace std;

typedef struct nodes
{
	struct nodes** children = new struct nodes*[childrenSize];
	char info;
	bool isLeaf;
} node;

node* initNode(node* motherNodePtr, char newChar)
{
	node* newNodePtr = new node();
	newNodePtr->info = newChar;

	motherNodePtr->children[newChar - 'a'] = newNodePtr;	
	return newNodePtr;
}

node* initRootNode()
{
	node* newNodePtr = new node();
	newNodePtr->info = '\0';
	newNodePtr->isLeaf = false;
	return newNodePtr;
}

void printTree(node* rootNode)
{
	if(rootNode == NULL)
	{
		return;
	}
	cout << rootNode->info << " ";
	for(int i=0; i<childrenSize; i++)
	{
		printTree(rootNode->children[i]);
	}
}

int addWord(node* rootNode,string word)
{
	node* motherNode = rootNode;
	int res = 0;

	for(int i=0; i<word.length(); i++)
	{
		if(motherNode->children[word[i]-'a'] == 0)
		{
			node* newNode = initNode(motherNode, word[i]);
			motherNode = newNode;
			// res++;
		}
		else
		{
			motherNode = motherNode->children[word[i]-'a'];
			if(i == word.length()-1)
				res--;
			res++;
		}
	}
	motherNode->isLeaf = true;
	return res + 1;
}

int main()
{
	node* rootNode = initRootNode();
	int n, res = 0;
	cin >> n;
	for(int i=0; i<n; i++)
	{
		string in;
		cin >> in;
		int tmp = addWord(rootNode, in);
		// cout << in << " " << tmp << endl;
		res += tmp;
	}
	cout << res << endl;
	// printTree(rootNode);
	// cout << endl;
}