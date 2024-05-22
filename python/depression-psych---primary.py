# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"Eu33313","system":"readv2"},{"code":"Eu32314","system":"readv2"},{"code":"Eu32311","system":"readv2"},{"code":"Eu33211","system":"readv2"},{"code":"Eu33311","system":"readv2"},{"code":"Eu32800","system":"readv2"},{"code":"Eu32313","system":"readv2"},{"code":"Eu32700","system":"readv2"},{"code":"E112400","system":"readv2"},{"code":"E112300","system":"readv2"},{"code":"Eu32300","system":"readv2"},{"code":"Eu32200","system":"readv2"},{"code":"E11..12","system":"readv2"},{"code":"Eu33312","system":"readv2"},{"code":"Eu32212","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depression-psych---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depression-psych---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depression-psych---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
