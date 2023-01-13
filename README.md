# map-outline
This utility generates a detailed outline of the world map without national borders. Data source was obtained from [NOAA.gov](https://www.ngdc.noaa.gov/mgg/shorelines/).

Print high res world outline:<br>
`python generate-map.py -s 128`

Print colored world outline:<br>
`python generate-map.py -s 32 --background blue --land yellow --outline green`

Print hex colored world outline:<br>
`python generate-map.py -s 32 --background '#0000ff' --land yellow --outline '#00ff00'`

Supply input data and specify output file:<br>
`python generate-map.py -d ./GSHHS_f_L1.shp -of ./output.png`

Default values:

| Parameter      | Value |
| ----------- | ----------- |
| outline      | black       |
| background   | white        |
| land   | white        |
| sizex   | 128        |
| sizey   | 128        |
| data   | GSHHS_f_L1.shp        |
| output   | world.png        |
