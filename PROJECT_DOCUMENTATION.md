# Data Analysis Project Documentation
## Phase 1 : Identifying and Defining
### Mind Map
 ![Project Ideas Mind Map](./images/mind%20map.png)

### Define Your Purpose
**Hypothesis :** Awareness of unethical practices in companies would reduce students' willingness to buy its products. However, when that company is popular or widely recognised, many would be more reluctant to refrain from buying these products even if they are unethically sourced.

### Requirements Outline
**Functional Requirements**

1. Data Loading: The system must be able to load .csv and .png files. When handling errors during file loading like incorrect format and missing files, the system should be able to report error messages(eg. File is missing).

2. Data Cleaning: System must be able to group same values(1-5) together in each question/column.

3. Data Analysis: System needs to calculate the median of each question/column.

4. Data Visualisation: Data will need to be visualised in a grouped bar chart or a boxplot using Matplotlib.

5. Data Reporting: The system ahould include a table output where columns are responses 1-5 and rows are Questions 1 through 3. The final dataset needs to be stored in a .csv file.


**Non-Functional Requirements**

1. Speed : The system should not take a unreasonable amount of time to process/load (should be around ~5-20 seconds max)
2. Security : All data taken from students should be anonymous and not attached to any gmails. 
3. Reliability : Error messages should be clear, specific and informative(eg. Unsupported file format). Data used and displayed in this project/final reporting should also b  e accurate to student responses, and within established range(1-5).
4. Usability : The 'README' document needs to clear and concise in the purpose of the system and how to use it. The User Interface should be accessible, easy to navigate and comprehensible to viewers.

**Use Case**

**Actor:** User

**Goal:** To access and interact with existing data on the ethics of chocolate companies (based on Google Form responses from GHS students) through the program’s user interface.  
**Preconditions:**

The dataset has already been preloaded into the system by an administrator / programmer(me).

NSW education email users(students & teachers) have access to the system interface.

**Main Flow:**

User opens the program and is presented with a text-based menu.

User selects one of the following options:
a. View visualisation (grouped bar chart/box plot)
b. Search or filter data based on individual responses OR responses in a specific question


System performs the requested action and outputs to user.


**Postconditions:**

User has viewed and/or interacted with the data.

Data remains available for further queries or analysis.


## Phase 2 : Researching and Planning
### Research Your Chosen Issue
**Chosen Issue :** Leading chocolate brands and their inadequate ethicalities.

Ethical issues surrounding cocoa sourcing such as deforestation, low wages, poor working conditions, child labour and a lack of transparency have both been addressed but have persisted in leading chocolate brands since the early 2000s. As an industry with a global market size of approximately $216.8 billion AUD and a popularity that isn't dying down any time soon, it is critical to also educate modern-day consumers on what practices they are supporting when they buy from specific companies.


https://apnews.com/article/chocolate-deforestation-cocoa-farming-nigeria-08b396be56cc65d08c950f61308539d3

According to an article by Taiwo Adebayo, irresponsible cocoa farming from chocolate companies has also had a detrimental environmental effect. Protected lands like the Omo Reserve Reserve in Nigeria, one of Africa’s “oldest and largest UNESCO Biosphere Reserves” are facing illegal deforestation for the expansion of cocoa farming lands, causing a consequent endangerment of native land and species like the African forest elephant. Trading companies buy cocoa supplies from these cocoa farmers in prohibited areas to sell to names like Snickers, Ferrero and Nutella.


https://www.sustainalytics.com/esg-research/resource/investors-esg-blog/child-labor-in-cocoa-supply-chains--unveiling-the-layers-of-human-rights-challenges?utm_source=chatgpt.com

To further highlight the issue at hand, this activity is an exploitation of the poverty of local Nigerian farmers and other like communities in developing countries of West Africa. Since the 1970s, large companies have decreased cocoa farmers' value in a chocolate bar from 50% to 6% today. Some researchers argue that this decline is an attempt to reduce prices to combat competition, however chocolate prices have risen by 14% in 2023 and it has become clear that profit is being prioritised over stable and reasonable wages for cocoa farmers. 


Due to this, in countries like Ghana, child labour within cocoa supply chains has become more prevalent as poverish families face systematic oppression and an income that is simply not enough to support everyday life. 45% of children in cocoa farming areas engage in farming activities, and as these children are mostly rooted in financial challenges and adversity, many supply chains expose them to poor working conditions including:
Exposure to pesticides
Carrying heavy loads continuously 
No social security or safety nets/regulations
Operating dangerous equipment
Long working hours + low pay


As a society, it is important for us consumers to be held responsible for what companies we buy from. Therefore, it is also pivotal to be bluntly aware and informed on which brands to avoid and which brands to support to ensure that in future, the chocolate industry will have strict regulations with strict consequences for those who continue to exploit workers and the environment. 


https://www.chocolatescorecard.com/

**These are the current main offenders:**

Mondelez (Cadbury, Milka, Toblerone),
Morinaga,
Lotte,
Glico,
Daito Cacao,
Meiji,
Nestle,
Godiva,
Starbucks,
Itochu Corporation,
Hershey's,
Ferrero

**Great and amazing brands to buy from:**

Tony’s Chocolate,
Beyond Good,
Coop,
HALBA,
Cemoi,
Ritter Sport

### Discuss the findings (one SEE-I)

### Planning
>**NOTE** - My data is from the results in the Google Form I created that was sent to Gosford High students (https://docs.google.com/forms/d/e/1FAIpQLScZJvZPyFoNlSzkuq3TSwnd-fCinHsBgpj-bX4cZNu_lbbQoA/viewform?usp=dialog)

|Field |Datatype |Format for Display |Description |Example |Validation |
|------|---------|-------------------|------------|--------|-----------|
|       

## Phase 4 : Testing and Evaluating
### Analyse and Conclude
### Test Your Analysis

## Evaluation
**1. Evaluate your system and results in relation to your Requirements Outline**

**2. Evaluate your system in relation to peer feedback**

**3. Evaluate your project in relation to project management**

**4. Evaluate your system in relation to its data and security. Is the data valid, accurate and timely? Is it unbiased? Do we need to improve its security -- If so, how? Could the UX be more accessible -- how?**