# iFly-Supp-Converter

Converts FSL NavData csv to iFly Supplemental NavData, including SIDs, STARs, APPs and SUPPs

## 数据释义
- Supp文件夹包含机场补充基础数据，包括机场速度限制及高度、过渡高度、过渡高度层信息。其中速度限制高度为推算值，可能存在偏差。Supp文件中亦可自行添加停机位坐标，但本数据包中不含该项。
- Star文件夹包含机场进场程序及进近程序，含trs结尾文件为过渡程序。
- Sid文件夹包含机场离场程序，含trs结尾文件为过渡程序。
- 进离场数据已包含当期所有Navigraph数据。程序各项内容与FSL数据对齐。

## 安装说明
1. 对于所有平台用户，请解压Sid、Star、Supp文件夹至`iFlyData/Permanent`下。

2. 对于P3D用户，请先将所有航路级别数据复制到`P3D路径\PMDG\Navdata`文件夹下，在P3D中加载任意PMDG机模，生成新的`ARPT_RWY.dat`文件，然后将文件复制到`iFlyData/Permanent`中并覆盖。

---
航路级别数据包含：
- `FMC_Ident.txt`
- `WPNAVAID.txt`
- `WPNAVAPT.txt`
- `WPNAVFIX.txt`
- `WPNAVGLS.txt`
- `WPNAVRTE.txt`
- `AIRPORTS.dat`