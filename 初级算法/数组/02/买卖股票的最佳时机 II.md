#  买卖股票的最佳时机 II

### C++解决：

思路：循环拿后一天的价格减去前一天的价格，如果相减大于0说明有利润。

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        for(int i=1;i<prices.size();i++){
            if(prices[i]-prices[i-1]>0){
                profit+=prices[i]-prices[i-1];
            }
        }
        return profit;
    }
};
```

### Python解决：

思路：和c++版本一样

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                profit+=prices[i]-prices[i-1]
        
        return profit
```

