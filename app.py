import streamlit as st
from scraper import get_coordinate, find_no_website, save_to_csv
import pandas as pd

st.set_page_config(
    page_title="Maps Lead Finder",
    page_icon="📍",
    layout="wide"
)

st.title("🎯 PROSPERA")
st.write("Find businesses without websites — sorted by urgency")

col1, col2 = st.columns(2)

with col1:
    location = st.text_input("📍 Location", placeholder="e.g. Kochi, Kerala")
    st.caption("Tip: Be specific — use a neighbourhood or landmark for better results e.g. 'Ramankulangara, Kollam' instead of just 'Kollam'")

with col2:
    place_type = st.selectbox("🏢 Business Type", [
        "restaurant", "doctor", "dentist", "gym",
        "lawyer", "hotel", "beauty_salon", "school"
    ])

search = st.button("🔍 Search", use_container_width=True)

if search:
    if not location:
        st.error("Please enter a location!")
    else:
        with st.spinner("Searching for businesses and analyzing reviews..."):
            coords = get_coordinate(location)

            if coords:
                results = find_no_website(
                    location=coords,
                    radius=5000,
                    place_type=place_type
                )
                results = sorted(results, key=lambda x: x["score"], reverse=True)

                st.success(f"🎯 Found {len(results)} businesses without a website!")

                col1, col2, col3 = st.columns(3)
                urgent = len([r for r in results if r["label"] == "🔴 URGENT"])
                medium = len([r for r in results if r["label"] == "🟡 MEDIUM"])
                low    = len([r for r in results if r["label"] == "🟢 LOW"])

                col1.metric("🔴 Urgent", urgent)
                col2.metric("🟡 Medium", medium)
                col3.metric("🟢 Low", low)

                st.divider()

                df = pd.DataFrame(results)
                st.dataframe(
                    df[["label", "score", "name", "phone", "rating", "reviews", "pain_points", "address", "reasons", "maps_link"]],
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "pain_points": st.column_config.TextColumn(width="medium"),
                        "reasons": st.column_config.TextColumn(width="large"),
                        "address": st.column_config.TextColumn(width="medium"),
                        "maps_link": st.column_config.LinkColumn("Maps", display_text="Open Maps"),
                    }
                )

                st.divider()

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv,
                    file_name="leads.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            else:
                st.error("Could not find that location. Try being more specific e.g. 'Kochi, Kerala'")