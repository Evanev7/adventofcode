#![allow(unused)]
#[derive(Debug, Clone)]
struct Equation {
    target_value: u64,
    terms: Vec<u64>,
}

// Returns a1a2a3b1b2b3
fn concat(a: u64, b: u64) -> u64 {
    a * 10u64.pow(b.ilog10() + 1) + b
}

fn main() {
    // Setup
    let equations = DATA
        .trim()
        .split("\n")
        .map(|e| {
            // .find() assumes ASCII. Which this is, but it's "bad practice".
            let colon_position = e.chars().position(|c| c == ':').unwrap();
            Equation {
                target_value: e[..colon_position].parse::<u64>().unwrap(),
                terms: e[(colon_position + 2)..]
                    .split(" ")
                    .map(str::parse::<u64>)
                    .map(Result::unwrap)
                    .collect::<Vec<_>>(),
            }
        })
        .collect::<Vec<Equation>>();

    // Loop version
    let now = std::time::Instant::now();
    let mut total: u64 = 0;
    for eqn in equations.clone() {
        for mut i in 0..(3u64.pow(eqn.terms.len() as u32 - 1)) {
            //dbg!(&eqn);
            let mut buff = eqn.terms.clone().into_iter().rev().collect::<Vec<_>>();
            let mut accum = buff.pop().unwrap();
            while !buff.is_empty() {
                match i % 3 {
                    0 => accum += buff.pop().unwrap(),
                    1 => accum *= buff.pop().unwrap(),
                    2 => {
                        accum = concat(accum, buff.pop().unwrap());
                    }
                    _ => unreachable!(),
                }
                //dbg!(&accum);
                i /= 3;
                if accum > eqn.target_value {
                    break;
                }
            }
            if accum == eqn.target_value {
                total += accum;
                break;
            }
        }
    }
    dbg!(now.elapsed());
    dbg!(total);

    // Malachy time
    let now = std::time::Instant::now();
    total = 0;
    for eqn in equations {
        if count_possibilities(eqn.target_value, eqn.terms, 0, 0) > 0 {
            total += eqn.target_value;
        }
    }
    dbg!(now.elapsed());
    dbg!(total);
}

fn count_possibilities(target: u64, ls: Vec<u64>, total: u64, i: usize) -> usize {
    if i >= ls.len() {
        if total == target {
            return 1;
        } else {
            return 0;
        }
    }
    if total > target {
        return 0;
    }
    count_possibilities(target, ls.clone(), total + ls[i], i + 1)
        + count_possibilities(target, ls.clone(), total * ls[i], i + 1)
        + count_possibilities(target, ls.clone(), concat(total, ls[i]), i + 1)
}

const DATA: &str = include_str!("../007.txt");
