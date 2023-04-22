import requests
import json
import streamlit.components.v1 as components
from PIL import Image
import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="FloraExplorer", layout="wide")
st.title("FloraExplorer")
API_KEY = st.secrets['plant']
PROJECT = "all"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"


df = pd.read_csv('plant_code.csv', delimiter=",")
df['Scientific Name with Author'] = df['Scientific Name with Author'].str.replace(' ', '')
# st.dataframe(data=df)

if "run" not in st.session_state:
    st.session_state['run'] = True

organ = st.radio(
        "Select plant feature",
        ('leaf', 'flower'), index=0)
uploaded_file = st.file_uploader("Choose File", type=['jpeg', 'png', 'jpg'], accept_multiple_files=False, key=None, help=None,
                                             on_change=None, label_visibility="visible")
if uploaded_file is not None:
    if uploaded_file.name not in os.listdir("data"):
        with open("data/" + uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("File Uploaded Successfully")
    image_path_1 = "data/" + uploaded_file.name
    image_data_1 = open(image_path_1, 'rb')

    col1, col2 = st.columns(2)
    with col1:
        image = Image.open(image_path_1)
        st.image(image)

    dir = "data/"
    for file in os.scandir(dir):
        os.remove(file.path)

    data = {
        'organs': [organ]
    }

    files = [
        ('images', (image_path_1, image_data_1))
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    # pprint(response.status_code)
    # pprint(json_result)
    try:
        st.session_state['top_name'] = json_result['results'][0]['species']['commonNames'][0]
        st.session_state['sci_name'] = json_result['results'][0]['species']['scientificName']
    except:
        st.session_state['top_name'] = ""
        st.session_state['sci_name'] = ""

    with col2:
        for i in json_result['results']:
            if i['score'] >= 0.05:
                st.write(f"{i['score'] * 100:.2f}% - Common Name: {i['species']['commonNames']}")
                st.write(f"Scientific Name: {i['species']['scientificName']}")
                st.write(f"Family: {i['species']['family']['scientificName']}")
                st.write(f"Genus: {i['species']['genus']['scientificName']}")
                st.markdown("""---""")
# st.session_state['top_name']
# st.session_state['sci_name']

try:
    # st.session_state['plant_code'] = df.iloc[df.index[df['Common Name'] == st.session_state['top_name'].lower()].tolist()[0]]['Symbol']
    st.session_state['plant_code'] = df.iloc[df.index[df['Scientific Name with Author'] == st.session_state['sci_name'].replace(" ", '')].tolist()[0]]['Symbol']
    # st.write(st.session_state['plant_code'])
except:
    st.session_state['plant_code'] = None

# st.text(df[df['Common Name'] == st.session_state['top_name'].lower()].Symbol)

# st.write(api.plants_by("distributions", 286))
with st.expander("What are introduced species?"):
    st.info("Introduced species are plants, animals and micro-organisms that have been accidentally or deliberately introduced into areas beyond their native range. Invasive species are introduced species whose introduction or spread negatively impacts the environment, economy, and/or society including human health.")
if st.session_state['plant_code'] is not None:
    components.iframe(
        f"https://plants.usda.gov/home/plantProfile?symbol={st.session_state['plant_code']}",
        width=1300, height=600, scrolling=True)

#if "run" in st.session_state:
    # components.iframe("https://maps.eddmaps.org/google/eradication.cfm?notitle&&observationdatestart=1/1/2020&eradicationstatus=1,2,3&country=260&records=mappings&lat=49.7703&lng=-96.8116&zoom=5", width=1300, height=600, scrolling=False)

# components.iframe("https://maps.eddmaps.org/google/eradication.cfm?notitle&&observationdatestart=1/1/2020&country=260&records=mappings&eradicationstatus=1&lat=49.7703&lng=-96.8116&zoom=5", width=1350, height=600, scrolling=False)
# image_path_1 = 'data/dahlia-shutterstock.jpeg'
# image_data_1 = open(image_path_1, 'rb')
# image_path_2 = "../data/image_2.jpeg"
# image_data_2 = open(image_path_2, 'rb')


