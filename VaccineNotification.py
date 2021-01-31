import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from gtts import gTTS 

def sliceToText(text, htmlMarker):
    searchExp = htmlMarker + ">[A-Za-z\.,0-9+ ]*<"
    strippedDown = re.search(searchExp, str(text), flags=0).group()
    return strippedDown[len(htmlMarker)+1:len(strippedDown)-1]

def pullData():
    url = "https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html";
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    table = soup.find("div", class_="g-table-div g-eligibility-table")
    
    states = table.find_all("td", class_="g-cell g-name")
    ages = table.find_all("p", class_="g-use-cat-color")
    otherMarkers = table.find_all("td", class_="g-cell g-col")
    listFrame = []
    
    for index, state in enumerate(states):
        tempList = [sliceToText(state, "full\"")]
        
        age = sliceToText(ages[index], "")
        
        if(age != ''):
            age = age[:-1]
        else:
            age = "None"
        
        tempList.append(age)
        
        for i in range(3):
            mark = sliceToText(otherMarkers[i + 3*index], "p")
            if(mark == ''):
                mark = 'No'
            
            tempList.append(mark)
    
        listFrame.append(tempList)
    
    return pd.DataFrame(listFrame, columns=['State', 'Age', 'Healthcare', 'EssentialWorker', "HighRisk"])

def generateMessages(saveDirectory):
    stateData = pullData()
    
    for index, row in stateData.iterrows():
        
        eligibilityList = []
        eligibilityListSpan = []
                
        if(row['Age'] != 'None'):
            eligibilityList.append('people over the age of {}'.format(row['Age']))
            eligibilityListSpan.append('personas mayores de {} años'.format(row['Age']))
        
        else:
            eligibilityList.append('people of any age')
            eligibilityListSpan.append('personas de cualquier edad')

        
        if(row['EssentialWorker'] == 'Yes'):
            eligibilityList.append('some essential workers')
            eligibilityListSpan.append('algunos trabajadores esenciales')

            
        if(row['HighRisk'] == 'Yes'):
            eligibilityList.append('some high risk individuals')
            eligibilityListSpan.append('algunas personas de alto riesgo')

        
        message = "Hello. This is an automated reminder that in your state, {}, ".format(row['State'])
        spanMessage = "Hola. Este es un recordatorio automatizado de que en su estado, {}, ".format(row['State'])
        
        for index, item in enumerate(eligibilityList):
            if index == len(eligibilityList)-1 and index > 0:
                message += 'and '
                spanMessage += 'y '
            
            message += item + ', '
            spanMessage += eligibilityListSpan[index] + ', '
            
        message = message[:-2] + ' may be eligible for the coronavirus vaccine. If you think you qualify and want assistance registering for a vaccination, call 1-800-123-4567 to speak with a volunteer who will help you sign up.'
        spanMessage = spanMessage[:-2] + ' puede ser elegible para la vacuna contra el coronavirus. Si cree que califica y desea asistencia para registrarse para una vacunación, llame a 1-800-123-4567 para hablar con un voluntario que lo ayudará a inscribirse.'
                
        recording_en = gTTS(text=message, lang='en', slow=False)
        recording_es = gTTS(text=spanMessage, lang='es', slow=False)
        
        with open('{}/{}.mp3'.format(saveDirectory, row['State']), 'wb') as fp:
            recording_en.write_to_fp(fp)
            recording_es.write_to_fp(fp)
        
        
if __name__ == '__main__':
    generateMessages("/Users/Ari/Desktop/VaccineMessages")