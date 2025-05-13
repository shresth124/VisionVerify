import os
import shutil
import yaml
from ultralytics import YOLO
import random

# Create dataset structure
def create_dataset_structure():
    # Create directories
    os.makedirs('dataset/images/train', exist_ok=True)
    os.makedirs('dataset/images/val', exist_ok=True)
    os.makedirs('dataset/labels/train', exist_ok=True)
    os.makedirs('dataset/labels/val', exist_ok=True)
    
    # Copy and split images
    for img_class in ['fake_img', 'real_img']:
        images = os.listdir(img_class)
        random.shuffle(images)
        split_idx = int(len(images) * 0.8)  # 80% train, 20% val
        
        # Copy training images
        for img in images[:split_idx]:
            shutil.copy2(
                os.path.join(img_class, img),
                os.path.join('dataset/images/train', img)
            )
            # Create corresponding label file
            with open(os.path.join('dataset/labels/train', img.rsplit('.', 1)[0] + '.txt'), 'w') as f:
                class_id = 0 if img_class == 'fake_img' else 1
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")
        
        # Copy validation images
        for img in images[split_idx:]:
            shutil.copy2(
                os.path.join(img_class, img),
                os.path.join('dataset/images/val', img)
            )
            # Create corresponding label file
            with open(os.path.join('dataset/labels/val', img.rsplit('.', 1)[0] + '.txt'), 'w') as f:
                class_id = 0 if img_class == 'fake_img' else 1
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

# Create dataset.yaml
def create_dataset_yaml():
    yaml_content = {
        'path': 'dataset',
        'train': 'images/train',
        'val': 'images/val',
        'names': {
            0: 'Rejected',
            1: 'Accepted'
        }
    }
    
    with open('dataset.yaml', 'w') as f:
        yaml.dump(yaml_content, f)

def main():
    # Create dataset structure
    create_dataset_structure()
    create_dataset_yaml()
    
    # Initialize YOLO model
    model = YOLO('yolov8n.pt')
    
    # Train the model
    results = model.train(
        data='dataset.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        name='yolo_classifier'
    )
    
    # Validate the model
    model.val()

if __name__ == "__main__":
    main() 