import csv

def writeout_args(args, out_dir):
    fout = open(Path(out_dir).joinpath('arguments.csv', "wt"))
    csvout = csv.writer(fout)
    print('*' * 20)
    print('Write out Arguments...')
    print('*' * 20)
    for arg in dir(args):
        if not arg.startswith('_'):
            csvout.writerow([arg, str(getattr(args, arg))])
            print('%-25s %-25s' % (arg , str(getattr(args, arg))))
