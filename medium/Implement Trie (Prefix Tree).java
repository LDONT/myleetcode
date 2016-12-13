class TrieNode {       //实现字典树
    // Initialize your data structure here.
    public TrieNode[] children = new TrieNode[26];
    public boolean isin = false;
    public TrieNode() {}
}

public class Trie {
    private TrieNode root;
    private TrieNode ret;
    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        ret = root;
        for (int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if (ret.children[c-'a'] == null){
                ret.children[c-'a'] = new TrieNode();
            }
            ret = ret.children[c-'a'];
        }
        ret.isin = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        ret = root;
        for (int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if (ret.children[c-'a'] == null) return false;
            ret = ret.children[c-'a'];
        }
        return ret.isin;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {    //只判断字符串是否是子字符串，不一定是word
        ret = root;
        for (int i = 0; i < prefix.length(); i++){
            char c = prefix.charAt(i);
            if (ret.children[c-'a'] == null) return false;
            ret = ret.children[c-'a'];
        }
        return true;
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");