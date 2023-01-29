import pandas as pd

data = pd.read_csv (r'/home/youffes/result.csv',
                     sep=',' , error_bad_lines=False)
                       
df = pd.DataFrame(data, columns= ['globalcallid_callid','origlegcallidentifier','datetimeorigination','orignodeid','callpartynumber','callingpartyunicodeloginuserid','originalcalledpartynumber','finalcalledpartynumber','finalcalledpartyunicodeloginuserid','datetimeconnect','datetimedisconnect','lastredirectdn','pkid','totalwaittimeinqueue','callingpartynumber','callingpartynumberuri','originalcalledpartynumber_uri','finalcalledpartynumber_uri','lastredirectdn_uri'])

print(df)