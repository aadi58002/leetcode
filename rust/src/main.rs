use std::collections::{HashMap, HashSet};

pub fn word_pattern(pattern: String, s: String) -> bool {
    let words: Vec<&str> = s.split_whitespace().collect();
    let mut mapping = HashMap::new();
    if words.len() != pattern.len() {
        return false;
    };
    for (pat, ele) in words.iter().zip(pattern.chars()) {
        if mapping.contains_key(&ele) {
            if mapping.get(&ele).unwrap() != &pat {
                return false;
            }
        } else {
            mapping.insert(ele, pat);
        }
    }
    let mut uniq = HashSet::new();
    for ele in mapping.values() {
        if uniq.contains(&ele) {
            return false;
        } else {
            uniq.insert(ele);
        }
    }
    return true;
}

fn main(){}
