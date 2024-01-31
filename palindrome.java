class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
        int temp = x;
        int newval = 0;
        while (temp != 0)
        {
            int r = temp%10;
            newval = newval * 10 +r;
            temp/=10;

        }
        return newval == x;
        
    }
}
