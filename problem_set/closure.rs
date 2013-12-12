/*
  Believe it or not, closure ("|blah|") will bring you a pointer to a function, just like in C.
  Write a function that uses the closure to print:
    six = 6
  (hint: you really just need one line of code)
*/

fn main() {
  let closure = |num| println(fmt!("six = %?", num));
  call_closure(closure);
}

/*
  Answer:
    fn call_closure(b: &fn(int)) { b(6); }
    fn main() {
      let closure = |num| println(fmt!("six = %?", num));
      call_closure(closure);
    }
*/
