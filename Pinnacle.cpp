#include <iostream>
using namespace std;

struct Member {
    int prn;
    string name;
    Member* next;
};

class PinnacleClub {
    Member* head;

public:
    PinnacleClub() {
        head = nullptr;
    }

    void addPresident() {
        int prn;
        string name;
        cout << "Enter President PRN and Name: ";
        cin >> prn;
        cin.ignore();
        getline(cin, name);
        Member* newNode = new Member{prn, name, head};
        head = newNode;
    }

    void addSecretary() {
        int prn;
        string name;
        cout << "Enter Secretary PRN and Name: ";
        cin >> prn;
        cin.ignore();
        getline(cin, name);
        Member* newNode = new Member{prn, name, nullptr};
        if (!head) {
            head = newNode;
            return;
        }
        Member* temp = head;
        while (temp->next != nullptr)
            temp = temp->next;
        temp->next = newNode;
    }

    void addMember() {
        int prn;
        string name;
        cout << "Enter Member PRN and Name: ";
        cin >> prn;
        cin.ignore();
        getline(cin, name);
        Member* newNode = new Member{prn, name, nullptr};
        if (!head || !head->next) {
            cout << "Add President and Secretary first.\n";
            return;
        }
        Member* temp = head;
        while (temp->next->next != nullptr)
            temp = temp->next;
        newNode->next = temp->next;
        temp->next = newNode;
    }

    void deletePresident() {
        if (head) {
            Member* temp = head;
            head = head->next;
            delete temp;
            cout << "President deleted.\n";
        }
    }

    void deleteSecretary() {
        if (!head || !head->next) {
            cout << "Cannot delete Secretary.\n";
            return;
        }
        Member* temp = head;
        while (temp->next->next != nullptr)
            temp = temp->next;
        delete temp->next;
        temp->next = nullptr;
        cout << "Secretary deleted.\n";
    }

    void deleteMember() {
        if (!head || !head->next) {
            cout << "List is too small.\n";
            return;
        }
        int prn;
        cout << "Enter PRN of member to delete: ";
        cin >> prn;
        Member* temp = head;
        while (temp->next && temp->next->next && temp->next->prn != prn)
            temp = temp->next;
        if (temp->next && temp->next->next) {
            Member* toDelete = temp->next;
            temp->next = temp->next->next;
            delete toDelete;
            cout << "Member deleted.\n";
        } else {
            cout << "Member not found or cannot delete President/Secretary.\n";
        }
    }

    int countMembers() {
        int count = 0;
        Member* temp = head;
        while (temp) {
            count++;
            temp = temp->next;
        }
        return count;
    }

    void display() {
        Member* temp = head;
        int i = 1;
        while (temp) {
            cout << i++ << ". PRN: " << temp->prn << ", Name: " << temp->name;
            if (temp == head) cout << " [President]";
            else if (temp->next == nullptr) cout << " [Secretary]";
            cout << endl;
            temp = temp->next;
        }
    }

    Member* getHead() {
        return head;
    }

    void setTail(Member* tail) {
        if (!head) {
            head = tail;
            return;
        }
        Member* temp = head;
        while (temp->next != nullptr)
            temp = temp->next;
        temp->next = tail;
    }
};

// Concatenate club2 to club1
void concatenate(PinnacleClub& club1, PinnacleClub& club2) {
    club1.setTail(club2.getHead());
}

int main() {
    PinnacleClub divA, divB;
    int choice;

    cout << "Enter members for Division A:\n";
    divA.addPresident();
    int n;
    cout << "How many general members to add? ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        divA.addMember();
    }
    divA.addSecretary();

    cout << "\nEnter members for Division B:\n";
    divB.addPresident();
    cout << "How many general members to add? ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        divB.addMember();
    }
    divB.addSecretary();

    do {
        cout << "\n--- Pinnacle Club Menu ---\n";
        cout << "1. Display Division A Members\n";
        cout << "2. Display Division B Members\n";
        cout << "3. Concatenate Div A and Div B\n";
        cout << "4. Delete President (Div A)\n";
        cout << "5. Delete Secretary (Div A)\n";
        cout << "6. Delete Member by PRN (Div A)\n";
        cout << "7. Count Members (Div A)\n";
        cout << "8. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                divA.display();
                break;
            case 2:
                divB.display();
                break;
            case 3:
                concatenate(divA, divB);
                cout << "Concatenated Division B into Division A.\n";
                break;
            case 4:
                divA.deletePresident();
                break;
            case 5:
                divA.deleteSecretary();
                break;
            case 6:
                divA.deleteMember();
                break;
            case 7:
                cout << "Total members: " << divA.countMembers() << endl;
                break;
            case 8:
                cout << "Exiting.\n";
                break;
            default:
                cout << "Invalid choice.\n";
        }
    } while (choice != 8);

    return 0;
}
