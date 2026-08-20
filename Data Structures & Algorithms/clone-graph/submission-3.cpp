/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution
{
public:
    unordered_map<Node*, Node*> oldToNew;
    Node* cloneGraph(Node* node)
    {
        if (node == nullptr)
            return node;
        else if (oldToNew.contains(node))
            return oldToNew[node];

        int val = node->val;
        vector<Node*> neighbors;
        neighbors.reserve(node->neighbors.size());
        Node* copy = new Node(val);
        oldToNew[node] = copy;
        
        for(const auto &other: node->neighbors)
        {
            neighbors.push_back(cloneGraph(other));
        }

        copy->neighbors = neighbors;

        return copy;
    }
};
