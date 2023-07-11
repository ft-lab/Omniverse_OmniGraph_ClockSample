import omni.graph.core as og
import omni.graph.core._omni_graph_core as _og
import omni.graph.tools.ogn as ogn
import numpy
import sys
import traceback
import carb

class RotationByTimeDatabase(og.Database):
    """Helper class providing simplified access to data on nodes of type ft_lab.OmniGraph.GetDateTime.RotationByTime

    Class Members:
        node: Node being evaluated

    Attribute Value Properties:
        Inputs:
            inputs.a1_defaultRotateXYZ
            inputs.a2_rotationAxis
            inputs.b1_hour
            inputs.b2_minute
            inputs.b3_second
        Outputs:
            outputs.a1_hourRotateXYZ
            outputs.a2_minuteRotateXYZ
            outputs.a3_secondRotateXYZ
    """

    # Omniverse Create 2022.3.3 (Kit.104)
    #GENERATOR_VERSION = (1, 17, 2)
    #TARGET_VERSION = (2, 65, 4)

    # Imprint the generator and target ABI versions in the file for JIT generation
    # USD Composer 2023.1.0 beta (Kit.105)
    GENERATOR_VERSION = (1, 31, 1)
    TARGET_VERSION = (2, 107, 4)

    # This is an internal object that provides per-class storage of a per-node data dictionary
    PER_NODE_DATA = {}

    INTERFACE = og.Database._get_interface([
        ('inputs:a1_defaultRotateXYZ', 'float[3]', 0, 'Default RotateXYZ', 'Default rotateXYZ', {}, True, None, False, ''),
        ('inputs:a2_rotationAxis', 'int', 0, 'Rotation Axis', 'Rotation axis (0:X, 1:Y, 2:Z)', {}, True, None, False, ''),
        ('inputs:b1_hour', 'int', 0, 'Hour', 'Hour', {ogn.MetadataKeys.DEFAULT: '0'}, True, 0, False, ''),
        ('inputs:b2_minute', 'int', 0, 'Minute', 'Minute', {ogn.MetadataKeys.DEFAULT: '0'}, True, 0, False, ''),
        ('inputs:b3_second', 'int', 0, 'Second', 'Second', {ogn.MetadataKeys.DEFAULT: '0'}, True, 0, False, ''),
        ('outputs:a1_hourRotateXYZ', 'float[3]', 0, 'Hour RotateXYZ', 'Hour RotateXYZ', {}, True, None, False, ''),
        ('outputs:a2_minuteRotateXYZ', 'float[3]', 0, 'Minute RotateXYZ', 'Minute RotateXYZ', {}, True, None, False, ''),
        ('outputs:a3_secondRotateXYZ', 'float[3]', 0, 'Second RotateXYZ', 'Second RotateXYZ', {}, True, None, False, ''),
    ])

    # ----------------------------------------------------.
    # Processing Input Parameters.
    # ----------------------------------------------------.
    class ValuesForInputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {"a1_defaultRotateXYZ", "a2_rotationAxis", "b1_hour", "b2_minute", "b3_second"}
        """Helper class that creates natural hierarchical access to input attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedReadAttributes = [self._attributes.a1_defaultRotateXYZ, self._attributes.a2_rotationAxis, self._attributes.b1_hour, self._attributes.b2_minute, self._attributes.b3_second]
            self._batchedReadValues = [[0.0, 0.0, 0.0], 0, 0, 0, 0]

        @property
        def a1_defaultRotateXYZ(self):
            return self._batchedReadValues[0]

        @a1_defaultRotateXYZ.setter
        def a1_defaultRotateXYZ(self, value):
            self._batchedReadValues[0] = value

        @property
        def a2_rotationAxis(self):
            return self._batchedReadValues[1]

        @a2_rotationAxis.setter
        def a2_rotationAxis(self, value):
            self._batchedReadValues[1] = value

        @property
        def b1_hour(self):
            return self._batchedReadValues[2]

        @b1_hour.setter
        def b1_hour(self, value):
            self._batchedReadValues[2] = value

        @property
        def b2_minute(self):
            return self._batchedReadValues[3]

        @b2_minute.setter
        def b2_minute(self, value):
            self._batchedReadValues[3] = value

        @property
        def b3_second(self):
            return self._batchedReadValues[4]

        @b3_second.setter
        def b3_second(self, value):
            self._batchedReadValues[4] = value

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

        def _prefetch(self):
            readAttributes = self._batchedReadAttributes
            newValues = _og._prefetch_input_attributes_data(readAttributes)
            if len(readAttributes) == len(newValues):
                self._batchedReadValues = newValues

    # ----------------------------------------------------.
    # Processing Output Parameter.
    # ----------------------------------------------------.
    class ValuesForOutputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = { "a1_hourRotateXYZ", "a2_minuiteRotateXYZ", "a3_secondRotateXYZ" }
        """Helper class that creates natural hierarchical access to output attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedWriteValues = { }

        @property
        def a1_hourRotateXYZ(self):
            value = self._batchedWriteValues.get(self._attributes.a1_hourRotateXYZ)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.a1_hourRotateXYZ)
                return data_view.get()

        @a1_hourRotateXYZ.setter
        def a1_hourRotateXYZ(self, value):
            self._batchedWriteValues[self._attributes.a1_hourRotateXYZ] = value

        @property
        def a2_minuteRotateXYZ(self):
            value = self._batchedWriteValues.get(self._attributes.a2_minuteRotateXYZ)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.a2_minuteRotateXYZ)
                return data_view.get()

        @a2_minuteRotateXYZ.setter
        def a2_minuteRotateXYZ(self, value):
            self._batchedWriteValues[self._attributes.a2_minuteRotateXYZ] = value

        @property
        def a3_secondRotateXYZ(self):
            value = self._batchedWriteValues.get(self._attributes.a3_secondRotateXYZ)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.a3_secondRotateXYZ)
                return data_view.get()

        @a3_secondRotateXYZ.setter
        def a3_secondRotateXYZ(self, value):
            self._batchedWriteValues[self._attributes.a3_secondRotateXYZ] = value

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

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_INPUT)
        self.inputs = RotationByTimeDatabase.ValuesForInputs(node, self.attributes.inputs, dynamic_attributes)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_OUTPUT)
        self.outputs = RotationByTimeDatabase.ValuesForOutputs(node, self.attributes.outputs, dynamic_attributes)

        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_STATE)
        self.state = RotationByTimeDatabase.ValuesForState(node, self.attributes.state, dynamic_attributes)

    # ----------------------------------------------------.
    # Class defining the ABI interface for the node type.
    # ----------------------------------------------------.
    class abi:
        @staticmethod
        def get_node_type():
            get_node_type_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'get_node_type', None)
            if callable(get_node_type_function):
                return get_node_type_function()
            return 'ft_lab.OmniGraph.GetDateTime.RotationByTime'
        
        @staticmethod
        def compute(context, node):
            def database_valid():
                return True
            try:
                per_node_data = RotationByTimeDatabase.PER_NODE_DATA[node.node_id()]
                db = per_node_data.get('_db')
                if db is None:
                    db = RotationByTimeDatabase(node)
                    per_node_data['_db'] = db
                if not database_valid():
                    per_node_data['_db'] = None
                    return False
            except:
                db = RotationByTimeDatabase(node)

            try:
                compute_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'compute', None)
                if callable(compute_function) and compute_function.__code__.co_argcount > 1:
                    return compute_function(context, node)

                db.inputs._prefetch()
                db.inputs._setting_locked = True
                with og.in_compute():
                    return RotationByTimeDatabase.NODE_TYPE_CLASS.compute(db)
            except Exception as error:
                stack_trace = "".join(traceback.format_tb(sys.exc_info()[2].tb_next))
                db.log_error(f'Assertion raised in compute - {error}\n{stack_trace}', add_context=False)
            finally:
                db.inputs._setting_locked = False
                db.outputs._commit()
            return False
        @staticmethod
        def initialize(context, node):
            RotationByTimeDatabase._initialize_per_node_data(node)
            initialize_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'initialize', None)
            if callable(initialize_function):
                initialize_function(context, node)
        @staticmethod
        def release(node):
            release_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'release', None)
            if callable(release_function):
                release_function(node)
            RotationByTimeDatabase._release_per_node_data(node)
        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            update_node_version_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'update_node_version', None)
            if callable(update_node_version_function):
                return update_node_version_function(context, node, old_version, new_version)
            return False
        @staticmethod
        def initialize_type(node_type):
            initialize_type_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'initialize_type', None)
            needs_initializing = True
            if callable(initialize_type_function):
                needs_initializing = initialize_type_function(node_type)
            if needs_initializing:
                node_type.set_metadata(ogn.MetadataKeys.EXTENSION, "ft_lab.OmniGraph.GetDateTime")
                node_type.set_metadata(ogn.MetadataKeys.UI_NAME, "Rotation By Time")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORIES, "examples")
                node_type.set_metadata(ogn.MetadataKeys.DESCRIPTION, "Rotation By Time")
                node_type.set_metadata(ogn.MetadataKeys.LANGUAGE, "Python")

                # Set Icon(svg).
                icon_path = carb.tokens.get_tokens_interface().resolve("${ft_lab.OmniGraph.GetDateTime}")
                icon_path = icon_path + '/' + "data/icons/rotationByTimeIcon.svg"
                node_type.set_metadata(ogn.MetadataKeys.ICON_PATH, icon_path)

                RotationByTimeDatabase.INTERFACE.add_to_node_type(node_type)
        @staticmethod
        def on_connection_type_resolve(node):
            on_connection_type_resolve_function = getattr(RotationByTimeDatabase.NODE_TYPE_CLASS, 'on_connection_type_resolve', None)
            if callable(on_connection_type_resolve_function):
                on_connection_type_resolve_function(node)
    NODE_TYPE_CLASS = None

    @staticmethod
    def register(node_type_class):
        RotationByTimeDatabase.NODE_TYPE_CLASS = node_type_class
        og.register_node_type(RotationByTimeDatabase.abi, 1)

    @staticmethod
    def deregister():
        og.deregister_node_type("ft_lab.OmniGraph.GetDateTime.RotationByTime")
