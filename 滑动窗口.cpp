#include "滑动窗口.h"
#include<iostream>
#include<queue>
#include<vector>
using namespace std;
#define int long long
const int N=1e6+5;
int n,k;
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q1;
priority_queue<pair<int,int>>q2;
int a[N];
int MIN[N],MAX[N];
int cnt;
signed main(){
    cin>>n>>k;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        if(i<=k){
            q1.push(make_pair(a[i],i));
            q2.push(make_pair(a[i],i));
        }
    }
    MIN[cnt]=q1.top().first;
    MAX[cnt++]=q2.top().first;
    for(int i=k+1;i<=n;i++){
        q1.push(make_pair(a[i],i));
        q2.push(make_pair(a[i],i));
        while(q1.top().second<=i-k){
            q1.pop();
        }
        while(q2.top().second<=i-k){
            q2.pop();
        }
        MIN[cnt]=q1.top().first;
        MAX[cnt++]=q2.top().first;
    }
    for(int i=0;i<cnt;i++){
        cout<<MIN[i]<<" ";
    }
    cout<<endl;
    for(int i=0;i<cnt;i++){
        cout<<MAX[i]<<" ";
    }


    return 0;
}