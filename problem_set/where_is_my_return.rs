/*
Q2: Where Is My Return?!
In Q1, you have learned how expression works, or at least you think you do. In Rust, basically everything that's not a declaration (declarations are let for variables; fn for functions; and any top-level named items such as traits, enum types, and static items) is an expression, including function bodies themselves! Therefore, there is usually no need for a return statement, because the result of the expression is used as the return value. Isn't this crazy...
*/

fn main() {
  if is_four(4) {
    println("It is four!");
  }
}   

fn is_four(x: int) -> bool {
   return (x == 4);
}

/*
Could you help me get rid of the keyword "return"? It just really bothers me...
*/
