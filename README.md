


# Send-IT   
[![Build Status](https://travis-ci.com/ipaullly/sendIT.svg?branch=ch-test-user-interactions-163458249)](https://travis-ci.com/ipaullly/sendIT) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/d5026cb302e349d7b08580df620e7ecd)](https://www.codacy.com/app/ipaullly/sendIT?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ipaullly/sendIT&amp;utm_campaign=Badge_Grade)

The project was done while participating in the Andela Developer Challenge simulated sprint of the application bootcamp. 
This is an app that allows users to create accounts and make delivery orders. The front-end was built using vanilla javaScript and consumed endpoints built with python/flask.
The app is live on the github-pages [link](https://ipaullly.github.io/sendIT/index.html) for this repo.
  
## Installation
Clone the repository to your local machine
```
git clone https://github.com/ipaullly/sendIT.git
```
Move into the project directory created after the clone command
```
cd *project_directory*
```
Initialize node for the project

```
npm init
```
Install all related dependencies from the package.json
```
npm install
```
To run the project on your local server
```
npm start
```

## Testing
Tests run using **jest** and **puppeteer**. run the following command within the project folder to see the test coverage
```
npm test
```
Alternatively view the [Travis-CI](https://travis-ci.com/ipaullly/sendIT) build report to view coverage.

## App features
- [ ] Users can create an account and log in.
- [ ] Users can create a parcel delivery order.
- [ ] Users can change the destination of a parcel delivery order.
- [ ] Users can cancel parcel delivery order.
- [ ] Users can see the details of a delivery order.
- [ ] Admin can change the **status** and **Current-location** of a parcel delivery order.

## Built Using
1.HTML
2.CSS
3.JAVASCRIPT
