import pandas

csvData = pandas.read_csv("./model/keypoint_classifier/keypoint.csv")

print(csvData.iloc[0:, 0])
#print(csvData.columns)          # Các nhãn của cột (lấy dòng đầu)

#csvData.sort_values(csvData.columns[0], axis=0, ascending=[True], inplace=True)
#csvData.sort_values(by=csvData.columns[0], axis=0, inplace=True)
print("-------------------")
#print(csvData.iloc[0:, 0])
print(csvData.iloc[0:, 0].groupby(csvData.iloc[0:, 0]).count())

#csvData.to_csv("./model/keypoint_classifier/keypoint.csv", index=False)
