class Solution {
public:
    string convert(string s) {
        string result = "";
        for(char c : s) {
            if((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                result += c;
            }
            else if(c >= 'A' && c <= 'Z') {
                result += c + 32;
            }
        }
        return result;
    }
    bool isPalindrome(string s) {
        string newS = convert(s);
        for(int i=0;i<(int)newS.size()/2;i++){
            if (newS[i]==newS[newS.size()-1-i]) continue;
            else return false;
        }
        return true;
    }
};
