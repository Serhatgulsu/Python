

All = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="All", header=0, index_col=0)
All60 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="All60", header=0, index_col=0)
All55 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="All55", header=0, index_col=0)
All50 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="All50", header=0, index_col=0)
All40 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="All40", header=0, index_col=0)
All30 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="All30", header=0, index_col=0)
Marmara = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Marmara", header=0, index_col=0)
Karadeniz = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Karadeniz", header=0, index_col=0)
DoguAnadolu = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="DoguAnadolu", header=0, index_col=0)
Ankaradogu = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Ankaradogu", header=0, index_col=0)
IcAnadolu = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="IcAnadolu", header=0, index_col=0)
Ege = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Ege", header=0, index_col=0)
Akdeniz = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Akdeniz", header=0, index_col=0)
Transfer60 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Transfer60", header=0, index_col=0)
Transfer55 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Transfer55", header=0, index_col=0)
Transfer50 = pd.read_excel("//Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Transfer50", header=0, index_col=0)
Transfer40 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Transfer40", header=0, index_col=0)
Transfer30 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Transfer30", header=0, index_col=0)
Yenileme60 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme60", header=0, index_col=0)
Yenileme55 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme55", header=0, index_col=0)
Yenileme50 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme50", header=0, index_col=0)
Yenileme40 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme40", header=0, index_col=0)
Yenileme30 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme30", header=0, index_col=0)

pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)

#Ultimate_all

GenelHitRatioAll = np.array(All['Ultimate Hit Ratio'])
print(GenelHitRatioAll)
for a in GenelHitRatioAll:
    GenelHitRatioAlllists = [np.array(GenelHitRatioAll[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAlllists)
GenelHitRatioAllnonseasonality = [pm.auto_arima((np.array(GenelHitRatioAll[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAllnonseasonality)
GenelHitRatioAllpredict1 = ([GenelHitRatioAllnonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAllpre2 = pd.DataFrame(GenelHitRatioAllpredict1)
GenelHitRatioAllIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAllpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAllLowerInterval = [(np.concatenate(GenelHitRatioAllIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAllUpperInterval = [(np.concatenate(GenelHitRatioAllIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAllConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAllLowerInterval,
                        "Upper": GenelHitRatioAllUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAllpredict1 = ([GenelHitRatioAllnonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAllp1 = []
for i in range(0, 79):
    GenelHitRatioAllp1.append(float(str(GenelHitRatioAllpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAllp1)
GenelHitRatioAlllistpredict = pd.DataFrame({'Predict': GenelHitRatioAllp1,
                          'Lower': GenelHitRatioAllConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioAllConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAlllist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAll’',
                       '50 aylik hit': GenelHitRatioAlllists,
                      'Non-Seasonality': GenelHitRatioAllnonseasonality,
                       'Hit Ratio': All['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAllfinallist = pd.merge(GenelHitRatioAlllist, GenelHitRatioAlllistpredict, on='Sira', how='inner')
print(GenelHitRatioAllfinallist)
GenelHitRatioAllfinallist["Alert"]  = [0 if (GenelHitRatioAllfinallist['Hit Ratio'][i]> GenelHitRatioAllfinallist["Lower"][i]) & (GenelHitRatioAllfinallist['Hit Ratio'][i]< GenelHitRatioAllfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAllfinallist[GenelHitRatioAllfinallist["Alert"]==1])


#Ultimate_TransferAll

GenelHitRatioTransfer = np.array(All["Transfer Hit Ratio"])
print(GenelHitRatioTransfer)
for a in GenelHitRatioTransfer:
    GenelHitRatioTransferlists = [np.array(GenelHitRatioTransfer[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferlists)
GenelHitRatioTransfernonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransfer[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransfernonseasonality)
GenelHitRatioTransferpredict1 = ([GenelHitRatioTransfernonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferpre2 = pd.DataFrame(GenelHitRatioTransferpredict1)
GenelHitRatioTransferIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferLowerInterval = [(np.concatenate(GenelHitRatioTransferIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferUpperInterval = [(np.concatenate(GenelHitRatioTransferIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferLowerInterval,
                        "Upper": GenelHitRatioTransferUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferpredict1 = ([GenelHitRatioTransfernonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferp1 = []
for i in range(0, 79):
    GenelHitRatioTransferp1.append(float(str(GenelHitRatioTransferpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferp1)
GenelHitRatioTransferlistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferp1,
                          'Lower': GenelHitRatioTransferConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransfer’',
                       '50 aylik hit': GenelHitRatioTransferlists,
                      'Non-Seasonality': GenelHitRatioTransfernonseasonality,
                       'Hit Ratio': All["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferfinallist = pd.merge(GenelHitRatioTransferlist, GenelHitRatioTransferlistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferfinallist)
GenelHitRatioTransferfinallist["Alert"]  = [0 if (GenelHitRatioTransferfinallist['Hit Ratio'][i]> GenelHitRatioTransferfinallist["Lower"][i]) & (GenelHitRatioTransferfinallist['Hit Ratio'][i]< GenelHitRatioTransferfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferfinallist[GenelHitRatioTransferfinallist["Alert"]==1])

#Ultimate_YenilemeAll

GenelHitRatioYenileme = np.array(All["Yenileme Hit Ratio"])
print(GenelHitRatioYenileme)
for a in GenelHitRatioYenileme:
    GenelHitRatioYenilemelists = [np.array(GenelHitRatioYenileme[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemelists)
GenelHitRatioYenilemenonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenileme[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemenonseasonality)
GenelHitRatioYenilemepredict1 = ([GenelHitRatioYenilemenonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemepre2 = pd.DataFrame(GenelHitRatioYenilemepredict1)
GenelHitRatioYenilemeIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemepre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeLowerInterval = [(np.concatenate(GenelHitRatioYenilemeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeUpperInterval = [(np.concatenate(GenelHitRatioYenilemeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeLowerInterval,
                        "Upper": GenelHitRatioYenilemeUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemepredict1 = ([GenelHitRatioYenilemenonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemep1 = []
for i in range(0, 79):
    GenelHitRatioYenilemep1.append(float(str(GenelHitRatioYenilemepredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemep1)
GenelHitRatioYenilemelistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemep1,
                          'Lower': GenelHitRatioYenilemeConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemelist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenileme’',
                       '50 aylik hit': GenelHitRatioYenilemelists,
                      'Non-Seasonality': GenelHitRatioYenilemenonseasonality,
                       'Hit Ratio': All["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemefinallist = pd.merge(GenelHitRatioYenilemelist, GenelHitRatioYenilemelistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemefinallist)
GenelHitRatioYenilemefinallist["Alert"]  = [0 if (GenelHitRatioYenilemefinallist['Hit Ratio'][i]> GenelHitRatioYenilemefinallist["Lower"][i]) & (GenelHitRatioYenilemefinallist['Hit Ratio'][i]< GenelHitRatioYenilemefinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemefinallist[GenelHitRatioYenilemefinallist["Alert"]==1])


#Ultimate_all60

GenelHitRatioAll60 = np.array(All60['Ultimate Hit Ratio'])
print(GenelHitRatioAll60)
for a in GenelHitRatioAll60:
    GenelHitRatioAll60lists = [np.array(GenelHitRatioAll60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAll60lists)
GenelHitRatioAll60nonseasonality = [pm.auto_arima((np.array(GenelHitRatioAll60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAll60nonseasonality)
GenelHitRatioAll60predict1 = ([GenelHitRatioAll60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAll60pre2 = pd.DataFrame(GenelHitRatioAll60predict1)
GenelHitRatioAll60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAll60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAll60LowerInterval = [(np.concatenate(GenelHitRatioAll60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAll60UpperInterval = [(np.concatenate(GenelHitRatioAll60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAll60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAll60LowerInterval,
                        "Upper": GenelHitRatioAll60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAll60predict1 = ([GenelHitRatioAll60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAll60p1 = []
for i in range(0, 79):
    GenelHitRatioAll60p1.append(float(str(GenelHitRatioAll60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAll60p1)
GenelHitRatioAll60listpredict = pd.DataFrame({'Predict': GenelHitRatioAll60p1,
                          'Lower': GenelHitRatioAll60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioAll60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAll60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAll60’',
                       '50 aylik hit': GenelHitRatioAll60lists,
                      'Non-Seasonality': GenelHitRatioAll60nonseasonality,
                       'Hit Ratio': All60['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAll60finallist = pd.merge(GenelHitRatioAll60list, GenelHitRatioAll60listpredict, on='Sira', how='inner')
print(GenelHitRatioAll60finallist)
GenelHitRatioAll60finallist["Alert"]  = [0 if (GenelHitRatioAll60finallist['Hit Ratio'][i]> GenelHitRatioAll60finallist["Lower"][i]) & (GenelHitRatioAll60finallist['Hit Ratio'][i]< GenelHitRatioAll60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAll60finallist[GenelHitRatioAll60finallist["Alert"]==1])


#Ultimate_Transfer60

GenelHitRatioTransfer60 = np.array(All60["Transfer Hit Ratio"])
print(GenelHitRatioTransfer60)
for a in GenelHitRatioTransfer60:
    GenelHitRatioTransfer60lists = [np.array(GenelHitRatioTransfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransfer60lists)
GenelHitRatioTransfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransfer60nonseasonality)
GenelHitRatioTransfer60predict1 = ([GenelHitRatioTransfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransfer60pre2 = pd.DataFrame(GenelHitRatioTransfer60predict1)
GenelHitRatioTransfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransfer60LowerInterval = [(np.concatenate(GenelHitRatioTransfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransfer60UpperInterval = [(np.concatenate(GenelHitRatioTransfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransfer60LowerInterval,
                        "Upper": GenelHitRatioTransfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransfer60predict1 = ([GenelHitRatioTransfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransfer60p1 = []
for i in range(0, 79):
    GenelHitRatioTransfer60p1.append(float(str(GenelHitRatioTransfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransfer60p1)
GenelHitRatioTransfer60listpredict = pd.DataFrame({'Predict': GenelHitRatioTransfer60p1,
                          'Lower': GenelHitRatioTransfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransfer60’',
                       '50 aylik hit': GenelHitRatioTransfer60lists,
                      'Non-Seasonality': GenelHitRatioTransfer60nonseasonality,
                       'Hit Ratio': All60["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransfer60finallist = pd.merge(GenelHitRatioTransfer60list, GenelHitRatioTransfer60listpredict, on='Sira', how='inner')
print(GenelHitRatioTransfer60finallist)
GenelHitRatioTransfer60finallist["Alert"]  = [0 if (GenelHitRatioTransfer60finallist['Hit Ratio'][i]> GenelHitRatioTransfer60finallist["Lower"][i]) & (GenelHitRatioTransfer60finallist['Hit Ratio'][i]< GenelHitRatioTransfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransfer60finallist[GenelHitRatioTransfer60finallist["Alert"]==1])

#Ultimate_YenilemeAll

GenelHitRatioYenileme60 = np.array(All60["Yenileme Hit Ratio"])
print(GenelHitRatioYenileme60)
for a in GenelHitRatioYenileme60:
    GenelHitRatioYenileme60lists = [np.array(GenelHitRatioYenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenileme60lists)
GenelHitRatioYenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenileme60nonseasonality)
GenelHitRatioYenileme60predict1 = ([GenelHitRatioYenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenileme60pre2 = pd.DataFrame(GenelHitRatioYenileme60predict1)
GenelHitRatioYenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenileme60LowerInterval = [(np.concatenate(GenelHitRatioYenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenileme60UpperInterval = [(np.concatenate(GenelHitRatioYenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenileme60LowerInterval,
                        "Upper": GenelHitRatioYenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenileme60predict1 = ([GenelHitRatioYenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenileme60p1 = []
for i in range(0, 79):
    GenelHitRatioYenileme60p1.append(float(str(GenelHitRatioYenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenileme60p1)
GenelHitRatioYenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatioYenileme60p1,
                          'Lower': GenelHitRatioYenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenileme60’',
                       '50 aylik hit': GenelHitRatioYenileme60lists,
                      'Non-Seasonality': GenelHitRatioYenileme60nonseasonality,
                       'Hit Ratio': All60["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenileme60finallist = pd.merge(GenelHitRatioYenileme60list, GenelHitRatioYenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatioYenileme60finallist)
GenelHitRatioYenileme60finallist["Alert"]  = [0 if (GenelHitRatioYenileme60finallist['Hit Ratio'][i]> GenelHitRatioYenileme60finallist["Lower"][i]) & (GenelHitRatioYenileme60finallist['Hit Ratio'][i]< GenelHitRatioYenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenileme60finallist[GenelHitRatioYenileme60finallist["Alert"]==1])


#Ultimate_all55

GenelHitRatioAll55 = np.array(All55['Ultimate Hit Ratio'])
print(GenelHitRatioAll55)
for a in GenelHitRatioAll55:
    GenelHitRatioAll55lists = [np.array(GenelHitRatioAll55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAll55lists)
GenelHitRatioAll55nonseasonality = [pm.auto_arima((np.array(GenelHitRatioAll55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAll55nonseasonality)
GenelHitRatioAll55predict1 = ([GenelHitRatioAll55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAll55pre2 = pd.DataFrame(GenelHitRatioAll55predict1)
GenelHitRatioAll55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAll55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAll55LowerInterval = [(np.concatenate(GenelHitRatioAll55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAll55UpperInterval = [(np.concatenate(GenelHitRatioAll55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAll55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAll55LowerInterval,
                        "Upper": GenelHitRatioAll55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAll55predict1 = ([GenelHitRatioAll55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAll55p1 = []
for i in range(0, 79):
    GenelHitRatioAll55p1.append(float(str(GenelHitRatioAll55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAll55p1)
GenelHitRatioAll55listpredict = pd.DataFrame({'Predict': GenelHitRatioAll55p1,
                          'Lower': GenelHitRatioAll55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioAll55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAll55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAll55’',
                       '50 aylik hit': GenelHitRatioAll55lists,
                      'Non-Seasonality': GenelHitRatioAll55nonseasonality,
                       'Hit Ratio': All55['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAll55finallist = pd.merge(GenelHitRatioAll55list, GenelHitRatioAll55listpredict, on='Sira', how='inner')
print(GenelHitRatioAll55finallist)
GenelHitRatioAll55finallist["Alert"]  = [0 if (GenelHitRatioAll55finallist['Hit Ratio'][i]> GenelHitRatioAll55finallist["Lower"][i]) & (GenelHitRatioAll55finallist['Hit Ratio'][i]< GenelHitRatioAll55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAll55finallist[GenelHitRatioAll55finallist["Alert"]==1])


#Ultimate_Transfer55

GenelHitRatioTransfer55 = np.array(All55["Transfer Hit Ratio"])
print(GenelHitRatioTransfer55)
for a in GenelHitRatioTransfer55:
    GenelHitRatioTransfer55lists = [np.array(GenelHitRatioTransfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransfer55lists)
GenelHitRatioTransfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransfer55nonseasonality)
GenelHitRatioTransfer55predict1 = ([GenelHitRatioTransfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransfer55pre2 = pd.DataFrame(GenelHitRatioTransfer55predict1)
GenelHitRatioTransfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransfer55LowerInterval = [(np.concatenate(GenelHitRatioTransfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransfer55UpperInterval = [(np.concatenate(GenelHitRatioTransfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransfer55LowerInterval,
                        "Upper": GenelHitRatioTransfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransfer55predict1 = ([GenelHitRatioTransfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransfer55p1 = []
for i in range(0, 79):
    GenelHitRatioTransfer55p1.append(float(str(GenelHitRatioTransfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransfer55p1)
GenelHitRatioTransfer55listpredict = pd.DataFrame({'Predict': GenelHitRatioTransfer55p1,
                          'Lower': GenelHitRatioTransfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransfer55’',
                       '50 aylik hit': GenelHitRatioTransfer55lists,
                      'Non-Seasonality': GenelHitRatioTransfer55nonseasonality,
                       'Hit Ratio': All55["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransfer55finallist = pd.merge(GenelHitRatioTransfer55list, GenelHitRatioTransfer55listpredict, on='Sira', how='inner')
print(GenelHitRatioTransfer55finallist)
GenelHitRatioTransfer55finallist["Alert"]  = [0 if (GenelHitRatioTransfer55finallist['Hit Ratio'][i]> GenelHitRatioTransfer55finallist["Lower"][i]) & (GenelHitRatioTransfer55finallist['Hit Ratio'][i]< GenelHitRatioTransfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransfer55finallist[GenelHitRatioTransfer55finallist["Alert"]==1])

#Ultimate_YenilemeAll55

GenelHitRatioYenileme55 = np.array(All55["Yenileme Hit Ratio"])
print(GenelHitRatioYenileme55)
for a in GenelHitRatioYenileme55:
    GenelHitRatioYenileme55lists = [np.array(GenelHitRatioYenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenileme55lists)
GenelHitRatioYenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenileme55nonseasonality)
GenelHitRatioYenileme55predict1 = ([GenelHitRatioYenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenileme55pre2 = pd.DataFrame(GenelHitRatioYenileme55predict1)
GenelHitRatioYenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenileme55LowerInterval = [(np.concatenate(GenelHitRatioYenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenileme55UpperInterval = [(np.concatenate(GenelHitRatioYenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenileme55LowerInterval,
                        "Upper": GenelHitRatioYenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenileme55predict1 = ([GenelHitRatioYenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenileme55p1 = []
for i in range(0, 79):
    GenelHitRatioYenileme55p1.append(float(str(GenelHitRatioYenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenileme55p1)
GenelHitRatioYenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatioYenileme55p1,
                          'Lower': GenelHitRatioYenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenileme55’',
                       '50 aylik hit': GenelHitRatioYenileme55lists,
                      'Non-Seasonality': GenelHitRatioYenileme55nonseasonality,
                       'Hit Ratio': All55["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenileme55finallist = pd.merge(GenelHitRatioYenileme55list, GenelHitRatioYenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatioYenileme55finallist)
GenelHitRatioYenileme55finallist["Alert"]  = [0 if (GenelHitRatioYenileme55finallist['Hit Ratio'][i]> GenelHitRatioYenileme55finallist["Lower"][i]) & (GenelHitRatioYenileme55finallist['Hit Ratio'][i]< GenelHitRatioYenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenileme55finallist[GenelHitRatioYenileme55finallist["Alert"]==1])


#Ultimate_all50

GenelHitRatioAll50 = np.array(All50['Ultimate Hit Ratio'])
print(GenelHitRatioAll50)
for a in GenelHitRatioAll50:
    GenelHitRatioAll50lists = [np.array(GenelHitRatioAll50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAll50lists)
GenelHitRatioAll50nonseasonality = [pm.auto_arima((np.array(GenelHitRatioAll50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAll50nonseasonality)
GenelHitRatioAll50predict1 = ([GenelHitRatioAll50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAll50pre2 = pd.DataFrame(GenelHitRatioAll50predict1)
GenelHitRatioAll50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAll50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAll50LowerInterval = [(np.concatenate(GenelHitRatioAll50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAll50UpperInterval = [(np.concatenate(GenelHitRatioAll50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAll50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAll50LowerInterval,
                        "Upper": GenelHitRatioAll50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAll50predict1 = ([GenelHitRatioAll50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAll50p1 = []
for i in range(0, 79):
    GenelHitRatioAll50p1.append(float(str(GenelHitRatioAll50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAll50p1)
GenelHitRatioAll50listpredict = pd.DataFrame({'Predict': GenelHitRatioAll50p1,
                          'Lower': GenelHitRatioAll50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioAll50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAll50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAll50’',
                       '50 aylik hit': GenelHitRatioAll50lists,
                      'Non-Seasonality': GenelHitRatioAll50nonseasonality,
                       'Hit Ratio': All50['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAll50finallist = pd.merge(GenelHitRatioAll50list, GenelHitRatioAll50listpredict, on='Sira', how='inner')
print(GenelHitRatioAll50finallist)
GenelHitRatioAll50finallist["Alert"]  = [0 if (GenelHitRatioAll50finallist['Hit Ratio'][i]> GenelHitRatioAll50finallist["Lower"][i]) & (GenelHitRatioAll50finallist['Hit Ratio'][i]< GenelHitRatioAll50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAll50finallist[GenelHitRatioAll50finallist["Alert"]==1])


#Ultimate_Transfer50

GenelHitRatioTransfer50 = np.array(All50["Transfer Hit Ratio"])
print(GenelHitRatioTransfer50)
for a in GenelHitRatioTransfer50:
    GenelHitRatioTransfer50lists = [np.array(GenelHitRatioTransfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransfer50lists)
GenelHitRatioTransfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransfer50nonseasonality)
GenelHitRatioTransfer50predict1 = ([GenelHitRatioTransfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransfer50pre2 = pd.DataFrame(GenelHitRatioTransfer50predict1)
GenelHitRatioTransfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransfer50LowerInterval = [(np.concatenate(GenelHitRatioTransfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransfer50UpperInterval = [(np.concatenate(GenelHitRatioTransfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransfer50LowerInterval,
                        "Upper": GenelHitRatioTransfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransfer50predict1 = ([GenelHitRatioTransfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransfer50p1 = []
for i in range(0, 79):
    GenelHitRatioTransfer50p1.append(float(str(GenelHitRatioTransfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransfer50p1)
GenelHitRatioTransfer50listpredict = pd.DataFrame({'Predict': GenelHitRatioTransfer50p1,
                          'Lower': GenelHitRatioTransfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransfer50’',
                       '50 aylik hit': GenelHitRatioTransfer50lists,
                      'Non-Seasonality': GenelHitRatioTransfer50nonseasonality,
                       'Hit Ratio': All50["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransfer50finallist = pd.merge(GenelHitRatioTransfer50list, GenelHitRatioTransfer50listpredict, on='Sira', how='inner')
print(GenelHitRatioTransfer50finallist)
GenelHitRatioTransfer50finallist["Alert"]  = [0 if (GenelHitRatioTransfer50finallist['Hit Ratio'][i]> GenelHitRatioTransfer50finallist["Lower"][i]) & (GenelHitRatioTransfer50finallist['Hit Ratio'][i]< GenelHitRatioTransfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransfer50finallist[GenelHitRatioTransfer50finallist["Alert"]==1])

#Ultimate_YenilemeAll50

GenelHitRatioYenileme50 = np.array(All50["Yenileme Hit Ratio"])
print(GenelHitRatioYenileme50)
for a in GenelHitRatioYenileme50:
    GenelHitRatioYenileme50lists = [np.array(GenelHitRatioYenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenileme50lists)
GenelHitRatioYenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenileme50nonseasonality)
GenelHitRatioYenileme50predict1 = ([GenelHitRatioYenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenileme50pre2 = pd.DataFrame(GenelHitRatioYenileme50predict1)
GenelHitRatioYenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenileme50LowerInterval = [(np.concatenate(GenelHitRatioYenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenileme50UpperInterval = [(np.concatenate(GenelHitRatioYenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenileme50LowerInterval,
                        "Upper": GenelHitRatioYenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenileme50predict1 = ([GenelHitRatioYenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenileme50p1 = []
for i in range(0, 79):
    GenelHitRatioYenileme50p1.append(float(str(GenelHitRatioYenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenileme50p1)
GenelHitRatioYenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatioYenileme50p1,
                          'Lower': GenelHitRatioYenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenileme50’',
                       '50 aylik hit': GenelHitRatioYenileme50lists,
                      'Non-Seasonality': GenelHitRatioYenileme50nonseasonality,
                       'Hit Ratio': All50["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenileme50finallist = pd.merge(GenelHitRatioYenileme50list, GenelHitRatioYenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatioYenileme50finallist)
GenelHitRatioYenileme50finallist["Alert"]  = [0 if (GenelHitRatioYenileme50finallist['Hit Ratio'][i]> GenelHitRatioYenileme50finallist["Lower"][i]) & (GenelHitRatioYenileme50finallist['Hit Ratio'][i]< GenelHitRatioYenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenileme50finallist[GenelHitRatioYenileme50finallist["Alert"]==1])


#Ultimate_all40

GenelHitRatioAll40 = np.array(All40['Ultimate Hit Ratio'])
print(GenelHitRatioAll40)
for a in GenelHitRatioAll40:
    GenelHitRatioAll40lists = [np.array(GenelHitRatioAll40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAll40lists)
GenelHitRatioAll40nonseasonality = [pm.auto_arima((np.array(GenelHitRatioAll40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAll40nonseasonality)
GenelHitRatioAll40predict1 = ([GenelHitRatioAll40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAll40pre2 = pd.DataFrame(GenelHitRatioAll40predict1)
GenelHitRatioAll40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAll40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAll40LowerInterval = [(np.concatenate(GenelHitRatioAll40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAll40UpperInterval = [(np.concatenate(GenelHitRatioAll40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAll40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAll40LowerInterval,
                        "Upper": GenelHitRatioAll40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAll40predict1 = ([GenelHitRatioAll40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAll40p1 = []
for i in range(0, 79):
    GenelHitRatioAll40p1.append(float(str(GenelHitRatioAll40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAll40p1)
GenelHitRatioAll40listpredict = pd.DataFrame({'Predict': GenelHitRatioAll40p1,
                          'Lower': GenelHitRatioAll40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioAll40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAll40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAll40’',
                       '40 aylik hit': GenelHitRatioAll40lists,
                      'Non-Seasonality': GenelHitRatioAll40nonseasonality,
                       'Hit Ratio': All40['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAll40finallist = pd.merge(GenelHitRatioAll40list, GenelHitRatioAll40listpredict, on='Sira', how='inner')
print(GenelHitRatioAll40finallist)
GenelHitRatioAll40finallist["Alert"]  = [0 if (GenelHitRatioAll40finallist['Hit Ratio'][i]> GenelHitRatioAll40finallist["Lower"][i]) & (GenelHitRatioAll40finallist['Hit Ratio'][i]< GenelHitRatioAll40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAll40finallist[GenelHitRatioAll40finallist["Alert"]==1])


#Ultimate_Transfer40

GenelHitRatioTransfer40 = np.array(All40["Transfer Hit Ratio"])
print(GenelHitRatioTransfer40)
for a in GenelHitRatioTransfer40:
    GenelHitRatioTransfer40lists = [np.array(GenelHitRatioTransfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransfer40lists)
GenelHitRatioTransfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransfer40nonseasonality)
GenelHitRatioTransfer40predict1 = ([GenelHitRatioTransfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransfer40pre2 = pd.DataFrame(GenelHitRatioTransfer40predict1)
GenelHitRatioTransfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransfer40LowerInterval = [(np.concatenate(GenelHitRatioTransfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransfer40UpperInterval = [(np.concatenate(GenelHitRatioTransfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransfer40LowerInterval,
                        "Upper": GenelHitRatioTransfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransfer40predict1 = ([GenelHitRatioTransfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransfer40p1 = []
for i in range(0, 79):
    GenelHitRatioTransfer40p1.append(float(str(GenelHitRatioTransfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransfer40p1)
GenelHitRatioTransfer40listpredict = pd.DataFrame({'Predict': GenelHitRatioTransfer40p1,
                          'Lower': GenelHitRatioTransfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransfer40’',
                       '40 aylik hit': GenelHitRatioTransfer40lists,
                      'Non-Seasonality': GenelHitRatioTransfer40nonseasonality,
                       'Hit Ratio': All40["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransfer40finallist = pd.merge(GenelHitRatioTransfer40list, GenelHitRatioTransfer40listpredict, on='Sira', how='inner')
print(GenelHitRatioTransfer40finallist)
GenelHitRatioTransfer40finallist["Alert"]  = [0 if (GenelHitRatioTransfer40finallist['Hit Ratio'][i]> GenelHitRatioTransfer40finallist["Lower"][i]) & (GenelHitRatioTransfer40finallist['Hit Ratio'][i]< GenelHitRatioTransfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransfer40finallist[GenelHitRatioTransfer40finallist["Alert"]==1])

#Ultimate_YenilemeAll40

GenelHitRatioYenileme40 = np.array(All40["Yenileme Hit Ratio"])
print(GenelHitRatioYenileme40)
for a in GenelHitRatioYenileme40:
    GenelHitRatioYenileme40lists = [np.array(GenelHitRatioYenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenileme40lists)
GenelHitRatioYenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenileme40nonseasonality)
GenelHitRatioYenileme40predict1 = ([GenelHitRatioYenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenileme40pre2 = pd.DataFrame(GenelHitRatioYenileme40predict1)
GenelHitRatioYenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenileme40LowerInterval = [(np.concatenate(GenelHitRatioYenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenileme40UpperInterval = [(np.concatenate(GenelHitRatioYenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenileme40LowerInterval,
                        "Upper": GenelHitRatioYenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenileme40predict1 = ([GenelHitRatioYenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenileme40p1 = []
for i in range(0, 79):
    GenelHitRatioYenileme40p1.append(float(str(GenelHitRatioYenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenileme40p1)
GenelHitRatioYenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatioYenileme40p1,
                          'Lower': GenelHitRatioYenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenileme40’',
                       '40 aylik hit': GenelHitRatioYenileme40lists,
                      'Non-Seasonality': GenelHitRatioYenileme40nonseasonality,
                       'Hit Ratio': All40["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenileme40finallist = pd.merge(GenelHitRatioYenileme40list, GenelHitRatioYenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatioYenileme40finallist)
GenelHitRatioYenileme40finallist["Alert"]  = [0 if (GenelHitRatioYenileme40finallist['Hit Ratio'][i]> GenelHitRatioYenileme40finallist["Lower"][i]) & (GenelHitRatioYenileme40finallist['Hit Ratio'][i]< GenelHitRatioYenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenileme40finallist[GenelHitRatioYenileme40finallist["Alert"]==1])


#Ultimate_all30

GenelHitRatioAll30 = np.array(All30['Ultimate Hit Ratio'])
print(GenelHitRatioAll30)
for a in GenelHitRatioAll30:
    GenelHitRatioAll30lists = [np.array(GenelHitRatioAll30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAll30lists)
GenelHitRatioAll30nonseasonality = [pm.auto_arima((np.array(GenelHitRatioAll30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAll30nonseasonality)
GenelHitRatioAll30predict1 = ([GenelHitRatioAll30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAll30pre2 = pd.DataFrame(GenelHitRatioAll30predict1)
GenelHitRatioAll30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAll30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAll30LowerInterval = [(np.concatenate(GenelHitRatioAll30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAll30UpperInterval = [(np.concatenate(GenelHitRatioAll30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAll30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAll30LowerInterval,
                        "Upper": GenelHitRatioAll30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAll30predict1 = ([GenelHitRatioAll30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAll30p1 = []
for i in range(0, 79):
    GenelHitRatioAll30p1.append(float(str(GenelHitRatioAll30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAll30p1)
GenelHitRatioAll30listpredict = pd.DataFrame({'Predict': GenelHitRatioAll30p1,
                          'Lower': GenelHitRatioAll30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioAll30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAll30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAll30’',
                       '30 aylik hit': GenelHitRatioAll30lists,
                      'Non-Seasonality': GenelHitRatioAll30nonseasonality,
                       'Hit Ratio': All30['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAll30finallist = pd.merge(GenelHitRatioAll30list, GenelHitRatioAll30listpredict, on='Sira', how='inner')
print(GenelHitRatioAll30finallist)
GenelHitRatioAll30finallist["Alert"]  = [0 if (GenelHitRatioAll30finallist['Hit Ratio'][i]> GenelHitRatioAll30finallist["Lower"][i]) & (GenelHitRatioAll30finallist['Hit Ratio'][i]< GenelHitRatioAll30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAll30finallist[GenelHitRatioAll30finallist["Alert"]==1])


#Ultimate_Transfer30

GenelHitRatioTransfer30 = np.array(All30["Transfer Hit Ratio"])
print(GenelHitRatioTransfer30)
for a in GenelHitRatioTransfer30:
    GenelHitRatioTransfer30lists = [np.array(GenelHitRatioTransfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransfer30lists)
GenelHitRatioTransfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransfer30nonseasonality)
GenelHitRatioTransfer30predict1 = ([GenelHitRatioTransfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransfer30pre2 = pd.DataFrame(GenelHitRatioTransfer30predict1)
GenelHitRatioTransfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransfer30LowerInterval = [(np.concatenate(GenelHitRatioTransfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransfer30UpperInterval = [(np.concatenate(GenelHitRatioTransfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransfer30LowerInterval,
                        "Upper": GenelHitRatioTransfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransfer30predict1 = ([GenelHitRatioTransfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransfer30p1 = []
for i in range(0, 79):
    GenelHitRatioTransfer30p1.append(float(str(GenelHitRatioTransfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransfer30p1)
GenelHitRatioTransfer30listpredict = pd.DataFrame({'Predict': GenelHitRatioTransfer30p1,
                          'Lower': GenelHitRatioTransfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransfer30’',
                       '30 aylik hit': GenelHitRatioTransfer30lists,
                      'Non-Seasonality': GenelHitRatioTransfer30nonseasonality,
                       'Hit Ratio': All30["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransfer30finallist = pd.merge(GenelHitRatioTransfer30list, GenelHitRatioTransfer30listpredict, on='Sira', how='inner')
print(GenelHitRatioTransfer30finallist)
GenelHitRatioTransfer30finallist["Alert"]  = [0 if (GenelHitRatioTransfer30finallist['Hit Ratio'][i]> GenelHitRatioTransfer30finallist["Lower"][i]) & (GenelHitRatioTransfer30finallist['Hit Ratio'][i]< GenelHitRatioTransfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransfer30finallist[GenelHitRatioTransfer30finallist["Alert"]==1])

#Ultimate_Yenileme30

GenelHitRatioYenileme30 = np.array(All30["Yenileme Hit Ratio"])
print(GenelHitRatioYenileme30)
for a in GenelHitRatioYenileme30:
    GenelHitRatioYenileme30lists = [np.array(GenelHitRatioYenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenileme30lists)
GenelHitRatioYenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenileme30nonseasonality)
GenelHitRatioYenileme30predict1 = ([GenelHitRatioYenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenileme30pre2 = pd.DataFrame(GenelHitRatioYenileme30predict1)
GenelHitRatioYenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenileme30LowerInterval = [(np.concatenate(GenelHitRatioYenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenileme30UpperInterval = [(np.concatenate(GenelHitRatioYenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenileme30LowerInterval,
                        "Upper": GenelHitRatioYenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenileme30predict1 = ([GenelHitRatioYenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenileme30p1 = []
for i in range(0, 79):
    GenelHitRatioYenileme30p1.append(float(str(GenelHitRatioYenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenileme30p1)
GenelHitRatioYenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatioYenileme30p1,
                          'Lower': GenelHitRatioYenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenileme30’',
                       '30 aylik hit': GenelHitRatioYenileme30lists,
                      'Non-Seasonality': GenelHitRatioYenileme30nonseasonality,
                       'Hit Ratio': All30["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenileme30finallist = pd.merge(GenelHitRatioYenileme30list, GenelHitRatioYenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatioYenileme30finallist)
GenelHitRatioYenileme30finallist["Alert"]  = [0 if (GenelHitRatioYenileme30finallist['Hit Ratio'][i]> GenelHitRatioYenileme30finallist["Lower"][i]) & (GenelHitRatioYenileme30finallist['Hit Ratio'][i]< GenelHitRatioYenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenileme30finallist[GenelHitRatioYenileme30finallist["Alert"]==1])


#Ultimate_Marmara

GenelHitRatioMarmara = np.array(Marmara['Ultimate Hit Ratio'])
print(GenelHitRatioMarmara)
for a in GenelHitRatioMarmara:
    GenelHitRatioMarmaralists = [np.array(GenelHitRatioMarmara[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioMarmaralists)
GenelHitRatioMarmaranonseasonality = [pm.auto_arima((np.array(GenelHitRatioMarmara[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioMarmaranonseasonality)
GenelHitRatioMarmarapredict1 = ([GenelHitRatioMarmaranonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioMarmarapre2 = pd.DataFrame(GenelHitRatioMarmarapredict1)
GenelHitRatioMarmaraIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioMarmarapre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioMarmaraLowerInterval = [(np.concatenate(GenelHitRatioMarmaraIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioMarmaraUpperInterval = [(np.concatenate(GenelHitRatioMarmaraIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioMarmaraConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioMarmaraLowerInterval,
                        "Upper": GenelHitRatioMarmaraUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioMarmarapredict1 = ([GenelHitRatioMarmaranonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioMarmarap1 = []
for i in range(0, 79):
    GenelHitRatioMarmarap1.append(float(str(GenelHitRatioMarmarapredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioMarmarap1)
GenelHitRatioMarmaralistpredict = pd.DataFrame({'Predict': GenelHitRatioMarmarap1,
                          'Lower': GenelHitRatioMarmaraConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioMarmaraConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioMarmaralist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioMarmara’',
                       'Marmara aylik hit': GenelHitRatioMarmaralists,
                      'Non-Seasonality': GenelHitRatioMarmaranonseasonality,
                       'Hit Ratio': Marmara['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioMarmarafinallist = pd.merge(GenelHitRatioMarmaralist, GenelHitRatioMarmaralistpredict, on='Sira', how='inner')
print(GenelHitRatioMarmarafinallist)
GenelHitRatioMarmarafinallist["Alert"]  = [0 if (GenelHitRatioMarmarafinallist['Hit Ratio'][i]> GenelHitRatioMarmarafinallist["Lower"][i]) & (GenelHitRatioMarmarafinallist['Hit Ratio'][i]< GenelHitRatioMarmarafinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioMarmarafinallist[GenelHitRatioMarmarafinallist["Alert"]==1])


#Ultimate_TransferMarmara

GenelHitRatioTransferMarmara = np.array(Marmara["Transfer Hit Ratio"])
print(GenelHitRatioTransferMarmara)
for a in GenelHitRatioTransferMarmara:
    GenelHitRatioTransferMarmaralists = [np.array(GenelHitRatioTransferMarmara[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferMarmaralists)
GenelHitRatioTransferMarmaranonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferMarmara[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferMarmaranonseasonality)
GenelHitRatioTransferMarmarapredict1 = ([GenelHitRatioTransferMarmaranonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferMarmarapre2 = pd.DataFrame(GenelHitRatioTransferMarmarapredict1)
GenelHitRatioTransferMarmaraIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferMarmarapre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferMarmaraLowerInterval = [(np.concatenate(GenelHitRatioTransferMarmaraIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferMarmaraUpperInterval = [(np.concatenate(GenelHitRatioTransferMarmaraIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferMarmaraConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferMarmaraLowerInterval,
                        "Upper": GenelHitRatioTransferMarmaraUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferMarmarapredict1 = ([GenelHitRatioTransferMarmaranonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferMarmarap1 = []
for i in range(0, 79):
    GenelHitRatioTransferMarmarap1.append(float(str(GenelHitRatioTransferMarmarapredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferMarmarap1)
GenelHitRatioTransferMarmaralistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferMarmarap1,
                          'Lower': GenelHitRatioTransferMarmaraConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferMarmaraConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferMarmaralist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferMarmara’',
                       'Marmara aylik hit': GenelHitRatioTransferMarmaralists,
                      'Non-Seasonality': GenelHitRatioTransferMarmaranonseasonality,
                       'Hit Ratio': Marmara["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferMarmarafinallist = pd.merge(GenelHitRatioTransferMarmaralist, GenelHitRatioTransferMarmaralistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferMarmarafinallist)
GenelHitRatioTransferMarmarafinallist["Alert"]  = [0 if (GenelHitRatioTransferMarmarafinallist['Hit Ratio'][i]> GenelHitRatioTransferMarmarafinallist["Lower"][i]) & (GenelHitRatioTransferMarmarafinallist['Hit Ratio'][i]< GenelHitRatioTransferMarmarafinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferMarmarafinallist[GenelHitRatioTransferMarmarafinallist["Alert"]==1])

#Ultimate_YenilemeMarmara

GenelHitRatioYenilemeMarmara = np.array(Marmara["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeMarmara)
for a in GenelHitRatioYenilemeMarmara:
    GenelHitRatioYenilemeMarmaralists = [np.array(GenelHitRatioYenilemeMarmara[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeMarmaralists)
GenelHitRatioYenilemeMarmaranonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeMarmara[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeMarmaranonseasonality)
GenelHitRatioYenilemeMarmarapredict1 = ([GenelHitRatioYenilemeMarmaranonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeMarmarapre2 = pd.DataFrame(GenelHitRatioYenilemeMarmarapredict1)
GenelHitRatioYenilemeMarmaraIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeMarmarapre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeMarmaraLowerInterval = [(np.concatenate(GenelHitRatioYenilemeMarmaraIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeMarmaraUpperInterval = [(np.concatenate(GenelHitRatioYenilemeMarmaraIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeMarmaraConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeMarmaraLowerInterval,
                        "Upper": GenelHitRatioYenilemeMarmaraUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeMarmarapredict1 = ([GenelHitRatioYenilemeMarmaranonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeMarmarap1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeMarmarap1.append(float(str(GenelHitRatioYenilemeMarmarapredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeMarmarap1)
GenelHitRatioYenilemeMarmaralistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeMarmarap1,
                          'Lower': GenelHitRatioYenilemeMarmaraConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeMarmaraConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeMarmaralist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeMarmara’',
                       'Marmara aylik hit': GenelHitRatioYenilemeMarmaralists,
                      'Non-Seasonality': GenelHitRatioYenilemeMarmaranonseasonality,
                       'Hit Ratio': Marmara["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeMarmarafinallist = pd.merge(GenelHitRatioYenilemeMarmaralist, GenelHitRatioYenilemeMarmaralistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeMarmarafinallist)
GenelHitRatioYenilemeMarmarafinallist["Alert"]  = [0 if (GenelHitRatioYenilemeMarmarafinallist['Hit Ratio'][i]> GenelHitRatioYenilemeMarmarafinallist["Lower"][i]) & (GenelHitRatioYenilemeMarmarafinallist['Hit Ratio'][i]< GenelHitRatioYenilemeMarmarafinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeMarmarafinallist[GenelHitRatioYenilemeMarmarafinallist["Alert"]==1])



#Ultimate_Karadeniz

GenelHitRatioKaradeniz = np.array(Karadeniz['Ultimate Hit Ratio'])
print(GenelHitRatioKaradeniz)
for a in GenelHitRatioKaradeniz:
    GenelHitRatioKaradenizlists = [np.array(GenelHitRatioKaradeniz[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioKaradenizlists)
GenelHitRatioKaradeniznonseasonality = [pm.auto_arima((np.array(GenelHitRatioKaradeniz[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioKaradeniznonseasonality)
GenelHitRatioKaradenizpredict1 = ([GenelHitRatioKaradeniznonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioKaradenizpre2 = pd.DataFrame(GenelHitRatioKaradenizpredict1)
GenelHitRatioKaradenizIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioKaradenizpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioKaradenizLowerInterval = [(np.concatenate(GenelHitRatioKaradenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioKaradenizUpperInterval = [(np.concatenate(GenelHitRatioKaradenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioKaradenizConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioKaradenizLowerInterval,
                        "Upper": GenelHitRatioKaradenizUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioKaradenizpredict1 = ([GenelHitRatioKaradeniznonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioKaradenizp1 = []
for i in range(0, 79):
    GenelHitRatioKaradenizp1.append(float(str(GenelHitRatioKaradenizpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioKaradenizp1)
GenelHitRatioKaradenizlistpredict = pd.DataFrame({'Predict': GenelHitRatioKaradenizp1,
                          'Lower': GenelHitRatioKaradenizConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioKaradenizConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioKaradenizlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioKaradeniz’',
                       'Karadeniz aylik hit': GenelHitRatioKaradenizlists,
                      'Non-Seasonality': GenelHitRatioKaradeniznonseasonality,
                       'Hit Ratio': Karadeniz['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioKaradenizfinallist = pd.merge(GenelHitRatioKaradenizlist, GenelHitRatioKaradenizlistpredict, on='Sira', how='inner')
print(GenelHitRatioKaradenizfinallist)
GenelHitRatioKaradenizfinallist["Alert"]  = [0 if (GenelHitRatioKaradenizfinallist['Hit Ratio'][i]> GenelHitRatioKaradenizfinallist["Lower"][i]) & (GenelHitRatioKaradenizfinallist['Hit Ratio'][i]< GenelHitRatioKaradenizfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioKaradenizfinallist[GenelHitRatioKaradenizfinallist["Alert"]==1])


#Ultimate_TransferKaradeniz

GenelHitRatioTransferKaradeniz = np.array(Karadeniz["Transfer Hit Ratio"])
print(GenelHitRatioTransferKaradeniz)
for a in GenelHitRatioTransferKaradeniz:
    GenelHitRatioTransferKaradenizlists = [np.array(GenelHitRatioTransferKaradeniz[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferKaradenizlists)
GenelHitRatioTransferKaradeniznonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferKaradeniz[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferKaradeniznonseasonality)
GenelHitRatioTransferKaradenizpredict1 = ([GenelHitRatioTransferKaradeniznonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferKaradenizpre2 = pd.DataFrame(GenelHitRatioTransferKaradenizpredict1)
GenelHitRatioTransferKaradenizIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferKaradenizpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferKaradenizLowerInterval = [(np.concatenate(GenelHitRatioTransferKaradenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferKaradenizUpperInterval = [(np.concatenate(GenelHitRatioTransferKaradenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferKaradenizConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferKaradenizLowerInterval,
                        "Upper": GenelHitRatioTransferKaradenizUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferKaradenizpredict1 = ([GenelHitRatioTransferKaradeniznonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferKaradenizp1 = []
for i in range(0, 79):
    GenelHitRatioTransferKaradenizp1.append(float(str(GenelHitRatioTransferKaradenizpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferKaradenizp1)
GenelHitRatioTransferKaradenizlistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferKaradenizp1,
                          'Lower': GenelHitRatioTransferKaradenizConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferKaradenizConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferKaradenizlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferKaradeniz’',
                       'Karadeniz aylik hit': GenelHitRatioTransferKaradenizlists,
                      'Non-Seasonality': GenelHitRatioTransferKaradeniznonseasonality,
                       'Hit Ratio': Karadeniz["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferKaradenizfinallist = pd.merge(GenelHitRatioTransferKaradenizlist, GenelHitRatioTransferKaradenizlistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferKaradenizfinallist)
GenelHitRatioTransferKaradenizfinallist["Alert"]  = [0 if (GenelHitRatioTransferKaradenizfinallist['Hit Ratio'][i]> GenelHitRatioTransferKaradenizfinallist["Lower"][i]) & (GenelHitRatioTransferKaradenizfinallist['Hit Ratio'][i]< GenelHitRatioTransferKaradenizfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferKaradenizfinallist[GenelHitRatioTransferKaradenizfinallist["Alert"]==1])

#Ultimate_YenilemeKaradeniz

GenelHitRatioYenilemeKaradeniz = np.array(Karadeniz["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeKaradeniz)
for a in GenelHitRatioYenilemeKaradeniz:
    GenelHitRatioYenilemeKaradenizlists = [np.array(GenelHitRatioYenilemeKaradeniz[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeKaradenizlists)
GenelHitRatioYenilemeKaradeniznonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeKaradeniz[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeKaradeniznonseasonality)
GenelHitRatioYenilemeKaradenizpredict1 = ([GenelHitRatioYenilemeKaradeniznonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeKaradenizpre2 = pd.DataFrame(GenelHitRatioYenilemeKaradenizpredict1)
GenelHitRatioYenilemeKaradenizIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeKaradenizpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeKaradenizLowerInterval = [(np.concatenate(GenelHitRatioYenilemeKaradenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeKaradenizUpperInterval = [(np.concatenate(GenelHitRatioYenilemeKaradenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeKaradenizConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeKaradenizLowerInterval,
                        "Upper": GenelHitRatioYenilemeKaradenizUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeKaradenizpredict1 = ([GenelHitRatioYenilemeKaradeniznonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeKaradenizp1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeKaradenizp1.append(float(str(GenelHitRatioYenilemeKaradenizpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeKaradenizp1)
GenelHitRatioYenilemeKaradenizlistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeKaradenizp1,
                          'Lower': GenelHitRatioYenilemeKaradenizConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeKaradenizConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeKaradenizlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeKaradeniz’',
                       'Karadeniz aylik hit': GenelHitRatioYenilemeKaradenizlists,
                      'Non-Seasonality': GenelHitRatioYenilemeKaradeniznonseasonality,
                       'Hit Ratio': Karadeniz["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeKaradenizfinallist = pd.merge(GenelHitRatioYenilemeKaradenizlist, GenelHitRatioYenilemeKaradenizlistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeKaradenizfinallist)
GenelHitRatioYenilemeKaradenizfinallist["Alert"]  = [0 if (GenelHitRatioYenilemeKaradenizfinallist['Hit Ratio'][i]> GenelHitRatioYenilemeKaradenizfinallist["Lower"][i]) & (GenelHitRatioYenilemeKaradenizfinallist['Hit Ratio'][i]< GenelHitRatioYenilemeKaradenizfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeKaradenizfinallist[GenelHitRatioYenilemeKaradenizfinallist["Alert"]==1])



#Ultimate_DoguAnadolu

GenelHitRatioDoguAnadolu = np.array(DoguAnadolu['Ultimate Hit Ratio'])
print(GenelHitRatioDoguAnadolu)
for a in GenelHitRatioDoguAnadolu:
    GenelHitRatioDoguAnadolulists = [np.array(GenelHitRatioDoguAnadolu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioDoguAnadolulists)
GenelHitRatioDoguAnadolunonseasonality = [pm.auto_arima((np.array(GenelHitRatioDoguAnadolu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioDoguAnadolunonseasonality)
GenelHitRatioDoguAnadolupredict1 = ([GenelHitRatioDoguAnadolunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioDoguAnadolupre2 = pd.DataFrame(GenelHitRatioDoguAnadolupredict1)
GenelHitRatioDoguAnadoluIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioDoguAnadolupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioDoguAnadoluLowerInterval = [(np.concatenate(GenelHitRatioDoguAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioDoguAnadoluUpperInterval = [(np.concatenate(GenelHitRatioDoguAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioDoguAnadoluConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioDoguAnadoluLowerInterval,
                        "Upper": GenelHitRatioDoguAnadoluUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioDoguAnadolupredict1 = ([GenelHitRatioDoguAnadolunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioDoguAnadolup1 = []
for i in range(0, 79):
    GenelHitRatioDoguAnadolup1.append(float(str(GenelHitRatioDoguAnadolupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioDoguAnadolup1)
GenelHitRatioDoguAnadolulistpredict = pd.DataFrame({'Predict': GenelHitRatioDoguAnadolup1,
                          'Lower': GenelHitRatioDoguAnadoluConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioDoguAnadoluConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioDoguAnadolulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioDoguAnadolu’',
                       'DoguAnadolu aylik hit': GenelHitRatioDoguAnadolulists,
                      'Non-Seasonality': GenelHitRatioDoguAnadolunonseasonality,
                       'Hit Ratio': DoguAnadolu['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioDoguAnadolufinallist = pd.merge(GenelHitRatioDoguAnadolulist, GenelHitRatioDoguAnadolulistpredict, on='Sira', how='inner')
print(GenelHitRatioDoguAnadolufinallist)
GenelHitRatioDoguAnadolufinallist["Alert"]  = [0 if (GenelHitRatioDoguAnadolufinallist['Hit Ratio'][i]> GenelHitRatioDoguAnadolufinallist["Lower"][i]) & (GenelHitRatioDoguAnadolufinallist['Hit Ratio'][i]< GenelHitRatioDoguAnadolufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioDoguAnadolufinallist[GenelHitRatioDoguAnadolufinallist["Alert"]==1])


#Ultimate_TransferDoguAnadolu

GenelHitRatioTransferDoguAnadolu = np.array(DoguAnadolu["Transfer Hit Ratio"])
print(GenelHitRatioTransferDoguAnadolu)
for a in GenelHitRatioTransferDoguAnadolu:
    GenelHitRatioTransferDoguAnadolulists = [np.array(GenelHitRatioTransferDoguAnadolu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferDoguAnadolulists)
GenelHitRatioTransferDoguAnadolunonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferDoguAnadolu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferDoguAnadolunonseasonality)
GenelHitRatioTransferDoguAnadolupredict1 = ([GenelHitRatioTransferDoguAnadolunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferDoguAnadolupre2 = pd.DataFrame(GenelHitRatioTransferDoguAnadolupredict1)
GenelHitRatioTransferDoguAnadoluIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferDoguAnadolupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferDoguAnadoluLowerInterval = [(np.concatenate(GenelHitRatioTransferDoguAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferDoguAnadoluUpperInterval = [(np.concatenate(GenelHitRatioTransferDoguAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferDoguAnadoluConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferDoguAnadoluLowerInterval,
                        "Upper": GenelHitRatioTransferDoguAnadoluUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferDoguAnadolupredict1 = ([GenelHitRatioTransferDoguAnadolunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferDoguAnadolup1 = []
for i in range(0, 79):
    GenelHitRatioTransferDoguAnadolup1.append(float(str(GenelHitRatioTransferDoguAnadolupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferDoguAnadolup1)
GenelHitRatioTransferDoguAnadolulistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferDoguAnadolup1,
                          'Lower': GenelHitRatioTransferDoguAnadoluConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferDoguAnadoluConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferDoguAnadolulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferDoguAnadolu’',
                       'DoguAnadolu aylik hit': GenelHitRatioTransferDoguAnadolulists,
                      'Non-Seasonality': GenelHitRatioTransferDoguAnadolunonseasonality,
                       'Hit Ratio': DoguAnadolu["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferDoguAnadolufinallist = pd.merge(GenelHitRatioTransferDoguAnadolulist, GenelHitRatioTransferDoguAnadolulistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferDoguAnadolufinallist)
GenelHitRatioTransferDoguAnadolufinallist["Alert"]  = [0 if (GenelHitRatioTransferDoguAnadolufinallist['Hit Ratio'][i]> GenelHitRatioTransferDoguAnadolufinallist["Lower"][i]) & (GenelHitRatioTransferDoguAnadolufinallist['Hit Ratio'][i]< GenelHitRatioTransferDoguAnadolufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferDoguAnadolufinallist[GenelHitRatioTransferDoguAnadolufinallist["Alert"]==1])

#Ultimate_YenilemeDoguAnadolu

GenelHitRatioYenilemeDoguAnadolu = np.array(DoguAnadolu["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeDoguAnadolu)
for a in GenelHitRatioYenilemeDoguAnadolu:
    GenelHitRatioYenilemeDoguAnadolulists = [np.array(GenelHitRatioYenilemeDoguAnadolu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeDoguAnadolulists)
GenelHitRatioYenilemeDoguAnadolunonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeDoguAnadolu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeDoguAnadolunonseasonality)
GenelHitRatioYenilemeDoguAnadolupredict1 = ([GenelHitRatioYenilemeDoguAnadolunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeDoguAnadolupre2 = pd.DataFrame(GenelHitRatioYenilemeDoguAnadolupredict1)
GenelHitRatioYenilemeDoguAnadoluIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeDoguAnadolupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeDoguAnadoluLowerInterval = [(np.concatenate(GenelHitRatioYenilemeDoguAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeDoguAnadoluUpperInterval = [(np.concatenate(GenelHitRatioYenilemeDoguAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeDoguAnadoluConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeDoguAnadoluLowerInterval,
                        "Upper": GenelHitRatioYenilemeDoguAnadoluUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeDoguAnadolupredict1 = ([GenelHitRatioYenilemeDoguAnadolunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeDoguAnadolup1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeDoguAnadolup1.append(float(str(GenelHitRatioYenilemeDoguAnadolupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeDoguAnadolup1)
GenelHitRatioYenilemeDoguAnadolulistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeDoguAnadolup1,
                          'Lower': GenelHitRatioYenilemeDoguAnadoluConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeDoguAnadoluConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeDoguAnadolulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeDoguAnadolu’',
                       'DoguAnadolu aylik hit': GenelHitRatioYenilemeDoguAnadolulists,
                      'Non-Seasonality': GenelHitRatioYenilemeDoguAnadolunonseasonality,
                       'Hit Ratio': DoguAnadolu["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeDoguAnadolufinallist = pd.merge(GenelHitRatioYenilemeDoguAnadolulist, GenelHitRatioYenilemeDoguAnadolulistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeDoguAnadolufinallist)
GenelHitRatioYenilemeDoguAnadolufinallist["Alert"]  = [0 if (GenelHitRatioYenilemeDoguAnadolufinallist['Hit Ratio'][i]> GenelHitRatioYenilemeDoguAnadolufinallist["Lower"][i]) & (GenelHitRatioYenilemeDoguAnadolufinallist['Hit Ratio'][i]< GenelHitRatioYenilemeDoguAnadolufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeDoguAnadolufinallist[GenelHitRatioYenilemeDoguAnadolufinallist["Alert"]==1])

#Ultimate_Ankaradogu

GenelHitRatioAnkaradogu = np.array(Ankaradogu['Ultimate Hit Ratio'])
print(GenelHitRatioAnkaradogu)
for a in GenelHitRatioAnkaradogu:
    GenelHitRatioAnkaradogulists = [np.array(GenelHitRatioAnkaradogu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAnkaradogulists)
GenelHitRatioAnkaradogunonseasonality = [pm.auto_arima((np.array(GenelHitRatioAnkaradogu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAnkaradogunonseasonality)
GenelHitRatioAnkaradogupredict1 = ([GenelHitRatioAnkaradogunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAnkaradogupre2 = pd.DataFrame(GenelHitRatioAnkaradogupredict1)
GenelHitRatioAnkaradoguIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAnkaradogupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAnkaradoguLowerInterval = [(np.concatenate(GenelHitRatioAnkaradoguIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAnkaradoguUpperInterval = [(np.concatenate(GenelHitRatioAnkaradoguIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAnkaradoguConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAnkaradoguLowerInterval,
                        "Upper": GenelHitRatioAnkaradoguUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAnkaradogupredict1 = ([GenelHitRatioAnkaradogunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAnkaradogup1 = []
for i in range(0, 79):
    GenelHitRatioAnkaradogup1.append(float(str(GenelHitRatioAnkaradogupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAnkaradogup1)
GenelHitRatioAnkaradogulistpredict = pd.DataFrame({'Predict': GenelHitRatioAnkaradogup1,
                          'Lower': GenelHitRatioAnkaradoguConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioAnkaradoguConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAnkaradogulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAnkaradogu’',
                       'Ankaradogu aylik hit': GenelHitRatioAnkaradogulists,
                      'Non-Seasonality': GenelHitRatioAnkaradogunonseasonality,
                       'Hit Ratio': Ankaradogu['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAnkaradogufinallist = pd.merge(GenelHitRatioAnkaradogulist, GenelHitRatioAnkaradogulistpredict, on='Sira', how='inner')
print(GenelHitRatioAnkaradogufinallist)
GenelHitRatioAnkaradogufinallist["Alert"]  = [0 if (GenelHitRatioAnkaradogufinallist['Hit Ratio'][i]> GenelHitRatioAnkaradogufinallist["Lower"][i]) & (GenelHitRatioAnkaradogufinallist['Hit Ratio'][i]< GenelHitRatioAnkaradogufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAnkaradogufinallist[GenelHitRatioAnkaradogufinallist["Alert"]==1])


#Ultimate_TransferAnkaradogu

GenelHitRatioTransferAnkaradogu = np.array(Ankaradogu["Transfer Hit Ratio"])
print(GenelHitRatioTransferAnkaradogu)
for a in GenelHitRatioTransferAnkaradogu:
    GenelHitRatioTransferAnkaradogulists = [np.array(GenelHitRatioTransferAnkaradogu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferAnkaradogulists)
GenelHitRatioTransferAnkaradogunonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferAnkaradogu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferAnkaradogunonseasonality)
GenelHitRatioTransferAnkaradogupredict1 = ([GenelHitRatioTransferAnkaradogunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferAnkaradogupre2 = pd.DataFrame(GenelHitRatioTransferAnkaradogupredict1)
GenelHitRatioTransferAnkaradoguIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferAnkaradogupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferAnkaradoguLowerInterval = [(np.concatenate(GenelHitRatioTransferAnkaradoguIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferAnkaradoguUpperInterval = [(np.concatenate(GenelHitRatioTransferAnkaradoguIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferAnkaradoguConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferAnkaradoguLowerInterval,
                        "Upper": GenelHitRatioTransferAnkaradoguUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferAnkaradogupredict1 = ([GenelHitRatioTransferAnkaradogunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferAnkaradogup1 = []
for i in range(0, 79):
    GenelHitRatioTransferAnkaradogup1.append(float(str(GenelHitRatioTransferAnkaradogupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferAnkaradogup1)
GenelHitRatioTransferAnkaradogulistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferAnkaradogup1,
                          'Lower': GenelHitRatioTransferAnkaradoguConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferAnkaradoguConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferAnkaradogulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferAnkaradogu’',
                       'Ankaradogu aylik hit': GenelHitRatioTransferAnkaradogulists,
                      'Non-Seasonality': GenelHitRatioTransferAnkaradogunonseasonality,
                       'Hit Ratio': Ankaradogu["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferAnkaradogufinallist = pd.merge(GenelHitRatioTransferAnkaradogulist, GenelHitRatioTransferAnkaradogulistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferAnkaradogufinallist)
GenelHitRatioTransferAnkaradogufinallist["Alert"]  = [0 if (GenelHitRatioTransferAnkaradogufinallist['Hit Ratio'][i]> GenelHitRatioTransferAnkaradogufinallist["Lower"][i]) & (GenelHitRatioTransferAnkaradogufinallist['Hit Ratio'][i]< GenelHitRatioTransferAnkaradogufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferAnkaradogufinallist[GenelHitRatioTransferAnkaradogufinallist["Alert"]==1])

#Ultimate_YenilemeAnkaradogu

GenelHitRatioYenilemeAnkaradogu = np.array(Ankaradogu["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeAnkaradogu)
for a in GenelHitRatioYenilemeAnkaradogu:
    GenelHitRatioYenilemeAnkaradogulists = [np.array(GenelHitRatioYenilemeAnkaradogu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeAnkaradogulists)
GenelHitRatioYenilemeAnkaradogunonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeAnkaradogu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeAnkaradogunonseasonality)
GenelHitRatioYenilemeAnkaradogupredict1 = ([GenelHitRatioYenilemeAnkaradogunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeAnkaradogupre2 = pd.DataFrame(GenelHitRatioYenilemeAnkaradogupredict1)
GenelHitRatioYenilemeAnkaradoguIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeAnkaradogupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeAnkaradoguLowerInterval = [(np.concatenate(GenelHitRatioYenilemeAnkaradoguIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeAnkaradoguUpperInterval = [(np.concatenate(GenelHitRatioYenilemeAnkaradoguIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeAnkaradoguConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeAnkaradoguLowerInterval,
                        "Upper": GenelHitRatioYenilemeAnkaradoguUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeAnkaradogupredict1 = ([GenelHitRatioYenilemeAnkaradogunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeAnkaradogup1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeAnkaradogup1.append(float(str(GenelHitRatioYenilemeAnkaradogupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeAnkaradogup1)
GenelHitRatioYenilemeAnkaradogulistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeAnkaradogup1,
                          'Lower': GenelHitRatioYenilemeAnkaradoguConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeAnkaradoguConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeAnkaradogulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeAnkaradogu’',
                       'Ankaradogu aylik hit': GenelHitRatioYenilemeAnkaradogulists,
                      'Non-Seasonality': GenelHitRatioYenilemeAnkaradogunonseasonality,
                       'Hit Ratio': Ankaradogu["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeAnkaradogufinallist = pd.merge(GenelHitRatioYenilemeAnkaradogulist, GenelHitRatioYenilemeAnkaradogulistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeAnkaradogufinallist)
GenelHitRatioYenilemeAnkaradogufinallist["Alert"]  = [0 if (GenelHitRatioYenilemeAnkaradogufinallist['Hit Ratio'][i]> GenelHitRatioYenilemeAnkaradogufinallist["Lower"][i]) & (GenelHitRatioYenilemeAnkaradogufinallist['Hit Ratio'][i]< GenelHitRatioYenilemeAnkaradogufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeAnkaradogufinallist[GenelHitRatioYenilemeAnkaradogufinallist["Alert"]==1])


#Ultimate_IcAnadolu

GenelHitRatioIcAnadolu = np.array(IcAnadolu['Ultimate Hit Ratio'])
print(GenelHitRatioIcAnadolu)
for a in GenelHitRatioIcAnadolu:
    GenelHitRatioIcAnadolulists = [np.array(GenelHitRatioIcAnadolu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioIcAnadolulists)
GenelHitRatioIcAnadolunonseasonality = [pm.auto_arima((np.array(GenelHitRatioIcAnadolu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioIcAnadolunonseasonality)
GenelHitRatioIcAnadolupredict1 = ([GenelHitRatioIcAnadolunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioIcAnadolupre2 = pd.DataFrame(GenelHitRatioIcAnadolupredict1)
GenelHitRatioIcAnadoluIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioIcAnadolupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioIcAnadoluLowerInterval = [(np.concatenate(GenelHitRatioIcAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioIcAnadoluUpperInterval = [(np.concatenate(GenelHitRatioIcAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioIcAnadoluConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioIcAnadoluLowerInterval,
                        "Upper": GenelHitRatioIcAnadoluUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioIcAnadolupredict1 = ([GenelHitRatioIcAnadolunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioIcAnadolup1 = []
for i in range(0, 79):
    GenelHitRatioIcAnadolup1.append(float(str(GenelHitRatioIcAnadolupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioIcAnadolup1)
GenelHitRatioIcAnadolulistpredict = pd.DataFrame({'Predict': GenelHitRatioIcAnadolup1,
                          'Lower': GenelHitRatioIcAnadoluConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioIcAnadoluConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioIcAnadolulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioIcAnadolu’',
                       'IcAnadolu aylik hit': GenelHitRatioIcAnadolulists,
                      'Non-Seasonality': GenelHitRatioIcAnadolunonseasonality,
                       'Hit Ratio': IcAnadolu['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioIcAnadolufinallist = pd.merge(GenelHitRatioIcAnadolulist, GenelHitRatioIcAnadolulistpredict, on='Sira', how='inner')
print(GenelHitRatioIcAnadolufinallist)
GenelHitRatioIcAnadolufinallist["Alert"]  = [0 if (GenelHitRatioIcAnadolufinallist['Hit Ratio'][i]> GenelHitRatioIcAnadolufinallist["Lower"][i]) & (GenelHitRatioIcAnadolufinallist['Hit Ratio'][i]< GenelHitRatioIcAnadolufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioIcAnadolufinallist[GenelHitRatioIcAnadolufinallist["Alert"]==1])


#Ultimate_TransferIcAnadolu

GenelHitRatioTransferIcAnadolu = np.array(IcAnadolu["Transfer Hit Ratio"])
print(GenelHitRatioTransferIcAnadolu)
for a in GenelHitRatioTransferIcAnadolu:
    GenelHitRatioTransferIcAnadolulists = [np.array(GenelHitRatioTransferIcAnadolu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferIcAnadolulists)
GenelHitRatioTransferIcAnadolunonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferIcAnadolu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferIcAnadolunonseasonality)
GenelHitRatioTransferIcAnadolupredict1 = ([GenelHitRatioTransferIcAnadolunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferIcAnadolupre2 = pd.DataFrame(GenelHitRatioTransferIcAnadolupredict1)
GenelHitRatioTransferIcAnadoluIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferIcAnadolupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferIcAnadoluLowerInterval = [(np.concatenate(GenelHitRatioTransferIcAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferIcAnadoluUpperInterval = [(np.concatenate(GenelHitRatioTransferIcAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferIcAnadoluConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferIcAnadoluLowerInterval,
                        "Upper": GenelHitRatioTransferIcAnadoluUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferIcAnadolupredict1 = ([GenelHitRatioTransferIcAnadolunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferIcAnadolup1 = []
for i in range(0, 79):
    GenelHitRatioTransferIcAnadolup1.append(float(str(GenelHitRatioTransferIcAnadolupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferIcAnadolup1)
GenelHitRatioTransferIcAnadolulistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferIcAnadolup1,
                          'Lower': GenelHitRatioTransferIcAnadoluConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferIcAnadoluConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferIcAnadolulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferIcAnadolu’',
                       'IcAnadolu aylik hit': GenelHitRatioTransferIcAnadolulists,
                      'Non-Seasonality': GenelHitRatioTransferIcAnadolunonseasonality,
                       'Hit Ratio': IcAnadolu["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferIcAnadolufinallist = pd.merge(GenelHitRatioTransferIcAnadolulist, GenelHitRatioTransferIcAnadolulistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferIcAnadolufinallist)
GenelHitRatioTransferIcAnadolufinallist["Alert"]  = [0 if (GenelHitRatioTransferIcAnadolufinallist['Hit Ratio'][i]> GenelHitRatioTransferIcAnadolufinallist["Lower"][i]) & (GenelHitRatioTransferIcAnadolufinallist['Hit Ratio'][i]< GenelHitRatioTransferIcAnadolufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferIcAnadolufinallist[GenelHitRatioTransferIcAnadolufinallist["Alert"]==1])

#Ultimate_YenilemeIcAnadolu

GenelHitRatioYenilemeIcAnadolu = np.array(IcAnadolu["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeIcAnadolu)
for a in GenelHitRatioYenilemeIcAnadolu:
    GenelHitRatioYenilemeIcAnadolulists = [np.array(GenelHitRatioYenilemeIcAnadolu[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeIcAnadolulists)
GenelHitRatioYenilemeIcAnadolunonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeIcAnadolu[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeIcAnadolunonseasonality)
GenelHitRatioYenilemeIcAnadolupredict1 = ([GenelHitRatioYenilemeIcAnadolunonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeIcAnadolupre2 = pd.DataFrame(GenelHitRatioYenilemeIcAnadolupredict1)
GenelHitRatioYenilemeIcAnadoluIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeIcAnadolupre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeIcAnadoluLowerInterval = [(np.concatenate(GenelHitRatioYenilemeIcAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeIcAnadoluUpperInterval = [(np.concatenate(GenelHitRatioYenilemeIcAnadoluIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeIcAnadoluConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeIcAnadoluLowerInterval,
                        "Upper": GenelHitRatioYenilemeIcAnadoluUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeIcAnadolupredict1 = ([GenelHitRatioYenilemeIcAnadolunonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeIcAnadolup1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeIcAnadolup1.append(float(str(GenelHitRatioYenilemeIcAnadolupredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeIcAnadolup1)
GenelHitRatioYenilemeIcAnadolulistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeIcAnadolup1,
                          'Lower': GenelHitRatioYenilemeIcAnadoluConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeIcAnadoluConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeIcAnadolulist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeIcAnadolu’',
                       'IcAnadolu aylik hit': GenelHitRatioYenilemeIcAnadolulists,
                      'Non-Seasonality': GenelHitRatioYenilemeIcAnadolunonseasonality,
                       'Hit Ratio': IcAnadolu["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeIcAnadolufinallist = pd.merge(GenelHitRatioYenilemeIcAnadolulist, GenelHitRatioYenilemeIcAnadolulistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeIcAnadolufinallist)
GenelHitRatioYenilemeIcAnadolufinallist["Alert"]  = [0 if (GenelHitRatioYenilemeIcAnadolufinallist['Hit Ratio'][i]> GenelHitRatioYenilemeIcAnadolufinallist["Lower"][i]) & (GenelHitRatioYenilemeIcAnadolufinallist['Hit Ratio'][i]< GenelHitRatioYenilemeIcAnadolufinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeIcAnadolufinallist[GenelHitRatioYenilemeIcAnadolufinallist["Alert"]==1])


#Ultimate_Ege

GenelHitRatioEge = np.array(Ege['Ultimate Hit Ratio'])
print(GenelHitRatioEge)
for a in GenelHitRatioEge:
    GenelHitRatioEgelists = [np.array(GenelHitRatioEge[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioEgelists)
GenelHitRatioEgenonseasonality = [pm.auto_arima((np.array(GenelHitRatioEge[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioEgenonseasonality)
GenelHitRatioEgepredict1 = ([GenelHitRatioEgenonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioEgepre2 = pd.DataFrame(GenelHitRatioEgepredict1)
GenelHitRatioEgeIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioEgepre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioEgeLowerInterval = [(np.concatenate(GenelHitRatioEgeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioEgeUpperInterval = [(np.concatenate(GenelHitRatioEgeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioEgeConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioEgeLowerInterval,
                        "Upper": GenelHitRatioEgeUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioEgepredict1 = ([GenelHitRatioEgenonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioEgep1 = []
for i in range(0, 79):
    GenelHitRatioEgep1.append(float(str(GenelHitRatioEgepredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioEgep1)
GenelHitRatioEgelistpredict = pd.DataFrame({'Predict': GenelHitRatioEgep1,
                          'Lower': GenelHitRatioEgeConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioEgeConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioEgelist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioEge’',
                       'Ege aylik hit': GenelHitRatioEgelists,
                      'Non-Seasonality': GenelHitRatioEgenonseasonality,
                       'Hit Ratio': Ege['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioEgefinallist = pd.merge(GenelHitRatioEgelist, GenelHitRatioEgelistpredict, on='Sira', how='inner')
print(GenelHitRatioEgefinallist)
GenelHitRatioEgefinallist["Alert"]  = [0 if (GenelHitRatioEgefinallist['Hit Ratio'][i]> GenelHitRatioEgefinallist["Lower"][i]) & (GenelHitRatioEgefinallist['Hit Ratio'][i]< GenelHitRatioEgefinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioEgefinallist[GenelHitRatioEgefinallist["Alert"]==1])


#Ultimate_TransferEge

GenelHitRatioTransferEge = np.array(Ege["Transfer Hit Ratio"])
print(GenelHitRatioTransferEge)
for a in GenelHitRatioTransferEge:
    GenelHitRatioTransferEgelists = [np.array(GenelHitRatioTransferEge[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferEgelists)
GenelHitRatioTransferEgenonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferEge[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferEgenonseasonality)
GenelHitRatioTransferEgepredict1 = ([GenelHitRatioTransferEgenonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferEgepre2 = pd.DataFrame(GenelHitRatioTransferEgepredict1)
GenelHitRatioTransferEgeIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferEgepre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferEgeLowerInterval = [(np.concatenate(GenelHitRatioTransferEgeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferEgeUpperInterval = [(np.concatenate(GenelHitRatioTransferEgeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferEgeConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferEgeLowerInterval,
                        "Upper": GenelHitRatioTransferEgeUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferEgepredict1 = ([GenelHitRatioTransferEgenonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferEgep1 = []
for i in range(0, 79):
    GenelHitRatioTransferEgep1.append(float(str(GenelHitRatioTransferEgepredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferEgep1)
GenelHitRatioTransferEgelistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferEgep1,
                          'Lower': GenelHitRatioTransferEgeConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferEgeConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferEgelist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferEge’',
                       'Ege aylik hit': GenelHitRatioTransferEgelists,
                      'Non-Seasonality': GenelHitRatioTransferEgenonseasonality,
                       'Hit Ratio': Ege["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferEgefinallist = pd.merge(GenelHitRatioTransferEgelist, GenelHitRatioTransferEgelistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferEgefinallist)
GenelHitRatioTransferEgefinallist["Alert"]  = [0 if (GenelHitRatioTransferEgefinallist['Hit Ratio'][i]> GenelHitRatioTransferEgefinallist["Lower"][i]) & (GenelHitRatioTransferEgefinallist['Hit Ratio'][i]< GenelHitRatioTransferEgefinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferEgefinallist[GenelHitRatioTransferEgefinallist["Alert"]==1])

#Ultimate_YenilemeEge

GenelHitRatioYenilemeEge = np.array(Ege["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeEge)
for a in GenelHitRatioYenilemeEge:
    GenelHitRatioYenilemeEgelists = [np.array(GenelHitRatioYenilemeEge[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeEgelists)
GenelHitRatioYenilemeEgenonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeEge[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeEgenonseasonality)
GenelHitRatioYenilemeEgepredict1 = ([GenelHitRatioYenilemeEgenonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeEgepre2 = pd.DataFrame(GenelHitRatioYenilemeEgepredict1)
GenelHitRatioYenilemeEgeIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeEgepre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeEgeLowerInterval = [(np.concatenate(GenelHitRatioYenilemeEgeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeEgeUpperInterval = [(np.concatenate(GenelHitRatioYenilemeEgeIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeEgeConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeEgeLowerInterval,
                        "Upper": GenelHitRatioYenilemeEgeUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeEgepredict1 = ([GenelHitRatioYenilemeEgenonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeEgep1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeEgep1.append(float(str(GenelHitRatioYenilemeEgepredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeEgep1)
GenelHitRatioYenilemeEgelistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeEgep1,
                          'Lower': GenelHitRatioYenilemeEgeConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeEgeConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeEgelist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeEge’',
                       'Ege aylik hit': GenelHitRatioYenilemeEgelists,
                      'Non-Seasonality': GenelHitRatioYenilemeEgenonseasonality,
                       'Hit Ratio': Ege["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeEgefinallist = pd.merge(GenelHitRatioYenilemeEgelist, GenelHitRatioYenilemeEgelistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeEgefinallist)
GenelHitRatioYenilemeEgefinallist["Alert"]  = [0 if (GenelHitRatioYenilemeEgefinallist['Hit Ratio'][i]> GenelHitRatioYenilemeEgefinallist["Lower"][i]) & (GenelHitRatioYenilemeEgefinallist['Hit Ratio'][i]< GenelHitRatioYenilemeEgefinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeEgefinallist[GenelHitRatioYenilemeEgefinallist["Alert"]==1])

#Ultimate_Akdeniz

GenelHitRatioAkdeniz = np.array(Akdeniz['Ultimate Hit Ratio'])
print(GenelHitRatioAkdeniz)
for a in GenelHitRatioAkdeniz:
    GenelHitRatioAkdenizlists = [np.array(GenelHitRatioAkdeniz[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioAkdenizlists)
GenelHitRatioAkdeniznonseasonality = [pm.auto_arima((np.array(GenelHitRatioAkdeniz[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioAkdeniznonseasonality)
GenelHitRatioAkdenizpredict1 = ([GenelHitRatioAkdeniznonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioAkdenizpre2 = pd.DataFrame(GenelHitRatioAkdenizpredict1)
GenelHitRatioAkdenizIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioAkdenizpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioAkdenizLowerInterval = [(np.concatenate(GenelHitRatioAkdenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioAkdenizUpperInterval = [(np.concatenate(GenelHitRatioAkdenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioAkdenizConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioAkdenizLowerInterval,
                        "Upper": GenelHitRatioAkdenizUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioAkdenizpredict1 = ([GenelHitRatioAkdeniznonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioAkdenizp1 = []
for i in range(0, 79):
    GenelHitRatioAkdenizp1.append(float(str(GenelHitRatioAkdenizpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioAkdenizp1)
GenelHitRatioAkdenizlistpredict = pd.DataFrame({'Predict': GenelHitRatioAkdenizp1,
                          'Lower': GenelHitRatioAkdenizConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioAkdenizConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioAkdenizlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioAkdeniz’',
                       'Akdeniz aylik hit': GenelHitRatioAkdenizlists,
                      'Non-Seasonality': GenelHitRatioAkdeniznonseasonality,
                       'Hit Ratio': Akdeniz['Ultimate Hit Ratio'][49:],
                     'Sira': range(0,79),})
GenelHitRatioAkdenizfinallist = pd.merge(GenelHitRatioAkdenizlist, GenelHitRatioAkdenizlistpredict, on='Sira', how='inner')
print(GenelHitRatioAkdenizfinallist)
GenelHitRatioAkdenizfinallist["Alert"]  = [0 if (GenelHitRatioAkdenizfinallist['Hit Ratio'][i]> GenelHitRatioAkdenizfinallist["Lower"][i]) & (GenelHitRatioAkdenizfinallist['Hit Ratio'][i]< GenelHitRatioAkdenizfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioAkdenizfinallist[GenelHitRatioAkdenizfinallist["Alert"]==1])


#Ultimate_TransferAkdeniz

GenelHitRatioTransferAkdeniz = np.array(Akdeniz["Transfer Hit Ratio"])
print(GenelHitRatioTransferAkdeniz)
for a in GenelHitRatioTransferAkdeniz:
    GenelHitRatioTransferAkdenizlists = [np.array(GenelHitRatioTransferAkdeniz[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioTransferAkdenizlists)
GenelHitRatioTransferAkdeniznonseasonality = [pm.auto_arima((np.array(GenelHitRatioTransferAkdeniz[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioTransferAkdeniznonseasonality)
GenelHitRatioTransferAkdenizpredict1 = ([GenelHitRatioTransferAkdeniznonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioTransferAkdenizpre2 = pd.DataFrame(GenelHitRatioTransferAkdenizpredict1)
GenelHitRatioTransferAkdenizIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioTransferAkdenizpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioTransferAkdenizLowerInterval = [(np.concatenate(GenelHitRatioTransferAkdenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioTransferAkdenizUpperInterval = [(np.concatenate(GenelHitRatioTransferAkdenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioTransferAkdenizConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioTransferAkdenizLowerInterval,
                        "Upper": GenelHitRatioTransferAkdenizUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioTransferAkdenizpredict1 = ([GenelHitRatioTransferAkdeniznonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioTransferAkdenizp1 = []
for i in range(0, 79):
    GenelHitRatioTransferAkdenizp1.append(float(str(GenelHitRatioTransferAkdenizpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioTransferAkdenizp1)
GenelHitRatioTransferAkdenizlistpredict = pd.DataFrame({'Predict': GenelHitRatioTransferAkdenizp1,
                          'Lower': GenelHitRatioTransferAkdenizConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioTransferAkdenizConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioTransferAkdenizlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioTransferAkdeniz’',
                       'Akdeniz aylik hit': GenelHitRatioTransferAkdenizlists,
                      'Non-Seasonality': GenelHitRatioTransferAkdeniznonseasonality,
                       'Hit Ratio': Akdeniz["Transfer Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioTransferAkdenizfinallist = pd.merge(GenelHitRatioTransferAkdenizlist, GenelHitRatioTransferAkdenizlistpredict, on='Sira', how='inner')
print(GenelHitRatioTransferAkdenizfinallist)
GenelHitRatioTransferAkdenizfinallist["Alert"]  = [0 if (GenelHitRatioTransferAkdenizfinallist['Hit Ratio'][i]> GenelHitRatioTransferAkdenizfinallist["Lower"][i]) & (GenelHitRatioTransferAkdenizfinallist['Hit Ratio'][i]< GenelHitRatioTransferAkdenizfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioTransferAkdenizfinallist[GenelHitRatioTransferAkdenizfinallist["Alert"]==1])

#Ultimate_YenilemeAkdeniz

GenelHitRatioYenilemeAkdeniz = np.array(Akdeniz["Yenileme Hit Ratio"])
print(GenelHitRatioYenilemeAkdeniz)
for a in GenelHitRatioYenilemeAkdeniz:
    GenelHitRatioYenilemeAkdenizlists = [np.array(GenelHitRatioYenilemeAkdeniz[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatioYenilemeAkdenizlists)
GenelHitRatioYenilemeAkdeniznonseasonality = [pm.auto_arima((np.array(GenelHitRatioYenilemeAkdeniz[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatioYenilemeAkdeniznonseasonality)
GenelHitRatioYenilemeAkdenizpredict1 = ([GenelHitRatioYenilemeAkdeniznonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatioYenilemeAkdenizpre2 = pd.DataFrame(GenelHitRatioYenilemeAkdenizpredict1)
GenelHitRatioYenilemeAkdenizIntervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatioYenilemeAkdenizpre2[1],
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeAkdenizLowerInterval = [(np.concatenate(GenelHitRatioYenilemeAkdenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatioYenilemeAkdenizUpperInterval = [(np.concatenate(GenelHitRatioYenilemeAkdenizIntervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatioYenilemeAkdenizConfidence_Interval = pd.DataFrame({"Lower": GenelHitRatioYenilemeAkdenizLowerInterval,
                        "Upper": GenelHitRatioYenilemeAkdenizUpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatioYenilemeAkdenizpredict1 = ([GenelHitRatioYenilemeAkdeniznonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatioYenilemeAkdenizp1 = []
for i in range(0, 79):
    GenelHitRatioYenilemeAkdenizp1.append(float(str(GenelHitRatioYenilemeAkdenizpredict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatioYenilemeAkdenizp1)
GenelHitRatioYenilemeAkdenizlistpredict = pd.DataFrame({'Predict': GenelHitRatioYenilemeAkdenizp1,
                          'Lower': GenelHitRatioYenilemeAkdenizConfidence_Interval["Lower"],
                            'Upper': GenelHitRatioYenilemeAkdenizConfidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatioYenilemeAkdenizlist = pd.DataFrame({ 'Genel %10' : 'GenelHitRatioYenilemeAkdeniz’',
                       'Akdeniz aylik hit': GenelHitRatioYenilemeAkdenizlists,
                      'Non-Seasonality': GenelHitRatioYenilemeAkdeniznonseasonality,
                       'Hit Ratio': Akdeniz["Yenileme Hit Ratio"][49:],
                     'Sira': range(0,79),})
GenelHitRatioYenilemeAkdenizfinallist = pd.merge(GenelHitRatioYenilemeAkdenizlist, GenelHitRatioYenilemeAkdenizlistpredict, on='Sira', how='inner')
print(GenelHitRatioYenilemeAkdenizfinallist)
GenelHitRatioYenilemeAkdenizfinallist["Alert"]  = [0 if (GenelHitRatioYenilemeAkdenizfinallist['Hit Ratio'][i]> GenelHitRatioYenilemeAkdenizfinallist["Lower"][i]) & (GenelHitRatioYenilemeAkdenizfinallist['Hit Ratio'][i]< GenelHitRatioYenilemeAkdenizfinallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatioYenilemeAkdenizfinallist[GenelHitRatioYenilemeAkdenizfinallist["Alert"]==1])

#Ultimate_1Transfer60

GenelHitRatio1Transfer60 = np.array(Transfer60[1])
print(GenelHitRatio1Transfer60)
for a in GenelHitRatio1Transfer60:
    GenelHitRatio1Transfer60lists = [np.array(GenelHitRatio1Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Transfer60lists)
GenelHitRatio1Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Transfer60nonseasonality)
GenelHitRatio1Transfer60predict1 = ([GenelHitRatio1Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Transfer60pre2 = pd.DataFrame(GenelHitRatio1Transfer60predict1)
GenelHitRatio1Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer60LowerInterval = [(np.concatenate(GenelHitRatio1Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Transfer60UpperInterval = [(np.concatenate(GenelHitRatio1Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
 GenelHitRatio1Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Transfer60LowerInterval,
                        "Upper": GenelHitRatio1Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer60predict1 = ([GenelHitRatio1Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio1Transfer60p1.append(float(str(GenelHitRatio1Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Transfer60p1)
GenelHitRatio1Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio1Transfer60p1,
                          'Lower': GenelHitRatio1Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio1Transfer60lists,
                      'Non-Seasonality': GenelHitRatio1Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Transfer60finallist = pd.merge(GenelHitRatio1Transfer60list, GenelHitRatio1Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio1Transfer60finallist)
GenelHitRatio1Transfer60finallist["Alert"]  = [0 if (GenelHitRatio1Transfer60finallist['Hit Ratio'][i]> GenelHitRatio1Transfer60finallist["Lower"][i]) & (GenelHitRatio1Transfer60finallist['Hit Ratio'][i]< GenelHitRatio1Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Transfer60finallist[GenelHitRatio1Transfer60finallist["Alert"]==1])

#Ultimate_6Transfer60

GenelHitRatio6Transfer60 = np.array(Transfer60[6])
print(GenelHitRatio6Transfer60)
for a in GenelHitRatio6Transfer60:
    GenelHitRatio6Transfer60lists = [np.array(GenelHitRatio6Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Transfer60lists)
GenelHitRatio6Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Transfer60nonseasonality)
GenelHitRatio6Transfer60predict1 = ([GenelHitRatio6Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Transfer60pre2 = pd.DataFrame(GenelHitRatio6Transfer60predict1)
GenelHitRatio6Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer60LowerInterval = [(np.concatenate(GenelHitRatio6Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Transfer60UpperInterval = [(np.concatenate(GenelHitRatio6Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Transfer60LowerInterval,
                        "Upper": GenelHitRatio6Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer60predict1 = ([GenelHitRatio6Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio6Transfer60p1.append(float(str(GenelHitRatio6Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Transfer60p1)
GenelHitRatio6Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio6Transfer60p1,
                          'Lower': GenelHitRatio6Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio6Transfer60lists,
                      'Non-Seasonality': GenelHitRatio6Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Transfer60finallist = pd.merge(GenelHitRatio6Transfer60list, GenelHitRatio6Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio6Transfer60finallist)
GenelHitRatio6Transfer60finallist["Alert"]  = [0 if (GenelHitRatio6Transfer60finallist['Hit Ratio'][i]> GenelHitRatio6Transfer60finallist["Lower"][i]) & (GenelHitRatio6Transfer60finallist['Hit Ratio'][i]< GenelHitRatio6Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Transfer60finallist[GenelHitRatio6Transfer60finallist["Alert"]==1])

#Ultimate_7Transfer60

GenelHitRatio7Transfer60 = np.array(Transfer60[7])
print(GenelHitRatio7Transfer60)
for a in GenelHitRatio7Transfer60:
    GenelHitRatio7Transfer60lists = [np.array(GenelHitRatio7Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Transfer60lists)
GenelHitRatio7Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Transfer60nonseasonality)
GenelHitRatio7Transfer60predict1 = ([GenelHitRatio7Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Transfer60pre2 = pd.DataFrame(GenelHitRatio7Transfer60predict1)
GenelHitRatio7Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer60LowerInterval = [(np.concatenate(GenelHitRatio7Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Transfer60UpperInterval = [(np.concatenate(GenelHitRatio7Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Transfer60LowerInterval,
                        "Upper": GenelHitRatio7Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer60predict1 = ([GenelHitRatio7Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio7Transfer60p1.append(float(str(GenelHitRatio7Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Transfer60p1)
GenelHitRatio7Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio7Transfer60p1,
                          'Lower': GenelHitRatio7Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio7Transfer60lists,
                      'Non-Seasonality': GenelHitRatio7Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Transfer60finallist = pd.merge(GenelHitRatio7Transfer60list, GenelHitRatio7Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio7Transfer60finallist)
GenelHitRatio7Transfer60finallist["Alert"]  = [0 if (GenelHitRatio7Transfer60finallist['Hit Ratio'][i]> GenelHitRatio7Transfer60finallist["Lower"][i]) & (GenelHitRatio7Transfer60finallist['Hit Ratio'][i]< GenelHitRatio7Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Transfer60finallist[GenelHitRatio7Transfer60finallist["Alert"]==1])

#Ultimate_16Transfer60

GenelHitRatio16Transfer60 = np.array(Transfer60[16])
print(GenelHitRatio16Transfer60)
for a in GenelHitRatio16Transfer60:
    GenelHitRatio16Transfer60lists = [np.array(GenelHitRatio16Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Transfer60lists)
GenelHitRatio16Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Transfer60nonseasonality)
GenelHitRatio16Transfer60predict1 = ([GenelHitRatio16Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Transfer60pre2 = pd.DataFrame(GenelHitRatio16Transfer60predict1)
GenelHitRatio16Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer60LowerInterval = [(np.concatenate(GenelHitRatio16Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Transfer60UpperInterval = [(np.concatenate(GenelHitRatio16Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Transfer60LowerInterval,
                        "Upper": GenelHitRatio16Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer60predict1 = ([GenelHitRatio16Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio16Transfer60p1.append(float(str(GenelHitRatio16Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Transfer60p1)
GenelHitRatio16Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio16Transfer60p1,
                          'Lower': GenelHitRatio16Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio16Transfer60lists,
                      'Non-Seasonality': GenelHitRatio16Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Transfer60finallist = pd.merge(GenelHitRatio16Transfer60list, GenelHitRatio16Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio16Transfer60finallist)
GenelHitRatio16Transfer60finallist["Alert"]  = [0 if (GenelHitRatio16Transfer60finallist['Hit Ratio'][i]> GenelHitRatio16Transfer60finallist["Lower"][i]) & (GenelHitRatio16Transfer60finallist['Hit Ratio'][i]< GenelHitRatio16Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Transfer60finallist[GenelHitRatio16Transfer60finallist["Alert"]==1])

#Ultimate_33Transfer60

GenelHitRatio33Transfer60 = np.array(Transfer60[33])
print(GenelHitRatio33Transfer60)
for a in GenelHitRatio33Transfer60:
    GenelHitRatio33Transfer60lists = [np.array(GenelHitRatio33Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Transfer60lists)
GenelHitRatio33Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Transfer60nonseasonality)
GenelHitRatio33Transfer60predict1 = ([GenelHitRatio33Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Transfer60pre2 = pd.DataFrame(GenelHitRatio33Transfer60predict1)
GenelHitRatio33Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer60LowerInterval = [(np.concatenate(GenelHitRatio33Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Transfer60UpperInterval = [(np.concatenate(GenelHitRatio33Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Transfer60LowerInterval,
                        "Upper": GenelHitRatio33Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer60predict1 = ([GenelHitRatio33Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio33Transfer60p1.append(float(str(GenelHitRatio33Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Transfer60p1)
GenelHitRatio33Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio33Transfer60p1,
                          'Lower': GenelHitRatio33Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio33Transfer60lists,
                      'Non-Seasonality': GenelHitRatio33Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Transfer60finallist = pd.merge(GenelHitRatio33Transfer60list, GenelHitRatio33Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio33Transfer60finallist)
GenelHitRatio33Transfer60finallist["Alert"]  = [0 if (GenelHitRatio33Transfer60finallist['Hit Ratio'][i]> GenelHitRatio33Transfer60finallist["Lower"][i]) & (GenelHitRatio33Transfer60finallist['Hit Ratio'][i]< GenelHitRatio33Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Transfer60finallist[GenelHitRatio33Transfer60finallist["Alert"]==1])


#Ultimate_34Transfer60

GenelHitRatio34Transfer60 = np.array(Transfer60[34])
print(GenelHitRatio34Transfer60)
for a in GenelHitRatio34Transfer60:
    GenelHitRatio34Transfer60lists = [np.array(GenelHitRatio34Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Transfer60lists)
GenelHitRatio34Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Transfer60nonseasonality)
GenelHitRatio34Transfer60predict1 = ([GenelHitRatio34Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Transfer60pre2 = pd.DataFrame(GenelHitRatio34Transfer60predict1)
GenelHitRatio34Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer60LowerInterval = [(np.concatenate(GenelHitRatio34Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Transfer60UpperInterval = [(np.concatenate(GenelHitRatio34Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Transfer60LowerInterval,
                        "Upper": GenelHitRatio34Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer60predict1 = ([GenelHitRatio34Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio34Transfer60p1.append(float(str(GenelHitRatio34Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Transfer60p1)
GenelHitRatio34Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio34Transfer60p1,
                          'Lower': GenelHitRatio34Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio34Transfer60lists,
                      'Non-Seasonality': GenelHitRatio34Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Transfer60finallist = pd.merge(GenelHitRatio34Transfer60list, GenelHitRatio34Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio34Transfer60finallist)
GenelHitRatio34Transfer60finallist["Alert"]  = [0 if (GenelHitRatio34Transfer60finallist['Hit Ratio'][i]> GenelHitRatio34Transfer60finallist["Lower"][i]) & (GenelHitRatio34Transfer60finallist['Hit Ratio'][i]< GenelHitRatio34Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Transfer60finallist[GenelHitRatio34Transfer60finallist["Alert"]==1])

#Ultimate_35Transfer60

GenelHitRatio35Transfer60 = np.array(Transfer60[35])
print(GenelHitRatio35Transfer60)
for a in GenelHitRatio35Transfer60:
    GenelHitRatio35Transfer60lists = [np.array(GenelHitRatio35Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Transfer60lists)
GenelHitRatio35Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Transfer60nonseasonality)
GenelHitRatio35Transfer60predict1 = ([GenelHitRatio35Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Transfer60pre2 = pd.DataFrame(GenelHitRatio35Transfer60predict1)
GenelHitRatio35Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer60LowerInterval = [(np.concatenate(GenelHitRatio35Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Transfer60UpperInterval = [(np.concatenate(GenelHitRatio35Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Transfer60LowerInterval,
                        "Upper": GenelHitRatio35Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer60predict1 = ([GenelHitRatio35Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio35Transfer60p1.append(float(str(GenelHitRatio35Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Transfer60p1)
GenelHitRatio35Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio35Transfer60p1,
                          'Lower': GenelHitRatio35Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio35Transfer60lists,
                      'Non-Seasonality': GenelHitRatio35Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Transfer60finallist = pd.merge(GenelHitRatio35Transfer60list, GenelHitRatio35Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio35Transfer60finallist)
GenelHitRatio35Transfer60finallist["Alert"]  = [0 if (GenelHitRatio35Transfer60finallist['Hit Ratio'][i]> GenelHitRatio35Transfer60finallist["Lower"][i]) & (GenelHitRatio35Transfer60finallist['Hit Ratio'][i]< GenelHitRatio35Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Transfer60finallist[GenelHitRatio35Transfer60finallist["Alert"]==1])

#Ultimate_38Transfer60

GenelHitRatio38Transfer60 = np.array(Transfer60[38])
print(GenelHitRatio38Transfer60)
for a in GenelHitRatio38Transfer60:
    GenelHitRatio38Transfer60lists = [np.array(GenelHitRatio38Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Transfer60lists)
GenelHitRatio38Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Transfer60nonseasonality)
GenelHitRatio38Transfer60predict1 = ([GenelHitRatio38Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Transfer60pre2 = pd.DataFrame(GenelHitRatio38Transfer60predict1)
GenelHitRatio38Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer60LowerInterval = [(np.concatenate(GenelHitRatio38Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Transfer60UpperInterval = [(np.concatenate(GenelHitRatio38Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Transfer60LowerInterval,
                        "Upper": GenelHitRatio38Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer60predict1 = ([GenelHitRatio38Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio38Transfer60p1.append(float(str(GenelHitRatio38Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Transfer60p1)
GenelHitRatio38Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio38Transfer60p1,
                          'Lower': GenelHitRatio38Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio38Transfer60lists,
                      'Non-Seasonality': GenelHitRatio38Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Transfer60finallist = pd.merge(GenelHitRatio38Transfer60list, GenelHitRatio38Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio38Transfer60finallist)
GenelHitRatio38Transfer60finallist["Alert"]  = [0 if (GenelHitRatio38Transfer60finallist['Hit Ratio'][i]> GenelHitRatio38Transfer60finallist["Lower"][i]) & (GenelHitRatio38Transfer60finallist['Hit Ratio'][i]< GenelHitRatio38Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Transfer60finallist[GenelHitRatio38Transfer60finallist["Alert"]==1])

#Ultimate_41Transfer60

GenelHitRatio41Transfer60 = np.array(Transfer60[41])
print(GenelHitRatio41Transfer60)
for a in GenelHitRatio41Transfer60:
    GenelHitRatio41Transfer60lists = [np.array(GenelHitRatio41Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Transfer60lists)
GenelHitRatio41Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Transfer60nonseasonality)
GenelHitRatio41Transfer60predict1 = ([GenelHitRatio41Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Transfer60pre2 = pd.DataFrame(GenelHitRatio41Transfer60predict1)
GenelHitRatio41Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer60LowerInterval = [(np.concatenate(GenelHitRatio41Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Transfer60UpperInterval = [(np.concatenate(GenelHitRatio41Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Transfer60LowerInterval,
                        "Upper": GenelHitRatio41Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer60predict1 = ([GenelHitRatio41Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio41Transfer60p1.append(float(str(GenelHitRatio41Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Transfer60p1)
GenelHitRatio41Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio41Transfer60p1,
                          'Lower': GenelHitRatio41Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio41Transfer60lists,
                      'Non-Seasonality': GenelHitRatio41Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Transfer60finallist = pd.merge(GenelHitRatio41Transfer60list, GenelHitRatio41Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio41Transfer60finallist)
GenelHitRatio41Transfer60finallist["Alert"]  = [0 if (GenelHitRatio41Transfer60finallist['Hit Ratio'][i]> GenelHitRatio41Transfer60finallist["Lower"][i]) & (GenelHitRatio41Transfer60finallist['Hit Ratio'][i]< GenelHitRatio41Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Transfer60finallist[GenelHitRatio41Transfer60finallist["Alert"]==1])

#Ultimate_55Transfer60

GenelHitRatio55Transfer60 = np.array(Transfer60[55])
print(GenelHitRatio55Transfer60)
for a in GenelHitRatio55Transfer60:
    GenelHitRatio55Transfer60lists = [np.array(GenelHitRatio55Transfer60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Transfer60lists)
GenelHitRatio55Transfer60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Transfer60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Transfer60nonseasonality)
GenelHitRatio55Transfer60predict1 = ([GenelHitRatio55Transfer60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Transfer60pre2 = pd.DataFrame(GenelHitRatio55Transfer60predict1)
GenelHitRatio55Transfer60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Transfer60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer60LowerInterval = [(np.concatenate(GenelHitRatio55Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Transfer60UpperInterval = [(np.concatenate(GenelHitRatio55Transfer60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Transfer60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Transfer60LowerInterval,
                        "Upper": GenelHitRatio55Transfer60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer60predict1 = ([GenelHitRatio55Transfer60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Transfer60p1 = []
for i in range(0, 79):
    GenelHitRatio55Transfer60p1.append(float(str(GenelHitRatio55Transfer60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Transfer60p1)
GenelHitRatio55Transfer60listpredict = pd.DataFrame({'Predict': GenelHitRatio55Transfer60p1,
                          'Lower': GenelHitRatio55Transfer60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Transfer60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Transfer60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Transfer60’',
                       'Transfer60 aylik hit': GenelHitRatio55Transfer60lists,
                      'Non-Seasonality': GenelHitRatio55Transfer60nonseasonality,
                       'Hit Ratio': Transfer60[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Transfer60finallist = pd.merge(GenelHitRatio55Transfer60list, GenelHitRatio55Transfer60listpredict, on='Sira', how='inner')
print(GenelHitRatio55Transfer60finallist)
GenelHitRatio55Transfer60finallist["Alert"]  = [0 if (GenelHitRatio55Transfer60finallist['Hit Ratio'][i]> GenelHitRatio55Transfer60finallist["Lower"][i]) & (GenelHitRatio55Transfer60finallist['Hit Ratio'][i]< GenelHitRatio55Transfer60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Transfer60finallist[GenelHitRatio55Transfer60finallist["Alert"]==1])


#Ultimate_1Transfer55

GenelHitRatio1Transfer55 = np.array(Transfer55[1])
print(GenelHitRatio1Transfer55)
for a in GenelHitRatio1Transfer55:
    GenelHitRatio1Transfer55lists = [np.array(GenelHitRatio1Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Transfer55lists)
GenelHitRatio1Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Transfer55nonseasonality)
GenelHitRatio1Transfer55predict1 = ([GenelHitRatio1Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Transfer55pre2 = pd.DataFrame(GenelHitRatio1Transfer55predict1)
GenelHitRatio1Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer55LowerInterval = [(np.concatenate(GenelHitRatio1Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Transfer55UpperInterval = [(np.concatenate(GenelHitRatio1Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Transfer55LowerInterval,
                        "Upper": GenelHitRatio1Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer55predict1 = ([GenelHitRatio1Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio1Transfer55p1.append(float(str(GenelHitRatio1Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Transfer55p1)
GenelHitRatio1Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio1Transfer55p1,
                          'Lower': GenelHitRatio1Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio1Transfer55lists,
                      'Non-Seasonality': GenelHitRatio1Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Transfer55finallist = pd.merge(GenelHitRatio1Transfer55list, GenelHitRatio1Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio1Transfer55finallist)
GenelHitRatio1Transfer55finallist["Alert"]  = [0 if (GenelHitRatio1Transfer55finallist['Hit Ratio'][i]> GenelHitRatio1Transfer55finallist["Lower"][i]) & (GenelHitRatio1Transfer55finallist['Hit Ratio'][i]< GenelHitRatio1Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Transfer55finallist[GenelHitRatio1Transfer55finallist["Alert"]==1])

#Ultimate_6Transfer55

GenelHitRatio6Transfer55 = np.array(Transfer55[6])
print(GenelHitRatio6Transfer55)
for a in GenelHitRatio6Transfer55:
    GenelHitRatio6Transfer55lists = [np.array(GenelHitRatio6Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Transfer55lists)
GenelHitRatio6Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Transfer55nonseasonality)
GenelHitRatio6Transfer55predict1 = ([GenelHitRatio6Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Transfer55pre2 = pd.DataFrame(GenelHitRatio6Transfer55predict1)
GenelHitRatio6Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer55LowerInterval = [(np.concatenate(GenelHitRatio6Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Transfer55UpperInterval = [(np.concatenate(GenelHitRatio6Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Transfer55LowerInterval,
                        "Upper": GenelHitRatio6Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer55predict1 = ([GenelHitRatio6Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio6Transfer55p1.append(float(str(GenelHitRatio6Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Transfer55p1)
GenelHitRatio6Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio6Transfer55p1,
                          'Lower': GenelHitRatio6Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio6Transfer55lists,
                      'Non-Seasonality': GenelHitRatio6Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Transfer55finallist = pd.merge(GenelHitRatio6Transfer55list, GenelHitRatio6Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio6Transfer55finallist)
GenelHitRatio6Transfer55finallist["Alert"]  = [0 if (GenelHitRatio6Transfer55finallist['Hit Ratio'][i]> GenelHitRatio6Transfer55finallist["Lower"][i]) & (GenelHitRatio6Transfer55finallist['Hit Ratio'][i]< GenelHitRatio6Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Transfer55finallist[GenelHitRatio6Transfer55finallist["Alert"]==1])

#Ultimate_7Transfer55

GenelHitRatio7Transfer55 = np.array(Transfer55[7])
print(GenelHitRatio7Transfer55)
for a in GenelHitRatio7Transfer55:
    GenelHitRatio7Transfer55lists = [np.array(GenelHitRatio7Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Transfer55lists)
GenelHitRatio7Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Transfer55nonseasonality)
GenelHitRatio7Transfer55predict1 = ([GenelHitRatio7Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Transfer55pre2 = pd.DataFrame(GenelHitRatio7Transfer55predict1)
GenelHitRatio7Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer55LowerInterval = [(np.concatenate(GenelHitRatio7Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Transfer55UpperInterval = [(np.concatenate(GenelHitRatio7Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Transfer55LowerInterval,
                        "Upper": GenelHitRatio7Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer55predict1 = ([GenelHitRatio7Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio7Transfer55p1.append(float(str(GenelHitRatio7Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Transfer55p1)
GenelHitRatio7Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio7Transfer55p1,
                          'Lower': GenelHitRatio7Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio7Transfer55lists,
                      'Non-Seasonality': GenelHitRatio7Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Transfer55finallist = pd.merge(GenelHitRatio7Transfer55list, GenelHitRatio7Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio7Transfer55finallist)
GenelHitRatio7Transfer55finallist["Alert"]  = [0 if (GenelHitRatio7Transfer55finallist['Hit Ratio'][i]> GenelHitRatio7Transfer55finallist["Lower"][i]) & (GenelHitRatio7Transfer55finallist['Hit Ratio'][i]< GenelHitRatio7Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Transfer55finallist[GenelHitRatio7Transfer55finallist["Alert"]==1])

#Ultimate_16Transfer55

GenelHitRatio16Transfer55 = np.array(Transfer55[16])
print(GenelHitRatio16Transfer55)
for a in GenelHitRatio16Transfer55:
    GenelHitRatio16Transfer55lists = [np.array(GenelHitRatio16Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Transfer55lists)
GenelHitRatio16Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Transfer55nonseasonality)
GenelHitRatio16Transfer55predict1 = ([GenelHitRatio16Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Transfer55pre2 = pd.DataFrame(GenelHitRatio16Transfer55predict1)
GenelHitRatio16Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer55LowerInterval = [(np.concatenate(GenelHitRatio16Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Transfer55UpperInterval = [(np.concatenate(GenelHitRatio16Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Transfer55LowerInterval,
                        "Upper": GenelHitRatio16Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer55predict1 = ([GenelHitRatio16Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio16Transfer55p1.append(float(str(GenelHitRatio16Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Transfer55p1)
GenelHitRatio16Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio16Transfer55p1,
                          'Lower': GenelHitRatio16Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio16Transfer55lists,
                      'Non-Seasonality': GenelHitRatio16Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Transfer55finallist = pd.merge(GenelHitRatio16Transfer55list, GenelHitRatio16Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio16Transfer55finallist)
GenelHitRatio16Transfer55finallist["Alert"]  = [0 if (GenelHitRatio16Transfer55finallist['Hit Ratio'][i]> GenelHitRatio16Transfer55finallist["Lower"][i]) & (GenelHitRatio16Transfer55finallist['Hit Ratio'][i]< GenelHitRatio16Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Transfer55finallist[GenelHitRatio16Transfer55finallist["Alert"]==1])

#Ultimate_33Transfer55

GenelHitRatio33Transfer55 = np.array(Transfer55[33])
print(GenelHitRatio33Transfer55)
for a in GenelHitRatio33Transfer55:
    GenelHitRatio33Transfer55lists = [np.array(GenelHitRatio33Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Transfer55lists)
GenelHitRatio33Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Transfer55nonseasonality)
GenelHitRatio33Transfer55predict1 = ([GenelHitRatio33Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Transfer55pre2 = pd.DataFrame(GenelHitRatio33Transfer55predict1)
GenelHitRatio33Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer55LowerInterval = [(np.concatenate(GenelHitRatio33Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Transfer55UpperInterval = [(np.concatenate(GenelHitRatio33Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Transfer55LowerInterval,
                        "Upper": GenelHitRatio33Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer55predict1 = ([GenelHitRatio33Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio33Transfer55p1.append(float(str(GenelHitRatio33Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Transfer55p1)
GenelHitRatio33Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio33Transfer55p1,
                          'Lower': GenelHitRatio33Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio33Transfer55lists,
                      'Non-Seasonality': GenelHitRatio33Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Transfer55finallist = pd.merge(GenelHitRatio33Transfer55list, GenelHitRatio33Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio33Transfer55finallist)
GenelHitRatio33Transfer55finallist["Alert"]  = [0 if (GenelHitRatio33Transfer55finallist['Hit Ratio'][i]> GenelHitRatio33Transfer55finallist["Lower"][i]) & (GenelHitRatio33Transfer55finallist['Hit Ratio'][i]< GenelHitRatio33Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Transfer55finallist[GenelHitRatio33Transfer55finallist["Alert"]==1])

#Ultimate_34Transfer55

GenelHitRatio34Transfer55 = np.array(Transfer55[34])
print(GenelHitRatio34Transfer55)
for a in GenelHitRatio34Transfer55:
    GenelHitRatio34Transfer55lists = [np.array(GenelHitRatio34Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Transfer55lists)
GenelHitRatio34Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Transfer55nonseasonality)
GenelHitRatio34Transfer55predict1 = ([GenelHitRatio34Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Transfer55pre2 = pd.DataFrame(GenelHitRatio34Transfer55predict1)
GenelHitRatio34Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer55LowerInterval = [(np.concatenate(GenelHitRatio34Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Transfer55UpperInterval = [(np.concatenate(GenelHitRatio34Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Transfer55LowerInterval,
                        "Upper": GenelHitRatio34Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer55predict1 = ([GenelHitRatio34Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio34Transfer55p1.append(float(str(GenelHitRatio34Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Transfer55p1)
GenelHitRatio34Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio34Transfer55p1,
                          'Lower': GenelHitRatio34Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio34Transfer55lists,
                      'Non-Seasonality': GenelHitRatio34Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Transfer55finallist = pd.merge(GenelHitRatio34Transfer55list, GenelHitRatio34Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio34Transfer55finallist)
GenelHitRatio34Transfer55finallist["Alert"]  = [0 if (GenelHitRatio34Transfer55finallist['Hit Ratio'][i]> GenelHitRatio34Transfer55finallist["Lower"][i]) & (GenelHitRatio34Transfer55finallist['Hit Ratio'][i]< GenelHitRatio34Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Transfer55finallist[GenelHitRatio34Transfer55finallist["Alert"]==1])



#Ultimate_35Transfer55

GenelHitRatio35Transfer55 = np.array(Transfer55[35])
print(GenelHitRatio35Transfer55)
for a in GenelHitRatio35Transfer55:
    GenelHitRatio35Transfer55lists = [np.array(GenelHitRatio35Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Transfer55lists)
GenelHitRatio35Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Transfer55nonseasonality)
GenelHitRatio35Transfer55predict1 = ([GenelHitRatio35Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Transfer55pre2 = pd.DataFrame(GenelHitRatio35Transfer55predict1)
GenelHitRatio35Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer55LowerInterval = [(np.concatenate(GenelHitRatio35Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Transfer55UpperInterval = [(np.concatenate(GenelHitRatio35Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Transfer55LowerInterval,
                        "Upper": GenelHitRatio35Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer55predict1 = ([GenelHitRatio35Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio35Transfer55p1.append(float(str(GenelHitRatio35Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Transfer55p1)
GenelHitRatio35Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio35Transfer55p1,
                          'Lower': GenelHitRatio35Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio35Transfer55lists,
                      'Non-Seasonality': GenelHitRatio35Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Transfer55finallist = pd.merge(GenelHitRatio35Transfer55list, GenelHitRatio35Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio35Transfer55finallist)
GenelHitRatio35Transfer55finallist["Alert"]  = [0 if (GenelHitRatio35Transfer55finallist['Hit Ratio'][i]> GenelHitRatio35Transfer55finallist["Lower"][i]) & (GenelHitRatio35Transfer55finallist['Hit Ratio'][i]< GenelHitRatio35Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Transfer55finallist[GenelHitRatio35Transfer55finallist["Alert"]==1])

#Ultimate_38Transfer55

GenelHitRatio38Transfer55 = np.array(Transfer55[38])
print(GenelHitRatio38Transfer55)
for a in GenelHitRatio38Transfer55:
    GenelHitRatio38Transfer55lists = [np.array(GenelHitRatio38Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Transfer55lists)
GenelHitRatio38Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Transfer55nonseasonality)
GenelHitRatio38Transfer55predict1 = ([GenelHitRatio38Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Transfer55pre2 = pd.DataFrame(GenelHitRatio38Transfer55predict1)
GenelHitRatio38Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer55LowerInterval = [(np.concatenate(GenelHitRatio38Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Transfer55UpperInterval = [(np.concatenate(GenelHitRatio38Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Transfer55LowerInterval,
                        "Upper": GenelHitRatio38Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer55predict1 = ([GenelHitRatio38Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio38Transfer55p1.append(float(str(GenelHitRatio38Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Transfer55p1)
GenelHitRatio38Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio38Transfer55p1,
                          'Lower': GenelHitRatio38Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio38Transfer55lists,
                      'Non-Seasonality': GenelHitRatio38Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Transfer55finallist = pd.merge(GenelHitRatio38Transfer55list, GenelHitRatio38Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio38Transfer55finallist)
GenelHitRatio38Transfer55finallist["Alert"]  = [0 if (GenelHitRatio38Transfer55finallist['Hit Ratio'][i]> GenelHitRatio38Transfer55finallist["Lower"][i]) & (GenelHitRatio38Transfer55finallist['Hit Ratio'][i]< GenelHitRatio38Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Transfer55finallist[GenelHitRatio38Transfer55finallist["Alert"]==1])

#Ultimate_41Transfer55

GenelHitRatio41Transfer55 = np.array(Transfer55[41])
print(GenelHitRatio41Transfer55)
for a in GenelHitRatio41Transfer55:
    GenelHitRatio41Transfer55lists = [np.array(GenelHitRatio41Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Transfer55lists)
GenelHitRatio41Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Transfer55nonseasonality)
GenelHitRatio41Transfer55predict1 = ([GenelHitRatio41Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Transfer55pre2 = pd.DataFrame(GenelHitRatio41Transfer55predict1)
GenelHitRatio41Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer55LowerInterval = [(np.concatenate(GenelHitRatio41Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Transfer55UpperInterval = [(np.concatenate(GenelHitRatio41Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Transfer55LowerInterval,
                        "Upper": GenelHitRatio41Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer55predict1 = ([GenelHitRatio41Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio41Transfer55p1.append(float(str(GenelHitRatio41Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Transfer55p1)
GenelHitRatio41Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio41Transfer55p1,
                          'Lower': GenelHitRatio41Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio41Transfer55lists,
                      'Non-Seasonality': GenelHitRatio41Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Transfer55finallist = pd.merge(GenelHitRatio41Transfer55list, GenelHitRatio41Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio41Transfer55finallist)
GenelHitRatio41Transfer55finallist["Alert"]  = [0 if (GenelHitRatio41Transfer55finallist['Hit Ratio'][i]> GenelHitRatio41Transfer55finallist["Lower"][i]) & (GenelHitRatio41Transfer55finallist['Hit Ratio'][i]< GenelHitRatio41Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Transfer55finallist[GenelHitRatio41Transfer55finallist["Alert"]==1])

#Ultimate_55Transfer55

GenelHitRatio55Transfer55 = np.array(Transfer55[55])
print(GenelHitRatio55Transfer55)
for a in GenelHitRatio55Transfer55:
    GenelHitRatio55Transfer55lists = [np.array(GenelHitRatio55Transfer55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Transfer55lists)
GenelHitRatio55Transfer55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Transfer55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Transfer55nonseasonality)
GenelHitRatio55Transfer55predict1 = ([GenelHitRatio55Transfer55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Transfer55pre2 = pd.DataFrame(GenelHitRatio55Transfer55predict1)
GenelHitRatio55Transfer55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Transfer55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer55LowerInterval = [(np.concatenate(GenelHitRatio55Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Transfer55UpperInterval = [(np.concatenate(GenelHitRatio55Transfer55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Transfer55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Transfer55LowerInterval,
                        "Upper": GenelHitRatio55Transfer55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer55predict1 = ([GenelHitRatio55Transfer55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Transfer55p1 = []
for i in range(0, 79):
    GenelHitRatio55Transfer55p1.append(float(str(GenelHitRatio55Transfer55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Transfer55p1)
GenelHitRatio55Transfer55listpredict = pd.DataFrame({'Predict': GenelHitRatio55Transfer55p1,
                          'Lower': GenelHitRatio55Transfer55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Transfer55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Transfer55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Transfer55’',
                       'Transfer55 aylik hit': GenelHitRatio55Transfer55lists,
                      'Non-Seasonality': GenelHitRatio55Transfer55nonseasonality,
                       'Hit Ratio': Transfer55[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Transfer55finallist = pd.merge(GenelHitRatio55Transfer55list, GenelHitRatio55Transfer55listpredict, on='Sira', how='inner')
print(GenelHitRatio55Transfer55finallist)
GenelHitRatio55Transfer55finallist["Alert"]  = [0 if (GenelHitRatio55Transfer55finallist['Hit Ratio'][i]> GenelHitRatio55Transfer55finallist["Lower"][i]) & (GenelHitRatio55Transfer55finallist['Hit Ratio'][i]< GenelHitRatio55Transfer55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Transfer55finallist[GenelHitRatio55Transfer55finallist["Alert"]==1])

#Ultimate_1Transfer50

GenelHitRatio1Transfer50 = np.array(Transfer50[1])
print(GenelHitRatio1Transfer50)
for a in GenelHitRatio1Transfer50:
    GenelHitRatio1Transfer50lists = [np.array(GenelHitRatio1Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Transfer50lists)
GenelHitRatio1Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Transfer50nonseasonality)
GenelHitRatio1Transfer50predict1 = ([GenelHitRatio1Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Transfer50pre2 = pd.DataFrame(GenelHitRatio1Transfer50predict1)
GenelHitRatio1Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer50LowerInterval = [(np.concatenate(GenelHitRatio1Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Transfer50UpperInterval = [(np.concatenate(GenelHitRatio1Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Transfer50LowerInterval,
                        "Upper": GenelHitRatio1Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer50predict1 = ([GenelHitRatio1Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio1Transfer50p1.append(float(str(GenelHitRatio1Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Transfer50p1)
GenelHitRatio1Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio1Transfer50p1,
                          'Lower': GenelHitRatio1Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio1Transfer50lists,
                      'Non-Seasonality': GenelHitRatio1Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Transfer50finallist = pd.merge(GenelHitRatio1Transfer50list, GenelHitRatio1Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio1Transfer50finallist)
GenelHitRatio1Transfer50finallist["Alert"]  = [0 if (GenelHitRatio1Transfer50finallist['Hit Ratio'][i]> GenelHitRatio1Transfer50finallist["Lower"][i]) & (GenelHitRatio1Transfer50finallist['Hit Ratio'][i]< GenelHitRatio1Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Transfer50finallist[GenelHitRatio1Transfer50finallist["Alert"]==1])

#Ultimate_6Transfer50

GenelHitRatio6Transfer50 = np.array(Transfer50[6])
print(GenelHitRatio6Transfer50)
for a in GenelHitRatio6Transfer50:
    GenelHitRatio6Transfer50lists = [np.array(GenelHitRatio6Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Transfer50lists)
GenelHitRatio6Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Transfer50nonseasonality)
GenelHitRatio6Transfer50predict1 = ([GenelHitRatio6Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Transfer50pre2 = pd.DataFrame(GenelHitRatio6Transfer50predict1)
GenelHitRatio6Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer50LowerInterval = [(np.concatenate(GenelHitRatio6Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Transfer50UpperInterval = [(np.concatenate(GenelHitRatio6Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Transfer50LowerInterval,
                        "Upper": GenelHitRatio6Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer50predict1 = ([GenelHitRatio6Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio6Transfer50p1.append(float(str(GenelHitRatio6Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Transfer50p1)
GenelHitRatio6Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio6Transfer50p1,
                          'Lower': GenelHitRatio6Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio6Transfer50lists,
                      'Non-Seasonality': GenelHitRatio6Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Transfer50finallist = pd.merge(GenelHitRatio6Transfer50list, GenelHitRatio6Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio6Transfer50finallist)
GenelHitRatio6Transfer50finallist["Alert"]  = [0 if (GenelHitRatio6Transfer50finallist['Hit Ratio'][i]> GenelHitRatio6Transfer50finallist["Lower"][i]) & (GenelHitRatio6Transfer50finallist['Hit Ratio'][i]< GenelHitRatio6Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Transfer50finallist[GenelHitRatio6Transfer50finallist["Alert"]==1])

#Ultimate_7Transfer50

GenelHitRatio7Transfer50 = np.array(Transfer50[7])
print(GenelHitRatio7Transfer50)
for a in GenelHitRatio7Transfer50:
    GenelHitRatio7Transfer50lists = [np.array(GenelHitRatio7Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Transfer50lists)
GenelHitRatio7Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Transfer50nonseasonality)
GenelHitRatio7Transfer50predict1 = ([GenelHitRatio7Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Transfer50pre2 = pd.DataFrame(GenelHitRatio7Transfer50predict1)
GenelHitRatio7Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer50LowerInterval = [(np.concatenate(GenelHitRatio7Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Transfer50UpperInterval = [(np.concatenate(GenelHitRatio7Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Transfer50LowerInterval,
                        "Upper": GenelHitRatio7Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer50predict1 = ([GenelHitRatio7Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio7Transfer50p1.append(float(str(GenelHitRatio7Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Transfer50p1)
GenelHitRatio7Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio7Transfer50p1,
                          'Lower': GenelHitRatio7Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio7Transfer50lists,
                      'Non-Seasonality': GenelHitRatio7Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Transfer50finallist = pd.merge(GenelHitRatio7Transfer50list, GenelHitRatio7Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio7Transfer50finallist)
GenelHitRatio7Transfer50finallist["Alert"]  = [0 if (GenelHitRatio7Transfer50finallist['Hit Ratio'][i]> GenelHitRatio7Transfer50finallist["Lower"][i]) & (GenelHitRatio7Transfer50finallist['Hit Ratio'][i]< GenelHitRatio7Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Transfer50finallist[GenelHitRatio7Transfer50finallist["Alert"]==1])

#Ultimate_16Transfer50

GenelHitRatio16Transfer50 = np.array(Transfer50[16])
print(GenelHitRatio16Transfer50)
for a in GenelHitRatio16Transfer50:
    GenelHitRatio16Transfer50lists = [np.array(GenelHitRatio16Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Transfer50lists)
GenelHitRatio16Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Transfer50nonseasonality)
GenelHitRatio16Transfer50predict1 = ([GenelHitRatio16Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Transfer50pre2 = pd.DataFrame(GenelHitRatio16Transfer50predict1)
GenelHitRatio16Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer50LowerInterval = [(np.concatenate(GenelHitRatio16Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Transfer50UpperInterval = [(np.concatenate(GenelHitRatio16Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Transfer50LowerInterval,
                        "Upper": GenelHitRatio16Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer50predict1 = ([GenelHitRatio16Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio16Transfer50p1.append(float(str(GenelHitRatio16Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Transfer50p1)
GenelHitRatio16Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio16Transfer50p1,
                          'Lower': GenelHitRatio16Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio16Transfer50lists,
                      'Non-Seasonality': GenelHitRatio16Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Transfer50finallist = pd.merge(GenelHitRatio16Transfer50list, GenelHitRatio16Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio16Transfer50finallist)
GenelHitRatio16Transfer50finallist["Alert"]  = [0 if (GenelHitRatio16Transfer50finallist['Hit Ratio'][i]> GenelHitRatio16Transfer50finallist["Lower"][i]) & (GenelHitRatio16Transfer50finallist['Hit Ratio'][i]< GenelHitRatio16Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Transfer50finallist[GenelHitRatio16Transfer50finallist["Alert"]==1])

#Ultimate_33Transfer50

GenelHitRatio33Transfer50 = np.array(Transfer50[33])
print(GenelHitRatio33Transfer50)
for a in GenelHitRatio33Transfer50:
    GenelHitRatio33Transfer50lists = [np.array(GenelHitRatio33Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Transfer50lists)
GenelHitRatio33Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Transfer50nonseasonality)
GenelHitRatio33Transfer50predict1 = ([GenelHitRatio33Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Transfer50pre2 = pd.DataFrame(GenelHitRatio33Transfer50predict1)
GenelHitRatio33Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer50LowerInterval = [(np.concatenate(GenelHitRatio33Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Transfer50UpperInterval = [(np.concatenate(GenelHitRatio33Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Transfer50LowerInterval,
                        "Upper": GenelHitRatio33Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer50predict1 = ([GenelHitRatio33Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio33Transfer50p1.append(float(str(GenelHitRatio33Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Transfer50p1)
GenelHitRatio33Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio33Transfer50p1,
                          'Lower': GenelHitRatio33Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio33Transfer50lists,
                      'Non-Seasonality': GenelHitRatio33Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Transfer50finallist = pd.merge(GenelHitRatio33Transfer50list, GenelHitRatio33Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio33Transfer50finallist)
GenelHitRatio33Transfer50finallist["Alert"]  = [0 if (GenelHitRatio33Transfer50finallist['Hit Ratio'][i]> GenelHitRatio33Transfer50finallist["Lower"][i]) & (GenelHitRatio33Transfer50finallist['Hit Ratio'][i]< GenelHitRatio33Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Transfer50finallist[GenelHitRatio33Transfer50finallist["Alert"]==1])

#Ultimate_34Transfer50

GenelHitRatio34Transfer50 = np.array(Transfer50[34])
print(GenelHitRatio34Transfer50)
for a in GenelHitRatio34Transfer50:
    GenelHitRatio34Transfer50lists = [np.array(GenelHitRatio34Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Transfer50lists)
GenelHitRatio34Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Transfer50nonseasonality)
GenelHitRatio34Transfer50predict1 = ([GenelHitRatio34Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Transfer50pre2 = pd.DataFrame(GenelHitRatio34Transfer50predict1)
GenelHitRatio34Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer50LowerInterval = [(np.concatenate(GenelHitRatio34Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Transfer50UpperInterval = [(np.concatenate(GenelHitRatio34Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Transfer50LowerInterval,
                        "Upper": GenelHitRatio34Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer50predict1 = ([GenelHitRatio34Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio34Transfer50p1.append(float(str(GenelHitRatio34Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Transfer50p1)
GenelHitRatio34Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio34Transfer50p1,
                          'Lower': GenelHitRatio34Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio34Transfer50lists,
                      'Non-Seasonality': GenelHitRatio34Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Transfer50finallist = pd.merge(GenelHitRatio34Transfer50list, GenelHitRatio34Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio34Transfer50finallist)
GenelHitRatio34Transfer50finallist["Alert"]  = [0 if (GenelHitRatio34Transfer50finallist['Hit Ratio'][i]> GenelHitRatio34Transfer50finallist["Lower"][i]) & (GenelHitRatio34Transfer50finallist['Hit Ratio'][i]< GenelHitRatio34Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Transfer50finallist[GenelHitRatio34Transfer50finallist["Alert"]==1])



#Ultimate_35Transfer50

GenelHitRatio35Transfer50 = np.array(Transfer50[35])
print(GenelHitRatio35Transfer50)
for a in GenelHitRatio35Transfer50:
    GenelHitRatio35Transfer50lists = [np.array(GenelHitRatio35Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Transfer50lists)
GenelHitRatio35Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Transfer50nonseasonality)
GenelHitRatio35Transfer50predict1 = ([GenelHitRatio35Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Transfer50pre2 = pd.DataFrame(GenelHitRatio35Transfer50predict1)
GenelHitRatio35Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer50LowerInterval = [(np.concatenate(GenelHitRatio35Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Transfer50UpperInterval = [(np.concatenate(GenelHitRatio35Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Transfer50LowerInterval,
                        "Upper": GenelHitRatio35Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer50predict1 = ([GenelHitRatio35Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio35Transfer50p1.append(float(str(GenelHitRatio35Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Transfer50p1)
GenelHitRatio35Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio35Transfer50p1,
                          'Lower': GenelHitRatio35Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio35Transfer50lists,
                      'Non-Seasonality': GenelHitRatio35Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Transfer50finallist = pd.merge(GenelHitRatio35Transfer50list, GenelHitRatio35Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio35Transfer50finallist)
GenelHitRatio35Transfer50finallist["Alert"]  = [0 if (GenelHitRatio35Transfer50finallist['Hit Ratio'][i]> GenelHitRatio35Transfer50finallist["Lower"][i]) & (GenelHitRatio35Transfer50finallist['Hit Ratio'][i]< GenelHitRatio35Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Transfer50finallist[GenelHitRatio35Transfer50finallist["Alert"]==1])

#Ultimate_38Transfer50

GenelHitRatio38Transfer50 = np.array(Transfer50[38])
print(GenelHitRatio38Transfer50)
for a in GenelHitRatio38Transfer50:
    GenelHitRatio38Transfer50lists = [np.array(GenelHitRatio38Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Transfer50lists)
GenelHitRatio38Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Transfer50nonseasonality)
GenelHitRatio38Transfer50predict1 = ([GenelHitRatio38Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Transfer50pre2 = pd.DataFrame(GenelHitRatio38Transfer50predict1)
GenelHitRatio38Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer50LowerInterval = [(np.concatenate(GenelHitRatio38Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Transfer50UpperInterval = [(np.concatenate(GenelHitRatio38Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Transfer50LowerInterval,
                        "Upper": GenelHitRatio38Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer50predict1 = ([GenelHitRatio38Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio38Transfer50p1.append(float(str(GenelHitRatio38Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Transfer50p1)
GenelHitRatio38Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio38Transfer50p1,
                          'Lower': GenelHitRatio38Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio38Transfer50lists,
                      'Non-Seasonality': GenelHitRatio38Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Transfer50finallist = pd.merge(GenelHitRatio38Transfer50list, GenelHitRatio38Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio38Transfer50finallist)
GenelHitRatio38Transfer50finallist["Alert"]  = [0 if (GenelHitRatio38Transfer50finallist['Hit Ratio'][i]> GenelHitRatio38Transfer50finallist["Lower"][i]) & (GenelHitRatio38Transfer50finallist['Hit Ratio'][i]< GenelHitRatio38Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Transfer50finallist[GenelHitRatio38Transfer50finallist["Alert"]==1])

#Ultimate_41Transfer50

GenelHitRatio41Transfer50 = np.array(Transfer50[41])
print(GenelHitRatio41Transfer50)
for a in GenelHitRatio41Transfer50:
    GenelHitRatio41Transfer50lists = [np.array(GenelHitRatio41Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Transfer50lists)
GenelHitRatio41Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Transfer50nonseasonality)
GenelHitRatio41Transfer50predict1 = ([GenelHitRatio41Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Transfer50pre2 = pd.DataFrame(GenelHitRatio41Transfer50predict1)
GenelHitRatio41Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer50LowerInterval = [(np.concatenate(GenelHitRatio41Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Transfer50UpperInterval = [(np.concatenate(GenelHitRatio41Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Transfer50LowerInterval,
                        "Upper": GenelHitRatio41Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer50predict1 = ([GenelHitRatio41Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio41Transfer50p1.append(float(str(GenelHitRatio41Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Transfer50p1)
GenelHitRatio41Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio41Transfer50p1,
                          'Lower': GenelHitRatio41Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio41Transfer50lists,
                      'Non-Seasonality': GenelHitRatio41Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Transfer50finallist = pd.merge(GenelHitRatio41Transfer50list, GenelHitRatio41Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio41Transfer50finallist)
GenelHitRatio41Transfer50finallist["Alert"]  = [0 if (GenelHitRatio41Transfer50finallist['Hit Ratio'][i]> GenelHitRatio41Transfer50finallist["Lower"][i]) & (GenelHitRatio41Transfer50finallist['Hit Ratio'][i]< GenelHitRatio41Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Transfer50finallist[GenelHitRatio41Transfer50finallist["Alert"]==1])

#Ultimate_55Transfer50

GenelHitRatio55Transfer50 = np.array(Transfer50[55])
print(GenelHitRatio55Transfer50)
for a in GenelHitRatio55Transfer50:
    GenelHitRatio55Transfer50lists = [np.array(GenelHitRatio55Transfer50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Transfer50lists)
GenelHitRatio55Transfer50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Transfer50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Transfer50nonseasonality)
GenelHitRatio55Transfer50predict1 = ([GenelHitRatio55Transfer50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Transfer50pre2 = pd.DataFrame(GenelHitRatio55Transfer50predict1)
GenelHitRatio55Transfer50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Transfer50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer50LowerInterval = [(np.concatenate(GenelHitRatio55Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Transfer50UpperInterval = [(np.concatenate(GenelHitRatio55Transfer50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Transfer50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Transfer50LowerInterval,
                        "Upper": GenelHitRatio55Transfer50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer50predict1 = ([GenelHitRatio55Transfer50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Transfer50p1 = []
for i in range(0, 79):
    GenelHitRatio55Transfer50p1.append(float(str(GenelHitRatio55Transfer50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Transfer50p1)
GenelHitRatio55Transfer50listpredict = pd.DataFrame({'Predict': GenelHitRatio55Transfer50p1,
                          'Lower': GenelHitRatio55Transfer50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Transfer50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Transfer50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Transfer50’',
                       'Transfer50 aylik hit': GenelHitRatio55Transfer50lists,
                      'Non-Seasonality': GenelHitRatio55Transfer50nonseasonality,
                       'Hit Ratio': Transfer50[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Transfer50finallist = pd.merge(GenelHitRatio55Transfer50list, GenelHitRatio55Transfer50listpredict, on='Sira', how='inner')
print(GenelHitRatio55Transfer50finallist)
GenelHitRatio55Transfer50finallist["Alert"]  = [0 if (GenelHitRatio55Transfer50finallist['Hit Ratio'][i]> GenelHitRatio55Transfer50finallist["Lower"][i]) & (GenelHitRatio55Transfer50finallist['Hit Ratio'][i]< GenelHitRatio55Transfer50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Transfer50finallist[GenelHitRatio55Transfer50finallist["Alert"]==1])

#Ultimate_1Transfer40

GenelHitRatio1Transfer40 = np.array(Transfer40[1])
print(GenelHitRatio1Transfer40)
for a in GenelHitRatio1Transfer40:
    GenelHitRatio1Transfer40lists = [np.array(GenelHitRatio1Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Transfer40lists)
GenelHitRatio1Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Transfer40nonseasonality)
GenelHitRatio1Transfer40predict1 = ([GenelHitRatio1Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Transfer40pre2 = pd.DataFrame(GenelHitRatio1Transfer40predict1)
GenelHitRatio1Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer40LowerInterval = [(np.concatenate(GenelHitRatio1Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Transfer40UpperInterval = [(np.concatenate(GenelHitRatio1Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Transfer40LowerInterval,
                        "Upper": GenelHitRatio1Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer40predict1 = ([GenelHitRatio1Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio1Transfer40p1.append(float(str(GenelHitRatio1Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Transfer40p1)
GenelHitRatio1Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio1Transfer40p1,
                          'Lower': GenelHitRatio1Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio1Transfer40lists,
                      'Non-Seasonality': GenelHitRatio1Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Transfer40finallist = pd.merge(GenelHitRatio1Transfer40list, GenelHitRatio1Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio1Transfer40finallist)
GenelHitRatio1Transfer40finallist["Alert"]  = [0 if (GenelHitRatio1Transfer40finallist['Hit Ratio'][i]> GenelHitRatio1Transfer40finallist["Lower"][i]) & (GenelHitRatio1Transfer40finallist['Hit Ratio'][i]< GenelHitRatio1Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Transfer40finallist[GenelHitRatio1Transfer40finallist["Alert"]==1])

#Ultimate_6Transfer40

GenelHitRatio6Transfer40 = np.array(Transfer40[6])
print(GenelHitRatio6Transfer40)
for a in GenelHitRatio6Transfer40:
    GenelHitRatio6Transfer40lists = [np.array(GenelHitRatio6Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Transfer40lists)
GenelHitRatio6Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Transfer40nonseasonality)
GenelHitRatio6Transfer40predict1 = ([GenelHitRatio6Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Transfer40pre2 = pd.DataFrame(GenelHitRatio6Transfer40predict1)
GenelHitRatio6Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer40LowerInterval = [(np.concatenate(GenelHitRatio6Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Transfer40UpperInterval = [(np.concatenate(GenelHitRatio6Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Transfer40LowerInterval,
                        "Upper": GenelHitRatio6Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer40predict1 = ([GenelHitRatio6Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio6Transfer40p1.append(float(str(GenelHitRatio6Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Transfer40p1)
GenelHitRatio6Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio6Transfer40p1,
                          'Lower': GenelHitRatio6Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio6Transfer40lists,
                      'Non-Seasonality': GenelHitRatio6Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Transfer40finallist = pd.merge(GenelHitRatio6Transfer40list, GenelHitRatio6Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio6Transfer40finallist)
GenelHitRatio6Transfer40finallist["Alert"]  = [0 if (GenelHitRatio6Transfer40finallist['Hit Ratio'][i]> GenelHitRatio6Transfer40finallist["Lower"][i]) & (GenelHitRatio6Transfer40finallist['Hit Ratio'][i]< GenelHitRatio6Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Transfer40finallist[GenelHitRatio6Transfer40finallist["Alert"]==1])

#Ultimate_7Transfer40

GenelHitRatio7Transfer40 = np.array(Transfer40[7])
print(GenelHitRatio7Transfer40)
for a in GenelHitRatio7Transfer40:
    GenelHitRatio7Transfer40lists = [np.array(GenelHitRatio7Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Transfer40lists)
GenelHitRatio7Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Transfer40nonseasonality)
GenelHitRatio7Transfer40predict1 = ([GenelHitRatio7Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Transfer40pre2 = pd.DataFrame(GenelHitRatio7Transfer40predict1)
GenelHitRatio7Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer40LowerInterval = [(np.concatenate(GenelHitRatio7Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Transfer40UpperInterval = [(np.concatenate(GenelHitRatio7Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Transfer40LowerInterval,
                        "Upper": GenelHitRatio7Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer40predict1 = ([GenelHitRatio7Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio7Transfer40p1.append(float(str(GenelHitRatio7Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Transfer40p1)
GenelHitRatio7Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio7Transfer40p1,
                          'Lower': GenelHitRatio7Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio7Transfer40lists,
                      'Non-Seasonality': GenelHitRatio7Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Transfer40finallist = pd.merge(GenelHitRatio7Transfer40list, GenelHitRatio7Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio7Transfer40finallist)
GenelHitRatio7Transfer40finallist["Alert"]  = [0 if (GenelHitRatio7Transfer40finallist['Hit Ratio'][i]> GenelHitRatio7Transfer40finallist["Lower"][i]) & (GenelHitRatio7Transfer40finallist['Hit Ratio'][i]< GenelHitRatio7Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Transfer40finallist[GenelHitRatio7Transfer40finallist["Alert"]==1])

#Ultimate_16Transfer40

GenelHitRatio16Transfer40 = np.array(Transfer40[16])
print(GenelHitRatio16Transfer40)
for a in GenelHitRatio16Transfer40:
    GenelHitRatio16Transfer40lists = [np.array(GenelHitRatio16Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Transfer40lists)
GenelHitRatio16Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Transfer40nonseasonality)
GenelHitRatio16Transfer40predict1 = ([GenelHitRatio16Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Transfer40pre2 = pd.DataFrame(GenelHitRatio16Transfer40predict1)
GenelHitRatio16Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer40LowerInterval = [(np.concatenate(GenelHitRatio16Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Transfer40UpperInterval = [(np.concatenate(GenelHitRatio16Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Transfer40LowerInterval,
                        "Upper": GenelHitRatio16Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer40predict1 = ([GenelHitRatio16Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio16Transfer40p1.append(float(str(GenelHitRatio16Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Transfer40p1)
GenelHitRatio16Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio16Transfer40p1,
                          'Lower': GenelHitRatio16Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio16Transfer40lists,
                      'Non-Seasonality': GenelHitRatio16Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Transfer40finallist = pd.merge(GenelHitRatio16Transfer40list, GenelHitRatio16Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio16Transfer40finallist)
GenelHitRatio16Transfer40finallist["Alert"]  = [0 if (GenelHitRatio16Transfer40finallist['Hit Ratio'][i]> GenelHitRatio16Transfer40finallist["Lower"][i]) & (GenelHitRatio16Transfer40finallist['Hit Ratio'][i]< GenelHitRatio16Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Transfer40finallist[GenelHitRatio16Transfer40finallist["Alert"]==1])

#Ultimate_33Transfer40

GenelHitRatio33Transfer40 = np.array(Transfer40[33])
print(GenelHitRatio33Transfer40)
for a in GenelHitRatio33Transfer40:
    GenelHitRatio33Transfer40lists = [np.array(GenelHitRatio33Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Transfer40lists)
GenelHitRatio33Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Transfer40nonseasonality)
GenelHitRatio33Transfer40predict1 = ([GenelHitRatio33Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Transfer40pre2 = pd.DataFrame(GenelHitRatio33Transfer40predict1)
GenelHitRatio33Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer40LowerInterval = [(np.concatenate(GenelHitRatio33Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Transfer40UpperInterval = [(np.concatenate(GenelHitRatio33Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Transfer40LowerInterval,
                        "Upper": GenelHitRatio33Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer40predict1 = ([GenelHitRatio33Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio33Transfer40p1.append(float(str(GenelHitRatio33Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Transfer40p1)
GenelHitRatio33Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio33Transfer40p1,
                          'Lower': GenelHitRatio33Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio33Transfer40lists,
                      'Non-Seasonality': GenelHitRatio33Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Transfer40finallist = pd.merge(GenelHitRatio33Transfer40list, GenelHitRatio33Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio33Transfer40finallist)
GenelHitRatio33Transfer40finallist["Alert"]  = [0 if (GenelHitRatio33Transfer40finallist['Hit Ratio'][i]> GenelHitRatio33Transfer40finallist["Lower"][i]) & (GenelHitRatio33Transfer40finallist['Hit Ratio'][i]< GenelHitRatio33Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Transfer40finallist[GenelHitRatio33Transfer40finallist["Alert"]==1])

#Ultimate_34Transfer40

GenelHitRatio34Transfer40 = np.array(Transfer40[34])
print(GenelHitRatio34Transfer40)
for a in GenelHitRatio34Transfer40:
    GenelHitRatio34Transfer40lists = [np.array(GenelHitRatio34Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Transfer40lists)
GenelHitRatio34Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Transfer40nonseasonality)
GenelHitRatio34Transfer40predict1 = ([GenelHitRatio34Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Transfer40pre2 = pd.DataFrame(GenelHitRatio34Transfer40predict1)
GenelHitRatio34Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer40LowerInterval = [(np.concatenate(GenelHitRatio34Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Transfer40UpperInterval = [(np.concatenate(GenelHitRatio34Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Transfer40LowerInterval,
                        "Upper": GenelHitRatio34Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer40predict1 = ([GenelHitRatio34Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio34Transfer40p1.append(float(str(GenelHitRatio34Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Transfer40p1)
GenelHitRatio34Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio34Transfer40p1,
                          'Lower': GenelHitRatio34Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio34Transfer40lists,
                      'Non-Seasonality': GenelHitRatio34Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Transfer40finallist = pd.merge(GenelHitRatio34Transfer40list, GenelHitRatio34Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio34Transfer40finallist)
GenelHitRatio34Transfer40finallist["Alert"]  = [0 if (GenelHitRatio34Transfer40finallist['Hit Ratio'][i]> GenelHitRatio34Transfer40finallist["Lower"][i]) & (GenelHitRatio34Transfer40finallist['Hit Ratio'][i]< GenelHitRatio34Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Transfer40finallist[GenelHitRatio34Transfer40finallist["Alert"]==1])



#Ultimate_35Transfer40

GenelHitRatio35Transfer40 = np.array(Transfer40[35])
print(GenelHitRatio35Transfer40)
for a in GenelHitRatio35Transfer40:
    GenelHitRatio35Transfer40lists = [np.array(GenelHitRatio35Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Transfer40lists)
GenelHitRatio35Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Transfer40nonseasonality)
GenelHitRatio35Transfer40predict1 = ([GenelHitRatio35Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Transfer40pre2 = pd.DataFrame(GenelHitRatio35Transfer40predict1)
GenelHitRatio35Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer40LowerInterval = [(np.concatenate(GenelHitRatio35Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Transfer40UpperInterval = [(np.concatenate(GenelHitRatio35Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Transfer40LowerInterval,
                        "Upper": GenelHitRatio35Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer40predict1 = ([GenelHitRatio35Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio35Transfer40p1.append(float(str(GenelHitRatio35Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Transfer40p1)
GenelHitRatio35Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio35Transfer40p1,
                          'Lower': GenelHitRatio35Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio35Transfer40lists,
                      'Non-Seasonality': GenelHitRatio35Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Transfer40finallist = pd.merge(GenelHitRatio35Transfer40list, GenelHitRatio35Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio35Transfer40finallist)
GenelHitRatio35Transfer40finallist["Alert"]  = [0 if (GenelHitRatio35Transfer40finallist['Hit Ratio'][i]> GenelHitRatio35Transfer40finallist["Lower"][i]) & (GenelHitRatio35Transfer40finallist['Hit Ratio'][i]< GenelHitRatio35Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Transfer40finallist[GenelHitRatio35Transfer40finallist["Alert"]==1])

#Ultimate_38Transfer40

GenelHitRatio38Transfer40 = np.array(Transfer40[38])
print(GenelHitRatio38Transfer40)
for a in GenelHitRatio38Transfer40:
    GenelHitRatio38Transfer40lists = [np.array(GenelHitRatio38Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Transfer40lists)
GenelHitRatio38Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Transfer40nonseasonality)
GenelHitRatio38Transfer40predict1 = ([GenelHitRatio38Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Transfer40pre2 = pd.DataFrame(GenelHitRatio38Transfer40predict1)
GenelHitRatio38Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer40LowerInterval = [(np.concatenate(GenelHitRatio38Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Transfer40UpperInterval = [(np.concatenate(GenelHitRatio38Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Transfer40LowerInterval,
                        "Upper": GenelHitRatio38Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer40predict1 = ([GenelHitRatio38Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio38Transfer40p1.append(float(str(GenelHitRatio38Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Transfer40p1)
GenelHitRatio38Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio38Transfer40p1,
                          'Lower': GenelHitRatio38Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio38Transfer40lists,
                      'Non-Seasonality': GenelHitRatio38Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Transfer40finallist = pd.merge(GenelHitRatio38Transfer40list, GenelHitRatio38Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio38Transfer40finallist)
GenelHitRatio38Transfer40finallist["Alert"]  = [0 if (GenelHitRatio38Transfer40finallist['Hit Ratio'][i]> GenelHitRatio38Transfer40finallist["Lower"][i]) & (GenelHitRatio38Transfer40finallist['Hit Ratio'][i]< GenelHitRatio38Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Transfer40finallist[GenelHitRatio38Transfer40finallist["Alert"]==1])

#Ultimate_41Transfer40

GenelHitRatio41Transfer40 = np.array(Transfer40[41])
print(GenelHitRatio41Transfer40)
for a in GenelHitRatio41Transfer40:
    GenelHitRatio41Transfer40lists = [np.array(GenelHitRatio41Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Transfer40lists)
GenelHitRatio41Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Transfer40nonseasonality)
GenelHitRatio41Transfer40predict1 = ([GenelHitRatio41Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Transfer40pre2 = pd.DataFrame(GenelHitRatio41Transfer40predict1)
GenelHitRatio41Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer40LowerInterval = [(np.concatenate(GenelHitRatio41Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Transfer40UpperInterval = [(np.concatenate(GenelHitRatio41Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Transfer40LowerInterval,
                        "Upper": GenelHitRatio41Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer40predict1 = ([GenelHitRatio41Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio41Transfer40p1.append(float(str(GenelHitRatio41Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Transfer40p1)
GenelHitRatio41Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio41Transfer40p1,
                          'Lower': GenelHitRatio41Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio41Transfer40lists,
                      'Non-Seasonality': GenelHitRatio41Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Transfer40finallist = pd.merge(GenelHitRatio41Transfer40list, GenelHitRatio41Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio41Transfer40finallist)
GenelHitRatio41Transfer40finallist["Alert"]  = [0 if (GenelHitRatio41Transfer40finallist['Hit Ratio'][i]> GenelHitRatio41Transfer40finallist["Lower"][i]) & (GenelHitRatio41Transfer40finallist['Hit Ratio'][i]< GenelHitRatio41Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Transfer40finallist[GenelHitRatio41Transfer40finallist["Alert"]==1])

#Ultimate_55Transfer40

GenelHitRatio55Transfer40 = np.array(Transfer40[55])
print(GenelHitRatio55Transfer40)
for a in GenelHitRatio55Transfer40:
    GenelHitRatio55Transfer40lists = [np.array(GenelHitRatio55Transfer40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Transfer40lists)
GenelHitRatio55Transfer40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Transfer40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Transfer40nonseasonality)
GenelHitRatio55Transfer40predict1 = ([GenelHitRatio55Transfer40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Transfer40pre2 = pd.DataFrame(GenelHitRatio55Transfer40predict1)
GenelHitRatio55Transfer40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Transfer40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer40LowerInterval = [(np.concatenate(GenelHitRatio55Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Transfer40UpperInterval = [(np.concatenate(GenelHitRatio55Transfer40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Transfer40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Transfer40LowerInterval,
                        "Upper": GenelHitRatio55Transfer40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer40predict1 = ([GenelHitRatio55Transfer40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Transfer40p1 = []
for i in range(0, 79):
    GenelHitRatio55Transfer40p1.append(float(str(GenelHitRatio55Transfer40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Transfer40p1)
GenelHitRatio55Transfer40listpredict = pd.DataFrame({'Predict': GenelHitRatio55Transfer40p1,
                          'Lower': GenelHitRatio55Transfer40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Transfer40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Transfer40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Transfer40’',
                       'Transfer40 aylik hit': GenelHitRatio55Transfer40lists,
                      'Non-Seasonality': GenelHitRatio55Transfer40nonseasonality,
                       'Hit Ratio': Transfer40[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Transfer40finallist = pd.merge(GenelHitRatio55Transfer40list, GenelHitRatio55Transfer40listpredict, on='Sira', how='inner')
print(GenelHitRatio55Transfer40finallist)
GenelHitRatio55Transfer40finallist["Alert"]  = [0 if (GenelHitRatio55Transfer40finallist['Hit Ratio'][i]> GenelHitRatio55Transfer40finallist["Lower"][i]) & (GenelHitRatio55Transfer40finallist['Hit Ratio'][i]< GenelHitRatio55Transfer40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Transfer40finallist[GenelHitRatio55Transfer40finallist["Alert"]==1])


#Ultimate_1Transfer30

GenelHitRatio1Transfer30 = np.array(Transfer30[1])
print(GenelHitRatio1Transfer30)
for a in GenelHitRatio1Transfer30:
    GenelHitRatio1Transfer30lists = [np.array(GenelHitRatio1Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Transfer30lists)
GenelHitRatio1Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Transfer30nonseasonality)
GenelHitRatio1Transfer30predict1 = ([GenelHitRatio1Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Transfer30pre2 = pd.DataFrame(GenelHitRatio1Transfer30predict1)
GenelHitRatio1Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer30LowerInterval = [(np.concatenate(GenelHitRatio1Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Transfer30UpperInterval = [(np.concatenate(GenelHitRatio1Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Transfer30LowerInterval,
                        "Upper": GenelHitRatio1Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Transfer30predict1 = ([GenelHitRatio1Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio1Transfer30p1.append(float(str(GenelHitRatio1Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Transfer30p1)
GenelHitRatio1Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio1Transfer30p1,
                          'Lower': GenelHitRatio1Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio1Transfer30lists,
                      'Non-Seasonality': GenelHitRatio1Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Transfer30finallist = pd.merge(GenelHitRatio1Transfer30list, GenelHitRatio1Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio1Transfer30finallist)
GenelHitRatio1Transfer30finallist["Alert"]  = [0 if (GenelHitRatio1Transfer30finallist['Hit Ratio'][i]> GenelHitRatio1Transfer30finallist["Lower"][i]) & (GenelHitRatio1Transfer30finallist['Hit Ratio'][i]< GenelHitRatio1Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Transfer30finallist[GenelHitRatio1Transfer30finallist["Alert"]==1])

#Ultimate_6Transfer30

GenelHitRatio6Transfer30 = np.array(Transfer30[6])
print(GenelHitRatio6Transfer30)
for a in GenelHitRatio6Transfer30:
    GenelHitRatio6Transfer30lists = [np.array(GenelHitRatio6Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Transfer30lists)
GenelHitRatio6Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Transfer30nonseasonality)
GenelHitRatio6Transfer30predict1 = ([GenelHitRatio6Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Transfer30pre2 = pd.DataFrame(GenelHitRatio6Transfer30predict1)
GenelHitRatio6Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer30LowerInterval = [(np.concatenate(GenelHitRatio6Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Transfer30UpperInterval = [(np.concatenate(GenelHitRatio6Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Transfer30LowerInterval,
                        "Upper": GenelHitRatio6Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Transfer30predict1 = ([GenelHitRatio6Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio6Transfer30p1.append(float(str(GenelHitRatio6Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Transfer30p1)
GenelHitRatio6Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio6Transfer30p1,
                          'Lower': GenelHitRatio6Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio6Transfer30lists,
                      'Non-Seasonality': GenelHitRatio6Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Transfer30finallist = pd.merge(GenelHitRatio6Transfer30list, GenelHitRatio6Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio6Transfer30finallist)
GenelHitRatio6Transfer30finallist["Alert"]  = [0 if (GenelHitRatio6Transfer30finallist['Hit Ratio'][i]> GenelHitRatio6Transfer30finallist["Lower"][i]) & (GenelHitRatio6Transfer30finallist['Hit Ratio'][i]< GenelHitRatio6Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Transfer30finallist[GenelHitRatio6Transfer30finallist["Alert"]==1])

#Ultimate_7Transfer30

GenelHitRatio7Transfer30 = np.array(Transfer30[7])
print(GenelHitRatio7Transfer30)
for a in GenelHitRatio7Transfer30:
    GenelHitRatio7Transfer30lists = [np.array(GenelHitRatio7Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Transfer30lists)
GenelHitRatio7Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Transfer30nonseasonality)
GenelHitRatio7Transfer30predict1 = ([GenelHitRatio7Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Transfer30pre2 = pd.DataFrame(GenelHitRatio7Transfer30predict1)
GenelHitRatio7Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer30LowerInterval = [(np.concatenate(GenelHitRatio7Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Transfer30UpperInterval = [(np.concatenate(GenelHitRatio7Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Transfer30LowerInterval,
                        "Upper": GenelHitRatio7Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Transfer30predict1 = ([GenelHitRatio7Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio7Transfer30p1.append(float(str(GenelHitRatio7Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Transfer30p1)
GenelHitRatio7Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio7Transfer30p1,
                          'Lower': GenelHitRatio7Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio7Transfer30lists,
                      'Non-Seasonality': GenelHitRatio7Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Transfer30finallist = pd.merge(GenelHitRatio7Transfer30list, GenelHitRatio7Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio7Transfer30finallist)
GenelHitRatio7Transfer30finallist["Alert"]  = [0 if (GenelHitRatio7Transfer30finallist['Hit Ratio'][i]> GenelHitRatio7Transfer30finallist["Lower"][i]) & (GenelHitRatio7Transfer30finallist['Hit Ratio'][i]< GenelHitRatio7Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Transfer30finallist[GenelHitRatio7Transfer30finallist["Alert"]==1])

#Ultimate_16Transfer30

GenelHitRatio16Transfer30 = np.array(Transfer30[16])
print(GenelHitRatio16Transfer30)
for a in GenelHitRatio16Transfer30:
    GenelHitRatio16Transfer30lists = [np.array(GenelHitRatio16Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Transfer30lists)
GenelHitRatio16Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Transfer30nonseasonality)
GenelHitRatio16Transfer30predict1 = ([GenelHitRatio16Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Transfer30pre2 = pd.DataFrame(GenelHitRatio16Transfer30predict1)
GenelHitRatio16Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer30LowerInterval = [(np.concatenate(GenelHitRatio16Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Transfer30UpperInterval = [(np.concatenate(GenelHitRatio16Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Transfer30LowerInterval,
                        "Upper": GenelHitRatio16Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Transfer30predict1 = ([GenelHitRatio16Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio16Transfer30p1.append(float(str(GenelHitRatio16Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Transfer30p1)
GenelHitRatio16Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio16Transfer30p1,
                          'Lower': GenelHitRatio16Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio16Transfer30lists,
                      'Non-Seasonality': GenelHitRatio16Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Transfer30finallist = pd.merge(GenelHitRatio16Transfer30list, GenelHitRatio16Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio16Transfer30finallist)
GenelHitRatio16Transfer30finallist["Alert"]  = [0 if (GenelHitRatio16Transfer30finallist['Hit Ratio'][i]> GenelHitRatio16Transfer30finallist["Lower"][i]) & (GenelHitRatio16Transfer30finallist['Hit Ratio'][i]< GenelHitRatio16Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Transfer30finallist[GenelHitRatio16Transfer30finallist["Alert"]==1])

#Ultimate_33Transfer30

GenelHitRatio33Transfer30 = np.array(Transfer30[33])
print(GenelHitRatio33Transfer30)
for a in GenelHitRatio33Transfer30:
    GenelHitRatio33Transfer30lists = [np.array(GenelHitRatio33Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Transfer30lists)
GenelHitRatio33Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Transfer30nonseasonality)
GenelHitRatio33Transfer30predict1 = ([GenelHitRatio33Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Transfer30pre2 = pd.DataFrame(GenelHitRatio33Transfer30predict1)
GenelHitRatio33Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer30LowerInterval = [(np.concatenate(GenelHitRatio33Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Transfer30UpperInterval = [(np.concatenate(GenelHitRatio33Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Transfer30LowerInterval,
                        "Upper": GenelHitRatio33Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Transfer30predict1 = ([GenelHitRatio33Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio33Transfer30p1.append(float(str(GenelHitRatio33Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Transfer30p1)
GenelHitRatio33Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio33Transfer30p1,
                          'Lower': GenelHitRatio33Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio33Transfer30lists,
                      'Non-Seasonality': GenelHitRatio33Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Transfer30finallist = pd.merge(GenelHitRatio33Transfer30list, GenelHitRatio33Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio33Transfer30finallist)
GenelHitRatio33Transfer30finallist["Alert"]  = [0 if (GenelHitRatio33Transfer30finallist['Hit Ratio'][i]> GenelHitRatio33Transfer30finallist["Lower"][i]) & (GenelHitRatio33Transfer30finallist['Hit Ratio'][i]< GenelHitRatio33Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Transfer30finallist[GenelHitRatio33Transfer30finallist["Alert"]==1])

#Ultimate_34Transfer30

GenelHitRatio34Transfer30 = np.array(Transfer30[34])
print(GenelHitRatio34Transfer30)
for a in GenelHitRatio34Transfer30:
    GenelHitRatio34Transfer30lists = [np.array(GenelHitRatio34Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Transfer30lists)
GenelHitRatio34Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Transfer30nonseasonality)
GenelHitRatio34Transfer30predict1 = ([GenelHitRatio34Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Transfer30pre2 = pd.DataFrame(GenelHitRatio34Transfer30predict1)
GenelHitRatio34Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer30LowerInterval = [(np.concatenate(GenelHitRatio34Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Transfer30UpperInterval = [(np.concatenate(GenelHitRatio34Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Transfer30LowerInterval,
                        "Upper": GenelHitRatio34Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Transfer30predict1 = ([GenelHitRatio34Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio34Transfer30p1.append(float(str(GenelHitRatio34Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Transfer30p1)
GenelHitRatio34Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio34Transfer30p1,
                          'Lower': GenelHitRatio34Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio34Transfer30lists,
                      'Non-Seasonality': GenelHitRatio34Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Transfer30finallist = pd.merge(GenelHitRatio34Transfer30list, GenelHitRatio34Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio34Transfer30finallist)
GenelHitRatio34Transfer30finallist["Alert"]  = [0 if (GenelHitRatio34Transfer30finallist['Hit Ratio'][i]> GenelHitRatio34Transfer30finallist["Lower"][i]) & (GenelHitRatio34Transfer30finallist['Hit Ratio'][i]< GenelHitRatio34Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Transfer30finallist[GenelHitRatio34Transfer30finallist["Alert"]==1])



#Ultimate_35Transfer30

GenelHitRatio35Transfer30 = np.array(Transfer30[35])
print(GenelHitRatio35Transfer30)
for a in GenelHitRatio35Transfer30:
    GenelHitRatio35Transfer30lists = [np.array(GenelHitRatio35Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Transfer30lists)
GenelHitRatio35Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Transfer30nonseasonality)
GenelHitRatio35Transfer30predict1 = ([GenelHitRatio35Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Transfer30pre2 = pd.DataFrame(GenelHitRatio35Transfer30predict1)
GenelHitRatio35Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer30LowerInterval = [(np.concatenate(GenelHitRatio35Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Transfer30UpperInterval = [(np.concatenate(GenelHitRatio35Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Transfer30LowerInterval,
                        "Upper": GenelHitRatio35Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Transfer30predict1 = ([GenelHitRatio35Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio35Transfer30p1.append(float(str(GenelHitRatio35Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Transfer30p1)
GenelHitRatio35Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio35Transfer30p1,
                          'Lower': GenelHitRatio35Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio35Transfer30lists,
                      'Non-Seasonality': GenelHitRatio35Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Transfer30finallist = pd.merge(GenelHitRatio35Transfer30list, GenelHitRatio35Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio35Transfer30finallist)
GenelHitRatio35Transfer30finallist["Alert"]  = [0 if (GenelHitRatio35Transfer30finallist['Hit Ratio'][i]> GenelHitRatio35Transfer30finallist["Lower"][i]) & (GenelHitRatio35Transfer30finallist['Hit Ratio'][i]< GenelHitRatio35Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Transfer30finallist[GenelHitRatio35Transfer30finallist["Alert"]==1])

#Ultimate_38Transfer30

GenelHitRatio38Transfer30 = np.array(Transfer30[38])
print(GenelHitRatio38Transfer30)
for a in GenelHitRatio38Transfer30:
    GenelHitRatio38Transfer30lists = [np.array(GenelHitRatio38Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Transfer30lists)
GenelHitRatio38Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Transfer30nonseasonality)
GenelHitRatio38Transfer30predict1 = ([GenelHitRatio38Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Transfer30pre2 = pd.DataFrame(GenelHitRatio38Transfer30predict1)
GenelHitRatio38Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer30LowerInterval = [(np.concatenate(GenelHitRatio38Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Transfer30UpperInterval = [(np.concatenate(GenelHitRatio38Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Transfer30LowerInterval,
                        "Upper": GenelHitRatio38Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Transfer30predict1 = ([GenelHitRatio38Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio38Transfer30p1.append(float(str(GenelHitRatio38Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Transfer30p1)
GenelHitRatio38Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio38Transfer30p1,
                          'Lower': GenelHitRatio38Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio38Transfer30lists,
                      'Non-Seasonality': GenelHitRatio38Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Transfer30finallist = pd.merge(GenelHitRatio38Transfer30list, GenelHitRatio38Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio38Transfer30finallist)
GenelHitRatio38Transfer30finallist["Alert"]  = [0 if (GenelHitRatio38Transfer30finallist['Hit Ratio'][i]> GenelHitRatio38Transfer30finallist["Lower"][i]) & (GenelHitRatio38Transfer30finallist['Hit Ratio'][i]< GenelHitRatio38Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Transfer30finallist[GenelHitRatio38Transfer30finallist["Alert"]==1])

#Ultimate_41Transfer30

GenelHitRatio41Transfer30 = np.array(Transfer30[41])
print(GenelHitRatio41Transfer30)
for a in GenelHitRatio41Transfer30:
    GenelHitRatio41Transfer30lists = [np.array(GenelHitRatio41Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Transfer30lists)
GenelHitRatio41Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Transfer30nonseasonality)
GenelHitRatio41Transfer30predict1 = ([GenelHitRatio41Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Transfer30pre2 = pd.DataFrame(GenelHitRatio41Transfer30predict1)
GenelHitRatio41Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer30LowerInterval = [(np.concatenate(GenelHitRatio41Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Transfer30UpperInterval = [(np.concatenate(GenelHitRatio41Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Transfer30LowerInterval,
                        "Upper": GenelHitRatio41Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Transfer30predict1 = ([GenelHitRatio41Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio41Transfer30p1.append(float(str(GenelHitRatio41Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Transfer30p1)
GenelHitRatio41Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio41Transfer30p1,
                          'Lower': GenelHitRatio41Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio41Transfer30lists,
                      'Non-Seasonality': GenelHitRatio41Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Transfer30finallist = pd.merge(GenelHitRatio41Transfer30list, GenelHitRatio41Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio41Transfer30finallist)
GenelHitRatio41Transfer30finallist["Alert"]  = [0 if (GenelHitRatio41Transfer30finallist['Hit Ratio'][i]> GenelHitRatio41Transfer30finallist["Lower"][i]) & (GenelHitRatio41Transfer30finallist['Hit Ratio'][i]< GenelHitRatio41Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Transfer30finallist[GenelHitRatio41Transfer30finallist["Alert"]==1])

#Ultimate_55Transfer30

GenelHitRatio55Transfer30 = np.array(Transfer30[55])
print(GenelHitRatio55Transfer30)
for a in GenelHitRatio55Transfer30:
    GenelHitRatio55Transfer30lists = [np.array(GenelHitRatio55Transfer30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Transfer30lists)
GenelHitRatio55Transfer30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Transfer30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Transfer30nonseasonality)
GenelHitRatio55Transfer30predict1 = ([GenelHitRatio55Transfer30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Transfer30pre2 = pd.DataFrame(GenelHitRatio55Transfer30predict1)
GenelHitRatio55Transfer30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Transfer30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer30LowerInterval = [(np.concatenate(GenelHitRatio55Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Transfer30UpperInterval = [(np.concatenate(GenelHitRatio55Transfer30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Transfer30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Transfer30LowerInterval,
                        "Upper": GenelHitRatio55Transfer30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Transfer30predict1 = ([GenelHitRatio55Transfer30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Transfer30p1 = []
for i in range(0, 79):
    GenelHitRatio55Transfer30p1.append(float(str(GenelHitRatio55Transfer30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Transfer30p1)
GenelHitRatio55Transfer30listpredict = pd.DataFrame({'Predict': GenelHitRatio55Transfer30p1,
                          'Lower': GenelHitRatio55Transfer30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Transfer30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Transfer30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Transfer30’',
                       'Transfer30 aylik hit': GenelHitRatio55Transfer30lists,
                      'Non-Seasonality': GenelHitRatio55Transfer30nonseasonality,
                       'Hit Ratio': Transfer30[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Transfer30finallist = pd.merge(GenelHitRatio55Transfer30list, GenelHitRatio55Transfer30listpredict, on='Sira', how='inner')
print(GenelHitRatio55Transfer30finallist)
GenelHitRatio55Transfer30finallist["Alert"]  = [0 if (GenelHitRatio55Transfer30finallist['Hit Ratio'][i]> GenelHitRatio55Transfer30finallist["Lower"][i]) & (GenelHitRatio55Transfer30finallist['Hit Ratio'][i]< GenelHitRatio55Transfer30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Transfer30finallist[GenelHitRatio55Transfer30finallist["Alert"]==1])

#Ultimate_1Yenileme55

GenelHitRatio1Yenileme55 = np.array(Yenileme55[1])
print(GenelHitRatio1Yenileme55)
for a in GenelHitRatio1Yenileme55:
    GenelHitRatio1Yenileme55lists = [np.array(GenelHitRatio1Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Yenileme55lists)
GenelHitRatio1Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Yenileme55nonseasonality)
GenelHitRatio1Yenileme55predict1 = ([GenelHitRatio1Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Yenileme55pre2 = pd.DataFrame(GenelHitRatio1Yenileme55predict1)
GenelHitRatio1Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio1Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio1Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Yenileme55LowerInterval,
                        "Upper": GenelHitRatio1Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme55predict1 = ([GenelHitRatio1Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio1Yenileme55p1.append(float(str(GenelHitRatio1Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Yenileme55p1)
GenelHitRatio1Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio1Yenileme55p1,
                          'Lower': GenelHitRatio1Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio1Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio1Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Yenileme55finallist = pd.merge(GenelHitRatio1Yenileme55list, GenelHitRatio1Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio1Yenileme55finallist)
GenelHitRatio1Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio1Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio1Yenileme55finallist["Lower"][i]) & (GenelHitRatio1Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio1Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Yenileme55finallist[GenelHitRatio1Yenileme55finallist["Alert"]==1])

#Ultimate_6Yenileme55

GenelHitRatio6Yenileme55 = np.array(Yenileme55[6])
print(GenelHitRatio6Yenileme55)
for a in GenelHitRatio6Yenileme55:
    GenelHitRatio6Yenileme55lists = [np.array(GenelHitRatio6Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Yenileme55lists)
GenelHitRatio6Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Yenileme55nonseasonality)
GenelHitRatio6Yenileme55predict1 = ([GenelHitRatio6Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Yenileme55pre2 = pd.DataFrame(GenelHitRatio6Yenileme55predict1)
GenelHitRatio6Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio6Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio6Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Yenileme55LowerInterval,
                        "Upper": GenelHitRatio6Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme55predict1 = ([GenelHitRatio6Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio6Yenileme55p1.append(float(str(GenelHitRatio6Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Yenileme55p1)
GenelHitRatio6Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio6Yenileme55p1,
                          'Lower': GenelHitRatio6Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio6Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio6Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Yenileme55finallist = pd.merge(GenelHitRatio6Yenileme55list, GenelHitRatio6Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio6Yenileme55finallist)
GenelHitRatio6Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio6Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio6Yenileme55finallist["Lower"][i]) & (GenelHitRatio6Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio6Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Yenileme55finallist[GenelHitRatio6Yenileme55finallist["Alert"]==1])

#Ultimate_7Yenileme55

GenelHitRatio7Yenileme55 = np.array(Yenileme55[7])
print(GenelHitRatio7Yenileme55)
for a in GenelHitRatio7Yenileme55:
    GenelHitRatio7Yenileme55lists = [np.array(GenelHitRatio7Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Yenileme55lists)
GenelHitRatio7Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Yenileme55nonseasonality)
GenelHitRatio7Yenileme55predict1 = ([GenelHitRatio7Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Yenileme55pre2 = pd.DataFrame(GenelHitRatio7Yenileme55predict1)
GenelHitRatio7Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio7Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio7Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Yenileme55LowerInterval,
                        "Upper": GenelHitRatio7Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme55predict1 = ([GenelHitRatio7Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio7Yenileme55p1.append(float(str(GenelHitRatio7Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Yenileme55p1)
GenelHitRatio7Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio7Yenileme55p1,
                          'Lower': GenelHitRatio7Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio7Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio7Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Yenileme55finallist = pd.merge(GenelHitRatio7Yenileme55list, GenelHitRatio7Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio7Yenileme55finallist)
GenelHitRatio7Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio7Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio7Yenileme55finallist["Lower"][i]) & (GenelHitRatio7Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio7Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Yenileme55finallist[GenelHitRatio7Yenileme55finallist["Alert"]==1])

#Ultimate_16Yenileme55

GenelHitRatio16Yenileme55 = np.array(Yenileme55[16])
print(GenelHitRatio16Yenileme55)
for a in GenelHitRatio16Yenileme55:
    GenelHitRatio16Yenileme55lists = [np.array(GenelHitRatio16Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Yenileme55lists)
GenelHitRatio16Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Yenileme55nonseasonality)
GenelHitRatio16Yenileme55predict1 = ([GenelHitRatio16Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Yenileme55pre2 = pd.DataFrame(GenelHitRatio16Yenileme55predict1)
GenelHitRatio16Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio16Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio16Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Yenileme55LowerInterval,
                        "Upper": GenelHitRatio16Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme55predict1 = ([GenelHitRatio16Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio16Yenileme55p1.append(float(str(GenelHitRatio16Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Yenileme55p1)
GenelHitRatio16Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio16Yenileme55p1,
                          'Lower': GenelHitRatio16Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio16Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio16Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Yenileme55finallist = pd.merge(GenelHitRatio16Yenileme55list, GenelHitRatio16Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio16Yenileme55finallist)
GenelHitRatio16Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio16Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio16Yenileme55finallist["Lower"][i]) & (GenelHitRatio16Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio16Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Yenileme55finallist[GenelHitRatio16Yenileme55finallist["Alert"]==1])

#Ultimate_33Yenileme55

GenelHitRatio33Yenileme55 = np.array(Yenileme55[33])
print(GenelHitRatio33Yenileme55)
for a in GenelHitRatio33Yenileme55:
    GenelHitRatio33Yenileme55lists = [np.array(GenelHitRatio33Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Yenileme55lists)
GenelHitRatio33Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Yenileme55nonseasonality)
GenelHitRatio33Yenileme55predict1 = ([GenelHitRatio33Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Yenileme55pre2 = pd.DataFrame(GenelHitRatio33Yenileme55predict1)
GenelHitRatio33Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio33Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio33Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Yenileme55LowerInterval,
                        "Upper": GenelHitRatio33Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme55predict1 = ([GenelHitRatio33Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio33Yenileme55p1.append(float(str(GenelHitRatio33Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Yenileme55p1)
GenelHitRatio33Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio33Yenileme55p1,
                          'Lower': GenelHitRatio33Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio33Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio33Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Yenileme55finallist = pd.merge(GenelHitRatio33Yenileme55list, GenelHitRatio33Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio33Yenileme55finallist)
GenelHitRatio33Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio33Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio33Yenileme55finallist["Lower"][i]) & (GenelHitRatio33Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio33Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Yenileme55finallist[GenelHitRatio33Yenileme55finallist["Alert"]==1])

#Ultimate_34Yenileme55

GenelHitRatio34Yenileme55 = np.array(Yenileme55[34])
print(GenelHitRatio34Yenileme55)
for a in GenelHitRatio34Yenileme55:
    GenelHitRatio34Yenileme55lists = [np.array(GenelHitRatio34Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Yenileme55lists)
GenelHitRatio34Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Yenileme55nonseasonality)
GenelHitRatio34Yenileme55predict1 = ([GenelHitRatio34Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Yenileme55pre2 = pd.DataFrame(GenelHitRatio34Yenileme55predict1)
GenelHitRatio34Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio34Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio34Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Yenileme55LowerInterval,
                        "Upper": GenelHitRatio34Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme55predict1 = ([GenelHitRatio34Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio34Yenileme55p1.append(float(str(GenelHitRatio34Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Yenileme55p1)
GenelHitRatio34Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio34Yenileme55p1,
                          'Lower': GenelHitRatio34Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio34Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio34Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Yenileme55finallist = pd.merge(GenelHitRatio34Yenileme55list, GenelHitRatio34Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio34Yenileme55finallist)
GenelHitRatio34Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio34Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio34Yenileme55finallist["Lower"][i]) & (GenelHitRatio34Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio34Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Yenileme55finallist[GenelHitRatio34Yenileme55finallist["Alert"]==1])



#Ultimate_35Yenileme55

GenelHitRatio35Yenileme55 = np.array(Yenileme55[35])
print(GenelHitRatio35Yenileme55)
for a in GenelHitRatio35Yenileme55:
    GenelHitRatio35Yenileme55lists = [np.array(GenelHitRatio35Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Yenileme55lists)
GenelHitRatio35Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Yenileme55nonseasonality)
GenelHitRatio35Yenileme55predict1 = ([GenelHitRatio35Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Yenileme55pre2 = pd.DataFrame(GenelHitRatio35Yenileme55predict1)
GenelHitRatio35Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio35Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio35Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Yenileme55LowerInterval,
                        "Upper": GenelHitRatio35Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme55predict1 = ([GenelHitRatio35Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio35Yenileme55p1.append(float(str(GenelHitRatio35Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Yenileme55p1)
GenelHitRatio35Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio35Yenileme55p1,
                          'Lower': GenelHitRatio35Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio35Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio35Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Yenileme55finallist = pd.merge(GenelHitRatio35Yenileme55list, GenelHitRatio35Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio35Yenileme55finallist)
GenelHitRatio35Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio35Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio35Yenileme55finallist["Lower"][i]) & (GenelHitRatio35Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio35Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Yenileme55finallist[GenelHitRatio35Yenileme55finallist["Alert"]==1])

#Ultimate_38Yenileme55

GenelHitRatio38Yenileme55 = np.array(Yenileme55[38])
print(GenelHitRatio38Yenileme55)
for a in GenelHitRatio38Yenileme55:
    GenelHitRatio38Yenileme55lists = [np.array(GenelHitRatio38Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Yenileme55lists)
GenelHitRatio38Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Yenileme55nonseasonality)
GenelHitRatio38Yenileme55predict1 = ([GenelHitRatio38Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Yenileme55pre2 = pd.DataFrame(GenelHitRatio38Yenileme55predict1)
GenelHitRatio38Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio38Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio38Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Yenileme55LowerInterval,
                        "Upper": GenelHitRatio38Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme55predict1 = ([GenelHitRatio38Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio38Yenileme55p1.append(float(str(GenelHitRatio38Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Yenileme55p1)
GenelHitRatio38Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio38Yenileme55p1,
                          'Lower': GenelHitRatio38Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio38Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio38Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Yenileme55finallist = pd.merge(GenelHitRatio38Yenileme55list, GenelHitRatio38Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio38Yenileme55finallist)
GenelHitRatio38Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio38Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio38Yenileme55finallist["Lower"][i]) & (GenelHitRatio38Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio38Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Yenileme55finallist[GenelHitRatio38Yenileme55finallist["Alert"]==1])

#Ultimate_41Yenileme55

GenelHitRatio41Yenileme55 = np.array(Yenileme55[41])
print(GenelHitRatio41Yenileme55)
for a in GenelHitRatio41Yenileme55:
    GenelHitRatio41Yenileme55lists = [np.array(GenelHitRatio41Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Yenileme55lists)
GenelHitRatio41Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Yenileme55nonseasonality)
GenelHitRatio41Yenileme55predict1 = ([GenelHitRatio41Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Yenileme55pre2 = pd.DataFrame(GenelHitRatio41Yenileme55predict1)
GenelHitRatio41Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio41Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio41Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Yenileme55LowerInterval,
                        "Upper": GenelHitRatio41Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme55predict1 = ([GenelHitRatio41Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio41Yenileme55p1.append(float(str(GenelHitRatio41Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Yenileme55p1)
GenelHitRatio41Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio41Yenileme55p1,
                          'Lower': GenelHitRatio41Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio41Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio41Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Yenileme55finallist = pd.merge(GenelHitRatio41Yenileme55list, GenelHitRatio41Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio41Yenileme55finallist)
GenelHitRatio41Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio41Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio41Yenileme55finallist["Lower"][i]) & (GenelHitRatio41Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio41Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Yenileme55finallist[GenelHitRatio41Yenileme55finallist["Alert"]==1])

#Ultimate_55Yenileme55

GenelHitRatio55Yenileme55 = np.array(Yenileme55[55])
print(GenelHitRatio55Yenileme55)
for a in GenelHitRatio55Yenileme55:
    GenelHitRatio55Yenileme55lists = [np.array(GenelHitRatio55Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Yenileme55lists)
GenelHitRatio55Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Yenileme55nonseasonality)
GenelHitRatio55Yenileme55predict1 = ([GenelHitRatio55Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Yenileme55pre2 = pd.DataFrame(GenelHitRatio55Yenileme55predict1)
GenelHitRatio55Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio55Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio55Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Yenileme55LowerInterval,
                        "Upper": GenelHitRatio55Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme55predict1 = ([GenelHitRatio55Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio55Yenileme55p1.append(float(str(GenelHitRatio55Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Yenileme55p1)
GenelHitRatio55Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio55Yenileme55p1,
                          'Lower': GenelHitRatio55Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio55Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio55Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Yenileme55finallist = pd.merge(GenelHitRatio55Yenileme55list, GenelHitRatio55Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio55Yenileme55finallist)
GenelHitRatio55Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio55Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio55Yenileme55finallist["Lower"][i]) & (GenelHitRatio55Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio55Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Yenileme55finallist[GenelHitRatio55Yenileme55finallist["Alert"]==1])


#Ultimate_1Yenileme60

GenelHitRatio1Yenileme60 = np.array(Yenileme60[1])
print(GenelHitRatio1Yenileme60)
for a in GenelHitRatio1Yenileme60:
    GenelHitRatio1Yenileme60lists = [np.array(GenelHitRatio1Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Yenileme60lists)
GenelHitRatio1Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Yenileme60nonseasonality)
GenelHitRatio1Yenileme60predict1 = ([GenelHitRatio1Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Yenileme60pre2 = pd.DataFrame(GenelHitRatio1Yenileme60predict1)
GenelHitRatio1Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio1Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio1Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Yenileme60LowerInterval,
                        "Upper": GenelHitRatio1Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme60predict1 = ([GenelHitRatio1Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio1Yenileme60p1.append(float(str(GenelHitRatio1Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Yenileme60p1)
GenelHitRatio1Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio1Yenileme60p1,
                          'Lower': GenelHitRatio1Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio1Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio1Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Yenileme60finallist = pd.merge(GenelHitRatio1Yenileme60list, GenelHitRatio1Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio1Yenileme60finallist)
GenelHitRatio1Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio1Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio1Yenileme60finallist["Lower"][i]) & (GenelHitRatio1Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio1Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Yenileme60finallist[GenelHitRatio1Yenileme60finallist["Alert"]==1])

#Ultimate_6Yenileme60

GenelHitRatio6Yenileme60 = np.array(Yenileme60[6])
print(GenelHitRatio6Yenileme60)
for a in GenelHitRatio6Yenileme60:
    GenelHitRatio6Yenileme60lists = [np.array(GenelHitRatio6Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Yenileme60lists)
GenelHitRatio6Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Yenileme60nonseasonality)
GenelHitRatio6Yenileme60predict1 = ([GenelHitRatio6Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Yenileme60pre2 = pd.DataFrame(GenelHitRatio6Yenileme60predict1)
GenelHitRatio6Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio6Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio6Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Yenileme60LowerInterval,
                        "Upper": GenelHitRatio6Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme60predict1 = ([GenelHitRatio6Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio6Yenileme60p1.append(float(str(GenelHitRatio6Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Yenileme60p1)
GenelHitRatio6Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio6Yenileme60p1,
                          'Lower': GenelHitRatio6Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio6Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio6Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Yenileme60finallist = pd.merge(GenelHitRatio6Yenileme60list, GenelHitRatio6Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio6Yenileme60finallist)
GenelHitRatio6Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio6Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio6Yenileme60finallist["Lower"][i]) & (GenelHitRatio6Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio6Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Yenileme60finallist[GenelHitRatio6Yenileme60finallist["Alert"]==1])

#Ultimate_7Yenileme60

GenelHitRatio7Yenileme60 = np.array(Yenileme60[7])
print(GenelHitRatio7Yenileme60)
for a in GenelHitRatio7Yenileme60:
    GenelHitRatio7Yenileme60lists = [np.array(GenelHitRatio7Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Yenileme60lists)
GenelHitRatio7Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Yenileme60nonseasonality)
GenelHitRatio7Yenileme60predict1 = ([GenelHitRatio7Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Yenileme60pre2 = pd.DataFrame(GenelHitRatio7Yenileme60predict1)
GenelHitRatio7Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio7Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio7Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Yenileme60LowerInterval,
                        "Upper": GenelHitRatio7Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme60predict1 = ([GenelHitRatio7Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio7Yenileme60p1.append(float(str(GenelHitRatio7Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Yenileme60p1)
GenelHitRatio7Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio7Yenileme60p1,
                          'Lower': GenelHitRatio7Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio7Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio7Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Yenileme60finallist = pd.merge(GenelHitRatio7Yenileme60list, GenelHitRatio7Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio7Yenileme60finallist)
GenelHitRatio7Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio7Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio7Yenileme60finallist["Lower"][i]) & (GenelHitRatio7Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio7Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Yenileme60finallist[GenelHitRatio7Yenileme60finallist["Alert"]==1])

#Ultimate_16Yenileme60

GenelHitRatio16Yenileme60 = np.array(Yenileme60[16])
print(GenelHitRatio16Yenileme60)
for a in GenelHitRatio16Yenileme60:
    GenelHitRatio16Yenileme60lists = [np.array(GenelHitRatio16Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Yenileme60lists)
GenelHitRatio16Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Yenileme60nonseasonality)
GenelHitRatio16Yenileme60predict1 = ([GenelHitRatio16Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Yenileme60pre2 = pd.DataFrame(GenelHitRatio16Yenileme60predict1)
GenelHitRatio16Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio16Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio16Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Yenileme60LowerInterval,
                        "Upper": GenelHitRatio16Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme60predict1 = ([GenelHitRatio16Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio16Yenileme60p1.append(float(str(GenelHitRatio16Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Yenileme60p1)
GenelHitRatio16Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio16Yenileme60p1,
                          'Lower': GenelHitRatio16Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio16Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio16Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Yenileme60finallist = pd.merge(GenelHitRatio16Yenileme60list, GenelHitRatio16Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio16Yenileme60finallist)
GenelHitRatio16Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio16Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio16Yenileme60finallist["Lower"][i]) & (GenelHitRatio16Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio16Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Yenileme60finallist[GenelHitRatio16Yenileme60finallist["Alert"]==1])

#Ultimate_33Yenileme60

GenelHitRatio33Yenileme60 = np.array(Yenileme60[33])
print(GenelHitRatio33Yenileme60)
for a in GenelHitRatio33Yenileme60:
    GenelHitRatio33Yenileme60lists = [np.array(GenelHitRatio33Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Yenileme60lists)
GenelHitRatio33Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Yenileme60nonseasonality)
GenelHitRatio33Yenileme60predict1 = ([GenelHitRatio33Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Yenileme60pre2 = pd.DataFrame(GenelHitRatio33Yenileme60predict1)
GenelHitRatio33Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio33Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio33Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Yenileme60LowerInterval,
                        "Upper": GenelHitRatio33Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme60predict1 = ([GenelHitRatio33Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio33Yenileme60p1.append(float(str(GenelHitRatio33Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Yenileme60p1)
GenelHitRatio33Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio33Yenileme60p1,
                          'Lower': GenelHitRatio33Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio33Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio33Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Yenileme60finallist = pd.merge(GenelHitRatio33Yenileme60list, GenelHitRatio33Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio33Yenileme60finallist)
GenelHitRatio33Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio33Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio33Yenileme60finallist["Lower"][i]) & (GenelHitRatio33Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio33Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Yenileme60finallist[GenelHitRatio33Yenileme60finallist["Alert"]==1])

#Ultimate_34Yenileme60

GenelHitRatio34Yenileme60 = np.array(Yenileme60[34])
print(GenelHitRatio34Yenileme60)
for a in GenelHitRatio34Yenileme60:
    GenelHitRatio34Yenileme60lists = [np.array(GenelHitRatio34Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Yenileme60lists)
GenelHitRatio34Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Yenileme60nonseasonality)
GenelHitRatio34Yenileme60predict1 = ([GenelHitRatio34Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Yenileme60pre2 = pd.DataFrame(GenelHitRatio34Yenileme60predict1)
GenelHitRatio34Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio34Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio34Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Yenileme60LowerInterval,
                        "Upper": GenelHitRatio34Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme60predict1 = ([GenelHitRatio34Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio34Yenileme60p1.append(float(str(GenelHitRatio34Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Yenileme60p1)
GenelHitRatio34Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio34Yenileme60p1,
                          'Lower': GenelHitRatio34Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio34Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio34Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Yenileme60finallist = pd.merge(GenelHitRatio34Yenileme60list, GenelHitRatio34Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio34Yenileme60finallist)
GenelHitRatio34Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio34Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio34Yenileme60finallist["Lower"][i]) & (GenelHitRatio34Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio34Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Yenileme60finallist[GenelHitRatio34Yenileme60finallist["Alert"]==1])



#Ultimate_35Yenileme60

GenelHitRatio35Yenileme60 = np.array(Yenileme60[35])
print(GenelHitRatio35Yenileme60)
for a in GenelHitRatio35Yenileme60:
    GenelHitRatio35Yenileme60lists = [np.array(GenelHitRatio35Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Yenileme60lists)
GenelHitRatio35Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Yenileme60nonseasonality)
GenelHitRatio35Yenileme60predict1 = ([GenelHitRatio35Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Yenileme60pre2 = pd.DataFrame(GenelHitRatio35Yenileme60predict1)
GenelHitRatio35Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio35Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio35Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Yenileme60LowerInterval,
                        "Upper": GenelHitRatio35Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme60predict1 = ([GenelHitRatio35Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio35Yenileme60p1.append(float(str(GenelHitRatio35Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Yenileme60p1)
GenelHitRatio35Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio35Yenileme60p1,
                          'Lower': GenelHitRatio35Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio35Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio35Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Yenileme60finallist = pd.merge(GenelHitRatio35Yenileme60list, GenelHitRatio35Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio35Yenileme60finallist)
GenelHitRatio35Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio35Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio35Yenileme60finallist["Lower"][i]) & (GenelHitRatio35Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio35Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Yenileme60finallist[GenelHitRatio35Yenileme60finallist["Alert"]==1])

#Ultimate_38Yenileme60

GenelHitRatio38Yenileme60 = np.array(Yenileme60[38])
print(GenelHitRatio38Yenileme60)
for a in GenelHitRatio38Yenileme60:
    GenelHitRatio38Yenileme60lists = [np.array(GenelHitRatio38Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Yenileme60lists)
GenelHitRatio38Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Yenileme60nonseasonality)
GenelHitRatio38Yenileme60predict1 = ([GenelHitRatio38Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Yenileme60pre2 = pd.DataFrame(GenelHitRatio38Yenileme60predict1)
GenelHitRatio38Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio38Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio38Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Yenileme60LowerInterval,
                        "Upper": GenelHitRatio38Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme60predict1 = ([GenelHitRatio38Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio38Yenileme60p1.append(float(str(GenelHitRatio38Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Yenileme60p1)
GenelHitRatio38Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio38Yenileme60p1,
                          'Lower': GenelHitRatio38Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio38Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio38Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Yenileme60finallist = pd.merge(GenelHitRatio38Yenileme60list, GenelHitRatio38Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio38Yenileme60finallist)
GenelHitRatio38Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio38Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio38Yenileme60finallist["Lower"][i]) & (GenelHitRatio38Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio38Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Yenileme60finallist[GenelHitRatio38Yenileme60finallist["Alert"]==1])

#Ultimate_41Yenileme60

GenelHitRatio41Yenileme60 = np.array(Yenileme60[41])
print(GenelHitRatio41Yenileme60)
for a in GenelHitRatio41Yenileme60:
    GenelHitRatio41Yenileme60lists = [np.array(GenelHitRatio41Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Yenileme60lists)
GenelHitRatio41Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Yenileme60nonseasonality)
GenelHitRatio41Yenileme60predict1 = ([GenelHitRatio41Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Yenileme60pre2 = pd.DataFrame(GenelHitRatio41Yenileme60predict1)
GenelHitRatio41Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio41Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio41Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Yenileme60LowerInterval,
                        "Upper": GenelHitRatio41Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme60predict1 = ([GenelHitRatio41Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio41Yenileme60p1.append(float(str(GenelHitRatio41Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Yenileme60p1)
GenelHitRatio41Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio41Yenileme60p1,
                          'Lower': GenelHitRatio41Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio41Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio41Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Yenileme60finallist = pd.merge(GenelHitRatio41Yenileme60list, GenelHitRatio41Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio41Yenileme60finallist)
GenelHitRatio41Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio41Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio41Yenileme60finallist["Lower"][i]) & (GenelHitRatio41Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio41Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Yenileme60finallist[GenelHitRatio41Yenileme60finallist["Alert"]==1])

#Ultimate_55Yenileme60

GenelHitRatio55Yenileme60 = np.array(Yenileme60[55])
print(GenelHitRatio55Yenileme60)
for a in GenelHitRatio55Yenileme60:
    GenelHitRatio55Yenileme60lists = [np.array(GenelHitRatio55Yenileme60[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Yenileme60lists)
GenelHitRatio55Yenileme60nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Yenileme60[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Yenileme60nonseasonality)
GenelHitRatio55Yenileme60predict1 = ([GenelHitRatio55Yenileme60nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Yenileme60pre2 = pd.DataFrame(GenelHitRatio55Yenileme60predict1)
GenelHitRatio55Yenileme60Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Yenileme60pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme60LowerInterval = [(np.concatenate(GenelHitRatio55Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Yenileme60UpperInterval = [(np.concatenate(GenelHitRatio55Yenileme60Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Yenileme60Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Yenileme60LowerInterval,
                        "Upper": GenelHitRatio55Yenileme60UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme60predict1 = ([GenelHitRatio55Yenileme60nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Yenileme60p1 = []
for i in range(0, 79):
    GenelHitRatio55Yenileme60p1.append(float(str(GenelHitRatio55Yenileme60predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Yenileme60p1)
GenelHitRatio55Yenileme60listpredict = pd.DataFrame({'Predict': GenelHitRatio55Yenileme60p1,
                          'Lower': GenelHitRatio55Yenileme60Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Yenileme60Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Yenileme60list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Yenileme60’',
                       'Yenileme60 aylik hit': GenelHitRatio55Yenileme60lists,
                      'Non-Seasonality': GenelHitRatio55Yenileme60nonseasonality,
                       'Hit Ratio': Yenileme60[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Yenileme60finallist = pd.merge(GenelHitRatio55Yenileme60list, GenelHitRatio55Yenileme60listpredict, on='Sira', how='inner')
print(GenelHitRatio55Yenileme60finallist)
GenelHitRatio55Yenileme60finallist["Alert"]  = [0 if (GenelHitRatio55Yenileme60finallist['Hit Ratio'][i]> GenelHitRatio55Yenileme60finallist["Lower"][i]) & (GenelHitRatio55Yenileme60finallist['Hit Ratio'][i]< GenelHitRatio55Yenileme60finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Yenileme60finallist[GenelHitRatio55Yenileme60finallist["Alert"]==1])


#Ultimate_1Yenileme50

GenelHitRatio1Yenileme50 = np.array(Yenileme50[1])
print(GenelHitRatio1Yenileme50)
for a in GenelHitRatio1Yenileme50:
    GenelHitRatio1Yenileme50lists = [np.array(GenelHitRatio1Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Yenileme50lists)
GenelHitRatio1Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Yenileme50nonseasonality)
GenelHitRatio1Yenileme50predict1 = ([GenelHitRatio1Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Yenileme50pre2 = pd.DataFrame(GenelHitRatio1Yenileme50predict1)
GenelHitRatio1Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio1Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio1Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Yenileme50LowerInterval,
                        "Upper": GenelHitRatio1Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme50predict1 = ([GenelHitRatio1Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio1Yenileme50p1.append(float(str(GenelHitRatio1Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Yenileme50p1)
GenelHitRatio1Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio1Yenileme50p1,
                          'Lower': GenelHitRatio1Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio1Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio1Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Yenileme50finallist = pd.merge(GenelHitRatio1Yenileme50list, GenelHitRatio1Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio1Yenileme50finallist)
GenelHitRatio1Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio1Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio1Yenileme50finallist["Lower"][i]) & (GenelHitRatio1Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio1Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Yenileme50finallist[GenelHitRatio1Yenileme50finallist["Alert"]==1])

#Ultimate_6Yenileme50

GenelHitRatio6Yenileme50 = np.array(Yenileme50[6])
print(GenelHitRatio6Yenileme50)
for a in GenelHitRatio6Yenileme50:
    GenelHitRatio6Yenileme50lists = [np.array(GenelHitRatio6Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Yenileme50lists)
GenelHitRatio6Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Yenileme50nonseasonality)
GenelHitRatio6Yenileme50predict1 = ([GenelHitRatio6Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Yenileme50pre2 = pd.DataFrame(GenelHitRatio6Yenileme50predict1)
GenelHitRatio6Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio6Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio6Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Yenileme50LowerInterval,
                        "Upper": GenelHitRatio6Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme50predict1 = ([GenelHitRatio6Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio6Yenileme50p1.append(float(str(GenelHitRatio6Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Yenileme50p1)
GenelHitRatio6Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio6Yenileme50p1,
                          'Lower': GenelHitRatio6Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio6Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio6Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Yenileme50finallist = pd.merge(GenelHitRatio6Yenileme50list, GenelHitRatio6Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio6Yenileme50finallist)
GenelHitRatio6Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio6Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio6Yenileme50finallist["Lower"][i]) & (GenelHitRatio6Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio6Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Yenileme50finallist[GenelHitRatio6Yenileme50finallist["Alert"]==1])

#Ultimate_7Yenileme50

GenelHitRatio7Yenileme50 = np.array(Yenileme50[7])
print(GenelHitRatio7Yenileme50)
for a in GenelHitRatio7Yenileme50:
    GenelHitRatio7Yenileme50lists = [np.array(GenelHitRatio7Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Yenileme50lists)
GenelHitRatio7Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Yenileme50nonseasonality)
GenelHitRatio7Yenileme50predict1 = ([GenelHitRatio7Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Yenileme50pre2 = pd.DataFrame(GenelHitRatio7Yenileme50predict1)
GenelHitRatio7Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio7Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio7Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Yenileme50LowerInterval,
                        "Upper": GenelHitRatio7Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme50predict1 = ([GenelHitRatio7Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio7Yenileme50p1.append(float(str(GenelHitRatio7Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Yenileme50p1)
GenelHitRatio7Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio7Yenileme50p1,
                          'Lower': GenelHitRatio7Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio7Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio7Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Yenileme50finallist = pd.merge(GenelHitRatio7Yenileme50list, GenelHitRatio7Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio7Yenileme50finallist)
GenelHitRatio7Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio7Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio7Yenileme50finallist["Lower"][i]) & (GenelHitRatio7Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio7Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Yenileme50finallist[GenelHitRatio7Yenileme50finallist["Alert"]==1])

#Ultimate_16Yenileme50

GenelHitRatio16Yenileme50 = np.array(Yenileme50[16])
print(GenelHitRatio16Yenileme50)
for a in GenelHitRatio16Yenileme50:
    GenelHitRatio16Yenileme50lists = [np.array(GenelHitRatio16Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Yenileme50lists)
GenelHitRatio16Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Yenileme50nonseasonality)
GenelHitRatio16Yenileme50predict1 = ([GenelHitRatio16Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Yenileme50pre2 = pd.DataFrame(GenelHitRatio16Yenileme50predict1)
GenelHitRatio16Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio16Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio16Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Yenileme50LowerInterval,
                        "Upper": GenelHitRatio16Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme50predict1 = ([GenelHitRatio16Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio16Yenileme50p1.append(float(str(GenelHitRatio16Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Yenileme50p1)
GenelHitRatio16Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio16Yenileme50p1,
                          'Lower': GenelHitRatio16Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio16Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio16Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Yenileme50finallist = pd.merge(GenelHitRatio16Yenileme50list, GenelHitRatio16Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio16Yenileme50finallist)
GenelHitRatio16Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio16Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio16Yenileme50finallist["Lower"][i]) & (GenelHitRatio16Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio16Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Yenileme50finallist[GenelHitRatio16Yenileme50finallist["Alert"]==1])

#Ultimate_33Yenileme50

GenelHitRatio33Yenileme50 = np.array(Yenileme50[33])
print(GenelHitRatio33Yenileme50)
for a in GenelHitRatio33Yenileme50:
    GenelHitRatio33Yenileme50lists = [np.array(GenelHitRatio33Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Yenileme50lists)
GenelHitRatio33Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Yenileme50nonseasonality)
GenelHitRatio33Yenileme50predict1 = ([GenelHitRatio33Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Yenileme50pre2 = pd.DataFrame(GenelHitRatio33Yenileme50predict1)
GenelHitRatio33Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio33Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio33Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Yenileme50LowerInterval,
                        "Upper": GenelHitRatio33Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme50predict1 = ([GenelHitRatio33Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio33Yenileme50p1.append(float(str(GenelHitRatio33Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Yenileme50p1)
GenelHitRatio33Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio33Yenileme50p1,
                          'Lower': GenelHitRatio33Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio33Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio33Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Yenileme50finallist = pd.merge(GenelHitRatio33Yenileme50list, GenelHitRatio33Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio33Yenileme50finallist)
GenelHitRatio33Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio33Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio33Yenileme50finallist["Lower"][i]) & (GenelHitRatio33Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio33Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Yenileme50finallist[GenelHitRatio33Yenileme50finallist["Alert"]==1])

#Ultimate_34Yenileme50

GenelHitRatio34Yenileme50 = np.array(Yenileme50[34])
print(GenelHitRatio34Yenileme50)
for a in GenelHitRatio34Yenileme50:
    GenelHitRatio34Yenileme50lists = [np.array(GenelHitRatio34Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Yenileme50lists)
GenelHitRatio34Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Yenileme50nonseasonality)
GenelHitRatio34Yenileme50predict1 = ([GenelHitRatio34Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Yenileme50pre2 = pd.DataFrame(GenelHitRatio34Yenileme50predict1)
GenelHitRatio34Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio34Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio34Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Yenileme50LowerInterval,
                        "Upper": GenelHitRatio34Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme50predict1 = ([GenelHitRatio34Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio34Yenileme50p1.append(float(str(GenelHitRatio34Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Yenileme50p1)
GenelHitRatio34Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio34Yenileme50p1,
                          'Lower': GenelHitRatio34Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio34Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio34Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Yenileme50finallist = pd.merge(GenelHitRatio34Yenileme50list, GenelHitRatio34Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio34Yenileme50finallist)
GenelHitRatio34Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio34Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio34Yenileme50finallist["Lower"][i]) & (GenelHitRatio34Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio34Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Yenileme50finallist[GenelHitRatio34Yenileme50finallist["Alert"]==1])



#Ultimate_35Yenileme50

GenelHitRatio35Yenileme50 = np.array(Yenileme50[35])
print(GenelHitRatio35Yenileme50)
for a in GenelHitRatio35Yenileme50:
    GenelHitRatio35Yenileme50lists = [np.array(GenelHitRatio35Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Yenileme50lists)
GenelHitRatio35Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Yenileme50nonseasonality)
GenelHitRatio35Yenileme50predict1 = ([GenelHitRatio35Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Yenileme50pre2 = pd.DataFrame(GenelHitRatio35Yenileme50predict1)
GenelHitRatio35Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio35Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio35Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Yenileme50LowerInterval,
                        "Upper": GenelHitRatio35Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme50predict1 = ([GenelHitRatio35Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio35Yenileme50p1.append(float(str(GenelHitRatio35Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Yenileme50p1)
GenelHitRatio35Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio35Yenileme50p1,
                          'Lower': GenelHitRatio35Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio35Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio35Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Yenileme50finallist = pd.merge(GenelHitRatio35Yenileme50list, GenelHitRatio35Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio35Yenileme50finallist)
GenelHitRatio35Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio35Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio35Yenileme50finallist["Lower"][i]) & (GenelHitRatio35Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio35Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Yenileme50finallist[GenelHitRatio35Yenileme50finallist["Alert"]==1])

#Ultimate_38Yenileme50

GenelHitRatio38Yenileme50 = np.array(Yenileme50[38])
print(GenelHitRatio38Yenileme50)
for a in GenelHitRatio38Yenileme50:
    GenelHitRatio38Yenileme50lists = [np.array(GenelHitRatio38Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Yenileme50lists)
GenelHitRatio38Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Yenileme50nonseasonality)
GenelHitRatio38Yenileme50predict1 = ([GenelHitRatio38Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Yenileme50pre2 = pd.DataFrame(GenelHitRatio38Yenileme50predict1)
GenelHitRatio38Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio38Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio38Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Yenileme50LowerInterval,
                        "Upper": GenelHitRatio38Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme50predict1 = ([GenelHitRatio38Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio38Yenileme50p1.append(float(str(GenelHitRatio38Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Yenileme50p1)
GenelHitRatio38Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio38Yenileme50p1,
                          'Lower': GenelHitRatio38Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio38Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio38Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Yenileme50finallist = pd.merge(GenelHitRatio38Yenileme50list, GenelHitRatio38Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio38Yenileme50finallist)
GenelHitRatio38Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio38Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio38Yenileme50finallist["Lower"][i]) & (GenelHitRatio38Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio38Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Yenileme50finallist[GenelHitRatio38Yenileme50finallist["Alert"]==1])

#Ultimate_41Yenileme50

GenelHitRatio41Yenileme50 = np.array(Yenileme50[41])
print(GenelHitRatio41Yenileme50)
for a in GenelHitRatio41Yenileme50:
    GenelHitRatio41Yenileme50lists = [np.array(GenelHitRatio41Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Yenileme50lists)
GenelHitRatio41Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Yenileme50nonseasonality)
GenelHitRatio41Yenileme50predict1 = ([GenelHitRatio41Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Yenileme50pre2 = pd.DataFrame(GenelHitRatio41Yenileme50predict1)
GenelHitRatio41Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio41Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio41Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Yenileme50LowerInterval,
                        "Upper": GenelHitRatio41Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme50predict1 = ([GenelHitRatio41Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio41Yenileme50p1.append(float(str(GenelHitRatio41Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Yenileme50p1)
GenelHitRatio41Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio41Yenileme50p1,
                          'Lower': GenelHitRatio41Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio41Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio41Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Yenileme50finallist = pd.merge(GenelHitRatio41Yenileme50list, GenelHitRatio41Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio41Yenileme50finallist)
GenelHitRatio41Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio41Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio41Yenileme50finallist["Lower"][i]) & (GenelHitRatio41Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio41Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Yenileme50finallist[GenelHitRatio41Yenileme50finallist["Alert"]==1])

#Ultimate_55Yenileme50

GenelHitRatio55Yenileme50 = np.array(Yenileme50[55])
print(GenelHitRatio55Yenileme50)
for a in GenelHitRatio55Yenileme50:
    GenelHitRatio55Yenileme50lists = [np.array(GenelHitRatio55Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Yenileme50lists)
GenelHitRatio55Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Yenileme50nonseasonality)
GenelHitRatio55Yenileme50predict1 = ([GenelHitRatio55Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Yenileme50pre2 = pd.DataFrame(GenelHitRatio55Yenileme50predict1)
GenelHitRatio55Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio55Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio55Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Yenileme50LowerInterval,
                        "Upper": GenelHitRatio55Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme50predict1 = ([GenelHitRatio55Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio55Yenileme50p1.append(float(str(GenelHitRatio55Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Yenileme50p1)
GenelHitRatio55Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio55Yenileme50p1,
                          'Lower': GenelHitRatio55Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio55Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio55Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Yenileme50finallist = pd.merge(GenelHitRatio55Yenileme50list, GenelHitRatio55Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio55Yenileme50finallist)
GenelHitRatio55Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio55Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio55Yenileme50finallist["Lower"][i]) & (GenelHitRatio55Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio55Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Yenileme50finallist[GenelHitRatio55Yenileme50finallist["Alert"]==1])

#Ultimate_1Yenileme40

GenelHitRatio1Yenileme40 = np.array(Yenileme40[1])
print(GenelHitRatio1Yenileme40)
for a in GenelHitRatio1Yenileme40:
    GenelHitRatio1Yenileme40lists = [np.array(GenelHitRatio1Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Yenileme40lists)
GenelHitRatio1Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Yenileme40nonseasonality)
GenelHitRatio1Yenileme40predict1 = ([GenelHitRatio1Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Yenileme40pre2 = pd.DataFrame(GenelHitRatio1Yenileme40predict1)
GenelHitRatio1Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio1Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio1Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Yenileme40LowerInterval,
                        "Upper": GenelHitRatio1Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme40predict1 = ([GenelHitRatio1Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio1Yenileme40p1.append(float(str(GenelHitRatio1Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Yenileme40p1)
GenelHitRatio1Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio1Yenileme40p1,
                          'Lower': GenelHitRatio1Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio1Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio1Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Yenileme40finallist = pd.merge(GenelHitRatio1Yenileme40list, GenelHitRatio1Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio1Yenileme40finallist)
GenelHitRatio1Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio1Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio1Yenileme40finallist["Lower"][i]) & (GenelHitRatio1Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio1Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Yenileme40finallist[GenelHitRatio1Yenileme40finallist["Alert"]==1])

#Ultimate_6Yenileme40

GenelHitRatio6Yenileme40 = np.array(Yenileme40[6])
print(GenelHitRatio6Yenileme40)
for a in GenelHitRatio6Yenileme40:
    GenelHitRatio6Yenileme40lists = [np.array(GenelHitRatio6Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Yenileme40lists)
GenelHitRatio6Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Yenileme40nonseasonality)
GenelHitRatio6Yenileme40predict1 = ([GenelHitRatio6Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Yenileme40pre2 = pd.DataFrame(GenelHitRatio6Yenileme40predict1)
GenelHitRatio6Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio6Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio6Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Yenileme40LowerInterval,
                        "Upper": GenelHitRatio6Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme40predict1 = ([GenelHitRatio6Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio6Yenileme40p1.append(float(str(GenelHitRatio6Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Yenileme40p1)
GenelHitRatio6Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio6Yenileme40p1,
                          'Lower': GenelHitRatio6Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio6Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio6Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Yenileme40finallist = pd.merge(GenelHitRatio6Yenileme40list, GenelHitRatio6Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio6Yenileme40finallist)
GenelHitRatio6Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio6Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio6Yenileme40finallist["Lower"][i]) & (GenelHitRatio6Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio6Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Yenileme40finallist[GenelHitRatio6Yenileme40finallist["Alert"]==1])

#Ultimate_7Yenileme40

GenelHitRatio7Yenileme40 = np.array(Yenileme40[7])
print(GenelHitRatio7Yenileme40)
for a in GenelHitRatio7Yenileme40:
    GenelHitRatio7Yenileme40lists = [np.array(GenelHitRatio7Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Yenileme40lists)
GenelHitRatio7Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Yenileme40nonseasonality)
GenelHitRatio7Yenileme40predict1 = ([GenelHitRatio7Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Yenileme40pre2 = pd.DataFrame(GenelHitRatio7Yenileme40predict1)
GenelHitRatio7Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio7Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio7Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Yenileme40LowerInterval,
                        "Upper": GenelHitRatio7Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme40predict1 = ([GenelHitRatio7Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio7Yenileme40p1.append(float(str(GenelHitRatio7Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Yenileme40p1)
GenelHitRatio7Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio7Yenileme40p1,
                          'Lower': GenelHitRatio7Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio7Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio7Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Yenileme40finallist = pd.merge(GenelHitRatio7Yenileme40list, GenelHitRatio7Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio7Yenileme40finallist)
GenelHitRatio7Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio7Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio7Yenileme40finallist["Lower"][i]) & (GenelHitRatio7Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio7Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Yenileme40finallist[GenelHitRatio7Yenileme40finallist["Alert"]==1])

#Ultimate_16Yenileme40

GenelHitRatio16Yenileme40 = np.array(Yenileme40[16])
print(GenelHitRatio16Yenileme40)
for a in GenelHitRatio16Yenileme40:
    GenelHitRatio16Yenileme40lists = [np.array(GenelHitRatio16Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Yenileme40lists)
GenelHitRatio16Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Yenileme40nonseasonality)
GenelHitRatio16Yenileme40predict1 = ([GenelHitRatio16Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Yenileme40pre2 = pd.DataFrame(GenelHitRatio16Yenileme40predict1)
GenelHitRatio16Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio16Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio16Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Yenileme40LowerInterval,
                        "Upper": GenelHitRatio16Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme40predict1 = ([GenelHitRatio16Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio16Yenileme40p1.append(float(str(GenelHitRatio16Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Yenileme40p1)
GenelHitRatio16Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio16Yenileme40p1,
                          'Lower': GenelHitRatio16Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio16Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio16Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Yenileme40finallist = pd.merge(GenelHitRatio16Yenileme40list, GenelHitRatio16Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio16Yenileme40finallist)
GenelHitRatio16Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio16Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio16Yenileme40finallist["Lower"][i]) & (GenelHitRatio16Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio16Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Yenileme40finallist[GenelHitRatio16Yenileme40finallist["Alert"]==1])

#Ultimate_33Yenileme40

GenelHitRatio33Yenileme40 = np.array(Yenileme40[33])
print(GenelHitRatio33Yenileme40)
for a in GenelHitRatio33Yenileme40:
    GenelHitRatio33Yenileme40lists = [np.array(GenelHitRatio33Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Yenileme40lists)
GenelHitRatio33Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Yenileme40nonseasonality)
GenelHitRatio33Yenileme40predict1 = ([GenelHitRatio33Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Yenileme40pre2 = pd.DataFrame(GenelHitRatio33Yenileme40predict1)
GenelHitRatio33Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio33Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio33Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Yenileme40LowerInterval,
                        "Upper": GenelHitRatio33Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme40predict1 = ([GenelHitRatio33Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio33Yenileme40p1.append(float(str(GenelHitRatio33Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Yenileme40p1)
GenelHitRatio33Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio33Yenileme40p1,
                          'Lower': GenelHitRatio33Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio33Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio33Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Yenileme40finallist = pd.merge(GenelHitRatio33Yenileme40list, GenelHitRatio33Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio33Yenileme40finallist)
GenelHitRatio33Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio33Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio33Yenileme40finallist["Lower"][i]) & (GenelHitRatio33Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio33Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Yenileme40finallist[GenelHitRatio33Yenileme40finallist["Alert"]==1])

#Ultimate_34Yenileme40

GenelHitRatio34Yenileme40 = np.array(Yenileme40[34])
print(GenelHitRatio34Yenileme40)
for a in GenelHitRatio34Yenileme40:
    GenelHitRatio34Yenileme40lists = [np.array(GenelHitRatio34Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Yenileme40lists)
GenelHitRatio34Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Yenileme40nonseasonality)
GenelHitRatio34Yenileme40predict1 = ([GenelHitRatio34Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Yenileme40pre2 = pd.DataFrame(GenelHitRatio34Yenileme40predict1)
GenelHitRatio34Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio34Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio34Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Yenileme40LowerInterval,
                        "Upper": GenelHitRatio34Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme40predict1 = ([GenelHitRatio34Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio34Yenileme40p1.append(float(str(GenelHitRatio34Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Yenileme40p1)
GenelHitRatio34Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio34Yenileme40p1,
                          'Lower': GenelHitRatio34Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio34Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio34Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Yenileme40finallist = pd.merge(GenelHitRatio34Yenileme40list, GenelHitRatio34Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio34Yenileme40finallist)
GenelHitRatio34Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio34Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio34Yenileme40finallist["Lower"][i]) & (GenelHitRatio34Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio34Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Yenileme40finallist[GenelHitRatio34Yenileme40finallist["Alert"]==1])



#Ultimate_35Yenileme40

GenelHitRatio35Yenileme40 = np.array(Yenileme40[35])
print(GenelHitRatio35Yenileme40)
for a in GenelHitRatio35Yenileme40:
    GenelHitRatio35Yenileme40lists = [np.array(GenelHitRatio35Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Yenileme40lists)
GenelHitRatio35Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Yenileme40nonseasonality)
GenelHitRatio35Yenileme40predict1 = ([GenelHitRatio35Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Yenileme40pre2 = pd.DataFrame(GenelHitRatio35Yenileme40predict1)
GenelHitRatio35Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio35Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio35Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Yenileme40LowerInterval,
                        "Upper": GenelHitRatio35Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme40predict1 = ([GenelHitRatio35Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio35Yenileme40p1.append(float(str(GenelHitRatio35Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Yenileme40p1)
GenelHitRatio35Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio35Yenileme40p1,
                          'Lower': GenelHitRatio35Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio35Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio35Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Yenileme40finallist = pd.merge(GenelHitRatio35Yenileme40list, GenelHitRatio35Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio35Yenileme40finallist)
GenelHitRatio35Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio35Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio35Yenileme40finallist["Lower"][i]) & (GenelHitRatio35Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio35Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Yenileme40finallist[GenelHitRatio35Yenileme40finallist["Alert"]==1])

#Ultimate_38Yenileme40

GenelHitRatio38Yenileme40 = np.array(Yenileme40[38])
print(GenelHitRatio38Yenileme40)
for a in GenelHitRatio38Yenileme40:
    GenelHitRatio38Yenileme40lists = [np.array(GenelHitRatio38Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Yenileme40lists)
GenelHitRatio38Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Yenileme40nonseasonality)
GenelHitRatio38Yenileme40predict1 = ([GenelHitRatio38Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Yenileme40pre2 = pd.DataFrame(GenelHitRatio38Yenileme40predict1)
GenelHitRatio38Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio38Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio38Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Yenileme40LowerInterval,
                        "Upper": GenelHitRatio38Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme40predict1 = ([GenelHitRatio38Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio38Yenileme40p1.append(float(str(GenelHitRatio38Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Yenileme40p1)
GenelHitRatio38Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio38Yenileme40p1,
                          'Lower': GenelHitRatio38Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio38Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio38Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Yenileme40finallist = pd.merge(GenelHitRatio38Yenileme40list, GenelHitRatio38Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio38Yenileme40finallist)
GenelHitRatio38Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio38Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio38Yenileme40finallist["Lower"][i]) & (GenelHitRatio38Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio38Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Yenileme40finallist[GenelHitRatio38Yenileme40finallist["Alert"]==1])

#Ultimate_41Yenileme40

GenelHitRatio41Yenileme40 = np.array(Yenileme40[41])
print(GenelHitRatio41Yenileme40)
for a in GenelHitRatio41Yenileme40:
    GenelHitRatio41Yenileme40lists = [np.array(GenelHitRatio41Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Yenileme40lists)
GenelHitRatio41Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Yenileme40nonseasonality)
GenelHitRatio41Yenileme40predict1 = ([GenelHitRatio41Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Yenileme40pre2 = pd.DataFrame(GenelHitRatio41Yenileme40predict1)
GenelHitRatio41Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio41Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio41Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Yenileme40LowerInterval,
                        "Upper": GenelHitRatio41Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme40predict1 = ([GenelHitRatio41Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio41Yenileme40p1.append(float(str(GenelHitRatio41Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Yenileme40p1)
GenelHitRatio41Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio41Yenileme40p1,
                          'Lower': GenelHitRatio41Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio41Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio41Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Yenileme40finallist = pd.merge(GenelHitRatio41Yenileme40list, GenelHitRatio41Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio41Yenileme40finallist)
GenelHitRatio41Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio41Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio41Yenileme40finallist["Lower"][i]) & (GenelHitRatio41Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio41Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Yenileme40finallist[GenelHitRatio41Yenileme40finallist["Alert"]==1])

#Ultimate_55Yenileme40

GenelHitRatio55Yenileme40 = np.array(Yenileme40[55])
print(GenelHitRatio55Yenileme40)
for a in GenelHitRatio55Yenileme40:
    GenelHitRatio55Yenileme40lists = [np.array(GenelHitRatio55Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Yenileme40lists)
GenelHitRatio55Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Yenileme40nonseasonality)
GenelHitRatio55Yenileme40predict1 = ([GenelHitRatio55Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Yenileme40pre2 = pd.DataFrame(GenelHitRatio55Yenileme40predict1)
GenelHitRatio55Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio55Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio55Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Yenileme40LowerInterval,
                        "Upper": GenelHitRatio55Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme40predict1 = ([GenelHitRatio55Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio55Yenileme40p1.append(float(str(GenelHitRatio55Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Yenileme40p1)
GenelHitRatio55Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio55Yenileme40p1,
                          'Lower': GenelHitRatio55Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio55Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio55Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Yenileme40finallist = pd.merge(GenelHitRatio55Yenileme40list, GenelHitRatio55Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio55Yenileme40finallist)
GenelHitRatio55Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio55Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio55Yenileme40finallist["Lower"][i]) & (GenelHitRatio55Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio55Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Yenileme40finallist[GenelHitRatio55Yenileme40finallist["Alert"]==1])

#Ultimate_1Yenileme30

GenelHitRatio1Yenileme30 = np.array(Yenileme30[1])
print(GenelHitRatio1Yenileme30)
for a in GenelHitRatio1Yenileme30:
    GenelHitRatio1Yenileme30lists = [np.array(GenelHitRatio1Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio1Yenileme30lists)
GenelHitRatio1Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio1Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio1Yenileme30nonseasonality)
GenelHitRatio1Yenileme30predict1 = ([GenelHitRatio1Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio1Yenileme30pre2 = pd.DataFrame(GenelHitRatio1Yenileme30predict1)
GenelHitRatio1Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio1Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio1Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio1Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio1Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio1Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio1Yenileme30LowerInterval,
                        "Upper": GenelHitRatio1Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio1Yenileme30predict1 = ([GenelHitRatio1Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio1Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio1Yenileme30p1.append(float(str(GenelHitRatio1Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio1Yenileme30p1)
GenelHitRatio1Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio1Yenileme30p1,
                          'Lower': GenelHitRatio1Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio1Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio1Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio1Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio1Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio1Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[1][49:],
                     'Sira': range(0,79),})
GenelHitRatio1Yenileme30finallist = pd.merge(GenelHitRatio1Yenileme30list, GenelHitRatio1Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio1Yenileme30finallist)
GenelHitRatio1Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio1Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio1Yenileme30finallist["Lower"][i]) & (GenelHitRatio1Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio1Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio1Yenileme30finallist[GenelHitRatio1Yenileme30finallist["Alert"]==1])

#Ultimate_6Yenileme30

GenelHitRatio6Yenileme30 = np.array(Yenileme30[6])
print(GenelHitRatio6Yenileme30)
for a in GenelHitRatio6Yenileme30:
    GenelHitRatio6Yenileme30lists = [np.array(GenelHitRatio6Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio6Yenileme30lists)
GenelHitRatio6Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio6Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio6Yenileme30nonseasonality)
GenelHitRatio6Yenileme30predict1 = ([GenelHitRatio6Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio6Yenileme30pre2 = pd.DataFrame(GenelHitRatio6Yenileme30predict1)
GenelHitRatio6Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio6Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio6Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio6Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio6Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio6Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio6Yenileme30LowerInterval,
                        "Upper": GenelHitRatio6Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio6Yenileme30predict1 = ([GenelHitRatio6Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio6Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio6Yenileme30p1.append(float(str(GenelHitRatio6Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio6Yenileme30p1)
GenelHitRatio6Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio6Yenileme30p1,
                          'Lower': GenelHitRatio6Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio6Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio6Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio6Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio6Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio6Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[6][49:],
                     'Sira': range(0,79),})
GenelHitRatio6Yenileme30finallist = pd.merge(GenelHitRatio6Yenileme30list, GenelHitRatio6Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio6Yenileme30finallist)
GenelHitRatio6Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio6Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio6Yenileme30finallist["Lower"][i]) & (GenelHitRatio6Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio6Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio6Yenileme30finallist[GenelHitRatio6Yenileme30finallist["Alert"]==1])

#Ultimate_7Yenileme30

GenelHitRatio7Yenileme30 = np.array(Yenileme30[7])
print(GenelHitRatio7Yenileme30)
for a in GenelHitRatio7Yenileme30:
    GenelHitRatio7Yenileme30lists = [np.array(GenelHitRatio7Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Yenileme30lists)
GenelHitRatio7Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Yenileme30nonseasonality)
GenelHitRatio7Yenileme30predict1 = ([GenelHitRatio7Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Yenileme30pre2 = pd.DataFrame(GenelHitRatio7Yenileme30predict1)
GenelHitRatio7Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio7Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio7Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Yenileme30LowerInterval,
                        "Upper": GenelHitRatio7Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme30predict1 = ([GenelHitRatio7Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio7Yenileme30p1.append(float(str(GenelHitRatio7Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Yenileme30p1)
GenelHitRatio7Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio7Yenileme30p1,
                          'Lower': GenelHitRatio7Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio7Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio7Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Yenileme30finallist = pd.merge(GenelHitRatio7Yenileme30list, GenelHitRatio7Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio7Yenileme30finallist)
GenelHitRatio7Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio7Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio7Yenileme30finallist["Lower"][i]) & (GenelHitRatio7Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio7Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Yenileme30finallist[GenelHitRatio7Yenileme30finallist["Alert"]==1])

#Ultimate_16Yenileme30

GenelHitRatio16Yenileme30 = np.array(Yenileme30[16])
print(GenelHitRatio16Yenileme30)
for a in GenelHitRatio16Yenileme30:
    GenelHitRatio16Yenileme30lists = [np.array(GenelHitRatio16Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Yenileme30lists)
GenelHitRatio16Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Yenileme30nonseasonality)
GenelHitRatio16Yenileme30predict1 = ([GenelHitRatio16Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Yenileme30pre2 = pd.DataFrame(GenelHitRatio16Yenileme30predict1)
GenelHitRatio16Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio16Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio16Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Yenileme30LowerInterval,
                        "Upper": GenelHitRatio16Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme30predict1 = ([GenelHitRatio16Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio16Yenileme30p1.append(float(str(GenelHitRatio16Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Yenileme30p1)
GenelHitRatio16Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio16Yenileme30p1,
                          'Lower': GenelHitRatio16Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio16Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio16Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Yenileme30finallist = pd.merge(GenelHitRatio16Yenileme30list, GenelHitRatio16Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio16Yenileme30finallist)
GenelHitRatio16Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio16Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio16Yenileme30finallist["Lower"][i]) & (GenelHitRatio16Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio16Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Yenileme30finallist[GenelHitRatio16Yenileme30finallist["Alert"]==1])

#Ultimate_33Yenileme30

GenelHitRatio33Yenileme30 = np.array(Yenileme30[33])
print(GenelHitRatio33Yenileme30)
for a in GenelHitRatio33Yenileme30:
    GenelHitRatio33Yenileme30lists = [np.array(GenelHitRatio33Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio33Yenileme30lists)
GenelHitRatio33Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio33Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio33Yenileme30nonseasonality)
GenelHitRatio33Yenileme30predict1 = ([GenelHitRatio33Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio33Yenileme30pre2 = pd.DataFrame(GenelHitRatio33Yenileme30predict1)
GenelHitRatio33Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio33Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio33Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio33Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio33Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio33Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio33Yenileme30LowerInterval,
                        "Upper": GenelHitRatio33Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio33Yenileme30predict1 = ([GenelHitRatio33Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio33Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio33Yenileme30p1.append(float(str(GenelHitRatio33Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio33Yenileme30p1)
GenelHitRatio33Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio33Yenileme30p1,
                          'Lower': GenelHitRatio33Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio33Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio33Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio33Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio33Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio33Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[33][49:],
                     'Sira': range(0,79),})
GenelHitRatio33Yenileme30finallist = pd.merge(GenelHitRatio33Yenileme30list, GenelHitRatio33Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio33Yenileme30finallist)
GenelHitRatio33Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio33Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio33Yenileme30finallist["Lower"][i]) & (GenelHitRatio33Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio33Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio33Yenileme30finallist[GenelHitRatio33Yenileme30finallist["Alert"]==1])

#Ultimate_34Yenileme30

GenelHitRatio34Yenileme30 = np.array(Yenileme30[34])
print(GenelHitRatio34Yenileme30)
for a in GenelHitRatio34Yenileme30:
    GenelHitRatio34Yenileme30lists = [np.array(GenelHitRatio34Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Yenileme30lists)
GenelHitRatio34Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Yenileme30nonseasonality)
GenelHitRatio34Yenileme30predict1 = ([GenelHitRatio34Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Yenileme30pre2 = pd.DataFrame(GenelHitRatio34Yenileme30predict1)
GenelHitRatio34Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio34Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio34Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Yenileme30LowerInterval,
                        "Upper": GenelHitRatio34Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme30predict1 = ([GenelHitRatio34Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio34Yenileme30p1.append(float(str(GenelHitRatio34Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Yenileme30p1)
GenelHitRatio34Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio34Yenileme30p1,
                          'Lower': GenelHitRatio34Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio34Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio34Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Yenileme30finallist = pd.merge(GenelHitRatio34Yenileme30list, GenelHitRatio34Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio34Yenileme30finallist)
GenelHitRatio34Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio34Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio34Yenileme30finallist["Lower"][i]) & (GenelHitRatio34Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio34Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Yenileme30finallist[GenelHitRatio34Yenileme30finallist["Alert"]==1])



#Ultimate_35Yenileme30

GenelHitRatio35Yenileme30 = np.array(Yenileme30[35])
print(GenelHitRatio35Yenileme30)
for a in GenelHitRatio35Yenileme30:
    GenelHitRatio35Yenileme30lists = [np.array(GenelHitRatio35Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Yenileme30lists)
GenelHitRatio35Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Yenileme30nonseasonality)
GenelHitRatio35Yenileme30predict1 = ([GenelHitRatio35Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Yenileme30pre2 = pd.DataFrame(GenelHitRatio35Yenileme30predict1)
GenelHitRatio35Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio35Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio35Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Yenileme30LowerInterval,
                        "Upper": GenelHitRatio35Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme30predict1 = ([GenelHitRatio35Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio35Yenileme30p1.append(float(str(GenelHitRatio35Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Yenileme30p1)
GenelHitRatio35Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio35Yenileme30p1,
                          'Lower': GenelHitRatio35Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio35Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio35Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Yenileme30finallist = pd.merge(GenelHitRatio35Yenileme30list, GenelHitRatio35Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio35Yenileme30finallist)
GenelHitRatio35Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio35Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio35Yenileme30finallist["Lower"][i]) & (GenelHitRatio35Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio35Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Yenileme30finallist[GenelHitRatio35Yenileme30finallist["Alert"]==1])

#Ultimate_38Yenileme30

GenelHitRatio38Yenileme30 = np.array(Yenileme30[38])
print(GenelHitRatio38Yenileme30)
for a in GenelHitRatio38Yenileme30:
    GenelHitRatio38Yenileme30lists = [np.array(GenelHitRatio38Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio38Yenileme30lists)
GenelHitRatio38Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio38Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio38Yenileme30nonseasonality)
GenelHitRatio38Yenileme30predict1 = ([GenelHitRatio38Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio38Yenileme30pre2 = pd.DataFrame(GenelHitRatio38Yenileme30predict1)
GenelHitRatio38Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio38Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio38Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio38Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio38Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio38Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio38Yenileme30LowerInterval,
                        "Upper": GenelHitRatio38Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio38Yenileme30predict1 = ([GenelHitRatio38Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio38Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio38Yenileme30p1.append(float(str(GenelHitRatio38Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio38Yenileme30p1)
GenelHitRatio38Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio38Yenileme30p1,
                          'Lower': GenelHitRatio38Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio38Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio38Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio38Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio38Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio38Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[38][49:],
                     'Sira': range(0,79),})
GenelHitRatio38Yenileme30finallist = pd.merge(GenelHitRatio38Yenileme30list, GenelHitRatio38Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio38Yenileme30finallist)
GenelHitRatio38Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio38Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio38Yenileme30finallist["Lower"][i]) & (GenelHitRatio38Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio38Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio38Yenileme30finallist[GenelHitRatio38Yenileme30finallist["Alert"]==1])

#Ultimate_41Yenileme30

GenelHitRatio41Yenileme30 = np.array(Yenileme30[41])
print(GenelHitRatio41Yenileme30)
for a in GenelHitRatio41Yenileme30:
    GenelHitRatio41Yenileme30lists = [np.array(GenelHitRatio41Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio41Yenileme30lists)
GenelHitRatio41Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio41Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio41Yenileme30nonseasonality)
GenelHitRatio41Yenileme30predict1 = ([GenelHitRatio41Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio41Yenileme30pre2 = pd.DataFrame(GenelHitRatio41Yenileme30predict1)
GenelHitRatio41Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio41Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio41Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio41Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio41Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio41Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio41Yenileme30LowerInterval,
                        "Upper": GenelHitRatio41Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio41Yenileme30predict1 = ([GenelHitRatio41Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio41Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio41Yenileme30p1.append(float(str(GenelHitRatio41Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio41Yenileme30p1)
GenelHitRatio41Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio41Yenileme30p1,
                          'Lower': GenelHitRatio41Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio41Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio41Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio41Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio41Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio41Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[41][49:],
                     'Sira': range(0,79),})
GenelHitRatio41Yenileme30finallist = pd.merge(GenelHitRatio41Yenileme30list, GenelHitRatio41Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio41Yenileme30finallist)
GenelHitRatio41Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio41Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio41Yenileme30finallist["Lower"][i]) & (GenelHitRatio41Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio41Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio41Yenileme30finallist[GenelHitRatio41Yenileme30finallist["Alert"]==1])

#Ultimate_55Yenileme30

GenelHitRatio55Yenileme30 = np.array(Yenileme30[55])
print(GenelHitRatio55Yenileme30)
for a in GenelHitRatio55Yenileme30:
    GenelHitRatio55Yenileme30lists = [np.array(GenelHitRatio55Yenileme30[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Yenileme30lists)
GenelHitRatio55Yenileme30nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Yenileme30[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Yenileme30nonseasonality)
GenelHitRatio55Yenileme30predict1 = ([GenelHitRatio55Yenileme30nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Yenileme30pre2 = pd.DataFrame(GenelHitRatio55Yenileme30predict1)
GenelHitRatio55Yenileme30Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Yenileme30pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme30LowerInterval = [(np.concatenate(GenelHitRatio55Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Yenileme30UpperInterval = [(np.concatenate(GenelHitRatio55Yenileme30Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Yenileme30Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Yenileme30LowerInterval,
                        "Upper": GenelHitRatio55Yenileme30UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme30predict1 = ([GenelHitRatio55Yenileme30nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Yenileme30p1 = []
for i in range(0, 79):
    GenelHitRatio55Yenileme30p1.append(float(str(GenelHitRatio55Yenileme30predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Yenileme30p1)
GenelHitRatio55Yenileme30listpredict = pd.DataFrame({'Predict': GenelHitRatio55Yenileme30p1,
                          'Lower': GenelHitRatio55Yenileme30Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Yenileme30Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Yenileme30list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Yenileme30’',
                       'Yenileme30 aylik hit': GenelHitRatio55Yenileme30lists,
                      'Non-Seasonality': GenelHitRatio55Yenileme30nonseasonality,
                       'Hit Ratio': Yenileme30[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Yenileme30finallist = pd.merge(GenelHitRatio55Yenileme30list, GenelHitRatio55Yenileme30listpredict, on='Sira', how='inner')
print(GenelHitRatio55Yenileme30finallist)
GenelHitRatio55Yenileme30finallist["Alert"]  = [0 if (GenelHitRatio55Yenileme30finallist['Hit Ratio'][i]> GenelHitRatio55Yenileme30finallist["Lower"][i]) & (GenelHitRatio55Yenileme30finallist['Hit Ratio'][i]< GenelHitRatio55Yenileme30finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Yenileme30finallist[GenelHitRatio55Yenileme30finallist["Alert"]==1])





print(GenelHitRatioAllfinallist[GenelHitRatioAllfinallist["Alert"]==1])
print(GenelHitRatioTransferfinallist[GenelHitRatioTransferfinallist["Alert"]==1])
print(GenelHitRatioYenilemefinallist[GenelHitRatioYenilemefinallist["Alert"]==1])
print(GenelHitRatioAll60finallist[GenelHitRatioAll60finallist["Alert"]==1])
print(GenelHitRatioTransfer60finallist[GenelHitRatioTransfer60finallist["Alert"]==1])
print(GenelHitRatioYenileme60finallist[GenelHitRatioYenileme60finallist["Alert"]==1])
print(GenelHitRatioAll55finallist[GenelHitRatioAll55finallist["Alert"]==1])
print(GenelHitRatioTransfer55finallist[GenelHitRatioTransfer55finallist["Alert"]==1])
print(GenelHitRatioYenileme55finallist[GenelHitRatioYenileme55finallist["Alert"]==1])
print(GenelHitRatioAll50finallist[GenelHitRatioAll50finallist["Alert"]==1])
print(GenelHitRatioTransfer50finallist[GenelHitRatioTransfer50finallist["Alert"]==1])
print(GenelHitRatioYenileme50finallist[GenelHitRatioYenileme50finallist["Alert"]==1])
print(GenelHitRatioAll40finallist[GenelHitRatioAll40finallist["Alert"]==1])
print(GenelHitRatioTransfer40finallist[GenelHitRatioTransfer40finallist["Alert"]==1])
print(GenelHitRatioYenileme40finallist[GenelHitRatioYenileme40finallist["Alert"]==1])
print(GenelHitRatioAll30finallist[GenelHitRatioAll30finallist["Alert"]==1])
print(GenelHitRatioTransfer30finallist[GenelHitRatioTransfer30finallist["Alert"]==1])
print(GenelHitRatioYenileme30finallist[GenelHitRatioYenileme30finallist["Alert"]==1])
print(GenelHitRatioMarmarafinallist[GenelHitRatioMarmarafinallist["Alert"]==1])
print(GenelHitRatioTransferMarmarafinallist[GenelHitRatioTransferMarmarafinallist["Alert"]==1])
print(GenelHitRatioYenilemeMarmarafinallist[GenelHitRatioYenilemeMarmarafinallist["Alert"]==1])
print(GenelHitRatioKaradenizfinallist[GenelHitRatioKaradenizfinallist["Alert"]==1])
print(GenelHitRatioTransferKaradenizfinallist[GenelHitRatioTransferKaradenizfinallist["Alert"]==1])
print(GenelHitRatioYenilemeKaradenizfinallist[GenelHitRatioYenilemeKaradenizfinallist["Alert"]==1])
print(GenelHitRatioDoguAnadolufinallist[GenelHitRatioDoguAnadolufinallist["Alert"]==1])
print(GenelHitRatioTransferDoguAnadolufinallist[GenelHitRatioTransferDoguAnadolufinallist["Alert"]==1])
print(GenelHitRatioYenilemeDoguAnadolufinallist[GenelHitRatioYenilemeDoguAnadolufinallist["Alert"]==1])
print(GenelHitRatioAnkaradogufinallist[GenelHitRatioAnkaradogufinallist["Alert"]==1])
print(GenelHitRatioTransferAnkaradogufinallist[GenelHitRatioTransferAnkaradogufinallist["Alert"]==1])
print(GenelHitRatioYenilemeAnkaradogufinallist[GenelHitRatioYenilemeAnkaradogufinallist["Alert"]==1])
print(GenelHitRatioIcAnadolufinallist[GenelHitRatioIcAnadolufinallist["Alert"]==1])
print(GenelHitRatioTransferIcAnadolufinallist[GenelHitRatioTransferIcAnadolufinallist["Alert"]==1])
print(GenelHitRatioYenilemeIcAnadolufinallist[GenelHitRatioYenilemeIcAnadolufinallist["Alert"]==1])
print(GenelHitRatioEgefinallist[GenelHitRatioEgefinallist["Alert"]==1])
print(GenelHitRatioTransferEgefinallist[GenelHitRatioTransferEgefinallist["Alert"]==1])
print(GenelHitRatioYenilemeEgefinallist[GenelHitRatioYenilemeEgefinallist["Alert"]==1])
print(GenelHitRatioAkdenizfinallist[GenelHitRatioAkdenizfinallist["Alert"]==1])
print(GenelHitRatioTransferAkdenizfinallist[GenelHitRatioTransferAkdenizfinallist["Alert"]==1])
print(GenelHitRatioYenilemeAkdenizfinallist[GenelHitRatioYenilemeAkdenizfinallist["Alert"]==1])
print(GenelHitRatio1Transfer60finallist[GenelHitRatio1Transfer60finallist["Alert"]==1])
print(GenelHitRatio6Transfer60finallist[GenelHitRatio6Transfer60finallist["Alert"]==1])
print(GenelHitRatio7Transfer60finallist[GenelHitRatio7Transfer60finallist["Alert"]==1])
print(GenelHitRatio16Transfer60finallist[GenelHitRatio16Transfer60finallist["Alert"]==1])
print(GenelHitRatio33Transfer60finallist[GenelHitRatio33Transfer60finallist["Alert"]==1])
print(GenelHitRatio34Transfer60finallist[GenelHitRatio34Transfer60finallist["Alert"]==1])
print(GenelHitRatio35Transfer60finallist[GenelHitRatio35Transfer60finallist["Alert"]==1])
print(GenelHitRatio38Transfer60finallist[GenelHitRatio38Transfer60finallist["Alert"]==1])
print(GenelHitRatio41Transfer60finallist[GenelHitRatio41Transfer60finallist["Alert"]==1])
print(GenelHitRatio55Transfer60finallist[GenelHitRatio55Transfer60finallist["Alert"]==1])
print(GenelHitRatio1Transfer55finallist[GenelHitRatio1Transfer55finallist["Alert"]==1])
print(GenelHitRatio6Transfer55finallist[GenelHitRatio6Transfer55finallist["Alert"]==1])
print(GenelHitRatio7Transfer55finallist[GenelHitRatio7Transfer55finallist["Alert"]==1])
print(GenelHitRatio16Transfer55finallist[GenelHitRatio16Transfer55finallist["Alert"]==1])
print(GenelHitRatio33Transfer55finallist[GenelHitRatio33Transfer55finallist["Alert"]==1])
print(GenelHitRatio34Transfer55finallist[GenelHitRatio34Transfer55finallist["Alert"]==1])
print(GenelHitRatio35Transfer55finallist[GenelHitRatio35Transfer55finallist["Alert"]==1])
print(GenelHitRatio38Transfer55finallist[GenelHitRatio38Transfer55finallist["Alert"]==1])
print(GenelHitRatio41Transfer55finallist[GenelHitRatio41Transfer55finallist["Alert"]==1])
print(GenelHitRatio55Transfer55finallist[GenelHitRatio55Transfer55finallist["Alert"]==1])
print(GenelHitRatio1Transfer50finallist[GenelHitRatio1Transfer50finallist["Alert"]==1])
print(GenelHitRatio6Transfer50finallist[GenelHitRatio6Transfer50finallist["Alert"]==1])
print(GenelHitRatio7Transfer50finallist[GenelHitRatio7Transfer50finallist["Alert"]==1])
print(GenelHitRatio16Transfer50finallist[GenelHitRatio16Transfer50finallist["Alert"]==1])
print(GenelHitRatio33Transfer50finallist[GenelHitRatio33Transfer50finallist["Alert"]==1])
print(GenelHitRatio34Transfer50finallist[GenelHitRatio34Transfer50finallist["Alert"]==1])
print(GenelHitRatio35Transfer50finallist[GenelHitRatio35Transfer50finallist["Alert"]==1])
print(GenelHitRatio38Transfer50finallist[GenelHitRatio38Transfer50finallist["Alert"]==1])
print(GenelHitRatio41Transfer50finallist[GenelHitRatio41Transfer50finallist["Alert"]==1])
print(GenelHitRatio55Transfer50finallist[GenelHitRatio55Transfer50finallist["Alert"]==1])
print(GenelHitRatio1Transfer40finallist[GenelHitRatio1Transfer40finallist["Alert"]==1])
print(GenelHitRatio6Transfer40finallist[GenelHitRatio6Transfer40finallist["Alert"]==1])
print(GenelHitRatio7Transfer40finallist[GenelHitRatio7Transfer40finallist["Alert"]==1])
print(GenelHitRatio16Transfer40finallist[GenelHitRatio16Transfer40finallist["Alert"]==1])
print(GenelHitRatio33Transfer40finallist[GenelHitRatio33Transfer40finallist["Alert"]==1])
print(GenelHitRatio34Transfer40finallist[GenelHitRatio34Transfer40finallist["Alert"]==1])
print(GenelHitRatio35Transfer40finallist[GenelHitRatio35Transfer40finallist["Alert"]==1])
print(GenelHitRatio38Transfer40finallist[GenelHitRatio38Transfer40finallist["Alert"]==1])
print(GenelHitRatio41Transfer40finallist[GenelHitRatio41Transfer40finallist["Alert"]==1])
print(GenelHitRatio55Transfer40finallist[GenelHitRatio55Transfer40finallist["Alert"]==1])
print(GenelHitRatio1Transfer30finallist[GenelHitRatio1Transfer30finallist["Alert"]==1])
print(GenelHitRatio6Transfer30finallist[GenelHitRatio6Transfer30finallist["Alert"]==1])
print(GenelHitRatio7Transfer30finallist[GenelHitRatio7Transfer30finallist["Alert"]==1])
print(GenelHitRatio16Transfer30finallist[GenelHitRatio16Transfer30finallist["Alert"]==1])
print(GenelHitRatio33Transfer30finallist[GenelHitRatio33Transfer30finallist["Alert"]==1])
print(GenelHitRatio34Transfer30finallist[GenelHitRatio34Transfer30finallist["Alert"]==1])
print(GenelHitRatio35Transfer30finallist[GenelHitRatio35Transfer30finallist["Alert"]==1])
print(GenelHitRatio38Transfer30finallist[GenelHitRatio38Transfer30finallist["Alert"]==1])
print(GenelHitRatio41Transfer30finallist[GenelHitRatio41Transfer30finallist["Alert"]==1])
print(GenelHitRatio55Transfer30finallist[GenelHitRatio55Transfer30finallist["Alert"]==1])
print(GenelHitRatio1Yenileme60finallist[GenelHitRatio1Yenileme60finallist["Alert"]==1])
print(GenelHitRatio6Yenileme60finallist[GenelHitRatio6Yenileme60finallist["Alert"]==1])
print(GenelHitRatio7Yenileme60finallist[GenelHitRatio7Yenileme60finallist["Alert"]==1])
print(GenelHitRatio16Yenileme60finallist[GenelHitRatio16Yenileme60finallist["Alert"]==1])
print(GenelHitRatio33Yenileme60finallist[GenelHitRatio33Yenileme60finallist["Alert"]==1])
print(GenelHitRatio34Yenileme60finallist[GenelHitRatio34Yenileme60finallist["Alert"]==1])
print(GenelHitRatio35Yenileme60finallist[GenelHitRatio35Yenileme60finallist["Alert"]==1])
print(GenelHitRatio38Yenileme60finallist[GenelHitRatio38Yenileme60finallist["Alert"]==1])
print(GenelHitRatio41Yenileme60finallist[GenelHitRatio41Yenileme60finallist["Alert"]==1])
print(GenelHitRatio55Yenileme60finallist[GenelHitRatio55Yenileme60finallist["Alert"]==1])
print(GenelHitRatio1Yenileme55finallist[GenelHitRatio1Yenileme55finallist["Alert"]==1])
print(GenelHitRatio6Yenileme55finallist[GenelHitRatio6Yenileme55finallist["Alert"]==1])
print(GenelHitRatio7Yenileme55finallist[GenelHitRatio7Yenileme55finallist["Alert"]==1])
print(GenelHitRatio16Yenileme55finallist[GenelHitRatio16Yenileme55finallist["Alert"]==1])
print(GenelHitRatio33Yenileme55finallist[GenelHitRatio33Yenileme55finallist["Alert"]==1])
print(GenelHitRatio34Yenileme55finallist[GenelHitRatio34Yenileme55finallist["Alert"]==1])
print(GenelHitRatio35Yenileme55finallist[GenelHitRatio35Yenileme55finallist["Alert"]==1])
print(GenelHitRatio38Yenileme55finallist[GenelHitRatio38Yenileme55finallist["Alert"]==1])
print(GenelHitRatio41Yenileme55finallist[GenelHitRatio41Yenileme55finallist["Alert"]==1])
print(GenelHitRatio55Yenileme55finallist[GenelHitRatio55Yenileme55finallist["Alert"]==1])
print(GenelHitRatio1Yenileme50finallist[GenelHitRatio1Yenileme50finallist["Alert"]==1])
print(GenelHitRatio6Yenileme50finallist[GenelHitRatio6Yenileme50finallist["Alert"]==1])
print(GenelHitRatio7Yenileme50finallist[GenelHitRatio7Yenileme50finallist["Alert"]==1])
print(GenelHitRatio16Yenileme50finallist[GenelHitRatio16Yenileme50finallist["Alert"]==1])
print(GenelHitRatio33Yenileme50finallist[GenelHitRatio33Yenileme50finallist["Alert"]==1])
print(GenelHitRatio34Yenileme50finallist[GenelHitRatio34Yenileme50finallist["Alert"]==1])
print(GenelHitRatio35Yenileme50finallist[GenelHitRatio35Yenileme50finallist["Alert"]==1])
print(GenelHitRatio38Yenileme50finallist[GenelHitRatio38Yenileme50finallist["Alert"]==1])
print(GenelHitRatio41Yenileme50finallist[GenelHitRatio41Yenileme50finallist["Alert"]==1])
print(GenelHitRatio55Yenileme50finallist[GenelHitRatio55Yenileme50finallist["Alert"]==1])
print(GenelHitRatio1Yenileme40finallist[GenelHitRatio1Yenileme40finallist["Alert"]==1])
print(GenelHitRatio6Yenileme40finallist[GenelHitRatio6Yenileme40finallist["Alert"]==1])
print(GenelHitRatio7Yenileme40finallist[GenelHitRatio7Yenileme40finallist["Alert"]==1])
print(GenelHitRatio16Yenileme40finallist[GenelHitRatio16Yenileme40finallist["Alert"]==1])
print(GenelHitRatio33Yenileme40finallist[GenelHitRatio33Yenileme40finallist["Alert"]==1])
print(GenelHitRatio34Yenileme40finallist[GenelHitRatio34Yenileme40finallist["Alert"]==1])
print(GenelHitRatio35Yenileme40finallist[GenelHitRatio35Yenileme40finallist["Alert"]==1])
print(GenelHitRatio38Yenileme40finallist[GenelHitRatio38Yenileme40finallist["Alert"]==1])
print(GenelHitRatio41Yenileme40finallist[GenelHitRatio41Yenileme40finallist["Alert"]==1])
print(GenelHitRatio55Yenileme40finallist[GenelHitRatio55Yenileme40finallist["Alert"]==1])
print(GenelHitRatio1Yenileme30finallist[GenelHitRatio1Yenileme30finallist["Alert"]==1])
print(GenelHitRatio6Yenileme30finallist[GenelHitRatio6Yenileme30finallist["Alert"]==1])
print(GenelHitRatio7Yenileme30finallist[GenelHitRatio7Yenileme30finallist["Alert"]==1])
print(GenelHitRatio16Yenileme30finallist[GenelHitRatio16Yenileme30finallist["Alert"]==1])
print(GenelHitRatio33Yenileme30finallist[GenelHitRatio33Yenileme30finallist["Alert"]==1])
print(GenelHitRatio34Yenileme30finallist[GenelHitRatio34Yenileme30finallist["Alert"]==1])
print(GenelHitRatio35Yenileme30finallist[GenelHitRatio35Yenileme30finallist["Alert"]==1])
print(GenelHitRatio38Yenileme30finallist[GenelHitRatio38Yenileme30finallist["Alert"]==1])
print(GenelHitRatio41Yenileme30finallist[GenelHitRatio41Yenileme30finallist["Alert"]==1])
print(GenelHitRatio55Yenileme30finallist[GenelHitRatio55Yenileme30finallist["Alert"]==1])



