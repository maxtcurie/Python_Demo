import optparse as op

parser = op.OptionParser(description='Extract generalized Miller shaping parameters from EQDSK files.')
parser.add_option('--rovera', '-r', action='store_const', const=1)
parser.add_option('--noplots', '-n', action='store_const', const=1)
parser.add_option('--conv', '-c', action='store_const', const=1)
parser.add_option('--method', '-m', action='store', type='int', dest="method",default=0)
options, args = parser.parse_args()
use_r_a = options.rovera
show_plots = (not options.noplots)
write_rhotor_rhopol_conversion = options.conv
tfmethod=options.method
if not write_rhotor_rhopol_conversion:
    if len(args) != 2:
        exit("""
Please give two arguments: <EQDSK filename> <Position in rho_tor>
optional: -r <Position in r/a>
          -c: Write rhotor/rhopol conversion to file
          -n: Suppress plots\n
          -m 0|1: Use 1d/2d method for creating rho_tor grid\n""")