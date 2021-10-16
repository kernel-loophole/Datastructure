#include<iostream>
using namespace std;

struct node {
	int  data;
	node* next;
};

class SinglyCircularLinkList {
private:
	node* head, * temp1, * temp;
public:
	SinglyCircularLinkList() {
		head = temp1 = temp = NULL;
	}

	node* create_node(char data) {
		node* link_node = new node();
		link_node->data = data;
		return link_node;
	}

	void add_node_to_tail(char data) {
		if (head == NULL) {
			head = create_node(data);
			head->next = head;
			return;
		}
		node* tail = get_tail();
		node* link_node = create_node(data);
		link_node->next = tail->next;
		tail->next = link_node;
	}

	node* get_tail() {
		node* iter = head;
		while (iter->next != head) {
			iter = iter->next;
		}
		return iter;
	}

	void print() {
		node* iter = head;
		if (head == NULL) return;
		do {
			cout << iter->data;
			iter = iter->next;
		} while (iter != head);
		cout << endl;

	}

	node* search_node(char key) {
		node* iter = head;
		while (iter->data != key) {
			iter = iter->next;
			if (iter == head) return NULL;
		}
		return iter;
	}

	void insert_at_value(char info, char key) {
		if (head == NULL) return;
		node* search = search_node(key);
		node* link_node = create_node(info);
		link_node->next = search->next;
		search->next = link_node;

	}

	node* get_prev(node* random_node) {
		node* temp_iter = head;
		if (random_node == NULL)
			return NULL;
		if (random_node == head)return head;
		while (temp_iter->next != random_node) {
			temp_iter = temp_iter->next;
		}
		return temp_iter;
	}

	void  delete_node(char key) {
		node* del_node = search_node(key);
		node* tail = get_tail();
		node* prev = get_prev(del_node);
		if (del_node == head) {
			tail->next = del_node->next;
			if (head->next == head)head = NULL;
			else head = head->next;

			delete del_node;
			del_node = NULL;
		}
		else {
			prev->next = del_node->next;
			delete del_node;
			del_node = NULL;
		}
	}

	void index() {

		int counter = 0;
		int mid;
		temp = head;
		temp1 = head;
		while (temp->next != head)
		{
			counter++;
	
			temp = temp->next;


		}
	//	cout << counter << endl;
		mid = counter / 2;
		int c = 0;
		//cout << mid << endl;
		temp = head;
		temp1 = head;
		while (temp->next!= head)
		{
        

			if (c == mid)
			{
 temp1=head;			
              for(int i=0;i<counter;i++)
              {
			  
				   	 //cout<<temp1->data<<endl;
             	temp1=temp->next;
			 temp->next=temp1;
					 cout<<temp1->data<<endl;             	
              temp=temp->next;
			 	temp1=temp1->next;
 }
			}
			c = c + 1;
			temp = temp->next;
		}
		do
		{
			cout<<"helo";
			cout<<temp1->data<<endl;
			temp1=temp1->next;
		}while(temp1!=head);
		

	

	}

};
int main() {

	SinglyCircularLinkList Ring;

	Ring.add_node_to_tail(0);
	Ring.add_node_to_tail(1);
	Ring.add_node_to_tail(2);
	Ring.add_node_to_tail(3);
	Ring.add_node_to_tail(4);
	Ring.add_node_to_tail(5);
	Ring.add_node_to_tail(6);
	Ring.add_node_to_tail(7);


	Ring.print();
	Ring.index();

}
