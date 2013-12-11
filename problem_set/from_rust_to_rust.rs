/*
Q1: Make It More Concise!
Though it isn't apparent in all code, there is a fundamental difference between Rust's syntax and predecessors like C. Many constructs that are statements(with ";" at the end) in C are expressions(without ";" at the end) in Rust, allowing code to be more concise. For example, you might write a piece of code like this:
*/

fn main() {
  let item = "muffin";
  let price;
  if item == "salad" {
    price = 3.50;
  } else if item == "muffin" {
    price = 2.25;
  } else {
    price = 2.00;
  }
  println(fmt!("%?", price));
}

/*
How would you make the code above more concise? (for this question, you can only delete words, punctuations, or change indentations)
*/


