class Solution {
public:
    int countDigits(int num) {

        int m = num;
        int count = 0;
        int rem = 0;

        while(num != 0)
        {
            rem = num % 10;
            if (m % rem == 0)
            {
                count += 1;
            }
            num = num / 10;
        }
        
        return  count;
    }
};