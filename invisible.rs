/*
  As you can see, our module hierarchy is now two modules deep. There is the crate root, which contains your main() function, and the module farm. The module farm also contains a function and a module white_animals, which futher contains two functions.
  However, somehow the following code does not compile due to the visibility problem. How would you change the code?
*/

mod farm {
  fn pig() { println("Heng heng"); }
  mod white_animals {
    fn cow() { println("Mooo"); }
    fn fox() { println("Ahh..."); }
  }
}

fn main() {
  ::farm::pig();
  ::farm::white_animals::cow();
}

/*Answer:

mod farm {
  pub fn pig() { println("Heng heng"); }
  mod white_animals {
    pub fn cow() { println("Mooo"); }
    pub fn fox() { println("Ahh..."); }
  }
}

fn main() {
  ::farm::pig();
  ::farm::white_animals::cow();
}
*/
