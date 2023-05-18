import csv
from ua_parser import user_agent_parser


def parse_csv(filename, count=True, write=True):
    '''
    Parse a CSV file of raw UAs into separate CSVs by browser
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        def listToString(s):
            str1 = ""
            for ele in s:
                str1 += ele
            return str1

        records = []

        for row in rows:
            if not row:    # Skip rows with no data
                continue

            unparsed_string = listToString(row)
            parsed_string = user_agent_parser.ParseUserAgent(unparsed_string)
            parsed_dict = dict(parsed_string)

            if not parsed_dict['family']:
                parsed_dict['family'] = "NA"
            if not parsed_dict['major']:
                parsed_dict['major'] = "NA"
            if not parsed_dict['minor']:
                parsed_dict['minor'] = "NA"
            if not parsed_dict['patch']:
                parsed_dict['patch'] = "NA"
            records.append(parsed_dict)

        csv_columns = ['family', 'major', 'minor', 'patch']
        chrome_records = []
        safari_records = []
        edge_records = []
        firefox_records = []
        opera_records = []
        other_records = []
        
        for record in records:
            if 'Safari' in record['family']:
                safari_records.append(record)
            elif 'Chrome' in record['family']:
                chrome_records.append(record)
            elif 'Edge' in record['family']:
                edge_records.append(record)
            elif 'Firefox' in record['family']:
                firefox_records.append(record)
            elif 'Opera' in record['family']:
                opera_records.append(record)
            else:
                other_records.append(record)

        if count:        
            print("Safari: ", len(safari_records))
            print("Chrome: ", len(chrome_records))
            print("Edge: ", len(edge_records))
            print("FF: ", len(firefox_records))
            print("Opera: ", len(opera_records))
            print("Other: ", len(other_records))

        if write:
            try:
                with open('Data/parsed_chrome_uas.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in chrome_records:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)

            try:
                with open('Data/parsed_safari_uas.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in safari_records:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)
                
            try:
                with open('Data/parsed_edge_uas.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in edge_records:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)
            
            try:
                with open('Data/parsed_opera_uas.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in opera_records:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)
            
            try:
                with open('Data/parsed_firefox_uas.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in firefox_records:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)
            
            try:
                with open('Data/parsed_other_uas.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in other_records:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)
