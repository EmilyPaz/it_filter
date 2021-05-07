# IT Filter Tool

![Image](https://media-exp1.licdn.com/dms/image/C4D1BAQHbjxTCUBgnMA/company-background_10000/0/1584032759755?e=1620489600&v=beta&t=2EDGpDv8om70ptFb-TJcBm1RdEZ2dhd-f_r8ZJykI-o)

## :point_right: **About**

My Ironhack Data Analytics Final Project consists in a tool made for IT Recruiters to use as a filter of our internal databases.

Probably the function of an IT Recruiter that takes the most part of our working day is the searching of valid candidates. This is a market where there's a lot of offer from different companies in all kind of sectors and the unemployment rate is very low, so it might by really difficult to find the perfect candidate. We use essentially InfoJobs and LinkedIn Recruiter to make our active search for candidates, but what happens with candidates we already talked to?

![Image](https://energyresourcing.com/wp-content/uploads/2019/02/recruitment-agency-gives-you-access-to-talent-pool.jpg)

Most SMEs and startups consulting companies don't have enough budget to hire HR services, as Factorial, Bizneo, E-Preselec, etc. Also, these services are not focused on IT consulting, is about HR management. So we usually use Excel to have a registration (besides employment portals comments) of the people we talk to day by day. In my experience in two different consulting companies, these internal databases are not useful as every member of the Recruiting Department has its own file made in different ways, they don't follow a single structure to make an easy searching, so they are not usually used as the first option when a client's need comes.

### **So... here's my proposal**

This tool has the purpose to extract a cvs file from a shared database with all members of a Recruiting Department that contains all contacted candidates with the skills we need. 

The database has to contain the main information we usually need to make a selection (name, email and phone is information I encoded to upload this tool in Github): profile (programmer, analyst/programmer, tester, administrator, DevOps...), level (junior, senior, expert), technology stack, time of experience, salary (if we know it), location and comments. 

With this tool, you'll introduce the technologies you need to search for, the kind of profile, level and location. Four words and here it goes! An entire csv file with all the information and people you need to start your searching without losing time doing active search, a lot of calls and messages, etc.

This tool has an extra that would probably help IT Recruiters to make a first sift: it contains an Machine Learning prediction model to predict salaries of all the candidates who's salaries are unknown for us, so we can have an estimation of what they'll probably looking for an economic change.

![Image](https://www.caminopartners.co.uk/rails/active_storage/representations/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBNEVaQmc9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--273c91a6cdb7a786e9fa3fe2ae91539ea101d985/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCam9MY21WemFYcGxTU0lPTWpBd01IZzJNREErQmpvR1JWUT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--90f28495d760ed1ad98beb2536ceee5a22f1c714/up_your_recruitment_game.jpg)


## :bug: **Status**

My next step is to make an API REST connection to Sharepoint so we can extract the main database from a cloud service where all members of a Recruiting Department can feed day by day this database.

## :computer: **Technology stack**

- Python :snake:
- Pandas :panda_face: 
- RegEx :bookmark_tabs:
- Hashlib MD5 :link:
- Scikit-learn :
- PyCharm :beetle:

## :open_file_folder: **Folder structure**
```
└── project
    ├── .idea
    ├── data
    ├── p_analysis
    │   ├── __init__.py
    │   └── m_analysis.py
    ├── p_reporting
    │   ├── __init__.py
    │   └── m_reporting.py
    ├── p_wrangling
    │   ├── __init__.py
    │   └── m_wrangling.py
    ├── results
    ├── .gitignore
    ├── README.md
    └── main_script.py
```

### :mailbox_with_mail: CONTACT INFO

If you have any comments or questions please contact me! emilypaz3012@gmail.com

