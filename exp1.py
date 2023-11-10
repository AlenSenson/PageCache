from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
li=["afdef","asdfds"]
a=[
    Choice("ap-southeast-2", name="Sydney"),
    Choice("ap-southeast-1", name="Singapore"),
    Separator(),
    "us-east-1",
    "us-east-2",
    ]+li
co=1

def main():
    
    action = inquirer.select(
        message="Select an action:",
        choices=[
            "Add Webpage",
            Choice(value=None, name="Exit"),
            Separator(),
        ],
        default=None,
    ).execute()

    if action:
        region = inquirer.select(
            message="Select regions:",
            choices=a,
            multiselect=True,
            transformer=lambda result: f"{len(result)} region{'s' if len(result) > 1 else ''} selected",
        ).execute()
    else:
        co=0


if __name__ == "__main__":
    while co:
        main()