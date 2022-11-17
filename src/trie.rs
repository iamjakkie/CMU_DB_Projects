use std::collections::VecDeque;
use std::fmt::{Display, Formatter};

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

pub struct Trie {
    pub root: Node,
}

impl Trie {
    pub fn new() -> Self{
        Trie { root: Node::new() }
    }
    pub fn insert(&mut self, s: &str) {
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
}

impl Display for Trie {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        let mut q: VecDeque<&Node> = VecDeque::new();
        let root = &self.root;
        q.push_back(root);

        while !q.is_empty() {
            for _ in 0..q.len() {
                if let Some(node) = q.pop_front() {
                    for c in node.children.iter() {
                        let r = write!(f, "{}", c.key.unwrap());
                        if r.is_err() {
                            return r;
                        }
                        if c.children.len() > 0 {
                            q.push_back(&c);
                        }
                    }
                }
            }
            if q.len() > 0 {
                let r = writeln!(f);
                if r.is_err() {
                    return r;
                }
            }
        }
        Ok(())
    }
}