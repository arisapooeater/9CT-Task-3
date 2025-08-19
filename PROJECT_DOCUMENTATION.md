# Data Analysis Project Documentation
## Phase 1 : Identifying and Defining
### Mind Map
 ![Project Ideas Mind Map](./images/mind%20map.png)

### Define Your Purpose
**Hypothesis :** Awareness of unethical practices in companies would reduce students' willingness to buy its products. However, when that company is popular or widely recognised, many would be more reluctant to refrain from buying these products even if they are unethically sourced.

### Requirements Outline
**Functional Requirements**

1. Data Loading: The system must be able to load .csv and .png files. When handling errors during file loading like incorrect format and missing files, the system should be able to report error messages(eg. File is missing).

2. Data Cleaning: System must be able to group same values(1-5) together in each question/column and be able to erase unnecessary data

3. Data Analysis: System needs to calculate the average of each question/column.

4. Data Visualisation: Data will need to be visualised in a grouped bar chart or a boxplot using Matplotlib.

5. Data Reporting: The system should include a table output where columns are responses 1-5 and rows are Questions 1 through 3. The final dataset needs to be stored in a .csv file.


**Non-Functional Requirements**

1. Speed : The system should not take a unreasonable amount of time to process/load (should be around ~5-20 seconds max)
2. Security : All data taken from students should be anonymous and not attached to any gmails. 
3. Reliability : Error messages should be clear, specific and informative(eg. Unsupported file format). Data used and displayed in this project/final reporting should also b  e accurate to student responses, and within established range(1-5).
4. Usability : The 'README' document needs to clear and concise in the purpose of the system and how to use it. The User Interface should be accessible, easy to navigate and comprehensible to viewers.

**Use Case**

**Actor:** User

**Goal:** To access and interact with existing data on the ethics of chocolate companies (based on Google Form responses from GHS students) through the program’s user interface.  
**Preconditions:**

The dataset has already been preloaded into the system by the programmer(me).

NSW education email users(students & teachers) have access to the system interface.

**Main Flow:**

User opens the program and is presented with a text-based menu.

User selects one of the following options:
a. View visualisation (grouped bar chart/box plot)
b. Search or filter data based on individual responses OR responses in a specific question
c. Exit


System performs the requested action and outputs to user.


**Postconditions:**

User has viewed and/or interacted with the data.


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
Awareness is a responsibility we all have as consumers to ultimately promote ethical company practices in the chocolate industry. Depending on the brands we buy from, we could be increasing demand for chocolates that are a product of worker exploitment, child slavery and unsustainable and possibly illegal cocoa sources. For example, choosing ethically sourced chocolates such as Tony’s Chocolate over chocolates that have aroused social issues is a responsible choice. But in general, Nestle chocolates are much more popular and affordable, which makes people buy them more -- But why is it so affordable? This is what makes being informed so critical. It’s just like buying a cheap ticket to your favourite band’s concert only to realise the band members are mistreating all the stage crew and they aren’t receiving any pay. Is this ethical consumption?

### Planning
>**NOTE** - My data is from the results in the Google Form I created that was sent to Gosford High students (https://docs.google.com/forms/d/e/1FAIpQLScZJvZPyFoNlSzkuq3TSwnd-fCinHsBgpj-bX4cZNu_lbbQoA/viewform?usp=dialog)

|Field |Datatype |Format for display |Description |Example | Validation |
|-------|-------------|-------------------------|----------------|------------|---------------|
|Control |Integer |N | Student's inclination to buying chocolate in general before any condition making/information brought to student's awareness |5 |Must be a number between range 1-5 inclusively
|After unethical practices identification |Integer |N | Student’s inclination to buying chocolate after identifying unethical practices within the company |1   |Must be a number between range 1-5 inclusively
|After brand recognition |Integer |N | Student’s inclination to buying chocolate after identifying unethical practices within the company AND the company itself |2 |Must be a number between range 1-5 inclusively


## Phase 4 : Testing and Evaluating
### Analyse and Conclude (two SEE-I)
Analyse your findings using at least one SEE-I paragraph. If you spot areas needing more research, make a note of them in your findings. Make sure to provide a conclusion on your hypothesis.

Analyse - (Identify components and the relationship between them.Draw out and relate implications. )


conclusion of hypothesis - 
My hypothesis was overall supported by the data analysed, but there are several unexplored areas that may need investigation for this project to be accurate and reliable. According to the comparison in the data visualisation, students ARE less willing to buy chocolate when made aware of unethical company practices but are more reluctant to refrain when the brand is widely recognised, (provingt that)

However, 
Evaluate
Example
Imagine
Awareness of unethical practices in companies would reduce students' willingness to buy its products. However, when that company is popular or widely recognised, many would be more reluctant to refrain from buying these products even if they are unethically sourced.


my hypothesis was overall supported by the data, but i believe the questions I asked the students in the Google Form isn't enough to just verify that yes, brand recognition and awareness of practices play roles in consumers buying chocolate
areas need more research - maybe questions in the gOOGLE FORM that was more like "What influenced you to buy the chocolate more/less?" and it could have the options 'brand recognition', 'bad practices in brand' and etc. so the students intentions and opinions was more clear. or questions that include a unpopular brand with good practices to see where consumer values really lay

### Peer Verifications
| Plus                                                                        |
|-----------------------------------------------------------------------------|
| The interface is consistent and easy to navigate                            |    
| The README file is comprehensive and contains visual representations        |
| Data searching                                                              |
| Timing in each action makes the program feel animated and more interactive  |    


| Minus                                                                       |
|-----------------------------------------------------------------------------|
| The timing of some actions are too long and reduces user engagement         |
| The program pauses while you inspect the visualisation, however some users want to compare the visualisations to other thngs

| Implication                                                                 |
|-----------------------------------------------------------------------------|

Plus

Timing sleep is very good bc it makes it feel animated
The interface is very easy to navigate and consistent
The instructions are very nice nice easy to understand
Nice error handling
Very good data searching 
The read me is very easy to follow and has visual representation and is very aesthetic


Minus
Sometimes the timesleep is too long
I dont like how u have to exit the chart and you can't run the code anymore


Implication
Overall is very good but there are changed that could be made to further enhance user experience and engagement. 



## Evaluation
**1. Evaluate your system and results in relation to your Requirements Outline**
My system and results adequately aligns with my functional and non-functional requirements, but has lacks some factors due to some changes. For the functional requirements, the system is satisfactory in terms of data cleaning and data reporting as Google Forms automatically sorts the data into columns and I removed the Timeframe column when I read the csv file into a dataframe. My system also completes the data analysis requirement as it calculates the average of each question's responses for the visualisation, which turned out not to be a grouped bar chort or box plot as they were either too difficult or wasn't what I wanted the data I got to look like. However, my system doesn't load png files as I stated in the data loading as there is no png file in my user interface to load.

On the other hand, in terms of non-functional requirements, the system is fast enough to load but also not automatic so the user is given time before moving on to the next command, and all data taken from students is anonymous, thanks to Google Forms setting options. For reliability, the data used and displayed in the final reporting is accurate to the student responses and within the established range of 1-5, and the error messages for user's incorrect commands are specific and clear, but I do not have any error messages coded for things like incorrect file format. Finally for the usability requirement, I believe my project's 'README' document is clear in the purpose of the system and how to use it as it also has images to guide users. However, the 'How To Use' section isn't as concise as it could be so next time that could be improved.  and the user interface is decently easy to navigate and (                )  but its not accessible for people with visual impairements so some colour, more visually contrasting and appealing graphics and maybe some audio that reads each option could greatly enhance the UX.


**2. Evaluate your system in relation to peer feedback**

**3. Evaluate your project in relation to project management**
In terms of project management, I'm pretty satisfied with my productivity compared to the last assessment. I finished the prac component of this assessment in around 3 days by doing some work at home and kept myself ahead of task to prevent myself from procrastinating or losing my mind like last time. I also can see on Github that my commits aren't too spaced out and are consistent with no big time gaps so I think that's good. Due to how fast I finished the user interface, I think I could've finished this documentation earlier, which is something I can improve on next time, however I was going through a bit of a study slump so I'm happy I gave time for myself while still working at a good pace in this project. Overall I think my project management was adequate and I'm content with the way I structured what and when I wanted to do each part of the project so I'm not stressed but also working productively.

**4. Evaluate your system in relation to its data and security. Is the data valid, accurate and timely? Is it unbiased? Do we need to improve its security -- If so, how? Could the UX be more accessible -- how?**
I believe my data is pretty valid as I tried to make it reflect how real consumers would react when buying chocolate at varying degrees of awareness/influences (awareness of unethical practices, influences of knowing the brand as popular etc). I tried my best to prioritise data accuracy by adding a control question at the beginning and seeing how the range of responses change as variables are added one at a time. Additionally, I made the format of the data I see the same (Range from 1-5) to be able to clearly see the nuances between each question's responses. However, I believe there will also be some skewing in accurracy as in these types of forms, students tend to be less honest as they know what the "right" answer should look like, or they may be influenced by aspects like peer pressure while responding. 

In terms of timeliness, I think my data is very reflective of the present as I received the data via a Google Form with student responses from the 31st of July to around 11th of August, which is this month. Furthermore, the topic I'm researching is not something that can drastically change in such a short amount of time so I personally believe my data is aligned with the current student's perspectives.

Moving on, in the user interface there's no way for the user to alter or update the data and they can only see a printed version of the data according to how they want to see it so with the little knowledge I have, I feel like its pretty secure. 
I also have the data stored in Google Sheets as well as in the Google Forms, but I searched up that I could've maybe made my data more secure by allowing VSC to send me display security alerts and also block malicious extensions/suspicious activity, as well as create stronger, unique passwords for all the accounts linked to the data here like my Github or my VSC account. However, I think the data is secure to the extend I can do right now.

Finally, I think my user interface is consistent with its design (the options/menus have these boxes around them and the questions are plain text) so I think it's simple to use. However, I also feel some areas are hard to understand, especially the options as they are a bit tricky to comprehend. Secondly, it's not very usable for visually impairemed people so if I were to do this project again (when I'm better at coding and stuff), it might be cool to play around with voices that read out the options or more colourful and visually contrasting UX designs to allow for a more unified experience.