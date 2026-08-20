class Solution {
public:
    double _myPow(double x, int n)
    {
        if (n==0)
            return 1.0;

        double halfPow = myPow(x, n/2);
        double power = halfPow * halfPow;
        if (n%2==1)
            power *= x;

        return power;
    }

    double myPow(double x, int n)
    {        
        if (n < 0)
        {
            return 1.0 / _myPow(x, -n);
        }
        else
        {
            return _myPow(x, n);
        }
    }
};
