#This program is used to generate a motion graph : when an object enters the scene
from MotionDetector import df
from bokeh.plotting import figure,show,output_file
from bokeh.model import HoverTool, ColumnDataSource

#converting datetime object to string
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds= ColumnDataSource(df)
p=figure(x_axis_type='datetime',height=100,width=500,responsive=True,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start,@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="blue",source=cds)

output_file("Graph1.html")
show(p)
