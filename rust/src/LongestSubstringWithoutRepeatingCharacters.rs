#[allow(unused_imports)]
use std::io::{self, Write, BufRead};
#[allow(unused_imports)]
macro_rules! input {
() => (std::io::stdin().lock().lines().next().map_or(Err(io::Error::new(io::ErrorKind::UnexpectedEof, "Input BufRead reached EOF before".to_string())), |line| line).unwrap());
    ($($arg:tt)*) => ({ std::io::stdout().write_fmt(format_args!($($arg)*)).unwrap(); std::io::stdout().flush().unwrap(); input!() });
}

fn main() {
    let input = input!();
    let (mut start,mut max) = (0,0);
    let mut char_pos = [0;128];
    for (pos,ch) in input.char_indices(){
        start = start.max(char_pos[ch as usize]);
        max = max.max(pos-start+1);
        char_pos[ch as usize] = pos+1;
    }
    println!("{max}");
}
