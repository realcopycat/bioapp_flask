from common.view import Resource,Namespace

userns = Namespace('aa', ordered=True)


@userns.route('/a')
class MyResource(Resource):
    def get(self):
        return {}

    @userns.response(403, 'Not Authorized')
    def post(self):
        userns.abort(403)
