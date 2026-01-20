**🚀 Project Overview**  
  
This project is an end-to-end machine learning system that assesses vineyard vegetation risk using Sentinel-2 satellite imagery.  
  
Using NDVI time series extracted from Google Earth Engine, the system:  
  
Analyzes vegetation dynamics across space and time   
  
Learns typical vs anomalous seasonal behavior using unsupervised learning  
  
Assigns risk levels to vineyard areas  
  
Serves predictions via a Dockerized FastAPI service  






**🛰️ Data Source**  
  
Satellite: Sentinel-2 (Surface Reflectance)  
  
Platform: Google Earth Engine  
  
Index: NDVI (Normalized Difference Vegetation Index)  
  
Region: Mediterranean vineyard (Ktima Gerovasileiou - Greece)  
  
Resolution: 10 meters  
  
Time span: 2022–2024 growing seasons  
  
  
  
**🧠 Methodology**  
  
1️⃣ NDVI Extraction (NDVI is computed per Sentinel-2 image --> Cloud and cirrus pixels are masked using the Scene Classification Layer (SCL) --> NDVI values are sampled at multiple grid points within the vineyard)  
  
2️⃣ Feature Engineering (For each [point_id, year] combination, seasonal features are computed: ndvi_mean, ndvi_max, ndvi_min, ndvi_std, ndvi_slope, ndvi_drop)  
  
3️⃣ Unsupervised Learning (Features are standardized - KMeans clustering is applied - Optimal number of clusters chosen via elbow method - Clusters are interpreted agronomically and mapped to:
      
-LOW_RISK  
-MEDIUM_RISK  
-HIGH_RISK  



**📂 Project Structure**
vineyard-risk-ml/  
│  
├── data/  
│   └── processed/  
│       └── vineyard_risk_dataset.csv  
│  
├── notebooks/  
│   ├── 01_ndvi_exploration.ipynb  
│   ├── 02_feature_engineering.ipynb  
│   └── 03_clustering.ipynb  
│  
├── src/  
│   ├── artifacts.py  
│   ├── schemas.py  
│   └── predict.py  
│  
├── api/  
│   └── main.py  
│  
├── models/  
│   ├── kmeans.pkl  
│   ├── scaler.pkl  
│   ├── features.pkl  
│   └── risk_map.pkl  
│  
├── Dockerfile  
├── requirements.txt  
├── .gitignore  
└── README.md  
