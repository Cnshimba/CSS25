import streamlit as st
import pandas as pd

def display_profile(name, field, institution):
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

def handle_publications(uploaded_file):
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
        return publications
    else:
        st.write("No file uploaded.")
        return None

def filter_publications(publications, keyword):
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

def visualize_trends(publications):
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

def main():
    # Title of the app
    st.title("Researcher Profile Page")

    # Collect basic information
    name = "Mr. Carlos Nshimba"
    field = "Cyber Security & IoT"
    institution = "Vaal University of Technology"

    # Display basic profile information
    display_profile(name, field, institution)

    # Add a section for publications
    st.header("Publications")
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    publications = handle_publications(uploaded_file)

    if publications is not None:
        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        filter_publications(publications, keyword)

        # Add a section for visualizing publication trends
        st.header("Publication Trends")
        visualize_trends(publications)

    # Add a contact section
    st.header("Contact Information")
    email = "nshimba@gmail.com"
    st.write(f"You can reach {name} at {email}.")

    # Sidebar
    st.sidebar.image("image.png")
    st.sidebar.header('PROFILE')
    st.sidebar.markdown("**ORCID:** [0000-0000-0000-0000](https://orcid.org/0000-0000-0000-0000)")
    st.sidebar.markdown("**Email:** nshimba@gmail.com")
    st.sidebar.slider('**Rate my page**', 0, 100)
    st.sidebar.button('Submit')

if __name__ == "__main__":
    main()
