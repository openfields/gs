# example from website:
# https://jcastellssala.com/2012/05/07/basic-network-analysis-with-grass/

# import data
v.in.ogr -o dsn=NWB_Enschede.shp output=roads
v.in.ogr -o dsn=Schools_corrected.shp output=schools

# add length field
v.db.addcol map=roads columns=LENGTH double

# update length field
v.to.db map=roads option=length units=meters columns=LENGTH

# create network
v.net input=roads points=schools, output=network operation=connect thresh=500

# report for network
v.category network op=report

# connect table for schools to network
v.db.connect map=network table=schools layer=2

# network allocation
v.net.alloc --overwrite --verbose input=network output=network_alloc ccats=1-63

# show with colors
d.vect -c map=network_alloc

# split net by cost
v.net.iso --overwrite input=network output=network_isolines ccats=1-64 costs=1000,2000,3000 afcolumn=LENGTH abcolumn=LENGTH

# for particular school: iso, color, display
v.net.iso --overwrite input=network output=network_iso_5 ccats=5 costs=1000,2000,3000 afcolumn=LENGTH abcolumn=LENGTH

d.vect -c map=network_iso_5

d.vect map=schools type=point where=cat=5 fcolor=9:157:9 icon=basic/circle size=10
