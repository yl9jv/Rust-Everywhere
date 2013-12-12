/*
  As you may know, variables in Rust are immutable by default! For example, if you want to change the value of x later, you definitely want to declare it in this way:
    let mut a = 10;
  Without the key word "mut", you will get a compile error! 
  Rust also formalizes the concept of object ownership to delegate management of an object's lifetime to either a variable or a task-local garbage collector. An object's owner is responsible for managing the lifetime of the object by calling the destructor, and the owner determines whether the object is mutable.
  Now given that the mutability is inherited, how do you modify the following code to make it compile?
  How would you add code to print out the value of y (hint: you need to dereference it first)?
*/

fn main() {
  struct Foo {x: int, y: ~int}
  let a = Foo {x: 5, y: ~10};
  a.x += 10;
  println(a.x.to_str());
}

/*
  Answer:
fn main() {
  struct Foo {x: int, y: ~int}
  let mut a = Foo {x: 5, y: ~10};
  a.x += 10;
  println(a.x.to_str());
  println((*a.y).to_str());
}
*/
