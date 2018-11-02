from flask import Flask, url_for, render_template, request, Markup
import os
import json
app = Flask(__name__)

@app.route("/") #annotation tells the URL that will amek this function run
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
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
  
  def fun_fact(state):
    
    for county in 
    
if __name__=="__main__":
    app.run(debug=True, port=66666)
