use std::io::{self, BufRead, Write};
macro_rules! input {
() => (std::io::stdin().lock().lines().next().map_or(Err(io::Error::new(io::ErrorKind::UnexpectedEof, "Input BufRead reached EOF before".to_string())), |line| line).unwrap());
    ($($arg:tt)*) => ({ std::io::stdout().write_fmt(format_args!($($arg)*)).unwrap(); std::io::stdout().flush().unwrap(); input!() });
}

pub fn reverse(x: i32) -> i32 {
    let final_val = match (x * if x.is_negative() { -1 } else { 1 })
        .to_string()
        .chars()
        .rev()
        .collect::<String>()
        .parse::<i32>()
    {
        Ok(val) => val,
        Err(_) => 0,
    };
    final_val * if x.is_negative() { -1 } else { 1 }
}

fn main() {
    let input = input!();
    println!("{:?}", reverse(input.parse().unwrap()));
}
