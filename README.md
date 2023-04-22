# FloraExplorer

## Inspiration
Inspired by numerous of plant identifier mobile apps such as PlantNet Plant Identification, I decided to create a web app that determines the plant species and checks if that plant is native in regions of North America.

## What it does
Drag and drop or upload a plant photo (leaf or flower) and the web app will output the basic info (name, family, genus) of the plant and display a plant profile that contains a colour coded map of its native status.
 
Green = Native

Blue = Introduced

_Introduced species are plants, animals and micro-organisms that have been accidentally or deliberately introduced into areas beyond their native range. Invasive species are introduced species whose introduction or spread negatively impacts the environment, economy, and/or society including human health._

## How we built it
Streamlit framework accepts photos then that plant photo is identified by Plantnet API. After obtaining the scientific name of the plant, it searches for its corresponding plant code/symbol in the United States Department of Agriculture (USDA) plant database to get the USDA plant profile. The plant profile is embedded as a Streamlit iframe component.

## Challenges we ran into
Sometimes, the USDA plant profile does not appear due to either the scientific name gathered from the Plantnet API does not exactly match with the given database or the database does not have this plant yet.

## Accomplishments that we're proud of
A working app that can identify plants and check its native status.

## What we learned
There are lots of introduced plants species than I thought initially. For instance, I come across the Purple Loosestrife often in the wild and I did not believe it was actually invasive in my area.
In Canada, it is estimated around [1,229 non-native vascular plants and 486 out of those are considered invasive](https://www.thecanadianencyclopedia.ca/en/article/invasive-species-in-canada-plants#:~:text=From%20the%20Arctic%20Cordillera%20with,extensive%20array%20of%20foreign%20plants.). In United States, there are around [755 invasive plant species](https://www.science.org/content/article/invasive-plants-taking-over-us#:~:text=Researchers%20led%20by%20biogeographer%20Bethany,Agriculture%20(USDA)%20PLANTS%20database.). 

## What's next for FloraExplorer
- Use a different database that has info on global native status (not just North America)
