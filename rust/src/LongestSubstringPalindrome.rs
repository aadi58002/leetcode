use std::io::{self, Write, BufRead};
macro_rules! input {
() => (std::io::stdin().lock().lines().next().map_or(Err(io::Error::new(io::ErrorKind::UnexpectedEof, "Input BufRead reached EOF before".to_string())), |line| line).unwrap());
    ($($arg:tt)*) => ({ std::io::stdout().write_fmt(format_args!($($arg)*)).unwrap(); std::io::stdout().flush().unwrap(); input!() });
}

// Personal attempt Unoptimized
// fn check_par(s: &[char])->bool{
//     let mut is_par = true;
//     for index in 0..s.len(){
//         if index < s.len()/2{
//             if s[index] != s[s.len()-index-1]{
//                 is_par = false;
//                 break;
//             } 
//         }else{
//             break;
//         }
//     }
//     is_par
// }

// fn main() {
//     let input = input!();
//     if input.len()==0{
//         println!("0");
//     }
//     let mut max = (0,0);
//     let inputs: Vec<char> = input.chars().collect();
//     for start in 0..inputs.len(){
//         for end in ((start+1)..inputs.len()).rev(){
//             if check_par(&inputs[start..=end]){
//                 if (end-start) > max.1-max.0{
//                     max=(start,end);
//                 }
//             }
//         }
//     }
//     let mut out_str = String::new();
//     for ele in max.0..=max.1{
//         out_str.push(inputs[ele]);
//     }
//     println!("{}",out_str);
// }

// Better and shorter version of above code
// fn pali(s: String)->String{
//     let mut window_len = s.len();
//     while window_len >0{
//         match s.as_bytes().windows(window_len).find(|val| val.iter().eq(val.iter().rev())){
//             Some(slice) => return String::from_utf8(slice.to_vec()).unwrap_or("".to_string()),
//             None => window_len-=1,
//         }
//     }
//     "".to_string()
// }

fn main(){
    let input = input!();
    println!("{}",pali(input));
}


