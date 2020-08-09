import csv
from pprint import pprint
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
'''Question 1:
What is the correlation between selecting a President and a Congressman of the
same party?
By determining the correlation between top ticket candidates and their party's
other candidates, party strategists can determine the best way to distribute
resources. A high correlation indicates that investing in party-building, or
top-ticket advertising and other campaign activites are the best ways to win
offices. A lower correlation indicates the need for dividing resources to
support individual candidates.
'''
def house_pres_correlation(congress_file, pres_file):
    with open(congress_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    with open(pres_file, "r") as fin:
        reader = csv.reader(fin)
        readerList2 = [line for line in reader]
    pres_dict = {}
    for i in readerList2[1:]:
        key = i[0], i[1]
        if key in pres_dict:
            if i[2] in pres_dict[key]:
                pres_dict[key][i[2]]["votes"] += int(i[4])
                pres_dict[key][i[2]]["vote percent"] = pres_dict[key][i[2]]["votes"] / int(i[5])
            else:
                pres_dict[key][i[2]] = {"party" : i[3], "votes" : int(i[4]), "vote percent" : int(i[4]) / int(i[5])}
        else:
            pres_dict[key] = {i[2] : {"party" : i[3], "votes" : int(i[4]), "vote percent" : int(i[4]) / int(i[5])}}
    winner_list = []
    for i in pres_dict:
        add_val = [0, 0, 0, 0, 0, 0]
        for j in pres_dict[i]:
            if pres_dict[i][j]["votes"] > add_val[4]:
                add_val = [i[0], i[1], j, pres_dict[i][j]["party"], pres_dict[i][j]["votes"], pres_dict[i][j]["vote percent"]]
            else:
                pass
        winner_list.append(add_val)
    house_dict = {}
    for i in readerList1[1:]:
        key1 = i[0] + i[1]
        if key1 in house_dict and i[6]:
            if i[3] in house_dict[key1]:
                house_dict[key1][i[3]] += float(i[5]) / float(i[6])
            else:
                house_dict[key1][i[3]] = float(i[5]) /float(i[6])
        else:
            house_dict[key1] = {i[3] : float(i[5]) / float(i[6])}
    house_pres_cor_list = []
    issue_list = []
    issue_list2 = []
    for i in winner_list:
        if i[0] + i[1] in house_dict:
            if i[3] in house_dict[i[0] + i[1]]:
                house_pres_cor_list += [[i[0], i[1], i[2], i[5], house_dict[i[0] + i[1]][i[3]]]]
            else:
                issue_list2 += [[i[0], i[1], i[3]]]
        else:
            issue_list += [[i[0], i[1]]]
    counter = 0
    correlation_calc = []
    for i in house_pres_cor_list:
        counter += 1
        correlation_calc += [[i[4], i[3]]]
    house_av = 0
    pres_av = 0
    for i in house_pres_cor_list:
        house_av += float(i[4])
        pres_av += float(i[3])
    house_av = house_av / counter
    pres_av = pres_av / counter
    for i in correlation_calc:
        i[0] = i[0] - house_av
        i[1] = i[1] - pres_av
    correlation_calc1 = []
    for i in correlation_calc:
        correlation_calc1 += [[i[0] * i[1], i[0] * i[0], i[1] * i[1]]]
    final_sums = [0, 0, 0]
    for i in correlation_calc1:
        final_sums[0] += i[0]
        final_sums[1] += i[1]
        final_sums[2] += i[2]
    correlation = final_sums[0] / math.sqrt(final_sums[1] * final_sums[2])
    correlation = str(round(correlation, 4) * 100) + "%."
    returnstatment = "Question 1:\nThe county-by-county correlation between votes for Congressmen and their party's Presidential candidate (where the Presidential candidate won in the county) is " + correlation
    return returnstatment


'''Question 2:
What is the correlation between selecting a President and a Senator of the
same party?
This is very similar to the first question in purpose. However, since Senators
are elected statewide (congressmen are elected at a district level), it is
likely that the correlation will be higher because Senators don't have the
ability to engage in an effective "meet-and-greet" strategy.
'''
def senate_pres_correlation(senate_file, pres_file):
    with open(senate_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    with open(pres_file, "r") as fin:
        reader = csv.reader(fin)
        readerList2 = [line for line in reader]
    pres_dict = {}
    for i in readerList2[1:]:
        key = i[0], i[1]
        if key in pres_dict:
            if i[2] in pres_dict[key]:
                pres_dict[key][i[2]]["votes"] += int(i[4])
                pres_dict[key][i[2]]["vote percent"] = pres_dict[key][i[2]]["votes"] / int(i[5])
            else:
                pres_dict[key][i[2]] = {"party" : i[3], "votes" : int(i[4]), "vote percent" : int(i[4]) / int(i[5])}
        else:
            pres_dict[key] = {i[2] : {"party" : i[3], "votes" : int(i[4]), "vote percent" : int(i[4]) / int(i[5])}}
    winner_list = []
    for i in pres_dict:
        add_val = [0, 0, 0, 0, 0, 0]
        for j in pres_dict[i]:
            if pres_dict[i][j]["votes"] > add_val[4]:
                add_val = [i[0], i[1], j, pres_dict[i][j]["party"], pres_dict[i][j]["votes"], pres_dict[i][j]["vote percent"]]
            else:
                pass
        winner_list.append(add_val)
    winner_list.insert(0, ["State", "County", "Candidate", "Party", "Votes", "Vote %"])
    with open("export1.csv", "w") as fout:
        writer = csv.writer(fout)
        writer.writerows(winner_list)
    senate_dict = {}
    for i in readerList1[1:]:
        key1 = i[0] + i[1]
        if key1 in senate_dict:
            if i[3] in senate_dict[key1]:
                senate_dict[key1][i[3]] += float(i[5]) / float(i[6])
            else:
                senate_dict[key1][i[3]] = float(i[5]) /float(i[6])
        else:
            senate_dict[key1] = {i[3] : float(i[5]) / float(i[6])}
    senate_pres_cor_list = []
    issue_list = []
    issue_list2 = []
    for i in winner_list[1:]:
        if i[0] + i[1] in senate_dict:
            if i[3] in senate_dict[i[0] + i[1]]:
                senate_pres_cor_list += [[i[0], i[1], i[2], i[5], senate_dict[i[0] + i[1]][i[3]]]]
            else:
                issue_list2 += [[i[0], i[1], i[3]]]
        else:
            issue_list += [[i[0], i[1]]]
    correlation_calc = []
    for i in senate_pres_cor_list:
        correlation_calc += [[i[4], i[3]]]
    senate_av = 0
    pres_av = 0
    counter = 0
    for i in correlation_calc:
        counter += 1
        i[0] = i[0] - senate_av
        i[1] = i[1] - pres_av
    correlation_calc1 = []
    for i in correlation_calc:
        correlation_calc1 += [[i[0] * i[1], i[0] * i[0], i[1] * i[1]]]
    final_sums = [0, 0, 0]
    for i in correlation_calc1:
        final_sums[0] += i[0]
        final_sums[1] += i[1]
        final_sums[2] += i[2]
    correlation = final_sums[0] / math.sqrt(final_sums[1] * final_sums[2])
    correlation = str(round(correlation, 4) * 100) + "%."
    returnstatment = "Question 2:\nThe county-by-county correlation between votes for Senator and their party's Presidential candidate (where the Presidential candidate won in the county) is " + correlation
    return returnstatment


'''Question 3:
Which Senators most outperformed their party’s Presidential candidate by vote
percent on a state-wide level?
This question can help political strategists determine the most effective
candidates without the noise of wide-spread top-ticket or party support. Those
Senators that most outperorm their party's candidate have proven individual
merit. Thus party strategists hoping to win over new states or defend battle-
ground states should model their candidates after these Senators.
'''
def better_senator(senate_file, pres_file):
    with open(senate_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    with open(pres_file, "r") as fin:
        reader = csv.reader(fin)
        readerList2 = [line for line in reader]
    pres_dict = {}
    for i in readerList2[1:]:
        key = i[0]
        if key in pres_dict:
            if i[3] in pres_dict[key]:
                pres_dict[key][i[3]]["votes"] += int(i[4])
            else:
                pres_dict[key][i[3]] = {"votes" : int(i[4]), "vote percent" : 0}
        else:
            pres_dict[key] = {i[3] : {"votes" : int(i[4]), "vote percent" : 0}}
    total_votes = {}
    for i in pres_dict:
        for j in pres_dict[i]:
            if i in total_votes:
                total_votes[i] += pres_dict[i][j]["votes"]
            else:
                total_votes[i] = pres_dict[i][j]["votes"]
    for i in pres_dict:
        for j in pres_dict[i]:
            pres_dict[i][j]["vote percent"] = pres_dict[i][j]["votes"] / total_votes[i]
    senate_dict = {}
    for i in readerList1[1:]:
        key1 = i[0]
        if key1 in senate_dict:
            if i[2] in senate_dict[key1]:
                senate_dict[key1][i[2]]["votes"] += int(i[5])
            else:
                senate_dict[key1][i[2]] = {"party" : i[3], "votes" : int(i[5]), "vote percent" : 0}
        else:
            senate_dict[key1] = {i[2] : {"party" : i[3], "votes" : int(i[5]), "vote percent" : 0}}
    total_votes1 = {}
    for i in senate_dict:
        for j in senate_dict[i]:
            if i in total_votes1:
                total_votes1[i] += senate_dict[i][j]["votes"]
            else:
                total_votes1[i] = senate_dict[i][j]["votes"]
    for i in senate_dict:
        for j in senate_dict[i]:
            senate_dict[i][j]["vote percent"] = senate_dict[i][j]["votes"] / total_votes1[i]
    winner_list = []
    for i in senate_dict:
        add_val = [0, 0, 0, 0, 0, 0]
        for j in senate_dict[i]:
            if senate_dict[i][j]["votes"] > add_val[3]:
                add_val = [i, j, senate_dict[i][j]["party"], senate_dict[i][j]["votes"], senate_dict[i][j]["vote percent"]]
            else:
                pass
        winner_list.append(add_val)
    for i in winner_list:
        if i[1] == "Rand PAUL" or i[1] == "John Hoeven":
            i[2] = "Republican"
    winner_list.insert(0, ["State", "Candidate", "Party", "Votes", "Vote %"])
    with open("export2.csv", "w") as fout:
        writer = csv.writer(fout)
        writer.writerows(winner_list)
    performance_list = []
    for i in winner_list[1:]:
        performance_list += [[i[0], i[1], i[2], i[4], pres_dict[i[0]][i[2]]["vote percent"], round(float(i[4]) - float(pres_dict[i[0]][i[2]]["vote percent"]), 4) * 100]]
    def sorter(i):
        return i[5]
    performance_list.sort(key=sorter, reverse=True)
    returnstatment1 = [["The top 5 Senators who outperformed their party's Presidential candidate:"]]
    counter = 0
    for i in performance_list[:5]:
        counter += 1
        returnstatment1 += [["{}. Senator {}, {} from {}, outperformed his party's Presidential candidate by {}%.".format(counter, i[1], "Democrat" if i[2] == "Democratic" else i[2], i[0], round(i[5], 2))]]
    return "Question 3:", returnstatment1

'''Question 4:
How do absentee or early ballots differ from regular, election day votes?
This can be an excellent metric of targeted ad selection. If absentee ballots or
early ballots vary significantly from election-day ballots in a particular
county, it may indicate that political ads, which target election-day voters,
may have had substantial effects on the electorate. By using this information
political stratgestis can design future ad campaigns Additionally, an
overarching statstic could indicate that one party had broader ad-based support
or help demonstrate the demographics that choose to vote via absentee or early
ballots.
'''
def vote_types(congress_file, senate_file):
    with open(congress_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    with open(senate_file, "r") as fin:
        reader = csv.reader(fin)
        readerList2 = [line for line in reader]
    congress_dict = {}
    for i in readerList1[1:]:
        if int(i[5]) > 0 and (i[4] == "early" or i[4] == "regular" or i[4] == "absentee"):
            name = i[0] + ", " + i[1]
            if name in congress_dict:
                if i[4] in congress_dict[name]:
                    if i[3] in congress_dict[name][i[4]]:
                        congress_dict[name][i[4]][i[3]] += int(i[5])
                    else:
                        congress_dict[name][i[4]][i[3]] = int(i[5])
                else:
                    congress_dict[name].update({i[4] : {i[3] : int(i[5])}})
            else:
                congress_dict[name] = {i[4] : {i[3] : int(i[5])}}
    senate_dict = {}
    for i in readerList2[1:]:
        if int(i[5]) > 0 and (i[4] == "early" or i[4] == "regular" or i[4] == "absentee"):
            name1 = i[0] + ", " + i[1]
            if name1 in senate_dict:
                if i[4] in senate_dict[name1]:
                    if i[3] in senate_dict[name1][i[4]]:
                        senate_dict[name1][i[4]][i[3]] += int(i[5])
                    else:
                        senate_dict[name1][i[4]][i[3]] = int(i[5])
                else:
                    senate_dict[name1].update({i[4] : {i[3] : int(i[5])}})
            else:
                senate_dict[name1] = {i[4] : {i[3] : int(i[5])}}
    the_list = [["location", "regular rep", "regular dem", "early rep", "early dem", "absentee rep", "absentee dem"]]
    for i in congress_dict:
        for j in congress_dict[i]:
            total_votes2 = 0
            for z in congress_dict[i][j]:
                total_votes2 += congress_dict[i][j][z]
            for z in congress_dict[i][j]:
                congress_dict[i][j][z] /= total_votes2
    for i in senate_dict:
        for j in senate_dict[i]:
            total_votes2 = 0
            for z in senate_dict[i][j]:
                total_votes2 += senate_dict[i][j][z]
            for z in senate_dict[i][j]:
                senate_dict[i][j][z] /= total_votes2
    for i in congress_dict:
        if "regular" in congress_dict[i] and "early" in congress_dict[i]:
            if "absentee" in congress_dict[i]:
                try:
                    the_list += [[i, congress_dict[i]["regular"]["Republican"], congress_dict[i]["regular"]["Democratic"], congress_dict[i]["early"]["Republican"], congress_dict[i]["early"]["Democratic"], congress_dict[i]["absentee"]["Republican"], congress_dict[i]["absentee"]["Democratic"]]]
                except:
                    pass
            else:
                try:
                    the_list += [[i, congress_dict[i]["regular"]["Republican"], congress_dict[i]["regular"]["Democratic"], congress_dict[i]["early"]["Republican"], congress_dict[i]["early"]["Democratic"], "Na", "Na"]]
                except:
                    pass
        elif "regular" in congress_dict[i] and "absentee" in congress_dict[i]:
            try:
                the_list += [[i, congress_dict[i]["regular"]["Republican"], congress_dict[i]["regular"]["Democratic"], "Na", "Na", congress_dict[i]["absentee"]["Republican"], congress_dict[i]["absentee"]["Democratic"]]]
            except:
                pass
    for i in senate_dict:
        if "regular" in senate_dict[i] and "early" in senate_dict[i]:
            if "absentee" in senate_dict[i]:
                try:
                    the_list += [[i, senate_dict[i]["regular"]["Republican"], senate_dict[i]["regular"]["Democratic"], senate_dict[i]["early"]["Republican"], senate_dict[i]["early"]["Democratic"], senate_dict[i]["absentee"]["Republican"], senate_dict[i]["absentee"]["Democratic"]]]
                except:
                    pass
            else:
                try:
                    the_list += [[i, senate_dict[i]["regular"]["Republican"], senate_dict[i]["regular"]["Democratic"], senate_dict[i]["early"]["Republican"], senate_dict[i]["early"]["Democratic"], "Na", "Na"]]
                except:
                    pass
        elif "regular" in senate_dict[i] and "absentee" in senate_dict[i]:
            try:
                the_list += [[i, senate_dict[i]["regular"]["Republican"], senate_dict[i]["regular"]["Democratic"], "Na", "Na", senate_dict[i]["absentee"]["Republican"], senate_dict[i]["absentee"]["Democratic"]]]
            except:
                pass
    final_list = [["location", "Rep. reg-early diff", "Dem. reg-early diff", "Rep. reg-abs diff", "Dem. reg-abs diff"]]
    for i in the_list[1:]:
        if not i[3] == "Na":
            if not i[5] == "Na":
                final_list += [[i[0], float(i[1]) - float(i[3]), float(i[2]) - float(i[4]), float(i[1]) - float(i[5]), float(i[2]) - float(i[6])]]
            else:
                final_list += [[i[0], float(i[1]) - float(i[3]), float(i[2]) - float(i[4]), "Na", "Na"]]
        else:
            final_list += [[i[0], "Na", "Na", float(i[1]) - float(i[5]), float(i[2]) - float(i[6])]]
    avg_reg_early_diff = 0
    counter = 0
    avg_reg_abs_diff = 0
    for i in final_list:
        try:
            avg_reg_early_diff += i[1]
            counter += 1
        except:
            pass
    avg_reg_early_diff /= counter
    counter = 0
    for i in final_list:
        try:
            avg_reg_abs_diff += i[3]
            counter += 1
        except:
            pass
    avg_reg_abs_diff /= counter
    if avg_reg_abs_diff > 0:
        if avg_reg_early_diff > 0:
            returnstatement2 = "Question 4:\nNation-wide absentee voters from a particular county are {}% more Republican and early voters are {}% more Republican than election day voters from their respective counties.".format(round(avg_reg_abs_diff * 100, 2), round(avg_reg_early_diff * 100, 2))
        else:
            returnstatement2 = "Question 4:\nNation-wide absentee voters from a particular county are {}% more Republican and early voters are {}% more Democratic than election day voters from their respective counties.".format(round(avg_reg_abs_diff * 100, 2), round(avg_reg_early_diff * -100, 2))
    elif avg_reg_abs_diff > 0:
        returnstatement2 = "Question 4:\nNation-wide absentee voters from a particular county are {}% more Democratic and early voters are {}% more Republican than election day voters from their respective counties.".format(round(avg_reg_abs_diff * -100, 2), round(avg_reg_early_diff * 100, 2))
    else:
        returnstatement2 = "Question 4:\nNation-wide absentee voters from a particular county are {}% more Democratic and early voters are {}% more Democratic than election day voters from their respective counties.".format(round(avg_reg_abs_diff * -100, 2), round(avg_reg_early_diff * -100, 2))
    return returnstatement2


'''Question 5:
Which counties were the most one-sided in their selection of a President,
Congressman, and Senator?
This can guide political parties use of resources. If a county is staunchly in
favor of one party, it may be a waste of effort and money for the opposing party
to invest resources in that particular county. On the other side of the
spectrum, it also demonstrates which states are the most vulnerable battle-
ground states, helping guide resources to the most contested areas.
'''
def slanted_counties(congress_file, pres_file, senate_file):
    with open(congress_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    with open(pres_file, "r") as fin:
        reader = csv.reader(fin)
        readerList2 = [line for line in reader]
    with open(senate_file, "r") as fin:
        reader = csv.reader(fin)
        readerList3 = [line for line in reader]
    pres_dict = {}
    for i in readerList2[1:]:
        key = i[0], i[1]
        if key in pres_dict:
            if i[2] in pres_dict[key]:
                pres_dict[key][i[2]]["votes"] += int(i[4])
                pres_dict[key][i[2]]["vote percent"] = pres_dict[key][i[2]]["votes"] / int(i[5])
            else:
                pres_dict[key][i[2]] = {"party" : i[3], "votes" : int(i[4]), "vote percent" : int(i[4]) / int(i[5])}
        else:
            pres_dict[key] = {i[2] : {"party" : i[3], "votes" : int(i[4]), "vote percent" : int(i[4]) / int(i[5])}}
    winner_list = []
    for i in pres_dict:
        add_val = [0, 0, 0, 0, 0, 0]
        for j in pres_dict[i]:
            if pres_dict[i][j]["votes"] > add_val[4]:
                add_val = [i[0], i[1], j, pres_dict[i][j]["party"], pres_dict[i][j]["votes"], pres_dict[i][j]["vote percent"]]
            else:
                pass
        winner_list.append(add_val)
    house_dict = {}
    for i in readerList1[1:]:
        key1 = i[0] + i[1]
        if key1 in house_dict and i[6]:
            if i[3] in house_dict[key1]:
                house_dict[key1][i[3]] += float(i[5]) / float(i[6])
            else:
                house_dict[key1][i[3]] = float(i[5]) /float(i[6])
        else:
            house_dict[key1] = {i[3] : float(i[5]) / float(i[6])}
    senate_dict = {}
    for i in readerList3[1:]:
        key2 = i[0] + i[1]
        if key2 in senate_dict:
            if i[3] in senate_dict[key2]:
                senate_dict[key2][i[3]] += float(i[5]) / float(i[6])
            else:
                senate_dict[key2][i[3]] = float(i[5]) /float(i[6])
        else:
            senate_dict[key2] = {i[3] : float(i[5]) / float(i[6])}
    county_av= []
    for i in winner_list:
        if i[0] + i[1] in house_dict and i[0] + i[1] in senate_dict:
            if "Republican" in house_dict[i[0] + i[1]] and "Democratic" in house_dict[i[0] + i[1]] and "Republican" in senate_dict[i[0] + i[1]] and "Democratic" in senate_dict[i[0] + i[1]]:
                if i[3] == "Republican":
                    county_av += [[i[0], i[1], round(i[5] * 100, 2), round(pres_dict[(i[0], i[1])]["Hillary Clinton"]["vote percent"] * 100, 2), round(house_dict[i[0] + i[1]]["Republican"] * 100, 2), round(house_dict[i[0] + i[1]]["Democratic"] * 100, 2), round(senate_dict[i[0] + i[1]]["Republican"] * 100, 2), round(senate_dict[i[0] + i[1]]["Democratic"] * 100, 2), 0, 0, 0]]
                elif i[3] == "Democratic":
                    county_av += [[i[0], i[1], round(pres_dict[(i[0], i[1])]["Donald Trump"]["vote percent"] * 100, 2), round(i[5] * 100, 2), round(house_dict[i[0] + i[1]]["Republican"] * 100, 2), round(house_dict[i[0] + i[1]]["Democratic"] * 100, 2), round(senate_dict[i[0] + i[1]]["Republican"] * 100, 2), round(senate_dict[i[0] + i[1]]["Democratic"] * 100, 2), 0, 0, 0]]
                else:
                    pass
            else:
                pass
        else:
            pass
    for i in county_av:
        higher_avg = 0
        i[8] = round((int(i[2]) + int(i[4]) + int(i[6])) / 3, 2)
        higher_avg = round((int(i[2]) + int(i[4]) + int(i[6])) / 3, 2)
        i[9] = round((int(i[3]) + int(i[5]) + int(i[7])) / 3, 2)
        if round((int(i[3]) + int(i[5]) + int(i[7])) / 3, 2) > round((int(i[2]) + int(i[4]) + int(i[6])) / 3, 2):
            higher_avg = round((int(i[3]) + int(i[5]) + int(i[7])) / 3, 2)
        i[10] = higher_avg
    def sorter(i):
        return i[10]
    county_av.sort(key=sorter, reverse=True)
    county_av.insert(0, ["State", "County", "Rep. Pres. Vote %", "Dem. Pres. Vote %", "Rep. House Vote %", "Dem. House Vote %", "Rep. Senate Vote %", "Dem. Senate Vote %", "Avg. Rep. Vote %", "Avg. Dem. Vote %", "Higher Avg. %"])
    with open ("export3.csv", "w") as fout:
        writer = csv.writer(fout)
        writer.writerows(county_av)
    return_list = [["The 20 most one-sided counties across all three federal elections:"]]
    counter = 0
    for i in county_av[1:21]:
        counter += 1
        if i[8] > i[9]:
            return_list += [[counter, i[0], i[1], "Avg = " + str(i[8]) + "% Republican."]]
        else:
            return_list += [[counter, i[0], i[1], "Avg = " + str(i[9]) + "% Democratic."]]
    return "Question 5:", return_list

'''
Visual 1:
This visual creates a scatterplot with using the top 9 Democratic & Republican
counties by average vote %. It graphs each county using the average vote % of
the House and Senate election on the x axis and the Presidential vote % on the y
axis. It provides greater depth to the driving forces behind the slant of the
county. It lets us know if it was driven by Presidential popularity, party
popularity or a combination of both.
'''
def dem_rep_counties_vis(county_av_file):
    with open(county_av_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    readerList1 = readerList1[1:]
    def sorter(i):
        return float(i[9])
    readerList1.sort(key=sorter, reverse=True)
    Democratic = {"Location" : [], "AvgVote" : [], "PresVote" : [], "AvgCongressVote" : []}
    for i in readerList1[:9]:
        Democratic["Location"] += [i[0] + ", " + i[1]]
        Democratic["AvgVote"] += [float(i[9])]
        Democratic["PresVote"] += [float(i[3])]
        Democratic["AvgCongressVote"] += [(float(i[5]) + float(i[7])) / 2]
    with open(county_av_file, "r") as fin:
        reader = csv.reader(fin)
        readerList2 = [line for line in reader]
    readerList2 = readerList2[1:]
    def sorter(i):
        return float(i[8])
    readerList2.sort(key=sorter, reverse=True)
    Republican = {"Location" : [], "AvgVote" : [], "PresVote" : [], "AvgCongressVote" : []}
    for i in readerList2[0:9]:
        Republican["Location"] += [i[0] + ", " + i[1]]
        Republican["AvgVote"] += [float(i[10])]
        Republican["PresVote"] += [float(i[2])]
        Republican["AvgCongressVote"] += [(float(i[4]) + float(i[6])) / 2]
    plt.scatter(Democratic["AvgCongressVote"], Democratic["PresVote"], label = "Democratic")
    plt.scatter(Republican["AvgCongressVote"], Republican["PresVote"], color="Red", label = "Republican")
    plt.xlabel("Avg. Congress Vote %")
    plt.ylabel("Pres. Vote %")
    plt.legend(loc = "upper left")
    plt.title("Avg. Congress and Presidential Vote % for Top 9 Rep. & Dem. Counties")
    for i in readerList1[0:9]:
        reader = i[0] + ", " + i[1].capitalize()
        if reader == "Maryland, Prince george's":
            plt.annotate(reader, ((float(i[5]) + float(i[7])) / 2,float(i[3])), textcoords="offset points", xytext=(-15,5), ha='center', fontsize = 5)
        elif reader == "New York, New york":
            plt.annotate(reader, ((float(i[5]) + float(i[7])) / 2,float(i[3])), textcoords="offset points", xytext=(10,7), ha='center', fontsize = 5)
        else:
            plt.annotate(reader, ((float(i[5]) + float(i[7])) / 2,float(i[3])), textcoords="offset points", xytext=(0,7), ha='center', fontsize = 5)
    for i in readerList2[0:9]:
        reader1 = i[0] + ", " + i[1].capitalize()
        if "Oklahoma, C" in reader1:
            plt.annotate(reader1, ((float(i[4]) + float(i[6])) / 2,float(i[2])), textcoords="offset points", xytext=(-15,7), ha='center', fontsize = 5)
        else:
            plt.annotate(reader1, ((float(i[4]) + float(i[6])) / 2,float(i[2])), textcoords="offset points", xytext=(0,-7), ha='center', fontsize = 5)
    plt.savefig("Visualization1.jpeg", dpi = 300)
    plt.show()


'''
Visual 2:
This visual creates a boxplot displaying the overall spread of winning senators
vote %. It allows us to understand which parties tend to compete and win in
smaller pools of applicants and which party finds success in larger and more
competetive pools. Additionally, it allows us to see the average and quartiles
of the vote %s neccessary to claim victory in senate elections.
'''
def senator_spread(senate_file):
    with open(senate_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    i_list = []
    for i in range(1,51):
        i_list += [i]
    input_list = []
    for i in readerList1[1:]:
        if i[2] == "Republican":
            input_list += [float(i[4]) * 100]
    input_list1 = []
    for i in readerList1:
        if i[2] == "Democratic":
            input_list1 += [float(i[4]) * 100]
    senator_data = pd.Series(data = input_list)
    senator_data1 = pd.Series(data = input_list1)
    x_data = pd.Series(data = 1)
    plt.boxplot([senator_data.values, senator_data1.values], labels = ["Republican", "Democratic"])
    plt.title("Vote % for Winning Senators")
    plt.ylabel("Vote %")
    plt.savefig("Visualization2.jpeg", dpi = 300)
    plt.show()

'''
Visual 3:
This visual creates a bar graph that displays the 10 most popular senators. It
provides interesting insight to the question of the political persona: what
combination of party affiliation, top-ticket support, and individual merit makes
the most compelling state-wide representative.
'''
def pop_senator_vis(senate_file, county_av_file):
    with open(senate_file, "r") as fin:
        reader = csv.reader(fin)
        readerList1 = [line for line in reader]
    names = []
    votes = []
    readerList1 = readerList1[1:]
    def sorter(i):
        return float(i[4])
    readerList1.sort(key=sorter, reverse=False)
    for i in readerList1[-11:]:
        if "," not in i[1]:
            names += [re.sub(r".*? ", "", i[1]).lower().capitalize()]
            votes += [float(i[4]) * 100]
        else:
            names += [re.sub(r",.*", "", i[1].lower().capitalize())]
            votes += [float(i[4]) * 100]
    senators = pd.Series(index = names, data=votes)
    senators.plot(y=senators.values, kind = "bar")
    plt.title("Most Popular Senators")
    plt.ylabel("Vote %")
    plt.savefig("Visualization3.jpeg", dpi = 300)
    plt.show()



print(house_pres_correlation("clean1.csv", "clean2.csv"))
print(senate_pres_correlation("clean3.csv", "clean2.csv"))
pprint(better_senator("clean3.csv", "clean2.csv"))
print(vote_types("clean1.csv", "clean3.csv"))
pprint(slanted_counties("clean1.csv", "clean2.csv", "clean3.csv"))
dem_rep_counties_vis("export3.csv")
senator_spread("export2.csv")
pop_senator_vis("export2.csv", "export3.csv")
