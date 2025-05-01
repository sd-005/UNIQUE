#include <iostream>
using namespace std;

struct Seat {
    int seatNo;
    bool booked;
    Seat* next;
    Seat* prev;
};

const int ROWS = 10;
const int SEATS = 7;

Seat* rows[ROWS];

void initializeSeats() {
    for (int i = 0; i < ROWS; i++) {
        Seat* head = nullptr;
        Seat* tail = nullptr;

        for (int j = 1; j <= SEATS; j++) {
            Seat* newSeat = new Seat{j, false, nullptr, nullptr};
            if (!head) {
                head = newSeat;
                tail = newSeat;
                newSeat->next = newSeat;
                newSeat->prev = newSeat;
            } else {
                newSeat->prev = tail;
                newSeat->next = head;
                tail->next = newSeat;
                head->prev = newSeat;
                tail = newSeat;
            }
        }
        rows[i] = head;
    }
}

void displaySeats() {
    for (int i = 0; i < ROWS; i++) {
        cout << "Row " << i + 1 << ": ";
        Seat* temp = rows[i];
        if (!temp) continue;
        do {
            cout << (temp->booked ? "[X] " : "[ ] ");
            temp = temp->next;
        } while (temp != rows[i]);
        cout << endl;
    }
}

void bookSeat(int row, int seatNo) {
    if (row < 1 || row > ROWS || seatNo < 1 || seatNo > SEATS) {
        cout << "Invalid input.\n";
        return;
    }
    Seat* temp = rows[row - 1];
    for (int i = 1; i < seatNo; i++) {
        temp = temp->next;
    }
    if (temp->booked) {
        cout << "Seat already booked.\n";
    } else {
        temp->booked = true;
        cout << "Seat booked successfully.\n";
    }
}

void cancelSeat(int row, int seatNo) {
    if (row < 1 || row > ROWS || seatNo < 1 || seatNo > SEATS) {
        cout << "Invalid input.\n";
        return;
    }
    Seat* temp = rows[row - 1];
    for (int i = 1; i < seatNo; i++) {
        temp = temp->next;
    }
    if (!temp->booked) {
        cout << "Seat is already free.\n";
    } else {
        temp->booked = false;
        cout << "Booking cancelled.\n";
    }
}

int main() {
    initializeSeats();

    // Optional: Randomly book some seats
    bookSeat(1, 2);
    bookSeat(3, 5);
    bookSeat(5, 1);

    int choice, row, seat;
    do {
        cout << "\n--- Cinemax Ticket Booking ---\n";
        cout << "1. Display available seats\n";
        cout << "2. Book a seat\n";
        cout << "3. Cancel booking\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                displaySeats();
                break;
            case 2:
                cout << "Enter row (1-10) and seat number (1-7): ";
                cin >> row >> seat;
                bookSeat(row, seat);
                break;
            case 3:
                cout << "Enter row (1-10) and seat number (1-7): ";
                cin >> row >> seat;
                cancelSeat(row, seat);
                break;
            case 4:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice.\n";
        }
    } while (choice != 4);

    return 0;
}
