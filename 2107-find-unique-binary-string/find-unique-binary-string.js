/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    var str = '';
    for (var i = 0; i <= nums.length; i++) {
        str = i.toString(2);
        str = '0'.repeat(nums.length - str.length) + str;
        if (!nums.includes(str)) {
            return str;
        }
    }
};