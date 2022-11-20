use crate::trie::Trie;

mod trie;
mod tree_viz;

fn main() {
    let mut trie = Trie::new();
    trie.insert("tea");
    trie.insert("test");
    println!("Entries: {}", trie.count_entries(&trie.root))
    // println!("{}", trie);
}
