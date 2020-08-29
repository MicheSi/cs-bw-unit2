/*
  Args:
    products: an array of arrays, each array representing a single item and
              what department it is in (ex: [["Cheese", "Dairy"], ...])
    shopping_list: an array representing the unsorted shopping list 
  Returns:
    A Number, how many department visits are saved by optimal shopping.
*/
function ordered_shopping(products, shopping_list) {
    // Your code here.
    // traverse through array
    // add 1st index of each array within the array to the items
    // add 2nd index of each array within the array to the departments
    // count total number of arrays within products - this is the max # of trips
    // count total # of departments - this is the # of optimal trips
    // subtract max - optimal to get difference
    items = []
    departments = []
    diff = 0

    for (l in products) {
        l[0] += items

        if (l[1] != dept) {
            l[1] += dept
        }

        diff = length(items) - length(dept)
    }
    return diff;
  }
  
  // DO NOT MODIFY BELOW THIS LINE
  
  const readline = require('readline');
  
  const rl = readline.createInterface({
    input: process.stdin,
  });
  
  var products = [];
  var shopping_list = [];
  var break_line = false;
  
  rl.on('line', (line) => {
    line = line.trim();
    if (line == '') {
      break_line = true;
      return;
    }
    if (break_line) {
      shopping_list.push(line);
    } else {
      row = line.split(',')
      products.push(row);
    }
  }).on('close', () => {
    console.log(ordered_shopping(products, shopping_list));
  });
  