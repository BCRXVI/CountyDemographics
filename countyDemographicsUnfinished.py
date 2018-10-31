import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for county in counties:
        if county["County"] < first:
            first = county["County"]
    return first
        
def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    state = counties[0]["State"]
    cName = counties[0]["County"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] > highest:
            highest=county["Age"]["Percent Under 18 Years"]
            state=county["State"]
            cName= county["County"]
    return cName + ' ' + state
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    cName = counties[0]["County"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] > highest:
            cName = county["County"]
            percent = county["Age"]["Percent Under 18 Years"]
    return str(highest)
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    state = counties[0]["State"]
    cName = counties[0]["County"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] > highest:
            cName = county["County"]
            percent = county["Age"]["Percent Under 18 Years"]
            state=county["State"]
    return cName + ' ' + state + ' ' + str(highest)
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    #Find the state in the dictionary with the most counties
    #Return the state with the most counties
    
    boi = {}
        
    for x in counties:
        state = x["State"]
        trfl = state in boi
        if (trfl == False):
            boi[state] = 0
            
        else:
            boi[state] = boi[state] + 1
    state = "CA"
    highest = boi["CA"]
    for x in boi: 
        if (boi[x] > highest):
            highest = boi[x]
            state = x
    return state + str(highest)
    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    
        highest = counties[0]["Age"]["Percent Under 18 Years"]
    cName = counties[0]["County"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] > highest:
            cName = county["County"]
            percent = county["Age"]["Percent Under 18 Years"]
    return str(highest)
    
if __name__ == '__main__':
    main()
