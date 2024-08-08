# s-g滤波
参考大佬TiRan_Yang

* 滤波窗口宽度
>n=2m+1

* 测点
>X<sub>i</sub>=(-m,...,m)

* 拟合公式
 >y=a0+a1*x+...+a(k-1)*x<sup>(k-1)</sup>

基于最小二乘法的多项式平滑，也叫卷积平滑
首先，多项式拟合，取宽度为n个点，作为集合X，用X<sub>m-1</sub>,...,X<sub>m+1</sub>,代替X<sub>m</sub>
即拟合公式。

得到n个方程(为什么是n个呢，采用最近邻补齐，__python自带__)，联立，用矩阵表示：
>Y<sub>(2m+1)* 1</sub>=X<sub>(2m+1) * k</sub> * A<sub>k * 1</sub>+E<sub>(2m+1)*1</sub>

用最小二乘法解得：
> A = (X<sup>T</sup> * X)<sup>-1</sup> * X<sup>T</sup> * Y

Y的滤波值：
> Y = X * A =X * (X<sup>T</sup> * X)<sup>-1</sup> * X<sup>T</sup> * Y =B * Y

可得：
>B=X * (X<sup>T</sup> * X)<sup>-1</sup> * X<sup>T</sup> 
