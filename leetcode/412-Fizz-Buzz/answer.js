/**
 * @param {number} n
 * @return {string[]}
 */

// https://leetcode.com/problems/fizz-buzz/

var fizzBuzz = function(n) {
    
    var ret_list = [];
    for (var i = 1; i <= n; ++i) {
        var res = "";
        if (i % 3 === 0) {
            res += "Fizz";
        }
        if (i % 5 === 0) {
            res += "Buzz";
        }
        if (res === "") {
            ret_list.push(String(i));
        } else {
            ret_list.push(res);
        }
    }
    return ret_list;
};