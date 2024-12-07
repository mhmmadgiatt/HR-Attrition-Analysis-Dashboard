import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# Load Data Function
@st.cache_data
def load_data(filepath):
    """
    Memuat data dari file CSV dengan caching untuk performa
    """
    df = pd.read_csv(filepath)
    
    # Mapping untuk berbagai kolom kategorikal
    education_mapping = {1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master', 5: 'Doctor'}
    
    # Konversi Attrition
    df['Attrition'] = df['Attrition'].replace({1: 'Yes', 0: 'No'})
    df['Education'] = df['Education'].map(education_mapping)
    
    return df

# Dashboard Main Function
def main():
    st.title("🧑‍💼 HR Attrition Analysis Dashboard")
    
    # Load Data
    data_path = 'processed_employee_data.csv'  # Pastikan file CSV tersedia
    df = load_data(data_path)
    
    # Sidebar for Filtering
    st.sidebar.header("📊 Dashboard Filter")
    
    # Department Filter
    departments = ['All'] + list(df['Department'].unique())
    selected_department = st.sidebar.selectbox(
        "Select Department", 
        departments
    )
    
    # Filter DataFrame based on Department
    if selected_department != 'All':
        df = df[df['Department'] == selected_department]
    
    # Create Metrics Row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total Employees", 
            value=len(df),
            delta=f"{len(df[df['Attrition'] == 'Yes'])} Attritions"
        )
    
    with col2:
        attrition_rate = (len(df[df['Attrition'] == 'Yes']) / len(df)) * 100
        st.metric(
            label="Attrition Rate", 
            value=f"{attrition_rate:.2f}%"
        )
    
    with col3:
        st.metric(
            label="Average Age", 
            value=f"{df['Age'].mean():.1f} Years"
        )
    
    # Visualization Grid
    st.markdown("## 📈 Attrition Analysis Visualizations")
    
    # Row 1: Attrition Comparisons
    col1, col2 = st.columns(2)
    
    with col1:
        # Attrition by Gender
        st.subheader("Attrition by Gender")
        # Prepare data manually
        gender_attrition_df = df.groupby(['Gender', 'Attrition']).size().reset_index(name='Count')
        
        fig_gender = px.bar(
            gender_attrition_df, 
            x='Gender', 
            y='Count', 
            color='Attrition',
            barmode='group',
            title='Attrition Distribution by Gender'
        )
        st.plotly_chart(fig_gender, use_container_width=True)
    
    with col2:
        # Attrition by Business Travel
        st.subheader("Attrition by Business Travel")
        travel_attrition_df = df.groupby(['BusinessTravel', 'Attrition']).size().reset_index(name='Count')
        
        fig_travel = px.bar(
            travel_attrition_df, 
            x='BusinessTravel', 
            y='Count', 
            color='Attrition',
            barmode='group',
            title='Attrition Distribution by Travel Frequency'
        )
        st.plotly_chart(fig_travel, use_container_width=True)
    
    # Row 2: More Complex Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Attrition by Job Role
        st.subheader("Attrition by Job Role")
        job_role_attrition_df = df[df['Attrition'] == 'Yes'].groupby('JobRole').size().reset_index(name='Attrition_Count')
        job_role_attrition_df = job_role_attrition_df.sort_values('Attrition_Count', ascending=False)
        
        fig_job_role = px.bar(
            job_role_attrition_df, 
            x='JobRole', 
            y='Attrition_Count',
            title='Job Roles with Highest Attrition'
        )
        st.plotly_chart(fig_job_role, use_container_width=True)
    
    with col2:
        # Attrition by Overtime
        st.subheader("Attrition by Overtime")
        overtime_attrition_df = df.groupby(['OverTime', 'Attrition']).size().reset_index(name='Count')
        overtime_attrition_df_yes = overtime_attrition_df[overtime_attrition_df['Attrition'] == 'Yes']
        
        fig_overtime = px.pie(
            overtime_attrition_df_yes,
            values='Count', 
            names='OverTime',
            title='Attrition Proportion by Overtime Status'
        )
        st.plotly_chart(fig_overtime, use_container_width=True)
    
    # Scatter Plot: Monthly Income vs Attrition
    st.subheader("Monthly Income vs Attrition")
    fig_income = px.scatter(
        df, 
        x='MonthlyIncome', 
        y='Age', 
        color='Attrition',
        title='Income and Age Distribution by Attrition Status',
        labels={'MonthlyIncome': 'Monthly Income', 'Age': 'Employee Age'}
    )
    st.plotly_chart(fig_income, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("### 📌 Key Insights")
    st.markdown("""
    - Monitor job roles and departments with high attrition
    - Analyze the impact of overtime and business travel
    - Consider income and age factors in retention strategies
    """)

if __name__ == "__main__":
    main()