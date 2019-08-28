//https://codeforces.com/contest/158/problem/B

#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    
    int n,one=0,two=0,three=0,four=0,result=0;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
    	cin>>arr[i];
    	if(arr[i]==1) one++;
    	else if(arr[i]==2) two++;
    	else if(arr[i]==3) three++;
    	else if(arr[i]==4) four++;
    }
    
    result=four+three;
    one=max(0,one-three);
    result+=(two/2);
    if(two%2){
    	one=max(0,one-2);
    	result++;
    }
    result+=one/4;
    if(one%4) result++;
    cout<<result<<endl;


    return 0;
}