from jira import JIRA, JIRAError


# to get proper ticket
def ProperTicket():
    print('Which ticket do you want?')
    ticket=str(input())
    issue = jira.issue(ticket)
    return issue

# print summary of current ticket
def SummaryTicket():
    issue = jira.issue("TES-1")
    summary = issue.fields.summary


# print info about all projects
def ProjectInfo():
    projects = jira.projects()
    return projects



# updated summary and description
def UpdateSummary():
    issue.update(summary="Media in not working updated2!", description="Changed the summary to be different new.")


# list of issues with summary:
def ListOfIssues():

    print("Is 5 tickets enough to display? 1-Yes, 2-No")
    accept = int(input())
    if accept == 1:
        ticketNumber = 5
    elif accept == 2:
        print("How many tickets would you like to see?")
        ticketNumber = int(input())
    else:
        print("You enter unproper value. Please start once again")
        exit(0)

    for issue in jira.search_issues('reporter = currentUser() order by created desc', maxResults=ticketNumber):
        #return all_issue
        print('{}: {}'.format(issue.key, issue.fields.summary))


#append new label
def NewLabel(issue):
    print('Which label would you like?')
    label=str(input())
    issue.fields.labels.append(label)
    issue.update(fields={"labels": issue.fields.labels})

#transition to other status:
def IssueTransition(issue):
    print('Current status is: ', issue.fields.status)
    print("which new status do you need?")
    print('''
         To Do
         In Progress
         In Review
         Done    
    ''')
    new_status=str(input())
    jira.transition_issue(issue, new_status)
    #print('Status changed to: ', new_status)
    return new_status


while True:


    try:
        # to connect to Jira
        jira_options = {'server': "http://localhost:8080/"}
        jira = JIRA(options=jira_options, basic_auth=("gmaksymv", "jira_test"))
        print("ATTEMPT")

    except JIRAError as err:
        print("Connection to Jira filed")
        #print(err.status_code, err.text)
        print(err.status_code)
        exit(0)
    else:
        print(''' -------
            Which operation would you like to execute?
            0 - Exit
            1-list of issues with summary'
            2-print info about all projects'
            3-Append new label
            4-Issue transition
                ''')

        option=int(input())
        if option==1:
            ListOfIssues()
        elif option==2:
            print(ProjectInfo())
        elif option==3:
            NewLabel(ProperTicket())
        elif option==4:
            print('Status changed to: ', IssueTransition(ProperTicket()))



        else:
            print('The script is stopped')
            break

exit()


