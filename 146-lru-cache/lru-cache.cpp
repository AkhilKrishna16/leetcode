class Node {
    public:
    Node* prev;
    Node* next;
    int key, val;

    Node(int key, int val) {
        this->prev = nullptr;
        this->next = nullptr;
        this->key = key;
        this->val = val;
    }
};

class LRUCache {
public:
    int capacity;
    unordered_map<int, Node*> lookup_table;
    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);

    LRUCache(int capacity) {
        // maybe think of using a queue
        // use a linked list, add to the back for recent, shift right
        // use a hashmap to actually access the nodes for O(1) lookup
        this->capacity = capacity;
        this->head->next = tail;
        this->tail->prev = head;
    }

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insert(Node* node) {
        node->next = head->next;
        node->next->prev = node;
        head->next = node;
        node->prev = head;
    }
    
    int get(int key) {
        if(!this->lookup_table.contains(key)) {
            return -1;
        }

        remove(this->lookup_table[key]);
        insert(this->lookup_table[key]);
        return this->lookup_table[key]->val;
    }
    
    void put(int key, int value) {
        // two cases: already in the list, so just move it to the front
        if(this->lookup_table.contains(key)) {
            remove(this->lookup_table[key]);
            insert(this->lookup_table[key]);
            this->lookup_table[key]->val = value;
        } else { // or not in the list, if not yet reached max capacity move to the front, else just remove tail and set the tail to tail prev, and insert at top the new node
            Node* node = new Node(key, value);
            if(this->lookup_table.size() < this->capacity) {
                insert(node);
                this->lookup_table[key] = node;
            } else {
                Node* lru = tail->prev;
                remove(lru);
                this->lookup_table[key] = node;
                this->lookup_table.erase(lru->key);
                insert(node);
                delete lru;
            }
            
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */