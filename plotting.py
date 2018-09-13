from script1 import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_String"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime", plot_height=250, plot_width=1300, sizing_mode="scale_width",
         title="Motion Graph",logo=None, toolbar_location="above")
p.yaxis.minor_tick_line_color=None      #for minor ticks (15cm wali me mm)
p.ygrid[0].ticker.desired_num_ticks=1   #for major ticks (15cm wali me cm)

hover=HoverTool(tooltips=[("Start: ","@Start_String"),("End :","@End_String")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color='green', source=cds)

output_file("Graph.html")
show(p)