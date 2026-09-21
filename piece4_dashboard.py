import streamlit as st
import pandas as pd
import numpy as np
import time
import os

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Live Traffic Congestion & Alert System",
    page_icon="🚦",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("🚦 Live Traffic Congestion & Alert System")

st.write(
    "Real-time traffic monitoring, congestion detection, "
    "alert analysis and machine learning prediction."
)


# =========================================================
# LOAD CONGESTION RESULTS
# =========================================================

try:

    df = pd.read_csv(
        "congestion_results.csv"
    )

except FileNotFoundError:

    st.error(
        "❌ congestion_results.csv not found. "
        "Please run the congestion detection program first."
    )

    st.stop()


# =========================================================
# CHECK DATA
# =========================================================

if df.empty:

    st.error(
        "❌ congestion_results.csv is empty."
    )

    st.stop()


# =========================================================
# SIDEBAR DATASET INFORMATION
# =========================================================

st.sidebar.header(
    "📊 Dataset Information"
)


st.sidebar.write(
    f"Total Records: {len(df)}"
)


st.sidebar.write(
    f"Cities: {df['City'].nunique()}"
)


st.sidebar.write(
    f"Vehicle Types: {df['Vehicle Type'].nunique()}"
)


# =========================================================
# SESSION STATE
# =========================================================

if "current_index" not in st.session_state:

    st.session_state.current_index = 0


current_index = (
    st.session_state.current_index
)


# Prevent invalid index

current_index = max(
    0,
    min(
        current_index,
        len(df) - 1
    )
)


st.session_state.current_index = (
    current_index
)


# =========================================================
# CURRENT LIVE DATA
# =========================================================

current_data = df.iloc[
    :current_index + 1
].copy()


# Latest record

latest_record = df.iloc[
    current_index
]


# =========================================================
# LIVE TRAFFIC MONITORING
# =========================================================

st.subheader(
    "🔴 Live Traffic Monitoring"
)


st.info(
    f"📡 Processing Record: "
    f"{current_index + 1} "
    f"out of {len(df)}"
)


# =========================================================
# CURRENT TRAFFIC ALERT
# =========================================================

current_status = str(
    latest_record["Status"]
).upper()


current_city = (
    latest_record["City"]
)


current_density = (
    latest_record["Traffic Density"]
)


if current_status == "CONGESTED":

    st.error(
        f"🚨 ALERT: High Traffic Detected in "
        f"{current_city}!"
    )


else:

    st.success(
        f"✅ Traffic is Normal in "
        f"{current_city}."
    )


# =========================================================
# LIVE METRICS
# =========================================================

st.subheader(
    "📊 Current Traffic Metrics"
)


speed = float(
    latest_record["Speed"]
)


severity = str(
    latest_record["Severity"]
)


city = (
    latest_record["City"]
)


vehicle_type = (
    latest_record["Vehicle Type"]
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🏙️ City",
        city
    )


with col2:

    st.metric(
        "🚗 Vehicle Type",
        vehicle_type
    )


with col3:

    st.metric(
        "⚡ Speed",
        f"{speed:.2f}"
    )


with col4:

    st.metric(
        "🚦 Traffic Density",
        current_density
    )


# =========================================================
# CURRENT TRAFFIC STATUS
# =========================================================

st.subheader(
    "📋 Current Traffic Status"
)


current_display = pd.DataFrame(
    [latest_record]
)


st.dataframe(
    current_display,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# CONGESTION STATUS
# =========================================================

st.subheader(
    "🚨 Current Congestion Status"
)


if current_status == "CONGESTED":

    if severity.upper() == "SEVERE":

        st.error(
            "🔴 SEVERE TRAFFIC CONGESTION DETECTED!"
        )

    else:

        st.warning(
            "🟠 HIGH TRAFFIC CONGESTION DETECTED!"
        )


else:

    st.success(
        "🟢 NORMAL TRAFFIC CONDITION"
    )


# =========================================================
# TRAFFIC DENSITY DISTRIBUTION
# =========================================================

st.subheader(
    "📊 Traffic Density Distribution"
)


density_counts = (
    current_data[
        "Traffic Density"
    ]
    .value_counts()
)


st.bar_chart(
    density_counts
)


# =========================================================
# TRAFFIC STATUS DISTRIBUTION
# =========================================================

st.subheader(
    "🚦 Traffic Status Distribution"
)


status_counts = (
    current_data[
        "Status"
    ]
    .value_counts()
)


st.bar_chart(
    status_counts
)


# =========================================================
# SPEED ANALYSIS
# =========================================================

st.subheader(
    "⚡ Traffic Speed Analysis"
)


if len(current_data) > 1:

    speed_data = (
        current_data[
            "Speed"
        ]
        .reset_index(
            drop=True
        )
    )


    st.line_chart(
        speed_data
    )


else:

    st.info(
        "Speed trend will appear as more "
        "traffic records are processed."
    )


# =========================================================
# CITY-WISE TRAFFIC ANALYSIS
# =========================================================

st.subheader(
    "🏙️ City-Wise Traffic Analysis"
)


city_counts = (
    current_data[
        "City"
    ]
    .value_counts()
)


st.bar_chart(
    city_counts
)


# =========================================================
# VEHICLE TYPE DISTRIBUTION
# =========================================================

st.subheader(
    "🚗 Vehicle Type Distribution"
)


vehicle_counts = (
    current_data[
        "Vehicle Type"
    ]
    .value_counts()
)


st.bar_chart(
    vehicle_counts
)


# =========================================================
# TRAFFIC ANALYTICS
# =========================================================

st.subheader(
    "📈 Traffic Analytics"
)


total_records = len(
    current_data
)


total_congested = len(

    current_data[

        current_data[
            "Status"
        ]
        .astype(str)
        .str.upper()
        == "CONGESTED"

    ]

)


total_normal = len(

    current_data[

        current_data[
            "Status"
        ]
        .astype(str)
        .str.upper()
        == "NORMAL"

    ]

)


if total_records > 0:

    congestion_rate = (

        total_congested
        / total_records

    ) * 100


else:

    congestion_rate = 0


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.metric(
        "📋 Records Processed",
        total_records
    )


with a2:

    st.metric(
        "🚨 Congested Records",
        total_congested
    )


with a3:

    st.metric(
        "✅ Normal Records",
        total_normal
    )


with a4:

    st.metric(
        "📈 Congestion Rate",
        f"{congestion_rate:.2f}%"
    )


# =========================================================
# SEVERITY ANALYSIS
# =========================================================

st.subheader(
    "🚨 Traffic Severity Analysis"
)


severity_counts = (

    current_data[
        "Severity"
    ]
    .value_counts()

)


st.bar_chart(
    severity_counts
)


# =========================================================
# CITY-WISE CONGESTION
# =========================================================

st.subheader(
    "🏆 City-Wise Congestion"
)


congested_data = current_data[

    current_data[
        "Status"
    ]
    .astype(str)
    .str.upper()
    == "CONGESTED"

]


if len(congested_data) > 0:


    city_congestion = (

        congested_data

        .groupby(
            "City"
        )

        .size()

        .sort_values(
            ascending=False
        )

    )


    st.bar_chart(
        city_congestion
    )


    most_congested_city = (

        city_congestion.idxmax()

    )


    st.info(
        f"🏆 Most Congested City: "
        f"{most_congested_city}"
    )


else:

    st.success(
        "No congestion detected yet."
    )


# =========================================================
# MACHINE LEARNING PREDICTION RESULTS
# =========================================================

st.subheader(
    "🤖 Machine Learning Traffic Prediction"
)


if os.path.exists(
    "ml_prediction_results.csv"
):


    try:


        prediction_df = pd.read_csv(
            "ml_prediction_results.csv"
        )


        if not prediction_df.empty:


            # ---------------------------------------------
            # MODEL PERFORMANCE
            # ---------------------------------------------

            mae = mean_absolute_error(

                prediction_df[
                    "Actual_Speed"
                ],

                prediction_df[
                    "Predicted_Speed"
                ]

            )


            rmse = np.sqrt(

                mean_squared_error(

                    prediction_df[
                        "Actual_Speed"
                    ],

                    prediction_df[
                        "Predicted_Speed"
                    ]

                )

            )


            r2 = r2_score(

                prediction_df[
                    "Actual_Speed"
                ],

                prediction_df[
                    "Predicted_Speed"
                ]

            )


            st.write(
                "### 📊 Model Performance"
            )


            p1, p2, p3 = st.columns(3)


            with p1:

                st.metric(
                    "MAE",
                    f"{mae:.2f}"
                )


            with p2:

                st.metric(
                    "RMSE",
                    f"{rmse:.2f}"
                )


            with p3:

                st.metric(
                    "R² Score",
                    f"{r2:.4f}"
                )


            # ---------------------------------------------
            # ACTUAL VS PREDICTED GRAPH
            # ---------------------------------------------

            st.write(
                "### 📈 Actual vs Predicted Speed"
            )


            chart_data = (

                prediction_df[

                    [

                        "Actual_Speed",

                        "Predicted_Speed"

                    ]

                ]

                .head(100)

            )


            st.line_chart(
                chart_data
            )


            # ---------------------------------------------
            # PREDICTION RESULTS TABLE
            # ---------------------------------------------

            st.write(
                "### 📋 Prediction Results"
            )


            st.dataframe(

                prediction_df.head(
                    20
                ),

                use_container_width=True,

                hide_index=True

            )


        else:


            st.warning(
                "⚠️ Prediction results file is empty."
            )


    except Exception as e:


        st.warning(
            f"⚠️ Could not load prediction results: {e}"
        )


else:


    st.info(

        "🤖 ML prediction results are not available yet. "
        "Please run Piece 6 Machine Learning Prediction first."

    )


# =========================================================
# ALERT HISTORY
# =========================================================

st.subheader(
    "🚨 Alert History"
)


if current_status == "CONGESTED":


    alert_file = (
        "alerts.csv"
    )


    new_alert = pd.DataFrame([{

        "Record Number":
        current_index + 1,

        "City":
        latest_record["City"],

        "Vehicle Type":
        latest_record[
            "Vehicle Type"
        ],

        "Speed":
        latest_record[
            "Speed"
        ],

        "Traffic Density":
        latest_record[
            "Traffic Density"
        ],

        "Severity":
        latest_record[
            "Severity"
        ],

        "Alert":
        "High traffic detected"

    }])


    # =====================================================
    # SAVE ALERT
    # =====================================================

    if os.path.exists(
        alert_file
    ):


        try:


            existing_alerts = (

                pd.read_csv(
                    alert_file
                )

            )


            duplicate = (

                (

                    existing_alerts[
                        "Record Number"
                    ]

                    == current_index + 1

                )

            ).any()


        except Exception:


            duplicate = False


        if not duplicate:


            new_alert.to_csv(

                alert_file,

                mode="a",

                header=False,

                index=False

            )


    else:


        new_alert.to_csv(

            alert_file,

            index=False

        )


# =========================================================
# DISPLAY ALERT HISTORY
# =========================================================

if os.path.exists(
    "alerts.csv"
):


    try:


        alerts = pd.read_csv(
            "alerts.csv"
        )


        if len(alerts) > 0:


            st.dataframe(

                alerts.tail(
                    10
                ),

                use_container_width=True,

                hide_index=True

            )


            total_alerts = len(
                alerts
            )


            severe_alerts = len(

                alerts[

                    alerts[
                        "Severity"
                    ]
                    .astype(str)
                    .str.upper()
                    == "SEVERE"

                ]

            )


            high_alerts = len(

                alerts[

                    alerts[
                        "Severity"
                    ]
                    .astype(str)
                    .str.upper()
                    == "HIGH"

                ]

            )


            x1, x2, x3 = st.columns(3)


            with x1:


                st.metric(

                    "🚨 Total Alerts",

                    total_alerts

                )


            with x2:


                st.metric(

                    "🔴 Severe Alerts",

                    severe_alerts

                )


            with x3:


                st.metric(

                    "🟠 High Alerts",

                    high_alerts

                )


        else:


            st.info(
                "No alerts recorded yet."
            )


    except Exception as e:


        st.warning(
            f"Could not read alerts.csv: {e}"
        )


else:


    st.info(
        "No congestion alerts recorded yet."
    )


# =========================================================
# LIVE STREAM PROGRESS
# =========================================================

progress = (

    (current_index + 1)

    / len(df)

)


percentage = (

    progress * 100

)


st.progress(

    progress,

    text=(

        f"Live stream progress: "

        f"{percentage:.2f}%"

    )

)


# =========================================================
# LIVE UPDATE
# =========================================================

if current_index < len(df) - 1:


    time.sleep(
        0.2
    )


    st.session_state.current_index += 1


    st.rerun()


else:


    st.success(
        "✅ Live traffic simulation completed."
    )


    if st.button(
        "🔄 Restart Live Simulation"
    ):


        st.session_state.current_index = 0


        # Remove old alerts

        if os.path.exists(
            "alerts.csv"
        ):


            os.remove(
                "alerts.csv"
            )


        st.rerun()