from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

Data = []


class People(Resource):
    def get(self, name):
        global Data
        for x in Data:
            if x['Data'] == name:
                return x
            return {'Data': "Subbu"}

    def post(self, name):
        tem = {'Data': name}
        global Data
        Data.append(tem)
        return tem

    def delete(self, name):
        for ind, x in enumerate(Data):
            if x['Data'] == name:
                tem = Data.pop(ind)
                return {'Note': "Deleted"}


api.add_resource(People, '/Name/<string:name>')


app.run()
