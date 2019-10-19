from flask import Flask, request
from flask_restplus import Api, Resource, fields
from server.services import example_service


app = Flask(__name__)
flask_app = Api(app=app,
                version='1.0',
                title='Microservice example',
                description='Python Flask server with basic structure and example API')
api = flask_app.namespace(name='api', description='Examples of endpoints')


@api.route('/isAlive')
@api.response(code=200, description='OK')
@api.response(code=500, description='Internal Server Error')
class IsAliveController(Resource):
    def get(self):
        try:
            return True
        except Exception as e:
            api.abort(500, e.__doc__, status='Internal Server Error', statusCode='500')


@api.route('/example/<string:key_name>')
@api.response(code=200, description='OK')
@api.response(code=400, description='Bad Request')
@api.response(code=500, description='Internal Server Error')
class ExampleController(Resource):
    model = api.model('Example Model', {'color': fields.String(required=True),
                                        'size': fields.Integer(),
                                        'is_active': fields.Boolean(required=True),
                                        'year': fields.Integer(required=True, min=1900)})

    @api.expect(model, validate=True)
    @api.param(name='identifier')
    def post(self, key_name):
        try:
            body = request.json
            parameter = request.args.get(key='identifier')
            value = example_service.get_value_by_key(dictionary=body, key=key_name)
            return {
                'identifier': parameter,
                'value': value
            }
        except KeyError as e:
            api.abort(400, e.__doc__, status='Bad Request', statusCode='400')
        except Exception as e:
            api.abort(500, e.__doc__, status='Internal Server Error', statusCode='500')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
