# Classifiers

## Classification - Genres

### Purpose
- Aid the developers and App Stores to correctly classify the Apps based on the description.
- Also to recommend a genre for a new App.

### Columns Used 
**App Description** - An elaborate description of the app given by the App developers.

**Category** - Actual category/genre of the app.

### Feature Engineering
- **Description**
  It is a text column.
   Need a way to weigh each words in the description appropriately.

- **tf-idf Vectorization**
term frequency–inverse document frequency
It is a measure used to evaluate the importance of a word in a text/document.
Converts strings to features based on its importance. 

### Results

| ![Google InfoGraphics](https://raw.githubusercontent.com/nareshkumar66675/Appomania/master/reports/Classification/AppGenreResult.png "Google InfoGraphics") | ![Apple Store](https://raw.githubusercontent.com/nareshkumar66675/Appomania/master/reports/Classification/AppGenreResultTab.png "Apple Store") |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|

## Classification - Content Rating

### Purpose
- Aid the developers and App Stores to correctly label the Apps for Content Rating.
- Also to recommend Content Rating for a new App.

#### Columns Used 
- **App Description** - An elaborate description of the app given by the App developers.
- **Category** - Category/genre of the app.
- **Content Rating** -  Content Rating of the App. For Ex: 4+, 12+,19+

### Results

| ![Google InfoGraphics](https://github.com/nareshkumar66675/Appomania/blob/master/reports/Classification/ContentRatingResult.png "Google InfoGraphics") | ![Apple Store](https://github.com/nareshkumar66675/Appomania/blob/master/reports/Classification/ContentRatingResultTab.png "Apple Store") |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
