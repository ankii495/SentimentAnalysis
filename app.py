from flask import Flask, render_template
from flask import request
from flask_cors import CORS
from TwitterSentimentAnalysis import TwitterClient
import json

data2={"conversation":[]}
new_arr=[]
 


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    api = TwitterClient()
    sACompanyX = api.analyseTweetData('CompanyX','')
    sACompanyY = api.analyseTweetData('CompanyY','')
    sACompanyXProdA = api.analyseTweetData('CompanyX','ProductA')
    sACompanyXProdB = api.analyseTweetData('CompanyX','ProductB')
    sACompanyYProdA1 = api.analyseTweetData('CompanyY','ProductA1')
    sACompanyYProdB1 = api.analyseTweetData('CompanyY','ProductB1')
    my_json_string =  json.dumps( [{
                                 "company":"CompanyX",
                                 "product":"",
                                 "positive":sACompanyX[0],
                                 "negative":sACompanyX[1]
                                },{
                                 "company":"CompanyY",
                                 "product":"",
                                 "positive":sACompanyY[0],
                                 "negative":sACompanyY[1]
                                    },{
                                  "company":"CompanyX",
                                 "product":"ProductA",
                                 "positive":sACompanyXProdA[0],
                                 "negative":sACompanyXProdA[1]
                                  },
                                  {
                                  "company":"CompanyY",
                                 "product":"A1",
                                 "positive":sACompanyYProdA1[0],
                                 "negative":sACompanyYProdA1[1]
                                  },{
                                  "company":"CompanyX",
                                 "product":"ProductB",
                                 "positive":sACompanyXProdB[0],
                                 "negative":sACompanyXProdB[1]
                                  },
                                  {
                                  "company":"CompanyY",
                                 "product":"B1",
                                 "positive":sACompanyYProdB1[0],
                                 "negative":sACompanyYProdB1[1]
                                  }]
                              )


    return my_json_string



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5004)
