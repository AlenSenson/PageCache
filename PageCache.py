from InquirerPy import inquirer, get_style
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy import inquirer

from pywebcopy import save_webpage
import webbrowser,os,csv



#Checking for folder
if not os.path.isdir('PageCache'):
    os.mkdir('PageCache')

#Change directory
os.chdir('PageCache')

#create csv file
if not os.path.isfile('PCrec.csv'):
    file= open('PCrec.csv','w')
    file.close()

#Accessing csv file
rows = []
with open('PCrec.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)


style = get_style(
    {"question": "bold", 
     "answer": "bold", 
     "input": "bold"
    }, 
    style_override=False
    )


#mainfunction
def main():
    os.system("cls")
    print("WELCOME TO PAGE CACHE")
    print("PageCache enables you to save web content for offline access,")
    print("ensuring you can view webpages even without an internet connection")
    print("\n\n")

    #providing options
    action = inquirer.select(
        message="Select an action:",
        choices=[
            Choice(value='add', name="Add Webpage"),
            Choice(value="exit", name="Exit"),
            Separator(),
        ] + [Choice(value= i[0], name=i[1]) for i in rows if i!=[] ],
        default=None,
        style = style,
    ).execute()

    
    #adding webpage
    if action=='add':
        name = inquirer.text(message="Enter webpage name:").execute()
        link = inquirer.text(message="Enter link:").execute()
        
        save_webpage(
            url=link,
            project_folder= os.getcwd(),
            project_name=str(len(rows)),
            bypass_robots=True,
            debug=False,
            open_in_browser=False,
            delay=None,
            threaded=False,
            )
        
        rec=[len(rows),name,link]
        rows.append(rec)
        print(rec)
        

        # writing to csv file
        with open('PCrec.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)


        os.system("cls")


    #exit
    elif action=='exit':
        exit()
        os.system("cls")


    #view webpage
    else:
        for root, dirs, files in os.walk(os.getcwd()+'\\'+str(action)):
            for file in files:
                if file[-5:] == ".html":
                    # Open the index.html file in the browser.
                    webbrowser.open(os.path.join(root, file))
        os.system("cls")


if __name__ == "__main__":
    while True:
        main()




