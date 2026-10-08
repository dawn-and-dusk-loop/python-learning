sales=[326.5,512.0,289.8,467.2,198.0,556.4,342.1]
total=0
for s in sales:
    total=total+s
print(f"本周总营业额:{total}")
print(f"日均营业额:{total/len(sales):.2f}")
sorted_sales=sorted(sales)
print(f"最高营业额:{sorted_sales[len(sorted_sales)-1]}")
print(f"最低营业额:{sorted_sales[0]}")