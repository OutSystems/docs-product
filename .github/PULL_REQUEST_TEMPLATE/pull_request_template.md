# Fetch and Display Data from the Database

One of the most common operations in a data-driven application is fetching data from the database, for example, to display it on the screen. In OutSystems, Aggregates provide this functionality.

To fetch data from the database in Reactive Web or Mobile:

1. On the Interface tab, right-click a screen and select if you want to retrieve data from the database or from the local storage to add an aggregate.
1. Open the aggregate, and drag the entities from where you want to fetch data from the Data tab to the aggregate.
1. Access the data using the output list of the aggregate.

To fetch data from the database in Traditional Web:

1. Drag the aggregate tool from the toolbox to any action flow. Aggregates are typically used in Preparation actions of screens.
1. Open the aggregate, and drag the entities from where you want to fetch data from the Data tab to the aggregate.
1. Access the data using the output list of the aggregate.

## In Reactive Web and Mobile

One of the most common operations in a data-driven application is fetching data from the database, for example, to display it on the screen. In OutSystems, Aggregates provide this functionality.

To fetch data from the database in Reactive Web or Mobile:

#### Bring Your Table to Your Screen
1. Drag a Table and drop it in the MainContent area of the screen.
![](images/Step1.png)

2. In the properties of the Table, set the Source property to an Aggregate List, in this example, GetProjects.List.
![](images/Step2.png)

The Table fetches the output of the Aggregate as the source of data

3. Top populate the Table, expand the Aggregate on the right of Service Studio, drag the main screen Entity, and drop it to the Table. 
![](images/Step3.png)

4. Your Table should now appear. In this example, the Table now has three columns, one per each attribute of the Project Entity
![](images/Step4.png)


#### Fetch Data from the Database
5. Select the Expression with the Name, by right-clicking the Task Manager on the Table. In
the menu that is displayed, select Link to -> MainFlow\ProjectDetail
![](images/Step5.png)


6. On the properties of the recently created Link, set the value of the ProjectId input
parameter of the OnClick to the proper .id, in this case GetProjects.List.Current.Project.Id

![](images/Step6.png)


This makes sure that the Id of the Project clicked on is passed to the ProjectDetail
Screen. This Id is useful to fetch the details of the project in the ProjectDetail.

7. Publish the module to the server to save the latest changes
![](images/Step7.png)

8. Open the application in the browser and make sure that all the Projects appear on a
Table. This is how you fetch and display data from the database.
![](images/Step8.png)

## In Traditional Web

In the following steps we will fetch Places from the database of a web app called GoOutWeb. Then we will use a Table Records widget to display them on the screen.

1. Add the Preparation action to the Places screen, and open it.
1. Drag the aggregate from the toolbar to the Preparation action. Then double-click on the aggregate to open it.
1. Drag the Place entity from the Data tab to the aggregate.
1. On the screen, add a Table Records widget from the toolbar.
1. Set the widget's  Source Record List property to `GetPlaces.List`. This binds the data to the widget.
1. Drag the Place entity from the Data tab to the Table Records widget on the screen.
1. Publish the application.

![Fetch and Display Data](images/fetch-display-web.gif)
