# 简易版贪吃蛇逻辑演示 (不需要额外的库)
# 运行后你会发现它像贪吃蛇一样，吃到食物变长

print("--- 简易贪吃蛇游戏 (文字版) ---")

# 初始蛇的长度
snake_length = 3
print(f"当前蛇的长度: {snake_length}")

# 模拟吃到食物
food_eaten = 0
while True:
    action = input("\n按回车键让蛇前进(输入 q 退出): ")
    if action == 'q':
        print("游戏结束！")
        break
    
    # 模拟遇到食物，长度增加
    snake_length += 1
    food_eaten += 1
    print(f"吃到了食物！当前蛇的长度: {snake_length}")
    
    # 课件中提到：触碰到边缘则游戏结束
    if snake_length >= 10:
        print("\n触碰到墙壁了，游戏结束！")时
        break