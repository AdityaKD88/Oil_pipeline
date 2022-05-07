from flask import Flask, render_template, request
import plotly
import pandas as pd
import plotly.express as px
import json

df = pd.read_csv('database.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cause')
def cause():
  causes = df['Cause Category'].value_counts()
  fig1 = px.bar(df, x=causes.index.values, y=causes.values, color=causes.index.values,
              title='Causes Category',
              labels={
                        'x':'Cuases',
                        'y':'No. of cases'
                        })
  graph1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
  
  fig2 = px.pie(df,names=causes.index,values=causes.values, 
                title='Percentage of different causes of oil spills')
  graph2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)


  causes_sub = df['Cause Subcategory'].value_counts()
  fig3 = px.bar(df, x=causes_sub.index.values, y=causes_sub.values, color=causes_sub.index.values,
            height=800, width=1200, title='Causes Subcategory',
            labels={
                    'x':'Sub-cuases',
                    'y':'No. of cases'
                     })
  graph3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('cause.html',graph1=graph1,graph2=graph2,graph3=graph3)

@app.route('/lost')
def lost():
  fig4 = px.scatter(df,x=df['Net Loss (Barrels)'].values,y=df['All Costs'].values,
                    log_x=True,log_y=True, title='Total loss', color='Accident Year',
                    labels={
                        'x':'Net Loss',
                        'y':'Total Cost'
                    })
  graph4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

  fig5 = px.scatter(df,x=df['Net Loss (Barrels)'].values,y=df['Environmental Remediation Costs'].values,
                    log_x=True,log_y=True, title='Environmental loss', color='Accident Year',
                    labels={
                        'x':'Net Loss',
                        'y':'Environmental Costs'
                    })
  graph5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

  fig6 = px.scatter(df,x=df['Net Loss (Barrels)'].values,y=df['Emergency Response Costs'].values,
                    log_x=True,log_y=True, title='Emergency loss', color='Accident Year',
                    labels={
                        'x':'Net Loss',
                        'y':'Emergency Costs'
                    })
  graph6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

  fig7 = px.scatter(df,x=df['Net Loss (Barrels)'].values,y=df['Property Damage Costs'].values,
                    log_x=True,log_y=True, title='Property Damage loss', color='Accident Year',
                    labels={
                        'x':'Net Loss',
                        'y':'Property Damage Costs'
                    })
  graph7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)

  fig8 = px.scatter(df,x=df['Net Loss (Barrels)'].values,y=df['Lost Commodity Costs'].values,
                    log_x=True,log_y=True, title='Commodity loss', color='Accident Year',
                    labels={
                        'x':'Net Loss',
                        'y':'Commodity Costs'
                    })
  graph8 = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)

  fig9 = px.scatter(df,x=df['Net Loss (Barrels)'].values,y=df['Other Costs'].values,
                    log_x=True,log_y=True, title='Other loss', color='Accident Year',
                    labels={
                        'x':'Net Loss',
                        'y':'Other Costs'
                    })
  graph9 = json.dumps(fig9, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('loss.html',graph4=graph4,graph5=graph5,graph6=graph6,graph7=graph7,graph8=graph8,graph9=graph9)

@app.route('/pipeline')
def pipeline():
  ptype = df['Pipeline Type'].value_counts()
  fig10 = px.bar(df, x=ptype.index.values, y=ptype.values, color=ptype.index.values,
              title='Pipeline Type',
              labels={
                    'x':'Pipeline Type',
                    'y':'No. of Accidents'
                    })
  graph10 = json.dumps(fig10, cls=plotly.utils.PlotlyJSONEncoder)
  
  pname=['ABOVEGROUND', 'UNDERGROUND', 'TANK','TRANSITION AREA']
  fig11 = px.pie(df,values=ptype,names=pname,title='Percentage of different Pipeline Type')
  graph11 = json.dumps(fig11, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('pipeline.html',graph10=graph10,graph11=graph11)

@app.route('/liquid')
def liquid():
  ldata = df['Liquid Type']
  ldata.replace({
      'HVL OR OTHER FLAMMABLE OR TOXIC FLUID, GAS':'HVL,Gas',
      'REFINED AND/OR PETROLEUM PRODUCT (NON-HVL), LIQUID':'Non-HVL,Liquid',
      'BIOFUEL / ALTERNATIVE FUEL(INCLUDING ETHANOL BLENDS)':'Biofuel'
  },inplace=True)
  ltype = ldata.value_counts()
  fig12 = px.bar(df, x=ltype.index.values, y=ltype.values, color=ltype.index.values,
                title='Liquid Type',
                labels={
                    'x':'Liquid Type',
                    'y':'No. of Accidents'
                    })
  graph12 = json.dumps(fig12, cls=plotly.utils.PlotlyJSONEncoder)

  fig13 = px.pie(df,values=ltype.values,names=ltype.index,title='Percentage of accidents of different liquid Type')
  graph13 = json.dumps(fig13, cls=plotly.utils.PlotlyJSONEncoder)

  lsdata = df['Liquid Subtype']
  lsdata.replace({
      'HVL OR OTHER FLAMMABLE OR TOXIC FLUID, GAS':'HVL,Gas',
      'REFINED AND/OR PETROLEUM PRODUCT (NON-HVL), LIQUID':'Non-HVL,Liquid',
      'BIOFUEL / ALTERNATIVE FUEL(INCLUDING ETHANOL BLENDS)':'Biofuel'
  },inplace=True)
  lstype = lsdata.value_counts()
  fig14 = px.bar(df, x=lstype.index.values, y=lstype.values, color=lstype.index.values,
                title='Sub-liquid Type',
                labels={
                    'x':'Sub-liquid Type',
                    'y':'No. of Accidents'
                    })
  graph14 = json.dumps(fig14, cls=plotly.utils.PlotlyJSONEncoder)

  fig15 = px.pie(df,values=lstype.values,names=lstype.index,title='Percentage of accidents of different sub-liquid Type')
  graph15 = json.dumps(fig15, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('liquid.html',graph12=graph12,graph13=graph13,graph14=graph14,graph15=graph15)

if __name__ == '__main__':
    app.run(debug=True)