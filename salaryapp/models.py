from django.db import models

# Create your models here.

class Data(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    MARRIED_CIV_SPOUSE = 'MCS'
    DIVORCED           = 'D'
    NEVER_MARRIED      = 'NM'
    SEPARATED          = 'S'
    WIDOWED            = 'W'
    MARRIED_SPOUSE_ABSENT = 'MSA'
    MARRIED_AF_SPOUSE  = 'MAS'
    MARTIAL_STATUS     = (
        (MARRIED_CIV_SPOUSE,'Married-civ-spouse'),
        (DIVORCED,'Divorced'),
        (NEVER_MARRIED,'Never-married'),
        (SEPARATED,'Separated'),
        (WIDOWED,'Widowed'),
        (MARRIED_SPOUSE_ABSENT,'Married-spouse-absent'),
        (MARRIED_AF_SPOUSE,'Married-AF-spouse')
    )

    WIFE = 'W'
    OWN_CHILD = 'OC'
    HUSBAND = 'H'
    NOT_IN_FAMILY = 'NIF'
    OTHER_RELATIVE = 'OR'
    UNMARRIED = 'U'
    RELATIONSHIP = (
        (WIFE,'Wife'),
        (OWN_CHILD,'Own-child'),
        (HUSBAND,'Husband'),
        (NOT_IN_FAMILY,'Not-in-family'),
        (OTHER_RELATIVE,'Other-relative'),
        (UNMARRIED,'Unmarried')
    )

    WHITE = 'WT'
    ASIAN_PAC_ISLANDER = 'API'
    AMER_INDIAN_ESKIMO = 'AIE'
    OTHER = 'O'
    BLACK = 'B'
    RACE = (
        (WHITE,'White'),
        (ASIAN_PAC_ISLANDER,'Asian-Pac-Islander'),
        (AMER_INDIAN_ESKIMO,'Amer-Indian-Eskimo'),
        (OTHER,'Other'),
        (BLACK,'Black')
    )

    BACHELORS = 'BA'
    SOME_COLLEGE = 'SC'
    STDA = '11'
    HS_GRAD = 'HG'
    PROF_SCHOOL = 'PS'
    ASSOC_ACDM = 'AA'
    ASSOC_VOC = 'AV'
    STDB = '9'
    STDC = '7'
    STDD = '12'
    MASTERS = 'MS'
    STDE = '1'
    STDF = '10'
    DOCTRATE = 'DOC'
    STDG = '5'
    PRESCHOOL = 'PRE'
    EDUCATION = (
        (BACHELORS,'Bachelors'),
        (SOME_COLLEGE,'Some-college'),
        (STDA,'11th'),
        (HS_GRAD,'HS-grad'),
        (PROF_SCHOOL,'Prof-school'),
        (ASSOC_ACDM,'Assoc-acdm'),
        (ASSOC_VOC,'Assoc-voc'),
        (STDB,'9th'),
        (STDC,'7th-8th'),
        (STDD,'12th'),
        (MASTERS,'Masters'),
        (STDE,'1st-4th'),
        (STDF,'10th'),
        (DOCTRATE,'Doctorate'),
        (STDG,'5th-6th'),
        (PRESCHOOL,'Preschool'),
    )

    PRIVATE = 'PR'
    SELF_EMP_NOT_INC = 'SENI'
    SELF_EMP_INC = 'SEI'
    FEDERAL_GOV = 'FG'
    LOCAL_GOV = 'LG'
    STATE_GOV = 'SG'
    WITHOUT_PAY = 'WP'
    NEVER_WORKED = 'NW'
    WORKCLASS = (
        (PRIVATE,'Private'),
        (SELF_EMP_NOT_INC,'Self-emp-not-inc'),
        (SELF_EMP_INC,'Self-emp-inc'),
        (FEDERAL_GOV,'Federal-gov'),
        (LOCAL_GOV,'Local-gov'),
        (STATE_GOV,'State-gov'),
        (WITHOUT_PAY,'Without-pay'),
        (NEVER_WORKED,'Never-worked'),
    )

    TECH_SUPPORT = 'TS'
    CRAFT_REPAIR = 'CR'
    OTHER_SERVICES = 'OS'
    SALES = 'SA'
    EXEC_MANAGERIAL = 'EM'
    PROF_SPECIALITY = 'PS'
    HANDLERS_CLEANERS = 'HC'
    MACHINE_OP_INSPCT = 'MOI'
    ADM_CLERICAL = 'AC'
    FARMING_FISHING = 'FF'
    TRANSPORT_MOVING = 'TM'
    PRIV_HOUSE_SERV = 'PHS'
    PROTECTIVE_SERV = 'PS'
    ARMED_FORCES = 'AF'
    OCCUPATION = (
        (TECH_SUPPORT,'Tech-support'),
        (CRAFT_REPAIR,'Craft-repair'),
        (OTHER_SERVICES,'Other-service'),
        (SALES,'Sales'),
        (EXEC_MANAGERIAL,'Exec-managerial'),
        (PROF_SPECIALITY,'Prof-specialty'),
        (HANDLERS_CLEANERS,'Handlers-cleaners'),
        (MACHINE_OP_INSPCT,'Machine-op-inspct'),
        (ADM_CLERICAL,'Adm-clerical'),
        (FARMING_FISHING,'Farming-fishing'),
        (TRANSPORT_MOVING,'Transport-moving'),
        (PRIV_HOUSE_SERV,'Priv-house-serv'),
        (PROTECTIVE_SERV,'Protective-serv'),
        (ARMED_FORCES,'Armed-Forces'),
    )

    UNITED_STATES = 'US'
    CAMBODIA = 'CA'
    ENGLAND = 'E'
    PUERTO_RICO = 'PR'
    CANADA = 'CD'
    GERMANY = 'G'
    OUTLYING_US = 'OU'
    INDIA = 'I'
    JAPAN = 'JP'
    GREECE = 'GR'
    SOUTH = 'SO'
    CHINA = 'CH'
    CUBA = 'CU'
    IRAN = 'IR'
    HONDURAS = 'HO'
    PHILIPPINES = 'PH'
    ITALY = 'IT'
    POLAND = 'PO'
    JAMAICA = 'JA'
    VIETNAM = 'VI'
    MEXICO = 'ME'
    PORTUGAL = 'POR'
    IRELAND = 'IR'
    FRANCE = 'FR'
    DOMINICAN_REPUBLIC = 'DR'
    LAOS = 'LA'
    ECUADOR = 'EC'
    TAIWAN = 'TW'
    HAITI = 'HT'
    COLUMBIA = 'CO'
    HUNGARY = 'HU'
    GUATEMALA = 'GU'
    NICARAGUA = 'NR'
    SCOTLAND = 'SL'
    THAILAND = 'TH'
    YUGOSLAVIA = 'YU'
    EL_SLAVADOR = 'ES'
    TRINADADTOBAGO = 'TT'
    PERU = 'PR'
    HONG = 'HG'
    HOLAND_NETHERLANDS = 'HN'
    NATIVE_COUNTRY = (
        (UNITED_STATES,'United-States'),
        (CAMBODIA,'Cambodia'),
        (ENGLAND,'England'),
        (PUERTO_RICO,'Puerto-Rico'),
        (CANADA,'Canada'),
        (GERMANY,'Germany'),
        (OUTLYING_US,'Outlying-US(Guam-USVI-etc)'),
        (INDIA,'India'),
        (JAPAN,'Japan'),
        (GREECE,'Greece'),
        (SOUTH,'South'),
        (CHINA,'China'),
        (CUBA,'Cuba'),
        (IRAN,'Iran'),
        (HONDURAS,'Honduras'),
        (PHILIPPINES,'Philippines'),
        (ITALY,'Italy'),
        (POLAND,'Poland'),
        (JAMAICA,'Jamaica'),
        (VIETNAM,'Vietnam'),
        (MEXICO,'Mexico'),
        (PORTUGAL,'Portugal'),
        (IRELAND,'Ireland'),
        (FRANCE,'France'),
        (DOMINICAN_REPUBLIC,'Dominican-Republic'),
        (LAOS,'Laos'),
        (ECUADOR,'Ecuador'),
        (TAIWAN,'Taiwan'),
        (HAITI,'Haiti'),
        (COLUMBIA,'Columbia'),
        (HUNGARY,'Hungary'),
        (GUATEMALA,'Guatemala'),
        (NICARAGUA,'Nicaragua'),
        (SCOTLAND,'Scotland'),
        (THAILAND,'Thailand'),
        (YUGOSLAVIA,'Yugoslavia'),
        (EL_SLAVADOR,'El-Salvador'),
        (TRINADADTOBAGO,'Trinadad&Tobago'),
        (PERU,'Peru'),
        (HONG,'Hong'),
        (HOLAND_NETHERLANDS,'Holand-Netherlands'),
    )

    GREATER_THAN = 'GT'
    LESS_THAN    = 'LT'
    SALARY_CHOICES = (
        (GREATER_THAN,'>50K'),
        (LESS_THAN,'<=50K'),
    )
    


    age             = models.FloatField(blank=True, null=True)
    workclass       = models.CharField(max_length=30, choices=WORKCLASS, blank=True, null=True)
    fnlwgt          = models.PositiveIntegerField(blank=True, null=True)
    education       = models.CharField(max_length=30, choices=EDUCATION, blank=True, null=True)
    education_num   = models.PositiveIntegerField(blank=True, null=True)
    martial_status  = models.CharField(max_length=30, choices=MARTIAL_STATUS, blank=True, null=True)
    occupation      = models.CharField(max_length=30, choices=OCCUPATION, blank=True, null=True)
    relationship    = models.CharField(max_length=30, choices=RELATIONSHIP, blank=True, null=True)
    race            = models.CharField(max_length=30, choices=RACE, blank=True, null=True)
    sex             = models.CharField(max_length=10, choices=SEX_CHOICES, blank=True, null=True)
    capital_gain    = models.PositiveIntegerField(blank=True, null=True)
    capital_loss    = models.PositiveIntegerField(blank=True, null=True)
    hours_per_week  = models.PositiveSmallIntegerField(blank=True, null=True)
    native_country  = models.CharField(max_length=30, choices=NATIVE_COUNTRY)
    salary_choices  = models.CharField(max_length=20, choices=SALARY_CHOICES)


    def __str__(self):
        return str(self.age)
 