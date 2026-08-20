class Node
{
public:
    map<char, Node> children;

    Node()
    {
    }
};

class PrefixTree 
{
public:
    Node root;
    
    PrefixTree()
    {
    }
    
    void insert(string word)
    {
        if (word.length()==0)
            return;

        Node *node = &root;
        int i = 0;

        while(i < word.length() && node->children.contains(word[i]))
        {
            node = &node->children[word[i++]];
        }
        
        while (i < word.length())
        {
            node->children[word[i]] = Node();
            // std::cout<<"Insert "<<word[i]<<' ';
            node = &node->children[word[i]];
            i++;
        }
        // std::cout<<std::endl;

        node->children['\0'] = Node();
    }
    
    bool search(string word)
    {
        return startsWith(word + '\0');
    }
    
    bool startsWith(string prefix)
    {
        Node *node = &root;
        for (int i=0; i<prefix.length(); ++i)
        {
            // std::cout<<"search "<<prefix[i]<<std::endl;
            if (node->children.contains(prefix[i]))
            {
                // std::cout<<"found  "<<prefix[i]<<std::endl;
                node = &node->children[prefix[i]];
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};
