# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers if they exist
        if not has_headers and select:
            raise RuntimeError('select argument requires column headers')
        elif has_headers:
            headers = next(rows)
        else:
            records = []
            for row in rows:
                if not row:    # Skip rows with no data
                    continue
                
                if types:
                    row = [func(val) for func, val in zip(types, row) ]
                record = (row[0], row[1])
                records.append(record)
                
            return records
        
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if not has_headers and select:
            raise RuntimeError('select argument requires column headers')
        elif select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
            
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                if silence_errors:
                    try: 
                        row = [ row[index] for index in indices ]
                    except Exception:
                        continue
                try: 
                    row = [ row[index] for index in indices ]
                except Exception as e:
                    print("Couldn't convert ", row)
                    print("Reason ", e)
                    continue
            if types:
                if silence_errors:
                    try: 
                        row = [func(val) for func, val in zip(types, row) ]
                    except Exception:
                        continue
                try: 
                    row = [func(val) for func, val in zip(types, row) ]
                except Exception as e:
                    print("Couldn't convert ", row)
                    print("Reason ", e)
                    continue
                
                    
                
            # Make a dict    
            record = dict(zip(headers, row))
            records.append(record)

    return records