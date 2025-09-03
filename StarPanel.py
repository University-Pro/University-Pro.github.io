import numpy as np
import matplotlib.pyplot as plt

class JoJoStandStats:
    """
    Initializes and draws a JoJo-style Stand Stats radar chart.
    """
    def __init__(self, stats_names, stats_values, title="Stand Stats"):
        if len(stats_names) != 6 or len(stats_values) != 6:
            raise ValueError("6 stats names and 6 stats values are required.")
            
        self.stats_names = stats_names
        self.stats_values = stats_values
        self.title = title
        
        self.grade_mapping = {'A': 1.0, 'B': 0.8, 'C': 0.6, 'D': 0.4, 'E': 0.2}
        self.numeric_values = [self.grade_mapping.get(v.upper(), 0) for v in self.stats_values]

    def _create_chart(self, ax):
        """
        Internal method to generate the radar chart on a given axis.
        """
        # Create angles for the 6 stats
        angles = np.linspace(0, 2 * np.pi, 6, endpoint=False).tolist()
        angles += angles[:1]
        
        # The data needs to be looped for the plot to be closed
        values = self.numeric_values + [self.numeric_values[0]]
        
        # Set theta direction and offset (top-down, clockwise)
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        # Set radial limits, this pushes the stat names outward
        ax.set_ylim(0, 1.4)

        # Draw grid lines
        grid_colors = ['#e0e0e0', '#d0d0d0', '#c0c0c0', '#b0b0b0', '#a0a0a0']
        for level in [0.2, 0.4, 0.6, 0.8, 1.0]:
            ax.plot(angles, [level] * 7, color=grid_colors[4], linewidth=1, alpha=0.7)
        
        # Draw the main data polygon
        ax.fill(angles, values, color='#8B0000', alpha=0.6)
        
        # Draw the main data line
        ax.plot(angles, values, color='#8B0000', linewidth=3, marker='o', markersize=8)
        
        # Set stat name labels (e.g., "Power", "Speed")
        ax.set_thetagrids(np.degrees(angles[:-1]), self.stats_names, fontsize=16, fontweight='bold')
        
        # Set radial labels (A-E)
        ax.set_rlabel_position(0)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(["E", "D", "C", "B", "A"], fontsize=12, fontweight='bold')
        
        # Add main title
        ax.set_title(self.title, size=24, color='#8B0000', y=1.15, fontweight='bold', fontfamily='serif')
        
        # Add grade labels on the plot (the letter grades)
        grade_colors = {'A': '#006400', 'B': '#32CD32', 'C': '#FFD700', 'D': '#FF8C00', 'E': '#DC143C'}
        for angle, grade, value in zip(angles[:-1], self.stats_values, self.numeric_values):
            color = grade_colors.get(grade.upper(), 'black')
            # Position the grade label slightly outside the data point
            ax.text(angle, value + 0.1, grade.upper(), ha='center', va='center', 
                   fontsize=16, fontweight='bold', color=color,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

        # --- New Additions: Outer Rings and Text ---

        # Add two outer rings
        outer_ring_angles = np.linspace(0, 2 * np.pi, 200) # Use more points for a smooth circle
        ax.plot(outer_ring_angles, [1.15] * 200, color='black', linewidth=2)
        ax.plot(outer_ring_angles, [1.25] * 200, color='black', linewidth=2)

        # Add "ABCD" between the rings
        r_abcd = 1.20
        angles_abcd_rad = np.deg2rad([45, 135, 225, 315])
        labels_abcd = ['A', 'B', 'C', 'D']
        for angle_rad, label in zip(angles_abcd_rad, labels_abcd):
            ax.text(angle_rad, r_abcd, label, ha='center', va='center', fontsize=18, fontweight='bold')

        # Add text outside the outermost ring
        r_outer_text = 1.35
        # Note: angles are clockwise from top (0=Top, pi/2=Left, pi=Bottom, 3pi/2=Right)
        ax.text(0, r_outer_text, 'STAND', ha='center', va='center', fontsize=16, fontweight='bold')
        ax.text(np.pi, r_outer_text, 'STATS', ha='center', va='center', fontsize=16, fontweight='bold')
        ax.text(np.pi / 2, r_outer_text, 'PARAMETER', ha='center', va='center', fontsize=16, fontweight='bold')
        ax.text(3 * np.pi / 2, r_outer_text, 'CHART', ha='center', va='center', fontsize=16, fontweight='bold')

        # --- End of New Additions ---

        # General appearance settings
        ax.grid(True, alpha=0.3)
        ax.spines['polar'].set_visible(True)
        ax.spines['polar'].set_color('#8B0000')
        ax.spines['polar'].set_linewidth(2)

    def draw_radar_chart(self):
        """
        Creates and displays the radar chart.
        """
        fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor('#f8f8f8')
        
        self._create_chart(ax)
        
        plt.tight_layout()
        plt.show()
    
    def save_radar_chart(self, filename):
        """
        Creates and saves the radar chart to a file.
        """
        fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor('#f8f8f8')
        
        self._create_chart(ax)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close()

# Example Usage
if __name__ == "__main__":
    # Define stats names and their grades
    stats_names = ["Power", "Speed", "Range", "Durability", "Precision", "Potential"]
    stats_values = ["A", "A", "C", "B", "A", "B"]
    
    # Create an instance of the stats chart
    stand_stats = JoJoStandStats(stats_names, stats_values, "Star Platinum Stats")
    
    # Display the chart
    stand_stats.draw_radar_chart()
    
    # Save the chart to a file
    stand_stats.save_radar_chart("star_platinum_stats_modified.png")
    print("Chart saved to star_platinum_stats_modified.png")