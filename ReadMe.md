### 最大子段和

判断前一个子序列的值是否为负，子序列和的表更新如下：
	sumSubArr[1] = sumSubArr[i-1] + arr[i] if sunSubArr[i-1] > 0 else arr[i]

### 最大上升子序列和
**注意**：子序列可以不连续。 将当前节点与前面每一个子序列和的大小进行比较，更新最大值

	for i in range(j): 
		if Arr[j] > Arr[i]:
			maxn = max(maxn, sumSubArr[j]+Arr[i])
	sumSubArr[i] = maxn
			 