import streamlit as st


def main_selection():
    st.sidebar.title('Open Source Apps')
    selection = st.sidebar.radio("Select the app to use",
                                 ['Wellbore 3D',
                                  'Data Collector',
                                  'Torque & Drag',
                                  'Temperature Distribution',
                                  'Load Cases',
                                  'Visualize Well Logs'
                                  ])

    return selection


def add_side_bar():
    # Content in sidebar

    st.sidebar.image('https://user-images.githubusercontent.com/52009346/93951385-73c43d00-fd46-11ea-9265-a795dbe089c9.png',
                     use_column_width=True)

    st.sidebar.write('_________________')

    st.sidebar.markdown('[Know more about our open source projects]'
                        '(https://prowellplan.com/modern-drilling-organization/open-source-boosting-the-'
                        'digital-transformation)')

    st.sidebar.write('_________________')
    st.sidebar.write()
    st.sidebar.markdown('[Well planning for professionals]'
                        '(https://prowellplan.com)')

    st.sidebar.image('https://prowellplan.com/imager/files/776/imac-compare_95a4de7dde4d2447564bbc200e9a931e.webp',
                     use_column_width=True)