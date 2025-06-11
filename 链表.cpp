#include<iostream>
#include<stdexcept>
using namespace std;

template<class T>
class CNode {
public:
    T data;
    CNode<T> *next;
    CNode(T val = T()) : data(val), next(nullptr) {}
};

template<class T>
class CList {
private:
    CNode<T> *head;
public:
    CList() : head(new CNode<T>()) {
        head->next = nullptr;
    }

    void append(T a) {
        CNode<T> *newNode = new CNode<T>(a);
        CNode<T> *current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }

    void insert(T a, int n) {
        if (n < 0) return;
        CNode<T> *newNode = new CNode<T>(a);
        CNode<T> *current = head;
        for (int i = 0; current != nullptr && i < n; ++i) {
            current = current->next;
        }
        if (current == nullptr) return;
        newNode->next = current->next;
        current->next = newNode;
    }

    void remove(int n) {
        if (n < 0) return;
        CNode<T> *current = head;
        for (int i = 1; current != nullptr && i < n; ++i) {
            current = current->next;
        }
        if (current == nullptr || current->next == nullptr) return;
        CNode<T> *temp = current->next;
        current->next = temp->next;
        delete temp;
    }

    T get(int n) {
        if (n < 0) throw out_of_range("Index out of range");
        CNode<T> *current = head->next;
        for (int i = 1; current != nullptr && i < n; ++i) {
            current = current->next;
        }
        if (current == nullptr) throw out_of_range("Index out of range");
        return current->data;
    }

    void set(T a, int n) {
        if (n < 0) return;
        CNode<T> *current = head->next;
        for (int i = 1; current != nullptr && i < n; ++i) {
            current = current->next;
        }
        if (current == nullptr) return;
        current->data = a;
    }

    void print() {
        CNode<T> *current = head->next;
        while (current != nullptr) {
            if(current->next==NULL){
                cout << current->data << endl;

            }
            else{
                cout << current->data << " ";
            }

            current = current->next;
        }

    }

    ~CList() {
        CNode<T> *current = head;
        while (current != nullptr) {
            CNode<T> *next = current->next;
            delete current;
            current = next;
        }
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        char s;
        cin >> s;
        if (s == 'I') {
            CList<int> x;
            int n;
            cin >> n;
            for (int i = 0; i < n; ++i) {
                int a;
                cin >> a;
                x.append(a);
            }
            int i, num;
            cin >> i >> num;
            x.insert(num, i);
            cin >> i;
            try {
                cout << x.get(i) << endl;
            } catch (const out_of_range& e) {
                cout << "error" << endl;
            }
            cin >> i;
            x.remove(i);
            cin >> i >> num;
            x.set(num, i);
            x.print();
        } else if (s == 'D') {
            CList<double> x;
            int n;
            cin >> n;
            for (int i = 0; i < n; ++i) {
                double a;
                cin >> a;
                x.append(a);
            }
            int i;
            double num;
            cin >> i >> num;
            x.insert(num, i);
            cin >> i;
            try {
                cout << x.get(i) << endl;
            } catch (const out_of_range& e) {
                cout << "error" << endl;
            }
            cin >> i;
            x.remove(i);
            cin >> i >> num;
            x.set(num, i);
            x.print();
        } else {
            CList<string> x;
            int n;
            cin >> n;
            for (int i = 0; i < n; ++i) {
                string a;
                cin >> a;
                x.append(a);
            }
            int i;
            string num;
            cin >> i >> num;
            x.insert(num, i);
            cin >> i;
            try {
                cout << x.get(i) << endl;
            } catch (const out_of_range& e) {
                cout << "error" << endl;
            }
            cin >> i;
            x.remove(i);
            cin >> i >> num;
            x.set(num, i);
            x.print();
        }
    }
    return 0;
}