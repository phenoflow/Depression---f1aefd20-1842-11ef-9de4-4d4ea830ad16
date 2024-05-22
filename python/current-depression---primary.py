# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"Eu33000","system":"readv2"},{"code":"Eu33315","system":"readv2"},{"code":"E113300","system":"readv2"},{"code":"Eu33.12","system":"readv2"},{"code":"Eu33.11","system":"readv2"},{"code":"Eu33.00","system":"readv2"},{"code":"Eu33.13","system":"readv2"},{"code":"E113.11","system":"readv2"},{"code":"E113700","system":"readv2"},{"code":"Eu33212","system":"readv2"},{"code":"E113z00","system":"readv2"},{"code":"E113400","system":"readv2"},{"code":"E113200","system":"readv2"},{"code":"E113.00","system":"readv2"},{"code":"Eu33200","system":"readv2"},{"code":"E113000","system":"readv2"},{"code":"Eu3y111","system":"readv2"},{"code":"Eu33z00","system":"readv2"},{"code":"Eu33316","system":"readv2"},{"code":"Eu33100","system":"readv2"},{"code":"E113100","system":"readv2"},{"code":"Eu33300","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["current-depression---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["current-depression---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["current-depression---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
