use crate::trie::Trie;

mod trie;
mod tree_viz;

fn main() {
    let mut trie = Trie::new();
    trie.insert("tea");
    trie.insert("test");

    println!("{}", trie);
}
