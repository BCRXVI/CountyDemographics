from flask import Flask, url_for, render_template, request
import os
import json
app = Flask(__name__)

@app.route("/") #annotation tells the URL that will amek this function run
def render_main():
    return render_template('home.html')
  
def get_state_options(counties):
  bom=[]
  
  for county in counties:
    state = county["State"]
    trfl = state in bom
    if (trfl == False):
      bom.append(state)
      
      
  options = ""
  for state in bom:
    options += Markup("<option value=\"" + state + "\">" + c + "</option>")
  
  print(options)

  if __name__=="__main__":
    app.run(debug=True, port=42069)
