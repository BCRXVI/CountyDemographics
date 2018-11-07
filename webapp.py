from flask import Flask, url_for, render_template, request, Markup
import os
import json
app = Flask(__name__)

def fun_fact(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    boi = 0
    highestcounty = ''
    for county in counties:
        if county["State"] == state:
            if (county['Income']['Median Household Income'] > boi):
                boi = county['Income']['Median Household Income']
                highestcounty = county['County']
    return state + ' ' + highestcounty + ' ' + str(boi)

@app.route("/") #annotation tells the URL that will make this function run
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    try:
        state = request.args['states']
        print(state)
        ff=fun_fact(state)
        print(ff)
        return render_template('home.html', states = get_state_options(counties), funfact = ff)
    except:
        return render_template('home.html', states = get_state_options(counties))
  
def get_state_options(counties):
  bom=[]
  

  
  for county in counties:
    state = county["State"]
    trfl = state in bom
    if (trfl == False):
      bom.append(state)
      
      
  options = ""
  for state in bom:
    options += Markup("<option value=\"" + state + "\">" + state + "</option>")

  return options
 

    
if __name__=="__main__":
    app.run(debug=True, port=66666)
