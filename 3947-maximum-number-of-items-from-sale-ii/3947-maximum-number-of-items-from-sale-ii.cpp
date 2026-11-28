class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        int mini = INT_MAX;
        int maxi = 0;
        for (auto i : items) {
            maxi = max(maxi, i[0]);
            mini = min(mini, i[1]);
        }
        vector<int> freq(maxi + 1, 0);
        for (auto i : items) {
            freq[i[0]]++;
        }
        vector<int> g(maxi + 1, 0);
        for (int i = 1; i <= maxi; i++) {
            if (freq[i] > 0) {
                for (int j = i; j <= maxi; j += i) {
                    g[i] += freq[j];
                }
            }
        }
        vector<pair<long long,long long>> t;
        for (auto i : items) {
            int c = i[1];
            int h = g[i[0]]-1;
            if(h>0&&c<2*mini){
                t.push_back({c,h});
            }
        }
        sort(t.begin(),t.end());
        long long ans=0;
        for(auto i:t){
            int c=i.first;
            int h=i.second;
            if(budget>=c){
                int temp=min(h,budget/c);
                budget-=temp*c;
                ans+=temp*2;
            }
            if(budget==0){
                break;
            }
        }
        ans+=budget/mini;
        return ans;
    }
};