import os
import cv2
import matplotlib.pyplot as plt

def display_data(root_dir, batch_size = 10):
    train_dir = os.path.join(root_dir, "bounding_box_train")
    if not os.path.exists(train_dir):
        raise FileNotFoundError(f"Error: Couldnt find in root directory.")
    
    image_files = [f for f in os.listdir(train_dir) if f.lower().endswith(".jpg")]
    print(f"Found images in training dataset.")

    for start in range(0, len(image_files), batch_size):
        batch = image_files[start: start + batch_size]
    # after each image, press enter to continue or q to quit
        for fname in batch:
            full_path = os.path.join(train_dir, fname)

            img_bgr = cv2.imread(full_path)
            if img_bgr is None:
                print(f"Could not read image")
                continue

            img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

            plt.imshow(img_rgb)
            plt.title(fname)
            plt.axis("off")
            plt.show()

        if (start + batch_size) < len(image_files):
            user_input = input (f"Press Enter to show the next batch, or 'q' to quit:")
            if user_input.lower() == 'q':
                print("Quitting...")
                break

if __name__ == "__main__":
    root_dir = "Market-1501-v15.09.15"
    display_data(root_dir)