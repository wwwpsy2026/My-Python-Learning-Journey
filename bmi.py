# 根据身高体重计算BMI指数
def calculate_bmi(weight, height):
    # 身高单位转换：厘米转米
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif 18.5 <= bmi < 24:
        return "正常"
    elif 24 <= bmi < 28:
        return "超重"
    else:
        return "肥胖"

# 主程序
print("--- BMI指数计算器 ---")
try:
    w = float(input("请输入您的体重(kg)："))
    h = float(input("请输入您的身高(cm)："))
    
    my_bmi = calculate_bmi(w, h)
    category = get_bmi_category(my_bmi)
    
    print(f"\n您的BMI指数为：{my_bmi:.2f}")
    print(f"您的体型分类为：{category}")
except ValueError:
    print("输入错误，请输入数字！")