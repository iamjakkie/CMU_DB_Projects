use crate::trie::Trie;

mod trie;
mod tree_viz;

fn main() {
    let mut trie = Trie::new();
    println!("Depth: {}", trie.depth());
    trie.insert("tea");
    println!("Depth: {}", trie.depth());
    trie.insert("test");
    println!("Entries: {}", trie.count_entries(&trie.root));
    println!("Depth: {}", trie.depth());
    trie.print(&trie.root);
    println!("{:?}", trie.get_level(3));
    // println!("{}", trie);
}
