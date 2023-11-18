读取 excel  注意有隐藏列

只读文件 无法读取

```python
from openpyxl import load_workbook

# 加载Excel文件
wb = load_workbook(latest_file, read_only=True)

# 获取第一个sheet的列属性
sheet = wb.active
# 获取隐藏列的索引
hidden_columns = [col_idx for col_idx, col in enumerate(sheet.iter_cols(), start=1) if col[0].hidden]

# 通过设置usecols参数，只读取除了隐藏列以外的列
df = pd.read_excel(latest_file, sheet_name=None, skiprows=1, usecols=lambda x: x not in hidden_columns)

```
