#include<iostream>
# define max 10
using namespace std;

class Pizza
{
      int front,rear;
      int orders[max];
      public:
      Pizza()
      {
            front=rear=-1;
      }
      bool add(int data);
      void serve();
      void display();
};

bool Pizza::add(int id)
{
      if(front==-1)
      {
            front=rear=0;
            orders[rear]=id;
            return true;
      }
      else
      {
            int pos=(rear+1)%max;
            if(pos==front)
            {
                  cout<<"Orders are full"<<endl;
                  return false;
            }
            else
            {
                  rear=pos;
                  orders[rear]=id;
                  return true;
            }
      }
}
void Pizza::serve()
{
      if(front==-1)
      {
            cout<<"No orders to serve"<<endl;
            return;
      }
      else
      {
          cout<<"Order no "<<orders[front]<<" has been served"<<endl;
            if(rear==front)
            {
                  front=rear=-1;
            }
            else
            {
                  front=(front+1)%max;
            }
      }
}
void Pizza::display()
{
      if(front==-1)
      {
            cout<<"No orders to display"<<endl;
            return;
      }
      else
      {
            int i=0;
            cout<<"Order ID's:-"<<endl;
            for(i=front;i!=rear;i=((i+1)%max))
            {
                  cout<<orders[i]<<" "<<endl;
            }
            cout<<orders[rear];
      }
}
int main()
{
      int ch;
      int id=0;
      Pizza p;
      do
      {
            cout<<"\nEnter your choice:-\n1)Add order\n2)Serve order\n3)Display orders\n4)Exit"<<endl;
            cin>>ch;
            switch(ch)
            {
            case 1:
            id++;
            if(p.add(id))
            {
                  cout<<"Order id "<<id<<" has been added"<<endl;
            }
            else
            {
                  id--;
            }
            break;

            case 2:
            p.serve();
            break;

            case 3:
            p.display();
            break;

            case 4:
            exit(0);
            break;

            default:
            cout<<"Wrong choice"<<endl;
      }
}while(true);
}
