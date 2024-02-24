safe_rate =  4 #미 국채 10년 수익률
stock_rate = 16 #코스피 1년 수익률
short_rate = 100 # 단기 상품 수익률
safe_var = 10 #미 국채 10년물 분산
stock_var = 147 #코스피 1년 분산
short_var = 1000 #단기 상품 분산

def f(x, y, z):
    return (safe_rate*x**2 + stock_rate*y**2 +short_rate*z**2)/(safe_var*x**2 + stock_var*y**2 + short_var*z**2)

def gradient(x, y, z):
    grad_x = (2 * safe_rate * x * (stock_var * y**2 + short_var * z**2) - 2 * safe_var * x**2 * (stock_rate * y**2 + short_rate * z**2)) / (safe_var * x**2 + stock_var * y**2 + short_var * z**2)**2
    grad_y = (2 * stock_rate * y * (safe_var * x**2 + short_var * z**2) - 2 * stock_var * y**2 * (safe_rate * x**2 + short_rate * z**2)) / (safe_var * x**2 + stock_var * y**2 + short_var * z**2)**2
    grad_z = (2 * short_rate * z * (safe_var * x**2 + stock_var * y**2) - 2 * short_var * z**2 * (safe_rate * x**2 + stock_rate * y**2)) / (safe_var * x**2 + stock_var * y**2 + short_var * z**2)**2
    return [grad_x, grad_y, grad_z]

x, y, z = 33.3, 33.3, 33.3  # 초기값 설정: 총합이 100이 되도록 분배
learning_rate = 0.1

for i in range(100):
    # 기울기 계산
    grad = gradient(x, y, z)

    # 이동
    x = max(0.00001, min(x - learning_rate * grad[0], 99.99999))
    y = max(0.00001, min(y - learning_rate * grad[1], 99.99999))
    z = max(0.00001, min(z - learning_rate * grad[2], 99.99999))
    
    # x, y, z의 합이 100이 되도록 조정
    total = x + y + z
    x = x / total * 100
    y = y / total * 100
    z = z / total * 100

print(f"최소값: f({x}, {y}, {z})")