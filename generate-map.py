import argparse, geopandas
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(prog = 'generate-map',
 formatter_class=argparse.RawTextHelpFormatter,
 description = 'Generate an outline map of the world with customizable map size, and colors of ocean, land and borders.',
 epilog='''
 Examples:
 Print high res world outline: %(prog)s -s 128
 Print colored world outline: %(prog)s -s 32 --background blue --land yellow --outline green 
 Print hex colored world outline: %(prog)s -s 32 --background '#0000ff' --land yellow --outline '#00ff00' 
 Supply input data and specify output file: %(prog)s -d ./GSHHS_f_L1.shp -of ./output.png
 ''')
parser.add_argument('-o', '--outline', type=str, default='black')
parser.add_argument('-b', '--background', type=str, default='white')
parser.add_argument('-l', '--land', type=str, default='white')
parser.add_argument('-s', '--size', type=int, default=0)
parser.add_argument('-sx', '--sizex', type=int, default=128)
parser.add_argument('-sy', '--sizey', type=int, default=128)
parser.add_argument('-d', '--data', type=str, default="GSHHS_f_L1.shp")
parser.add_argument('-of', '--output', type=str, default="world.png")
args = parser.parse_args()

outlineColor = args.outline
backgroundColor = args.background
landColor = args.land
if args.size > 0:
    sizeX = args.size
    sizeY = args.size
else:
    sizeX = args.sizex
    sizeY = args.sizey
inputFileLocation=args.data
outputFileLocation=args.output

plt.rcParams['axes.facecolor'] = backgroundColor
fig, ax = plt.subplots(figsize=(sizeX, sizeY))
gdf = geopandas.read_file(inputFileLocation)
gdf.plot(ax=ax, alpha=1, color=landColor, edgecolor=outlineColor)
fig.savefig(outputFileLocation, format="png")
