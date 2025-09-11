🩺 FitPulse: Health Anomaly Detection from Fitness Devices

FitPulse is a health anomaly detection system that processes fitness tracker data (heart rate, steps, and sleep) to identify unusual patterns and provide actionable insights into user behavior.

🚀 Features
🔹 Data Collection & Preprocessing

Import fitness data (heart rate, steps, sleep) from CSV/JSON formats.

Clean timestamps, handle missing values, and align data to consistent intervals.

🔹 Feature Extraction & Modeling

Extract statistical features with TSFresh.

Model seasonal trends and detect deviations using Facebook Prophet.

Apply clustering algorithms (KMeans, DBSCAN) to group behavioral patterns.

🔹 Anomaly Detection & Visualization

Rule-based anomalies (e.g., thresholds on HR, steps, or sleep hours).

Model-based anomalies (residual errors, clustering outliers).

Visualize insights with Matplotlib and Plotly.

🔹 Dashboard for Insights

Interactive dashboard built with Streamlit.

Upload fitness tracker files, run anomaly detection, and view results in real time.

Export anomaly reports to PDF/CSV.

🛠 Tools & Technologies

Python – core programming language.

Libraries:

Data: pandas, numpy

Visualization: matplotlib, plotly

ML/Stats: scikit-learn, tsfresh, prophet

Clustering: KMeans, DBSCAN

Streamlit – for interactive dashboard.

Data Formats: CSV, JSON.
