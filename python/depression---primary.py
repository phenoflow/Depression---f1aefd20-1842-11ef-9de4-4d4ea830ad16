# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"Eu32400","system":"readv2"},{"code":"Eu32z12","system":"readv2"},{"code":"Eu32z11","system":"readv2"},{"code":"Eu34111","system":"readv2"},{"code":"E2B0.00","system":"readv2"},{"code":"E2B..00","system":"readv2"},{"code":"Eu20400","system":"readv2"},{"code":"Eu92000","system":"readv2"},{"code":"62T1.00","system":"readv2"},{"code":"Eu53012","system":"readv2"},{"code":"E2B1.00","system":"readv2"},{"code":"Eu33z11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depression---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depression---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depression---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
