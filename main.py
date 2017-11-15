from urllib import request

goog_url = 'http://www.google.com/finance/historical?q=NASDAQ:GOOG&output=csv'

def download_stock_data(csv):
    response = request.urlopen(csv)
    csv_file = response.read()
    csv_str = str(csv_file)
    lines = csv_str.split('\\n')
    dest_url = r'crap/goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_stock_data(goog_url)