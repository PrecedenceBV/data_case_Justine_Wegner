import pandas as pd


# Load data
nps_scores = pd.read_csv('data-case/nps_scores.csv', sep=';')
call_data = pd.read_csv('data-case/call_data.csv',sep=',')

# Clean column names
nps_scores.columns = nps_scores.columns.str.strip().str.lower()


# === Call Data Analysis ===

# Average call duration
avg_call_duration = call_data['Call_Duration_Minutes'].mean()
print("\nAverage Call Duration (minutes):")
print(f"{avg_call_duration:.2f}")

# Average wait time
avg_wait_time = call_data['Wait_Time_Minutes'].mean()
print("\nAverage Wait Time (minutes):")
print(f"{avg_wait_time:.2f}")

# Average customer satisfaction score per call reason
avg_cust_sat_per_reason = call_data.groupby('Call_Reason')['Customer_Satisfaction_Score'].mean()
print("\nAverage Customer Satisfaction Score per Call Reason:")
print(avg_cust_sat_per_reason)

# Average customer satisfaction score by whether call was resolved
avg_cust_sat_resolved = call_data.groupby('call_resolved')['customer_satisfaction_score'].mean()
print("\nAverage Customer Satisfaction Score for resolved vs unresolved calls:")
print(avg_cust_sat_resolved)