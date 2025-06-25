# Liveness Detection for Rephotographed Images Using YOLOv8

This project explores a novel approach to detecting image spoofing (rephotographed images) by leveraging the YOLOv8 object detection architecture. Instead of its conventional use for object localization, YOLOv8 is repurposed here for full-image binary classification — distinguishing between *real (live)* and *rephotographed (fake)* biometric images. The model is trained on a small, manually curated dataset and shows promising results for deployment in secure KYC and biometric verification pipelines.

## 📌 Key Features

- ✅ Reformulates image liveness detection as a complete-frame object detection problem  
- ⚙️ Based on the lightweight **YOLOv8n** architecture for real-time performance  
- 🔍 Annotates full-image bounding boxes to transform object detection into binary classification  
- 📈 Outperforms traditional models like SVM and Random Forest on small datasets  
- 🔐 Applicable to fraud detection in KYC/biometric verification systems

## 🧠 Model Overview

- **Base Model:** YOLOv8n (Nano version for efficiency)  
- **Backbone:** CSPDarknet  
- **Neck:** PAN-FPN (Path Aggregation Network Feature Pyramid)  
- **Head:** Detection + Classification  

In our use case, the bounding box covers the entire image, and the head is used only for predicting class probabilities (live vs. spoofed).

## 📊 Results

| Metric    | Value |
|-----------|-------|
| Precision | 0.94  |
| Recall    | 0.92  |
| Accuracy  | 0.93  |
| F1 Score  | 0.93  |

Model demonstrates strong generalization despite a limited dataset of 108 images.
All images are annotated using YOLO-format with a single bounding box covering the entire image and a binary label:

0 = Fake (rephotographed)

1 = Real (live)

🤝 Acknowledgments
This project was developed by Aditi Saxena and Shresth Yadav as part of a research-based academic curriculum. The work builds upon Ultralytics' YOLOv8 framework and open-source liveness detection literature.

📬 Contact
For queries or collaborations, reach out via:

📧 aaditisaxena2004@gmail.com

📧 shresthyadav124@gmail.com
