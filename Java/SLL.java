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

    //Insert node - insert new node to the end
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

    // Delete Node by value
    public void deleteNode(SLL mySLL, int val){

        //set current node as a runner pointer    
        Node runner = head, prev = null;
        
        //if value we are looking for is at head of SLL
        if (runner != null && runner.value == val ){
            System.out.println("Found node at head of SLL");
        }

        //traverse to SLL and look for a given value
        while (runner != null && runner.value != val){
            prev = runner;
            runner = runner.next;
        }

        //if value we're looking for is at runner, which mean isn't null
        //remove current node (at runner position)
        if (runner != null){
            prev.next = runner.next;
            System.out.println(val+" is found and deleted!");
        }
        //given value is not exist in SLL
        if (runner == null){
            System.out.println(val+ " isn't found in SLL");
        }

    }

    // Delete Node by position
    public void deleteNodePosition(SLL mySLL, int idx){
        
        //set current node as a runner pointer
        Node runner = mySLL.head, prev = null;

        // if idx = 0, then head node itself is to be deleted.
        if (idx == 0 && runner != null){
            //change head
            mySLL.head = runner.next;
            System.out.println("Deleted node at head");
            //return mySLL;
        }

        //if idx is greater than 0, but less than size of SLL

        int counter = 0;

        while (runner != null) {
            if (counter == idx){
                prev.next = runner.next;
                break;
            }else {
                //if current runner is not the idx we are looking for, then continue to next node
                prev = runner;
                runner = runner.next;
                counter ++; //increment counter
            }
        }

        //idx is greater than size of SLL
        //runner should be at null

        if (runner == null){
            System.out.println("Position element not found");
        }

        //return mySLL;
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

        // myList.deleteNode(myList, 2);
        myList.deleteNodePosition(myList, 2);
        myList.PrintSLL();
    }

}