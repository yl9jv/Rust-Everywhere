/*Q3: Loop the Loop
  In Rust, loops are a little bit different. it looks something like this:
    for blah in blahhh.iter() {
      //do something with "blah";
    }
  Now suppose you were given a vector like this:
    let pigs = ~[~"pig1", ~"pig2", ~"pig_little"];
  How would you print them out in order (note that the strings are specified by pointers)?
*/

fn main() {
  let pigs = ~[~"pig1", ~"pig2", ~"pig_little"];
  for pig in pigs.iter() {
    println(*pig);
  }
}
