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
}

pub struct Trie {
    pub root: Node,
}

impl Trie {
    pub fn new() -> Self{
        Trie { root: Node::new() }
    }
    pub fn insert(&mut self, s: &str) {}
}

self.key_char = key_char
self._is_end = False
self._children = {}