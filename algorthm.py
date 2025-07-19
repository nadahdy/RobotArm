import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# أطوال الروابط
L1 = 70  # سم
L2 = 60  # سم

# زوايا المفاصل (بالتقدير الدائري)
theta1_vals = np.linspace(0, 2 * np.pi, 60)  # θ₁ من 0 إلى 360 درجة
theta2_vals = np.linspace(0, np.pi, 30)      # θ₂ من 0 إلى 180 درجة
theta3_vals = np.linspace(0, np.pi, 30)      # θ₃ من 0 إلى 180 درجة

# حساب إحداثيات نقطة النهاية لكل مجموعة زوايا
points = []

for t1 in theta1_vals:
    for t2 in theta2_vals:
        for t3 in theta3_vals:
            # إسقاط ثنائي الأبعاد في مستوى x-z
            x_plane = L1 * np.cos(t2) + L2 * np.cos(t2 + t3)
            z_plane = L1 * np.sin(t2) + L2 * np.sin(t2 + t3)

            # تدوير المستوى حول المحور Z بزاوية θ₁
            x = x_plane * np.cos(t1)
            y = x_plane * np.sin(t1)
            z = z_plane

            points.append([x, y, z])

# تحويل النقاط إلى مصفوفة NumPy
points = np.array(points)

# رسم المجال الحركي في فضاء ثلاثي الأبعاد
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1, alpha=0.3, c='blue')
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Z (cm)")
ax.set_title("Workspace of 4-DOF Robotic Arm")
plt.tight_layout()
plt.show()
