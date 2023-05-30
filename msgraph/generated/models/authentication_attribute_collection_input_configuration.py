from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_attribute_collection_input_type, authentication_attribute_collection_option_configuration

class AuthenticationAttributeCollectionInputConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationAttributeCollectionInputConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The built-in or custom attribute for which a value is being collected.
        self._attribute: Optional[str] = None
        # The default value of the attribute displayed to the end user.
        self._default_value: Optional[str] = None
        # Whether the attribute is editable by the end user.
        self._editable: Optional[bool] = None
        # Whether the attribute is displayed to the end user.
        self._hidden: Optional[bool] = None
        # The inputType property
        self._input_type: Optional[authentication_attribute_collection_input_type.AuthenticationAttributeCollectionInputType] = None
        # The label of the attribute field that will be displayed to end user, unless overridden.
        self._label: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The option values for certain multiple-option input types.
        self._options: Optional[List[authentication_attribute_collection_option_configuration.AuthenticationAttributeCollectionOptionConfiguration]] = None
        # Whether the field is required.
        self._required: Optional[bool] = None
        # The regex for the value of the field.
        self._validation_reg_ex: Optional[str] = None
        # Whether the value collected will be stored.
        self._write_to_directory: Optional[bool] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def attribute(self,) -> Optional[str]:
        """
        Gets the attribute property value. The built-in or custom attribute for which a value is being collected.
        Returns: Optional[str]
        """
        return self._attribute
    
    @attribute.setter
    def attribute(self,value: Optional[str] = None) -> None:
        """
        Sets the attribute property value. The built-in or custom attribute for which a value is being collected.
        Args:
            value: Value to set for the attribute property.
        """
        self._attribute = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationAttributeCollectionInputConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAttributeCollectionInputConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationAttributeCollectionInputConfiguration()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. The default value of the attribute displayed to the end user.
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. The default value of the attribute displayed to the end user.
        Args:
            value: Value to set for the default_value property.
        """
        self._default_value = value
    
    @property
    def editable(self,) -> Optional[bool]:
        """
        Gets the editable property value. Whether the attribute is editable by the end user.
        Returns: Optional[bool]
        """
        return self._editable
    
    @editable.setter
    def editable(self,value: Optional[bool] = None) -> None:
        """
        Sets the editable property value. Whether the attribute is editable by the end user.
        Args:
            value: Value to set for the editable property.
        """
        self._editable = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_attribute_collection_input_type, authentication_attribute_collection_option_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "attribute": lambda n : setattr(self, 'attribute', n.get_str_value()),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "inputType": lambda n : setattr(self, 'input_type', n.get_enum_value(authentication_attribute_collection_input_type.AuthenticationAttributeCollectionInputType)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(authentication_attribute_collection_option_configuration.AuthenticationAttributeCollectionOptionConfiguration)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "validationRegEx": lambda n : setattr(self, 'validation_reg_ex', n.get_str_value()),
            "writeToDirectory": lambda n : setattr(self, 'write_to_directory', n.get_bool_value()),
        }
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. Whether the attribute is displayed to the end user.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. Whether the attribute is displayed to the end user.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    @property
    def input_type(self,) -> Optional[authentication_attribute_collection_input_type.AuthenticationAttributeCollectionInputType]:
        """
        Gets the inputType property value. The inputType property
        Returns: Optional[authentication_attribute_collection_input_type.AuthenticationAttributeCollectionInputType]
        """
        return self._input_type
    
    @input_type.setter
    def input_type(self,value: Optional[authentication_attribute_collection_input_type.AuthenticationAttributeCollectionInputType] = None) -> None:
        """
        Sets the inputType property value. The inputType property
        Args:
            value: Value to set for the input_type property.
        """
        self._input_type = value
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. The label of the attribute field that will be displayed to end user, unless overridden.
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. The label of the attribute field that will be displayed to end user, unless overridden.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def options(self,) -> Optional[List[authentication_attribute_collection_option_configuration.AuthenticationAttributeCollectionOptionConfiguration]]:
        """
        Gets the options property value. The option values for certain multiple-option input types.
        Returns: Optional[List[authentication_attribute_collection_option_configuration.AuthenticationAttributeCollectionOptionConfiguration]]
        """
        return self._options
    
    @options.setter
    def options(self,value: Optional[List[authentication_attribute_collection_option_configuration.AuthenticationAttributeCollectionOptionConfiguration]] = None) -> None:
        """
        Sets the options property value. The option values for certain multiple-option input types.
        Args:
            value: Value to set for the options property.
        """
        self._options = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. Whether the field is required.
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. Whether the field is required.
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("attribute", self.attribute)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("editable", self.editable)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_enum_value("inputType", self.input_type)
        writer.write_str_value("label", self.label)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("options", self.options)
        writer.write_bool_value("required", self.required)
        writer.write_str_value("validationRegEx", self.validation_reg_ex)
        writer.write_bool_value("writeToDirectory", self.write_to_directory)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def validation_reg_ex(self,) -> Optional[str]:
        """
        Gets the validationRegEx property value. The regex for the value of the field.
        Returns: Optional[str]
        """
        return self._validation_reg_ex
    
    @validation_reg_ex.setter
    def validation_reg_ex(self,value: Optional[str] = None) -> None:
        """
        Sets the validationRegEx property value. The regex for the value of the field.
        Args:
            value: Value to set for the validation_reg_ex property.
        """
        self._validation_reg_ex = value
    
    @property
    def write_to_directory(self,) -> Optional[bool]:
        """
        Gets the writeToDirectory property value. Whether the value collected will be stored.
        Returns: Optional[bool]
        """
        return self._write_to_directory
    
    @write_to_directory.setter
    def write_to_directory(self,value: Optional[bool] = None) -> None:
        """
        Sets the writeToDirectory property value. Whether the value collected will be stored.
        Args:
            value: Value to set for the write_to_directory property.
        """
        self._write_to_directory = value
    

