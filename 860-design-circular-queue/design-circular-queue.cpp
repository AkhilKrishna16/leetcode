class MyCircularQueue {
public:
    vector<int> buffer;
    int maxSize = 0;
    int head = 0;
    int tail = 0;
    int count = 0;

    MyCircularQueue(int k) {
        this->maxSize = k;
        this->buffer.resize(this->maxSize, 0);
    }
    
    bool enQueue(int value) {
        if(this->count == this->maxSize) {
            return 0;
        }

        this->buffer[head] = value;
        head = (head + 1) % this->maxSize;
        this->count++;
        return 1;
    }
    
    bool deQueue() {
        if(this->count == 0) {
            return 0;
        }

        tail = (tail + 1) % this->maxSize;
        this->count--;
        return 1;
    }
    
    int Front() {
        return this->count == 0 ? -1 : this->buffer[tail];
    }
    
    int Rear() {
        return this->count == 0 ? -1 : this->buffer[(head - 1 + this->maxSize) % this->maxSize];
    }
    
    bool isEmpty() {
        return this->count == 0;
    }
    
    bool isFull() {
        return this->count == this->maxSize;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */