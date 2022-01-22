from flask import Blueprint as FlaskBlueprint
from flask.views import MethodViewType, MethodView


class Blueprint(FlaskBlueprint):

    # Order in which the methods are presented in the spec
    HTTP_METHODS = ["OPTIONS", "HEAD", "GET", "POST", "PUT", "PATCH", "DELETE"]

    DEFAULT_LOCATION_CONTENT_TYPE_MAPPING = {
        "json": "application/json",
        "form": "application/x-www-form-urlencoded",
        "files": "multipart/form-data",
    }



    def __init__(self, *args, **kwargs):

        self.description = kwargs.pop("description", "")

        super().__init__(*args, **kwargs)

        self._endpoints = []

    def add_url_rule(
        self,
        rule,
        endpoint=None,
        view_func=None,
        provide_automatic_options=None,
        *,
        parameters=None,
        tags=None,
        **options,
    ):

        if view_func is None:
            raise TypeError("view_func must be provided")

        if endpoint is None:
            endpoint = view_func.__name__

        # Ensure endpoint name is unique
        # - to avoid a name clash when registering a MethodView
        # - to use it as a key internally in endpoint -> doc mapping
        if endpoint in self._endpoints:
            endpoint = f"{endpoint}_{len(self._endpoints)}"
        self._endpoints.append(endpoint)

        if isinstance(view_func, MethodViewType):
            func = view_func.as_view(endpoint)
        else:
            func = view_func

        # Add URL rule in Flask and store endpoint documentation
        super().add_url_rule(rule, endpoint, func, **options)

    def route(self, rule, *, parameters=None, tags=None, **options):
        """Decorator to register view function in application and documentation

        Calls :meth:`add_url_rule <Blueprint.add_url_rule>`.
        """

        def decorator(func):
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(
                rule, endpoint, func, parameters=parameters, tags=tags, **options
            )
            return func

        return decorator

    def register_child_bp(self, bp_lists):
        for bp in bp_lists:
            self.register_blueprint(bp)

class View(MethodView):
    pass