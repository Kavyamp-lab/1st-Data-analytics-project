import pandas as pd

# Read CSV with correct separator
rfm = pd.read_csv("rfm_data.csv")

print(rfm.head())


# R score (lower recency = better)
rfm['R_Score'] = pd.qcut(
    rfm['Recency'].rank(method='first'),
    5,
    labels=[5,4,3,2,1]
)
# F score (higher frequency = better)
rfm['F_Score'] = pd.qcut(
    rfm['Frequency'].rank(method='first'),
    5,
    labels=[1,2,3,4,5]
)
# M score (higher monetary = better)
rfm['M_Score'] = pd.qcut(
    rfm['Monetary'],
    5,
    labels=[1,2,3,4,5]
)
# Combine RFM score
rfm['RFM_Score'] = (
    rfm['R_Score'].astype(str) +
    rfm['F_Score'].astype(str) +
    rfm['M_Score'].astype(str)
)
print(rfm.head())
# Customer Segmentation
def segment_customer(row):
    if row['R_Score'] >= 4 and row['F_Score'] >= 4 and row['M_Score'] >= 4:
        return 'Champion'
    elif row['R_Score'] >= 3 and row['F_Score'] >= 3:
        return 'Loyal'
    elif row['R_Score'] <= 2 and row['F_Score'] <= 2:
        return 'At Risk'
    else:
        return 'Churn Risk'
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

print(rfm[['CustomerID', 'RFM_Score', 'Segment']].head())

rfm.to_csv("rfm_final.csv", index=False)
print(rfm.columns)
