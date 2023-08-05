use std::io::{self, BufRead, Write};
macro_rules! input {
() => (std::io::stdin().lock().lines().next().map_or(Err(io::Error::new(io::ErrorKind::UnexpectedEof, "Input BufRead reached EOF before".to_string())), |line| line).unwrap());
    ($($arg:tt)*) => ({ std::io::stdout().write_fmt(format_args!($($arg)*)).unwrap(); std::io::stdout().flush().unwrap(); input!() });
}

pub fn convert(s: String, num_rows: i32) -> String {
    let mut zigzags: Vec<_> = (0..num_rows)
        .chain((1..num_rows - 1).rev())
        .cycle()
        .zip(s.chars())
        .collect();
    zigzags.sort_by_key(|&(row, _)| row);
    zigzags.into_iter().map(|(_, c)| c).collect()
}

fn main() {
    let input = input!();
    let rows_str = input!();
    let rows = rows_str.parse::<i32>().unwrap();
    println!("{}", convert(input, rows));
}
