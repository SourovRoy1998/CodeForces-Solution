//https://codeforces.com/contest/27/problem/C

#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    
    int maxi=INT_MIN,mini=INT_MAX,i=0,j=0,k=0;

    int n,temp;
    cin>>n;
    vector<int> arr(n);
    for(int l=1;l<=n;l++){
        cin>>temp;
        if((temp>=maxi && temp>mini && i<j) || (temp<maxi && temp<=mini && i>j) || (temp<maxi && temp>mini)) { k=l; break;}
        if(temp>maxi){ i=l; maxi=temp; }
        if(temp<mini){ j=l; mini=temp; }
    }

    if(k==0) cout<<0<<endl;
    else cout<<3<<endl<<i<<" "<<j<<" "<<k<<endl;
    return 0;
}