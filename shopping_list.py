# Do not remove these imports. You may add others if you wish.
import sys

# Args:
#   products: a list of lists, each list representing a single item and
#             what department it is in (ex: [["Cheese", "Dairy"], ...])
#   shopping_list: a list representing the unsorted shopping list
# Returns:
#   An int, how many department visits are saved by optimal shopping.
def ordered_shopping(products, shopping_list):
  # Your code goes here
# traverse through array
# add 1st index of each array within the array to the items
# add 2nd index of each array within the array to the departments
# count total number of arrays within products - this is the max # of trips
# count total # of departments - this is the # of optimal trips
# subtract max - optimal to get difference
    items = []
    dept = []

    for l in products:
        print(l)
        for i in l:
            print(i)
            items.append(i[0])
            dept.append(i[1])
        minDept = set(dept)
      
        return len(items) - len(minDept)

    return 0

# DO NOT MODIFY BELOW THIS LINE
def main():
  break_line = False
  products = []
  shopping_list = []

  for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
      break_line = True
      continue

    if break_line:
      shopping_list.append(line)
    else:
      products.append(line.split(","))

  print(ordered_shopping(products, shopping_list))

main()