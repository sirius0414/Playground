表格第一列是分组，从第3列开始每一列代表一种细胞比例；①通过聚类热图展示组1、2、3、4的细胞亚群分布特点；
②希望能够通过细胞亚群的不同，区分出这四组患者，特别是让组2和组3能被区分开。

黄的是T细胞，蓝的是B细胞，绿的是固有免疫细胞

* T细胞：Ratio可以都删掉，Parent也可以都删掉，
* Th1, Th2, Th17之间有弱关联；
* Tf1, Tf2, Tf17之间有弱关联；
* TUVW四列加起来约等于1
* 对于绿色的：Non, Inter, Classic 再加一项约等于1； 两个Class， 两个Inter， 两个Non之间也可能有关联；
```{r}