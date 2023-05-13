import omni.graph.core as og
import omni.graph.core._omni_graph_core as _og
import omni.graph.tools.ogn as ogn
import numpy
import sys
import traceback
import carb

class GetDateTimeDatabase(og.Database):
    """Helper class providing simplified access to data on nodes of type ft_lab.OmniGraph.GetDateTime.GetDateTime

    Class Members:
        node: Node being evaluated

    Attribute Value Properties:
        Inputs:
        Outputs:
            outputs.a1_year
            outputs.a2_month
            outputs.a3_day
            outputs.b1_hour
            outputs.b2_minute
            outputs.b3_second
    """

    # This is an internal object that provides per-class storage of a per-node data dictionary
    PER_NODE_DATA = {}

    INTERFACE = og.Database._get_interface([
        ('outputs:a1_year', 'int', 0, 'Year', 'output year', {ogn.MetadataKeys.DEFAULT: '2000'}, True, 0, False, ''),
        ('outputs:a2_month', 'int', 0, 'Month', 'output month', {ogn.MetadataKeys.DEFAULT: '1'}, True, 0, False, ''),
        ('outputs:a3_day', 'int', 0, 'Day', 'output day', {ogn.MetadataKeys.DEFAULT: '1'}, True, 0, False, ''),
        ('outputs:b1_hour', 'int', 0, 'Hour', 'output hour', {ogn.MetadataKeys.DEFAULT: '1'}, True, 0, False, ''),
        ('outputs:b2_minute', 'int', 0, 'Minute', 'output minute', {ogn.MetadataKeys.DEFAULT: '0'}, True, 0, False, ''),
        ('outputs:b3_second', 'int', 0, 'Second', 'output second', {ogn.MetadataKeys.DEFAULT: '0'}, True, 0, False, ''),
    ])

    # ----------------------------------------------------.
    # Processing Output Parameter.
    # ----------------------------------------------------.
    class ValuesForOutputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = { "a1_year", "a2_month", "a3_day", "b1_hour", "b2_month", "b3_second" }
        """Helper class that creates natural hierarchical access to output attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedWriteValues = { }

        @property
        def a1_year(self):
            value = self._batchedWriteValues.get(self._attributes.a1_year)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.a1_year)
                return data_view.get()

        @a1_year.setter
        def a1_year(self, value):
            self._batchedWriteValues[self._attributes.a1_year] = value

        @property
        def a2_month(self):
            value = self._batchedWriteValues.get(self._attributes.a2_month)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.a2_month)
                return data_view.get()

        @a2_month.setter
        def a2_month(self, value):
            self._batchedWriteValues[self._attributes.a2_month] = value

        @property
        def a3_day(self):
            value = self._batchedWriteValues.get(self._attributes.a3_day)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.a3_day)
                return data_view.get()

        @a3_day.setter
        def a3_day(self, value):
            self._batchedWriteValues[self._attributes.a3_day] = value

        @property
        def b1_hour(self):
            value = self._batchedWriteValues.get(self._attributes.b1_hour)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.b1_hour)
                return data_view.get()

        @b1_hour.setter
        def b1_hour(self, value):
            self._batchedWriteValues[self._attributes.b1_hour] = value

        @property
        def b2_minute(self):
            value = self._batchedWriteValues.get(self._attributes.b2_minute)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.b2_minute)
                return data_view.get()

        @b2_minute.setter
        def b2_minute(self, value):
            self._batchedWriteValues[self._attributes.b2_minute] = value

        @property
        def b3_second(self):
            value = self._batchedWriteValues.get(self._attributes.b3_second)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.b3_second)
                return data_view.get()

        @b3_second.setter
        def b3_second(self, value):
            self._batchedWriteValues[self._attributes.b3_second] = value


        def __getattr__(self, item: str):
            if item in self.LOCAL_PROPERTY_NAMES:
                return object.__getattribute__(self, item)
            else:
                return super().__getattr__(item)

        def __setattr__(self, item: str, new_value):
            if item in self.LOCAL_PROPERTY_NAMES:
                object.__setattr__(self, item, new_value)
            else:
                super().__setattr__(item, new_value)

        def _commit(self):
            _og._commit_output_attributes_data(self._batchedWriteValues)
            self._batchedWriteValues = { }

    class ValuesForState(og.DynamicAttributeAccess):
        """Helper class that creates natural hierarchical access to state attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)

    def __init__(self, node):
        super().__init__(node)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_OUTPUT)
        self.outputs = GetDateTimeDatabase.ValuesForOutputs(node, self.attributes.outputs, dynamic_attributes)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_STATE)
        self.state = GetDateTimeDatabase.ValuesForState(node, self.attributes.state, dynamic_attributes)

    # ----------------------------------------------------.
    # Class defining the ABI interface for the node type.
    # ----------------------------------------------------.
    class abi:
        @staticmethod
        def get_node_type():
            get_node_type_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'get_node_type', None)
            if callable(get_node_type_function):
                return get_node_type_function()
            return 'ft_lab.OmniGraph.GetDateTime.GetDateTime'
        
        @staticmethod
        def compute(context, node):
            try:
                per_node_data = GetDateTimeDatabase.PER_NODE_DATA[node.node_id()]
                db = per_node_data.get('_db')
                if db is None:
                    db = GetDateTimeDatabase(node)
                    per_node_data['_db'] = db
            except:
                db = GetDateTimeDatabase(node)

            try:
                compute_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'compute', None)
                if callable(compute_function) and compute_function.__code__.co_argcount > 1:
                    return compute_function(context, node)

                with og.in_compute():
                    return GetDateTimeDatabase.NODE_TYPE_CLASS.compute(db)
            except Exception as error:
                stack_trace = "".join(traceback.format_tb(sys.exc_info()[2].tb_next))
                db.log_error(f'Assertion raised in compute - {error}\n{stack_trace}', add_context=False)
            finally:
                db.outputs._commit()
            return False
        @staticmethod
        def initialize(context, node):
            GetDateTimeDatabase._initialize_per_node_data(node)
            initialize_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'initialize', None)
            if callable(initialize_function):
                initialize_function(context, node)
        @staticmethod
        def release(node):
            release_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'release', None)
            if callable(release_function):
                release_function(node)
            GetDateTimeDatabase._release_per_node_data(node)
        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            update_node_version_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'update_node_version', None)
            if callable(update_node_version_function):
                return update_node_version_function(context, node, old_version, new_version)
            return False
        @staticmethod
        def initialize_type(node_type):
            initialize_type_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'initialize_type', None)
            needs_initializing = True
            if callable(initialize_type_function):
                needs_initializing = initialize_type_function(node_type)
            if needs_initializing:
                node_type.set_metadata(ogn.MetadataKeys.EXTENSION, "ft_lab.OmniGraph.GetDateTime")
                node_type.set_metadata(ogn.MetadataKeys.UI_NAME, "Get DateTime")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORIES, "examples")
                node_type.set_metadata(ogn.MetadataKeys.DESCRIPTION, "Get current date and time")
                node_type.set_metadata(ogn.MetadataKeys.LANGUAGE, "Python")

                # Set Icon(svg).
                icon_path = carb.tokens.get_tokens_interface().resolve("${ft_lab.OmniGraph.GetDateTime}")
                icon_path = icon_path + '/' + "data/icons/icon.svg"
                node_type.set_metadata(ogn.MetadataKeys.ICON_PATH, icon_path)

                GetDateTimeDatabase.INTERFACE.add_to_node_type(node_type)
        @staticmethod
        def on_connection_type_resolve(node):
            on_connection_type_resolve_function = getattr(GetDateTimeDatabase.NODE_TYPE_CLASS, 'on_connection_type_resolve', None)
            if callable(on_connection_type_resolve_function):
                on_connection_type_resolve_function(node)
    NODE_TYPE_CLASS = None
    GENERATOR_VERSION = (1, 17, 2)
    TARGET_VERSION = (2, 65, 4)

    @staticmethod
    def register(node_type_class):
        GetDateTimeDatabase.NODE_TYPE_CLASS = node_type_class
        og.register_node_type(GetDateTimeDatabase.abi, 1)

    @staticmethod
    def deregister():
        og.deregister_node_type("ft_lab.OmniGraph.GetDateTime.GetDateTime")
