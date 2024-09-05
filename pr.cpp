class Node {
    int data;
    Node *next;

  public:
    Node(int data, Node *next = nullptr) : data{data}, next{next} {}
    ~Node() { delete next; }
    Node(const Node &other)
        : data{other.data}, next{other.next ? new Node{*other.next} : nullptr} {
    }
};

// default ctor
// dtor
// copy ctor
// move ctor
// copy assignmnet operator
// move assignment operator
