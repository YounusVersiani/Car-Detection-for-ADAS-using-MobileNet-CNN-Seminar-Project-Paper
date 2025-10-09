import cv2
import os

# use relative paths so the code works on any computer
static_frames_dir = './data/static_frames'
moving_frames_dir = './data/moving_frames'
kitti_sync_dir = './data/raw_kitti/image_02/data'  # optional folder for future KITTI data

os.makedirs(static_frames_dir, exist_ok=True)
os.makedirs(moving_frames_dir, exist_ok=True)

# Example: process 108 frames
for i in range(108):
    png_path = os.path.join(kitti_sync_dir, f'{i:010d}.png')
    frame = cv2.imread(png_path)
    if frame is None:
        print(f"Failed to load {png_path} - Check path or file existence")
        continue

    if i < 50:
        cv2.imwrite(os.path.join(static_frames_dir, f'frame_{i:03d}.jpg'), frame)
    elif i >= 58:
        moving_idx = i - 58
        cv2.imwrite(os.path.join(moving_frames_dir, f'frame_{moving_idx:03d}.jpg'), frame)

print("✅ Organized frames saved in ./data/")