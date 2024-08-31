import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu mẫu
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Vẽ đồ thị

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Đồ thị hàm sin')
plt.show()