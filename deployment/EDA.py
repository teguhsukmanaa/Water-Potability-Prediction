import streamlit as st

def app():
    # Libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Streamlit option to turn off the disable warning
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Load data
    df = pd.read_csv('water_potability.csv')

    # Page title
    st.title("Dataset Overview")
    with st.container(border=True):
        data_ov = '''
        Dataset yang digunakan pada project ini merupakan data terkait kualitas air dari beragam sampel air yang didasarkan pada berbagai parameter pengukuran karakteristik dan kandungan air. 

        Sumber Dataset:
        https://www.kaggle.com/datasets/adityakadiwal/water-potability

        Berikut merupakan deskripsi fitur-fitur yang ada didalam dataset:  
        1. `ph`: Nilai pH air (rentang 0-14).
        2. `Hardness`: Nilai kapasitas air untuk mengendapkan sabun yang disebabkan oleh Kalsium dan Magnesium (mg/L).
        3. `Solids`: Nilai Total Dissolved Solids (TDS)/jumlah padatan terlarut dalam air (ppm).
        4. `Chloramines`: Jumlah Chloramines dalam air (ppm).
        5. `Sulfate`: Jumlah Sulfates terlarut dalam air (mg/L).
        6. `Conductivity`: Tingkat Electrical conductivity air (μS/cm).
        7. `Organic_carbon`: Jumlah Organic Carbon dalam air (ppm).
        8. `Trihalomethanes`: Jumlah Trihalomethanes dalam air (μg/L).
        9. `Turbidity`: Tingkat kekeruhan/Pengukuran kemampuan pancaran cahaya air (NTU).
        10. `Potability`: Indikasi keamanan air untuk dikonsumsi (1=Layak/Berpotensi Konsumsi; 0=Tidak Layak).

        - Keterangan satuan ukur:
            + ppm: parts per million
            + μg/L: microgram per liter
            + mg/L: milligram per liter
            + µS/cm: microsiemens per centimeter (unit in the category of Electric conductivity)
            + NTU: Nephelometric Turbidity Unit (the unit used to measure the turbidity)
        '''
        st.markdown(data_ov)

    # Page title
    st.title("Exploratory Data Analysis (EDA) of Water Potability")

    # Data preview
    with st.container(border=True):
        st.subheader("Preview of the Dataset")
        st.write(df.head())

    # Data class proportion
    with st.container(border=True):
        st.subheader("Data class proportion")
        # Pie chart definition
        labels = ['Non-Potable', 'Potable']
        size = df['Potability'].value_counts()
        colors = ['skyblue', 'dodgerblue']
        explode = [0.1, 0]
        # figure
        fig, axes = plt.subplots(figsize=(10, 5))
        plt.pie(size, colors = colors, explode = explode,
                labels = labels, startangle = 90, autopct = '%.2f%%')
        plt.title('Potability Data Proportion', fontsize = 15)
        plt.legend()
        # Show figure
        st.pyplot(fig)
        # Caption
        text_1 = '''Dapat diketahui bahwa proporsi kelas klasifikasi pada dataset ini tidak seimbang, yang mana dataset ini didominasi oleh data kelas Non-Potable(0) yaitu sebesar 61% dan data kelas Potable(1) sebesar 39%. Adanya ketidakseimbangan proporsi data kelas ini dapat berpotensi adanya bias ketika training model sehingga akan menurunkan performa model dalam melakukan prediksi.'''
        st.markdown(text_1)

    # Distribution 1
    with st.container(border=True):
        st.subheader("pH Level Distibution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='ph', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('pH Level')
        plt.ylabel('Count')
        plt.title('pH Level Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_2 = '''Berdasarkan visualisasi dari histogram, secara keseluruhan data pH dapat dikatakan berdistribusi normal, namun masih dapat terlihat beberapa data di ujung kiri dan kanan histogram yang bisa saja terindikasi sebagai extreme values/outliers. Terkait tentang ph air, ph sendiri merupakan sebuah tingkat asam-basa sebuah materi. Adapun tingkat pH pada air konsumsi biasanya berkisar pada 6.5-8.5, yang mana pada histogram ini dapat kita ihat bahwa air yang layak konsumsi (potable) banyak berkumpul di rentang pH 6-8.'''
        st.markdown(text_2)

    # Distribution 2
    with st.container(border=True):
        st.subheader("Hardness Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Hardness', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Hardness (mg/L)')
        plt.ylabel('Count')
        plt.title('Hardness Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_3 = '''-'''
        st.markdown(text_3)

    # Distribution 3
    with st.container(border=True):
        st.subheader("Total Dissolved Solids (TDS) Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Solids', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Dissolved Solids (ppm)')
        plt.ylabel('Count')
        plt.title('Total Dissolved Solids Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_4 = '''-'''
        st.markdown(text_4)


    # Distribution 4
    with st.container(border=True):
        st.subheader("Chloramines Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Chloramines', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Amount of Chloramines (ppm)')
        plt.ylabel('Count')
        plt.title('Chloramines Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_5 = '''-'''
        st.markdown(text_5)

    # Distribution 5
    with st.container(border=True):
        st.subheader("Sulfate Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Sulfate', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Amount of Sulfate (mg/L)')
        plt.ylabel('Count')
        plt.title('Sulfate Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_6 = '''-'''
        st.markdown(text_6)

    # Distribution 6
    with st.container(border=True):
        st.subheader("Conductivity Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Conductivity', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Conductivity (μS/cm)')
        plt.ylabel('Count')
        plt.title('Conductivity Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_7 = '''-'''
        st.markdown(text_7)

    # Distribution 7
    with st.container(border=True):
        st.subheader("Organic Carbon Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Organic_carbon', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Amount of Organic Carbon (ppm)')
        plt.ylabel('Count')
        plt.title('Organic Carbon Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_8 = '''-'''
        st.markdown(text_8)

    # Distribution 8
    with st.container(border=True):
        st.subheader("Trihalomethanes Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Trihalomethanes', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Amount of Trihalomethanes (μg/L)')
        plt.ylabel('Count')
        plt.title('Trihalomethanes Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_9 = '''-'''
        st.markdown(text_9)

    # Distribution 9
    with st.container(border=True):
        st.subheader("Turbidity Distribution")
        # Create histogram
        plt.figure(figsize=(17, 8))
        sns.histplot(data=df, x='Turbidity', hue='Potability', bins=100, multiple='dodge', palette=['skyblue', 'dodgerblue'])
        plt.xlabel('Turbidity (NTU)')
        plt.ylabel('Count')
        plt.title('Turbidity Distribution Histogram', fontsize=18)
        # Adjust figure layout
        plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
        # Show figure
        st.pyplot()
        # Caption
        text_10 = '''-'''
        st.markdown(text_10)

    # Feature correlation
    with st.container(border=True):
        st.subheader("Data Correlation")
        # Create correlation heatmap
        corr_matrix = df.corr()
        plt.figure(figsize=(20, 10))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Data Correlation Heatmap', fontsize=18)
        st.pyplot()
        # Caption
        text_11 = '''Berdasarkan heatmap diatas, dapat diketahui bahwa korelasi antar data dalam dataset ini sangatlah kecil. Menurut saya, hal ini menandakan bahwa data yang ada kurang memuaskan karena jika dianalisa lebih dalam maka seharusnya karakteristik/parameter air seharusnya akan saling berkaitan, misalnya jika kandungan organic carbon dalam air meningkat maka biasanya tingkat pH air akan menurun (menjadi asam) serta secara tidak langsung akan menyebabkan air menjadi keruh atau sulit memencar cahaya (turbiditas menigkat).'''
        st.markdown(text_11)