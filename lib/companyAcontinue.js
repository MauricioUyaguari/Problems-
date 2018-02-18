// 1. How to get the second smallest number from an array

function secondsmall(array){
  if(array.length < 2) {return null};

  function arrayMin(arr){
    let i = 0;
    let min = arr[0] ;
    while(i < arr.length -1 ){
      if(arr[0] < min){
        min = arr[0];
      }
      i += 1;
    }
  }


  let min1 = arrayMin(array);





}




// 2. IsAnagram




// 3. Count unique substring of length k



// 4. look through array to find pairs that sum to k
// 5. reverse words in a sentence
// 6. Implement a HashMap class
//Inheritance, Encapsulation, Polymorphism
// 7. Find the second largest number in the array
//8. Implement a BST with the methods `put(t)`, `contains(t)`
// and `in_order_traversal`. Get the failing unit tests to pass.
// 9. Given a sorted array which has been rotated k times , need to find k
// 10. Given a binary tree find the maximum sum from leaf to leaf?
// 11. reverse a string
// 12. Reverse a linked-list.
// 13. algorithm to traverse binary tree
//14. How to remove a node from a singly-linked list when only given the pointer to the node
// 15. how is hashtable implented
//16. Write a program which performs Newton's Method to approximate the root of an arbitrary function.
// 17. a question on dynamic programming and other on hashmap.
//18 . How would you print all possible permutations for the first n(input) natural numbers
