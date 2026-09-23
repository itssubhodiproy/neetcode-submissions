class Solution {
public:
    bool isLHS(char c){
        return (c=='('||c=='{'||c=='[');
    }
    bool isSame(char c, char d){
        if (c=='(' && d==')') return true;
        if (c=='{' && d=='}') return true;
        if (c=='['&& d==']') return true;
        return false;
    }
    bool isValid(string s) {
        stack<char>st;

        for(auto it:s){
            if(isLHS(it)) st.push(it);
            else {
                if(!st.empty() && isSame(st.top(), it)) st.pop();
                else return false;
            }
        }
        return st.empty();
    }
};
