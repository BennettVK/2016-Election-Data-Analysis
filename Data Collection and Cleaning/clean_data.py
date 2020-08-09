import csv
import re
## Raw1
with open("raw1.csv", "r", encoding = "ISO-8859-1") as fin:
    reader = csv.reader(fin)
    readerList = [line for line in reader]
Clean_data = [[readerList[0][3], readerList[0][7], readerList[0][14], readerList[0][19], readerList[0][20], readerList[0][21]]]
for i in readerList:
    if i[2] == 'FALSE' and i[16] == 'US House':
        Clean_data += [[i[3], 'na' if i[12] == '' else re.sub(r" county", "", i[12].lower()), re.sub('\[Write-in\]', 'Write in', i[14]), 'Other' if i[19] == '' else 'Democratic' if i[19] == 'democrat' else i[19].capitalize(), "early" if "arly" in i[20] or "vance" in i[20] or "one stop" in i[20] else "regular" if i[20] == "ed" or "olling" in i[20] or "lection" in i[20] or i[20].lower() == "in person" else "absentee" if "bsentee" in i[20] or i[20] == "mail" else i[20].lower(), i[21]]]
votes_dict = {}
for i in Clean_data[1:]:
    key_info = i[0] + i[1] + i[2] + i[3] + i[4]
    key_info = re.sub(" ", "", key_info)
    if key_info in votes_dict:
        votes_dict[key_info]["votes"] += int(i[5])
    else:
        votes_dict[key_info] = {"info":[i[0], i[1], i[2], i[3], i[4]], "votes":int(i[5])}
final_clean = [[readerList[0][3], readerList[0][7], readerList[0][14], readerList[0][19], readerList[0][20], readerList[0][21], "Total Votes"]]
for i in votes_dict:
    final_clean += [[votes_dict[i]["info"][0], votes_dict[i]["info"][1], votes_dict[i]["info"][2], votes_dict[i]["info"][3], votes_dict[i]["info"][4], votes_dict[i]["votes"]]]
vote_count_dict = {}
for i in Clean_data[1:]:
    count_key = i[0] + i[1]
    if count_key in vote_count_dict:
        vote_count_dict[count_key] += int(i[5])
    else:
        vote_count_dict[count_key] = int(i[5])
for i in vote_count_dict:
    for j in final_clean:
        if i == j[0] + j[1]:
            j += [vote_count_dict[i]]
        else:
            pass
with open ("clean1.csv", "w") as fout:
    writer = csv.writer(fout)
    writer.writerows(final_clean)


    ### Raw2
with open("raw2.csv", "r") as fin:
    reader1 = csv.reader(fin)
    readerList1 = [line for line in reader1]
Clean_data1 = [[readerList1[0][1], readerList1[0][3], readerList1[0][6], readerList1[0][7], readerList1[0][8], readerList1[0][9]]]
for i in readerList1:
    if i[0] == "2016":
        if not i[8] == "NA":
            Clean_data1 += [[i[1], i[3].lower(), i[6], re.sub('Na', 'Other', 'Democratic' if i[7] == 'democrat' else 'Democratic' if i[7] == 'Democrat' else i[7].capitalize()), i[8]]]
tot_vot_dict = {}
for i in Clean_data1[1:]:
    key_info2 = i[0] + i[1]
    if key_info2 in tot_vot_dict:
        tot_vot_dict[key_info2] += int(i[4])
    else:
        tot_vot_dict[key_info2] = int(i[4])
for i in tot_vot_dict:
    for j in Clean_data1:
        if i == j[0] + j[1]:
            j += [tot_vot_dict[i]]
        else:
            pass
with open ("clean2.csv", "w") as fout:
    writer = csv.writer(fout)
    writer.writerows(Clean_data1)

### Raw3
with open("raw3.tsv", "r") as fin:
    reader2 = csv.reader(fin, delimiter="\t")
    readerList2 = [line for line in reader2]
Clean_data2 = [[readerList2[0][3], readerList2[0][7], readerList2[0][14], readerList2[0][19], readerList2[0][20], readerList2[0][21]]]
for i in readerList2:
    if i[2] == 'FALSE' and i[16] == 'US Senate':
        Clean_data2 += [[i[3], 'na' if i[12] == '' else re.sub(r" county", "", i[12].lower()), re.sub('\[Write-in\]', 'Write in', i[14]), 'Other' if i[19] == '' else 'Democratic' if i[19] == 'democrat' else i[19].capitalize(), "early" if "arly" in i[20] or "vance" in i[20] or "one stop" in i[20] else "regular" if i[20] == "ed" or "olling" in i[20] or "lection" in i[20] or i[20].lower() == "in person" else "absentee" if "bsentee" in i[20] or i[20] == "mail" else i[20].lower(), i[21]]]
votes_dict1 = {}
for i in Clean_data2[1:]:
    key_info1 = i[0] + i[1] + i[2] + i[3] + i[4]
    key_info1 = re.sub(" ", "", key_info1)
    if key_info1 in votes_dict1:
        votes_dict1[key_info1]["votes"] += int(i[5])
    else:
        votes_dict1[key_info1] = {"info":[i[0], i[1], i[2], i[3], i[4]], "votes":int(i[5])}
final_clean1 = [[readerList2[0][3], readerList2[0][7], readerList2[0][14], readerList2[0][19], readerList2[0][20], readerList2[0][21], "Total Votes"]]
for i in votes_dict1:
    if not votes_dict1[i]["votes"] == 0:
        final_clean1 += [[votes_dict1[i]["info"][0], votes_dict1[i]["info"][1], votes_dict1[i]["info"][2], votes_dict1[i]["info"][3], votes_dict1[i]["info"][4], votes_dict1[i]["votes"]]]
vote_count_dict1 = {}
for i in final_clean1[1:]:
    count_key1 = i[0] + i[1]
    if count_key1 in vote_count_dict1:
        vote_count_dict1[count_key1] += int(i[5])
    else:
        vote_count_dict1[count_key1] = int(i[5])
for i in vote_count_dict1:
    for j in final_clean1:
        if i == j[0] + j[1]:
            j += [vote_count_dict1[i]]
        else:
            pass
with open ("clean3.csv", "w") as fout:
    writer = csv.writer(fout)
    writer.writerows(final_clean1)
