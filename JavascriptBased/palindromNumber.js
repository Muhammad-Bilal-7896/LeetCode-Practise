// /**
//  * @param {number} x
//  * @return {boolean}
//  */
function reverseString(str) {
    // Step 1. Use the split() method to return a new array
    var splitString = str.split(""); // var splitString = "hello".split("");
    // ["h", "e", "l", "l", "o"]
 
    // Step 2. Use the reverse() method to reverse the new created array
    var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
    // ["o", "l", "l", "e", "h"]
 
    // Step 3. Use the join() method to join all elements of the array into a string
    var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
    // "olleh"
    
    //Step 4. Return the reversed string
    return joinArray; // "olleh"
}

function isPalindrome(x) {
    x = x.toString();
    let length = x.length;
    let pehli_wali_array = x;
    let reverse_array = reverseString(x);
    for(let i=0;i<length;i++)
    {
        if(pehli_wali_array[i]!=reverse_array[i]){
            return false
        }
    }
    return true;

}
let result = isPalindrome(123321);
console.log("The result of the check is : ",result);