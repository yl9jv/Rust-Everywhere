fn main() {
  let item = "muffin";
  let price =
    if item == "salad" {
        3.50
    } else if item == "muffin" {
        2.25
    } else {
        2.00
    };
  println(fmt!("%?", price));
}





