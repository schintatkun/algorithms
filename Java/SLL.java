class SLL {
    
    //Head of linked list
    Node head;
               
    // Node class
    // It is an inner class, which made static in order to allow main() can access it
    static class Node {
        int value;
        Node next;
            
        //Constructor to create a new node
        Node(int val){
            value = val;
            next = null;
        }
    }

    //function that will get all of value of Linked List

    public void PrintSLL(){

        //set pointer "runner" to head of linked list
        Node runner = head;
        while (runner != null){
            System.out.print(runner.value+" ");
            runner = runner.next;
        }
    }

    //AddFront - add new node to the front of SLL

    public void AddFront(int val){
        Node new_node = new Node(val);
        new_node.next = head;
        head = new_node;
    }

    //Insert node - insert new node to the back
    public void insertNode(SLL mySLL, int val){

        //create new node from input value
        Node new_node = new Node(val);
        new_node.next = null;

        //check if SLL is empty, then make a new node as head of SLL
        if (mySLL.head == null){
            mySLL.head = new_node;
        }
        else{
            //set pointer "runner" to traverse whole SLL till last node
            Node runner = mySLL.head;
            while (runner.next != null){
                runner = runner.next;
            }
            runner.next = new_node;
        }

    }

    public static void main(String[] args){

        // create empty list as myList
        SLL myList = new SLL();
        

        // create three new nodes
        myList.head = new Node(1);
        Node secondNode = new Node(2);
        Node thirdNode = new Node(3);


        //point 1st node to 2nd node
        myList.head.next = secondNode;


        //point 2nd node to 3rd node
        secondNode.next = thirdNode;

        //add new node by calling Addfront function
        myList.AddFront(55);

        //insert new node
        myList.insertNode(myList, 7);

        // print all value in Linked List
        myList.PrintSLL();
    }

}