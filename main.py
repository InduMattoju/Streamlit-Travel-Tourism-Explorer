import streamlit as st

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Travel & Tourism Explorer",
    layout="wide"
)

# SESSION STATE

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "trip_created" not in st.session_state:
    st.session_state.trip_created = False

# DESTINATION DATA

destinations = {

    "Goa": {
        "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2",
        "description": "Goa is famous for beautiful beaches, nightlife, water sports and Portuguese architecture.",
        "rating": 4.7,
        "best_time": "November - February",
        "budget": 15000
    },

    "Kerala": {
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944",
        "description": "Kerala is famous for backwaters, greenery, beaches, hill stations and traditional culture.",
        "rating": 4.8,
        "best_time": "October - March",
        "budget": 18000
    },

    "Manali": {
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23",
        "description": "Manali is a beautiful mountain destination famous for snow, trekking and adventure activities.",
        "rating": 4.6,
        "best_time": "October - June",
        "budget": 20000
    },

    "Hyderabad": {
        "image": "https://images.unsplash.com/photo-1572445271230-a78b5944a659",
        "description": "Hyderabad is known for Charminar, historical monuments, biryani and rich cultural heritage.",
        "rating": 4.5,
        "best_time": "October - February",
        "budget": 10000
    },

    "Jaipur": {
        "image": "https://images.unsplash.com/photo-1477587458883-47145ed94245",
        "description": "Jaipur is famous for forts, palaces, colorful markets and royal Rajasthani culture.",
        "rating": 4.6,
        "best_time": "October - March",
        "budget": 12000
    }
}

# SIDEBAR

st.sidebar.title("Travel Explorer")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Destinations",
        "Travel Videos",
        "Trip Planner",
        "Budget Calculator",
        "Booking",
        "Favorites"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("Travel Preferences")

budget_limit = st.sidebar.slider(
    "Your Budget",
    5000,
    100000,
    25000,
    step=5000
)

include_hotel = st.sidebar.checkbox(
    "Include Hotel",
    value=True
)

include_food = st.sidebar.checkbox(
    "Include Food",
    value=True
)

include_transport = st.sidebar.checkbox(
    "Include Transportation",
    value=True
)

# HOME

if page == "Home":

    st.title("Travel & Tourism Explorer")

    st.subheader(
        "Explore beautiful destinations and plan your perfect trip."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Destinations",
            "5"
        )

    with col2:
        st.metric(
            "Travel Categories",
            "6"
        )

    with col3:
        st.metric(
            "Average Rating",
            "4.6"
        )

    st.divider()

    st.header("Welcome to Travel Explorer")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            "https://images.unsplash.com/photo-1524492412937-b28074a5d7da",
            caption="Explore Incredible India",
            use_container_width=True
        )

    with col2:

        st.markdown(
            """
            ### Discover. Plan. Travel.

            This application helps you:

            - Explore tourist destinations
            - Watch travel videos
            - Create a trip plan
            - Calculate your travel budget
            - Submit a booking request
            - Save your favorite destinations

            Use the sidebar to explore all features.
            """
        )

    st.divider()

    st.header("Popular Destinations")

    col1, col2, col3 = st.columns(3)

    popular = ["Goa", "Kerala", "Manali"]

    for i, place in enumerate(popular):

        with [col1, col2, col3][i]:

            st.image(
                destinations[place]["image"],
                caption=place,
                use_container_width=True
            )

            st.write(
                f"Rating: {destinations[place]['rating']}/5"
            )

# DESTINATIONS
# ============================================================

elif page == "Destinations":

    st.title("Explore Destinations")

    selected = st.selectbox(
        "Select a Destination",
        list(destinations.keys())
    )

    data = destinations[selected]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            data["image"],
            caption=selected,
            use_container_width=True
        )

    with col2:

        st.header(selected)

        st.write(data["description"])

        st.write(
            f"Rating: {data['rating']}/5"
        )

        st.write(
            f"Best Time: {data['best_time']}"
        )

        st.write(
            f"Estimated Budget: Rs.{data['budget']:,}"
        )

        if selected not in st.session_state.favorites:

            if st.button("Add to Favorites"):

                st.session_state.favorites.append(
                    selected
                )

                st.success(
                    f"{selected} added to favorites!"
                )

        else:

            st.info(
                "Already added to favorites"
            )

    st.divider()

    st.subheader("Destination Information")

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:

        st.info(
            f"Destination\n\n{selected}"
        )

    with info_col2:

        st.info(
            f"Rating\n\n{data['rating']}/5"
        )

    with info_col3:

        st.info(
            f"Budget\n\nRs.{data['budget']:,}"
        )

# TRAVEL VIDEOS
# ============================================================
elif page == "Travel Videos":

    st.title("Travel Videos")

    st.write(
        "Watch travel videos and explore beautiful destinations."
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Goa",
            "Kerala",
            "Manali",
            "Hyderabad",
            "Jaipur"
        ]
    )


    # GOA
    with tab1:

        st.header("Goa Travel")

        st.video(
            "https://www.youtube.com/watch?v=t6GFHrhaGqs"
        )

        st.write(
            "Explore beaches, nightlife and adventure activities in Goa."
        )


    # KERALA
    with tab2:

        st.header("Kerala Travel")

        st.video(
            "https://www.youtube.com/watch?v=QOxyJo_nnbw"
        )

        st.write(
            "Explore Kerala's backwaters, nature and beautiful landscapes."
        )


    # MANALI
    with tab3:

        st.header("Manali Travel")

        st.video(
            "https://www.youtube.com/watch?v=ZzQC2TJ-frU"
        )

        st.write(
            "Explore mountains, snow and adventure activities in Manali."
        )


    # HYDERABAD
    with tab4:

        st.header("Hyderabad Travel")

        st.video(
            "https://www.youtube.com/watch?v=TO__okRgffM"
        )

        st.write(
            "Explore Charminar, historical places, food and culture of Hyderabad."
        )


    # JAIPUR
    with tab5:

        st.header("Jaipur Travel")

        st.video(
            "https://www.youtube.com/watch?v=tuHdk82Y_ss"
        )

        st.write(
            "Explore forts, palaces, markets and the royal culture of Jaipur."
        )

# TRIP PLANNER
# ============================================================
elif page == "Trip Planner":

    st.title("Trip Planner")

    st.write(
        "Create your personalized travel plan."
    )

    with st.form("trip_planner"):

        destination = st.selectbox(
            "Destination",
            list(destinations.keys())
        )

        travel_date = st.date_input(
            "Travel Date"
        )

        number_of_days = st.number_input(
            "Number of Days",
            min_value=1,
            max_value=30,
            value=3
        )

        number_of_people = st.number_input(
            "Number of People",
            min_value=1,
            max_value=20,
            value=2
        )

        activities = st.multiselect(
            "Select Activities",
            [
                "Sightseeing",
                "Shopping",
                "Adventure",
                "Beach",
                "Food",
                "Photography",
                "Historical Places"
            ]
        )

        submit_trip = st.form_submit_button(
            "Create Trip Plan"
        )

    if submit_trip:

        st.session_state.trip_created = True

        st.success(
            "Trip plan created successfully!"
        )

        st.divider()

        st.subheader("Your Trip Plan")

        st.write(
            f"Destination: {destination}"
        )

        st.write(
            f"Travel Date: {travel_date}"
        )

        st.write(
            f"Duration: {number_of_days} days"
        )

        st.write(
            f"Travelers: {number_of_people}"
        )

        st.subheader("Activities")

        if activities:

            for activity in activities:

                st.write(
                    f"{activity}"
                )

        else:

            st.warning(
                "No activities selected."
            )

# BUDGET CALCULATOR
# ============================================================
elif page == "Budget Calculator":

    st.title("Travel Budget Calculator")

    st.write(
        "Calculate the estimated cost of your trip."
    )

    col1, col2 = st.columns(2)

    with col1:

        hotel_per_day = st.number_input(
            "Hotel Cost per Day",
            min_value=0,
            value=2000
        )

        food_per_day = st.number_input(
            "Food Cost per Day",
            min_value=0,
            value=1000
        )

        transport_cost = st.number_input(
            "Transportation Cost",
            min_value=0,
            value=3000
        )

    with col2:

        days = st.slider(
            "Number of Days",
            1,
            30,
            5
        )

        people = st.slider(
            "Number of People",
            1,
            10,
            2
        )

    calculate = st.button(
        "Calculate Budget"
    )

    if calculate:

        hotel_total = (
            hotel_per_day *
            days *
            people
        )

        food_total = (
            food_per_day *
            days *
            people
        )

        total = (
            hotel_total +
            food_total +
            transport_cost
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Hotel",
                f"Rs.{hotel_total:,}"
            )

        with col2:

            st.metric(
                "Food",
                f"Rs.{food_total:,}"
            )

        with col3:

            st.metric(
                "Total",
                f"Rs.{total:,}"
            )

        st.divider()

        if total <= budget_limit:

            st.success(
                "Your trip is within your budget!"
            )

        else:

            st.warning(
                "Your trip exceeds your selected budget."
            )

# BOOKING
# ============================================================
elif page == "Booking":

    st.title("Travel Booking")

    st.write(
        "Submit your travel booking request."
    )

    with st.form("booking_form"):

        name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email"
        )

        phone = st.text_input(
            "Phone Number"
        )

        destination = st.selectbox(
            "Destination",
            list(destinations.keys())
        )

        travelers = st.number_input(
            "Number of Travelers",
            min_value=1,
            max_value=20,
            value=1
        )

        travel_date = st.date_input(
            "Travel Date"
        )

        travel_class = st.radio(
            "Travel Class",
            [
                "Economy",
                "Business"
            ]
        )

        special_requirements = st.text_area(
            "Special Requirements"
        )

        confirm = st.checkbox(
            "I confirm that the information is correct."
        )

        booking = st.form_submit_button(
            "Submit Booking"
        )

    if booking:

        if name == "":

            st.error(
                "Please enter your name."
            )

        elif email == "":

            st.error(
                "Please enter your email."
            )

        elif not confirm:

            st.error(
                "Please confirm the booking details."
            )

        else:

            st.success(
                "Booking request submitted successfully!"
            )

            st.write(
                f"Name: {name}"
            )

            st.write(
                f"Destination: {destination}"
            )

            st.write(
                f"Travelers: {travelers}"
            )

            st.write(
                f"Travel Date: {travel_date}"
            )

            st.write(
                f"Travel Class: {travel_class}"
            )

# FAVORITES
# ============================================================
elif page == "Favorites":

    st.title("My Favorite Destinations")

    if len(st.session_state.favorites) == 0:

        st.info(
            "You haven't added any favorite destinations yet."
        )

    else:

        st.write(
            "Your favorite destinations:"
        )

        for place in st.session_state.favorites:

            st.write(
                place
            )