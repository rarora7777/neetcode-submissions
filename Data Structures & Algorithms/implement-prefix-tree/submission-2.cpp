class Node
{
public:
    Node* children[26];
    bool endOfWord = false;

    Node()
    {
        for (int i=0; i<26; ++i)
            children[i] = nullptr;
    }
};

class PrefixTree 
{
public:
    Node *root;
    
    PrefixTree()
    {
        root = new Node();
    }
    
    void insert(string word)
    {
        if (word.length()==0)
            return;

        Node *node = root;
        int i = 0;

        while(i < word.length() && node->children[word[i] - 'a'] != nullptr)
        {
            node = node->children[word[i++] - 'a'];
        }
        
        while (i < word.length())
        {
            node->children[word[i] - 'a'] = new Node();
            // std::cout<<"Insert "<<word[i]<<' ';
            node = node->children[word[i] - 'a'];
            i++;
        }
        // std::cout<<std::endl;

        node->endOfWord = true;
    }

    bool _startsWith(string prefix, bool &endOfWord)
    {
        Node *node = root;
        for (int i=0; i<prefix.length(); ++i)
        {
            // std::cout<<"search "<<prefix[i]<<std::endl;
            if (node->children[prefix[i] - 'a'])
            {
                // std::cout<<"found  "<<prefix[i]<<std::endl;
                node = node->children[prefix[i] - 'a'];
            }
            else
            {
                return false;
            }
        }
        endOfWord = node->endOfWord;
        
        return true;
    }

    bool search(string word)
    {
        bool endOfWord;
        bool found = _startsWith(word, endOfWord);

        return found && endOfWord;
    }
    
    bool startsWith(string prefix)
    {
        bool endOfWord;
        return _startsWith(prefix, endOfWord);
    }
};
