import pandas as pd

def main():
    #routes = csv_reader()
    ...

def csv_reader():
    #routes = []
    for y in range(4):
        x = f"./info/route{y+1}.csv"
        with open(x,"r") as f:
            q = pd.read_csv(f)
    #return routes

'''
need something to take in csv
then multiple all distances but 7
get the total distances

'''

def export_info(route,values):
    ...
    with open(route,"w") as f:
        for value in values:
            ...


if __name__ == "__main__":
    #main()
    csv_reader()