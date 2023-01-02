#include<iostream>
using namespace std;

class Queue
{
    int front = -1;
    int  rear = -1;
    string arr[5];

    public :

    void get_order();
    void serve_order();
    void Display();


};

void Queue :: get_order()
{
    string val;
    if(front == -1 & rear == -1)
    {
        
        cout<<"Enter your name : ";
        cin >> val;
        front = 0;
        rear = 0;
        arr[front]=val;

    }
    else if((rear+1)%5 == front)
    {
        cout << "Full ....."<<endl;
    }
    else
    {
        cout << "Name : ";
        cin >> val;
        rear = (rear+1)%5;
        arr[rear] = val;
    }
}

void Queue :: serve_order()
{
    if(front == -1 && rear == -1)
    {
        cout << "no orders placed..... "<<endl;
    }
    else 
    {
        cout << "Order of " << arr[front] << " served..............."<<endl;
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            
            front = (front+1)%5;
        }
    }
}

void Queue :: Display()
{
    for (int i=front ; i != rear ; i = (i+1)%5)
    {
        cout << arr[i] <<endl;
    }
    cout << arr[rear] <<endl;
}

int main()
{
    Queue obj;

    int choice = 1;
    while (choice != 4) {
        cout << "Press 1 to Order" << endl;
        cout << "Press 2 to Get Order" << endl;
        cout << "Press 3 to Display List of Orders" << endl;
        cout << "Press 4 to Exit" << endl;
        cin >> choice;

        if (choice == 1) {
            obj.get_order();
        } else if (choice == 2) {
            obj.serve_order();
        } else if (choice == 3) {
            obj.Display();
        }
    }
    return 0;
}