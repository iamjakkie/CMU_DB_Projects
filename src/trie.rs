use std::collections::VecDeque;
use std::fmt::{Debug, Display, Formatter};
use std::cmp;

enum Side {
    Left,
    Right,
    Up,
}

enum DisplayElement {
    TrunkSpace,
    SpaceLeft,
    SpaceRight,
    SpaceSpace,
    Root,
}

impl DisplayElement {
    fn string(&self) -> String {
        match *self {
            DisplayElement::TrunkSpace => "    │   ".to_string(),
            DisplayElement::SpaceRight => "    ┌───".to_string(),
            DisplayElement::SpaceLeft => "    └───".to_string(),
            DisplayElement::SpaceSpace => "        ".to_string(),
            DisplayElement::Root => "├──".to_string(),
        }
    }
}

#[derive(Default)]
pub struct Node {
    pub key: Option<char>,
    pub is_end: bool,
    pub children: Vec<Node>,
    pub value: Option<String>
}

impl Node {
    pub fn new() -> Self {
        Node {
            ..Default::default()
        }
    }
    pub fn with_key(c: char) -> Self {
        Node {
            key: Some(c),
            ..Default::default()
        }
    }
}

impl PartialEq<Self> for Node {
    fn eq(&self, other: &Self) -> bool {
        self.key == other.key
    }
}

pub struct Trie {
    pub root: Node,
    pub depth: usize,
}

impl Default for Trie{
    fn default() -> Self {
        Self {
            root: Node::new(),
            depth: 0,
        }
    }
}

impl Trie {

    pub fn new() -> Self{
        Trie {
            root: Node::new(),
            ..Default::default()
    }
    }
    pub fn insert(&mut self, s: &str) {
        if self.depth < s.len() { self.depth = s.len() }
        let mut cur = &mut self.root;
        for c in s.chars() {
            match cur.children.binary_search_by(|f| f.key.cmp(&Some(c))) {
                Ok(i) => {
                    cur = &mut cur.children[i];
                },
                Err(i) => {
                    cur.children.insert(i, Node::with_key(c));
                    cur = &mut cur.children[i];
                }
            }
        }
        cur.value.replace(s.to_string());
    }

    pub fn count_entries(&self, node: &Node) -> i32{
        if *node == self.root {
            0 + node.children.iter().map(|x| self.count_entries(x)).sum::<i32>()
        } else {
            1 + node.children.iter().map(|x| self.count_entries(x)).sum::<i32>()
        }
    }

    pub fn print(&self, node: &Node) {
        if *node == self.root {
            print!("###");
        } else {
            println!("{}", node.key.unwrap());
            let _ = node.children.iter().map(|x| self.print(x));
        }
    }

    pub fn depth(&self) -> usize{
        self.depth
    }

    //
    // pub fn bfs(&self) {
    //     let mut q = VecDeque::new();
    //     q.push_back()
    // }

    pub fn get_level(&self, level: usize) -> Vec<Node>{
        if level == 0 { vec![self.root]}
        let mut cur_level: usize = 1;
        let mut cur_level_keys = self.root.children;
        let mut next_level_keys:Vec<Node> = Vec::new();
        while cur_level < level {
            next_level_keys.clear();
            cur_level_keys.iter().map(|x| next_level_keys.append(children));
            cur_level_keys = next_level_keys;
            cur_level +=1;
        }
        cur_level_keys
    }

    // pub fn get_keys_for_level(&self, level: usize) {
    //     let mut keys: Vec<Node> = Vec::new();
    //     match level {
    //         0 => { keys.append(*self.root) },
    //         1 => {
    //             self.root.children.iter().map(|x| keys.append(x))
    //         },
    //         _ => {
    //
    //         }
    //     }
    // }


    pub fn printer(&self) -> Vec<Vec<Node>> {
        let depth = self.depth();

        let levels =

    }
}
//
// impl Display for Trie {
//     // fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
//     //     let mut q: VecDeque<&Node> = VecDeque::new();
//     //     let root = &self.root;
//     //     q.push_back(root);
//     //
//     //     while !q.is_empty() {
//     //         for _ in 0..q.len() {
//     //             if let Some(node) = q.pop_front() {
//     //                 for c in node.children.iter() {
//     //                     let r = write!(f, "{}", c.key.unwrap());
//     //                     if r.is_err() {
//     //                         return r;
//     //                     }
//     //                     if c.children.len() > 0 {
//     //                         q.push_back(&c);
//     //                     }
//     //                 }
//     //             }
//     //         }
//     //         if q.len() > 0 {
//     //             let r = writeln!(f);
//     //             if r.is_err() {
//     //                 return r;
//     //             }
//     //         }
//     //     }
//     //     Ok(())
//     // }
//
//
//     fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
//         let mut v:Vec<DisplayElement> = Vec::new();
//         self.display(self.root, Side::Up, &mut v, f);
//     }
// }
