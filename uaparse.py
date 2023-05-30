import csv
from ua_parser import user_agent_parser


def parse_csv(
    filename, 
    count=True, 
    write=True, 
    has_headers=True,
    compatibility={
            'chrome': [49],
            'safari': [10, 1],
            'edge': [17],
            'firefox': [29],
            'opera': [36]
        }
):
    '''
    Parse a CSV file of raw UAs into separate CSVs by browser and print the results
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        def listToString(s):
            str1 = ""
            for ele in s:
                str1 += ele
            return str1

        records = []
        # Read the file headers if they exist
        if has_headers:
            headers = next(rows)
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            unparsed_string = listToString(row)
            parsed_string = user_agent_parser.ParseUserAgent(unparsed_string)
            parsed_dict = dict(parsed_string)

            if not parsed_dict['family']:
                parsed_dict['family'] = "NA"
            if not parsed_dict['major']:
                parsed_dict['major'] = 0
            if not parsed_dict['minor']:
                parsed_dict['minor'] = 0
            if not parsed_dict['patch']:
                parsed_dict['patch'] = 0
            records.append(parsed_dict)

        csv_columns = ['family', 'major', 'minor', 'patch']
        chrome_records = []
        safari_records = []
        edge_records = []
        firefox_records = []
        opera_records = []
        other_records = []
        rejected_chrome_records = []
        rejected_safari_records = []
        rejected_edge_records = []
        rejected_firefox_records = []
        rejected_opera_records = []

        for record in records:
            if 'Safari' in record['family']:
                safari_records.append(record)
                version = str(record.get('major', '0')) + '.' + str(record.get('minor','0'))
                check = float(version) 
                compatible_float = float(str(compatibility['safari'][0])+'.'+str(compatibility['safari'][1]))
                if 0 < check < compatible_float:
                    rejected_safari_records.append(record)
            elif 'Chrome' in record['family']:
                chrome_records.append(record)
                if int(record['major']) < compatibility['chrome'][0]:
                    rejected_chrome_records.append(record)
            elif 'Edge' in record['family']:
                edge_records.append(record)
                if int(record['major']) < compatibility['edge'][0]:
                    rejected_edge_records.append(record)
            elif 'Firefox' in record['family']:
                firefox_records.append(record)
                if int(record['major']) < compatibility['firefox'][0]:
                    rejected_firefox_records.append(record)
            elif 'Opera' in record['family']:
                opera_records.append(record)
                if int(record['major']) < compatibility['opera'][0]:
                    rejected_opera_records.append(record)
            else:
                other_records.append(record)

        if count:        
            print("Safari: ", len(safari_records), "Unsupported: ", len(rejected_safari_records))
            print("Chrome: ", len(chrome_records), "Unsupported: ", len(rejected_chrome_records))
            print("Edge: ", len(edge_records), "Unsupported: ", len(rejected_edge_records))
            print("FF: ", len(firefox_records), "Unsupported: ", len(rejected_firefox_records))
            print("Opera: ", len(opera_records), "Unsupported: ", len(rejected_opera_records))
            print("Other: ", len(other_records), "Unsupported: ???")

        def write_to_file(arr, file):
            try:
                with open(file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for record in arr:
                        writer.writerow(record)
            except IOError as e:
                print(e)
            except AttributeError as e:
                print(e)

        if write:
            write_to_file(safari_records, 'Data/parsed_safari_uas.csv')
            write_to_file(chrome_records, 'Data/parsed_chrome_uas.csv')
            write_to_file(edge_records, 'Data/parsed_edge_uas.csv')
            write_to_file(firefox_records, 'Data/parsed_firefox_uas.csv')
            write_to_file(opera_records, 'Data/parsed_opera_uas.csv')
            write_to_file(other_records, 'Data/parsed_other_uas.csv')  
