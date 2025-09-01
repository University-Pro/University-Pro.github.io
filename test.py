import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

class JoJoStandStats:
    def __init__(self, stats_names, stats_values, title="Stand Stats"):
        """
        初始化替身属性面板
        
        参数:
        stats_names: list, 6个属性的名称列表
        stats_values: list, 6个属性的数值列表(0-100)
        title: str, 图表标题
        """
        if len(stats_names) != 6 or len(stats_values) != 6:
            raise ValueError("需要提供6个属性名称和6个属性值")
        
        if any(v < 0 or v > 100 for v in stats_values):
            raise ValueError("属性值必须在0-100范围内")
            
        self.stats_names = stats_names
        self.stats_values = stats_values
        self.title = title
        
    def draw_radar_chart(self):
        """绘制六边形属性面板"""
        # 设置角度和标签位置
        angles = np.linspace(0, 2*np.pi, 6, endpoint=False).tolist()
        angles += angles[:1]  # 闭合图形
        
        # 归一化属性值 (0-100 到 0-1)
        values = [v/100 for v in self.stats_values]
        values += values[:1]  # 闭合图形
        
        # 创建图形和极坐标子图
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        
        # 绘制属性网格线
        for i in range(0, 101, 20):
            ax.plot(angles, [i/100] * 7, color='gray', linewidth=0.5, alpha=0.7)
        
        # 绘制属性区域
        ax.fill(angles, values, color='red', alpha=0.25)
        ax.plot(angles, values, color='red', linewidth=2)
        
        # 设置角度刻度和标签
        ax.set_theta_offset(np.pi/2)
        ax.set_theta_direction(-1)
        ax.set_thetagrids(np.degrees(angles[:-1]), self.stats_names)
        
        # 设置径向刻度和标签
        ax.set_rlabel_position(0)
        ax.set_ylim(0, 1)
        ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(["0", "20", "40", "60", "80", "100"])
        
        # 设置标题
        plt.title(self.title, size=20, color='darkred', y=1.1)
        
        # 添加数值标签
        for i, (angle, value) in enumerate(zip(angles[:-1], self.stats_values)):
            x = angle
            y = value/100 + 0.05  # 稍微偏移一点避免重叠
            ax.text(x, y, str(value), ha='center', va='center', 
                   fontsize=12, fontweight='bold', color='darkred')
        
        # 移除网格
        ax.grid(False)
        ax.spines['polar'].set_visible(False)
        
        plt.tight_layout()
        plt.show()
    
    def save_radar_chart(self, filename):
        """保存六边形属性面板为图片"""
        # 设置角度和标签位置
        angles = np.linspace(0, 2*np.pi, 6, endpoint=False).tolist()
        angles += angles[:1]  # 闭合图形
        
        # 归一化属性值 (0-100 到 0-1)
        values = [v/100 for v in self.stats_values]
        values += values[:1]  # 闭合图形
        
        # 创建图形和极坐标子图
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        
        # 绘制属性网格线
        for i in range(0, 101, 20):
            ax.plot(angles, [i/100] * 7, color='gray', linewidth=0.5, alpha=0.7)
        
        # 绘制属性区域
        ax.fill(angles, values, color='red', alpha=0.25)
        ax.plot(angles, values, color='red', linewidth=2)
        
        # 设置角度刻度和标签
        ax.set_theta_offset(np.pi/2)
        ax.set_theta_direction(-1)
        ax.set_thetagrids(np.degrees(angles[:-1]), self.stats_names)
        
        # 设置径向刻度和标签
        ax.set_rlabel_position(0)
        ax.set_ylim(0, 1)
        ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(["0", "20", "40", "60", "80", "100"])
        
        # 设置标题
        plt.title(self.title, size=20, color='darkred', y=1.1)
        
        # 添加数值标签
        for i, (angle, value) in enumerate(zip(angles[:-1], self.stats_values)):
            x = angle
            y = value/100 + 0.05  # 稍微偏移一点避免重叠
            ax.text(x, y, str(value), ha='center', va='center', 
                   fontsize=12, fontweight='bold', color='darkred')
        
        # 移除网格
        ax.grid(False)
        ax.spines['polar'].set_visible(False)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

# 示例使用
if __name__ == "__main__":
    # 定义属性名称和数值
    stats_names = ["Power", "Speed", "Range", "Durability", "Precision", "Potential"]
    stats_values = [95, 85, 60, 70, 90, 75]
    
    # 创建属性面板
    stand_stats = JoJoStandStats(stats_names, stats_values, "Star Platinum Stats")
    
    # 显示属性面板
    stand_stats.draw_radar_chart()
    
    # 保存属性面板为图片
    stand_stats.save_radar_chart("star_platinum_stats.png")