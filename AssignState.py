import csv

filename = 'ContactInformation.csv'

data = []

#initialize all state counts of volunteers to 0
ALcount = AKcount = AZcount = ARcount = CAcount = COcount = CTcount = DEcount = FLcount = GAcount = HIcount = IDcount = ILcount = INcount = IAcount = KScount = KYcount = LAcount = MEcount = MDcount = MAcount = MIcount = MNcount = MScount = MOcount = MTcount = NEcount = NVcount = NHcount = NJcount = NMcount = NYcount = NCcount = NDcount = OHcount = OKcount = ORcount = PAcount = RIcount = SCcount = SDcount = TNcount = TXcount = UTcount = VTcount = VAcount = WAcount = WVcount = WIcount = WYcount = 0

States = ['Maine' , 'New Hampshire', 'Massachusetts', 'Vermont', 'Rhode Island', 'Pennsylvania', 'New York', 'New Jersey', 'Connecticut', 'Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Ohio', 'Delaware', 'Maryland','Virginia', 'West Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Kentucky', 'Tennessee', 'Mississippi', 'Alabama','Oklahoma', 'Texas', 'Arkansas', 'Louisiana', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Minnesota', 'Iowa','Missouri', 'Idaho', 'Montana', 'Wyoming', 'Nevada', 'Utah', 'Colorado', 'Arizona', 'New Mexico', 'Alaska', 'Washington', 'Oregon', 'California', 'Hawaii']


reader = csv.reader(open (filename,'r'), delimiter = ',')
header = next(reader)
index = header.index('State you currently reside in')

for i in reader:
  data.append(i[index])


for i in data:
    if (i == 'Alabama'):
        ALcount = ALcount + 1
    if (i == 'Alaska'):
        AKcount = AKcount + 1
    if (i == 'Arizona'):
        AZcount = AZcount + 1
    if (i == 'Arkansas'):
        ARcount = ARcount + 1
    if (i == 'California'):
        CAcount = CAcount + 1
    if (i == 'Colorado'):
        COcount = COcount + 1
    if (i == 'Connecticut'):
        CTcount = CTcount + 1
    if (i == 'Delaware'):
        DEcount = DEcount + 1
    if (i == 'Florida'):
        FLcount = FLcount + 1
    if (i == 'Georgia'):
        GAcount = GAcount + 1
    if (i == 'Hawaii'):
        HIcount = HIcount + 1
    if (i == 'Idaho'):
        IDcount = IDcount + 1
    if (i == 'Illinois'):
        ILcount = ILcount + 1
    if (i == 'Indiana'):
        INcount = INcount + 1
    if (i == 'Iowa'):
        IAcount = IAcount + 1
    if (i == 'Kansas'):
        KScount = KScount + 1
    if (i == 'Kentucky'):
        KYcount = KYcount + 1
    if (i == 'Louisiana'):
        LAcount = LAcount + 1
    if (i == 'Maine'):
        MEcount = MEcount + 1
    if (i == 'Maryland'):
        MDcount = MDcount + 1
    if (i == 'Massachusetts'):
        MAcount = MAcount + 1
    if (i == 'Michigan'):
        MIcount = MIcount + 1
    if (i == 'Minnesota'):
        MNcount = MNcount + 1
    if (i == 'Mississippi'):
        MScount = MScount + 1
    if (i == 'Missouri'):
        MOcount = MOcount + 1
    if (i == 'Montana'):
        MTcount = MTcount + 1
    if (i == 'Nebraska'):
        NEcount = NEcount + 1
    if (i == 'Nevada'):
        NVcount = NVcount + 1
    if (i == 'New Hampshire'):
        NHcount = NHcount + 1
    if (i == 'New Jersey'):
        NJcount = NJcount + 1
    if (i == 'New Mexico'):
        NMcount = NMcount + 1
    if (i == 'New York'):
        NYcount = NYcount + 1
    if (i == 'North Carolina'):
        NCcount = NCcount + 1
    if (i == 'North Dakota'):
        NDcount = NDcount + 1
    if (i == 'Ohio'):
        OHcount = OHcount + 1
    if (i == 'Oklahoma'):
        OKcount = OKcount + 1
    if (i == 'Oregon'):
        ORcount = ORcount + 1
    if (i == 'Pennsylvania'):
        PAcount = PAcount + 1
    if (i == 'Rhode Island'):
        RIcount = RIcount + 1
    if (i == 'South Carolina'):
        SCcount = SCcount + 1
    if (i == 'South Dakota'):
        SDcount = SDcount + 1
    if (i == 'Tennessee'):
        TNcount = TNcount + 1
    if (i == 'Texas'):
        TXcount = TXcount + 1
    if (i == 'Utah'):
        UTcount = UTcount + 1
    if (i == 'Vermont'):
        VTcount = VTcount + 1
    if (i == 'Virginia'):
        VAcount = VAcount + 1
    if (i == 'Washington'):
        WAcount = WAcount + 1
    if (i == 'West Virginia'):
        WVcount = WVcount + 1
    if (i == 'Wisconsin'):
        WIcount = WIcount + 1
    if (i == 'Wyoming'):
        WYcount = WYcount + 1


NorthEastBracket = [MEcount,NHcount,MAcount,VTcount,RIcount,PAcount]

TriStateBracket = [NYcount, NJcount, CTcount]

EastNorthCentralBracket = [WIcount,MIcount,ILcount,INcount,OHcount]

SouthAtlanticBracket = [DEcount, MDcount, VAcount, WVcount, NCcount, SCcount, GAcount, FLcount]

SouthCentralBracket = [KYcount, TNcount, MScount, ALcount, OKcount, TXcount, ARcount, LAcount]

WestNorthCentralBracket = [NDcount, SDcount, NEcount, KScount, MNcount, IAcount, MOcount]

MountainBracket = [IDcount, MTcount, WYcount, NVcount, UTcount, COcount, AZcount, NMcount]

PacificBracket = [AKcount,WAcount,ORcount,CAcount,HIcount]


newVolunteerState = data[len(data) - 1] #gives last state entered in ContactInformation
stateIndex = 0
assignedState = ' '
for y in range(0,len(States)):
    if (newVolunteerState == States[y]):
        stateIndex = y

if (stateIndex <= 5):
    assignedState = States[min(NorthEastBracket)]
elif (6 <= stateIndex <= 8):
    assignedState = States[6 + min(TriStateBracket)]
elif (9 <= stateIndex <= 13):
    assignedState = States[9 + min(EastNorthCentralBracket)]
elif (14 <= stateIndex <= 21):
    assignedState = States[14 + min(SouthAtlanticBracket)]
elif (22 <= stateIndex <= 29):
    assignedState = States[22 + min(SouthCentralBracket)]
elif (30 <= stateIndex <= 36):
    assignedState = States[30 + min(WestNorthCentralBracket)]
elif (37 <= stateIndex <= 44):
    assignedState = States[37 + min(MountainBracket)]
elif (45 <= stateIndex <= 49):
    assignedState = States[45 + min(PacificBracket)]
